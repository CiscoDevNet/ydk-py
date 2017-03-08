#  ----------------------------------------------------------------
# Copyright 2016 Cisco Systems
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------
""" _encoder.py

   Encoder.

"""
from ._validator import validate_entity
from ._value_encoder import ValueEncoder
from lxml import etree
from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_LIST , REFERENCE_LEAFLIST, \
                                 REFERENCE_UNION, ANYXML_CLASS, REFERENCE_BITS, \
                                 REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS
from ydk.types import Empty, DELETE, READ, Decimal64, YList, YLeafList, YListItem

from ._importer import _yang_ns


class XmlEncoder(object):
    def __init__(self):
        self.encode_value = ValueEncoder().encode
        self.app=''
        self.python_imports = {}

    def encode(self, entity):
        ''' Convert the entity to an xml payload '''
        ret = etree.tostring(self.encode_to_xml(entity, etree.Element('a'), ''), method='xml', pretty_print='True', encoding='utf-8').decode('utf-8')
        self._add_imports()
        self.app = _enclose_function_definition(entity, self.app)
        return ret

    def encode_to_xml(self, entity, root, optype, is_filter=False):
        ''' Convert the entity to an xml payload '''
        # if the entity has a parent hierarchy use that to get
        # the parent related envelope that we need
        if (hasattr(entity, 'mtype') and not entity.mtype == ANYXML_CLASS) and \
            (not is_filter and hasattr(entity, '_has_data') and not entity._has_data()):
            return

        validate_entity(entity, optype)

        if entity_is_rpc_input(entity):
            elem = root
        else:
            elem = etree.SubElement(root, entity.i_meta.yang_name)
            self._store_import(entity.i_meta.pmodule_name)
            self.app += _get_object_declaration_statement(entity)

            parent_ns = None
            current_parent = root
            while current_parent != None and parent_ns is None:
                parent_ns = current_parent.get('xmlns')
                current_parent = current_parent.getparent()

            if entity.i_meta.namespace is not None and parent_ns != entity.i_meta.namespace:
                elem.set('xmlns', entity.i_meta.namespace)


        for member in entity.i_meta.meta_info_class_members:
            value = getattr(entity, member.presentation_name)
            if value is None or isinstance(value, list) and value == []:
                continue

            if not member.mtype == ANYXML_CLASS and hasattr(value, '_has_data') and not value._has_data():
                continue

            member_elem = None
            NSMAP = {}
            if member.mtype not in [REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST, REFERENCE_IDENTITY_CLASS, \
                                    REFERENCE_UNION] or isinstance(value, DELETE) or isinstance(value, READ):
                if entity.i_meta.namespace is not None \
                    and entity.i_meta.namespace != _yang_ns._namespaces[member.module_name]:
                    NSMAP[None] = _yang_ns._namespaces[member.module_name]
                member_elem = etree.SubElement(elem, member.name, nsmap=NSMAP)
                if member.mtype == ANYXML_CLASS:
                    self.encode_to_xml(value, member_elem, optype)
                    continue

            if isinstance(value, DELETE) and not is_filter:
                xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'
                member_elem.set('{' + xc + '}operation', 'delete')
            elif isinstance(value, READ):
                continue
            elif member.mtype == REFERENCE_CLASS:
                self.encode_to_xml(value, elem, optype)
                self.app += _get_member_assignment_statement(entity, member)
            elif member.mtype == REFERENCE_LIST:
                child_list = value
                for child in child_list:
                    self.encode_to_xml(child, elem, optype)
                    self.app += _get_member_append_statement(entity, member)
            elif member.mtype == REFERENCE_LEAFLIST and isinstance(value, list):
                for child in value:

                    if entity.i_meta.namespace is not None and entity.i_meta.namespace != _yang_ns._namespaces[member.module_name]:
                        NSMAP[None] = _yang_ns._namespaces[member.module_name]
                    text = self.encode_value(member, NSMAP, child.item)
                    member_elem = etree.SubElement(elem, member.name, nsmap=NSMAP)
                    member_elem.text = text
                    self.app += _get_value_append_statement(entity, member, text)
            elif member.mtype == REFERENCE_UNION:
                for contained_member in member.members:
                    NSMAP={}
                    if self._encode_union_member(entity, contained_member, value, elem, NSMAP):
                        break
            elif member.mtype == REFERENCE_IDENTITY_CLASS:
                text = self.encode_value(member, NSMAP, value)
                member_elem = etree.SubElement(elem, member.name, nsmap=NSMAP)
                member_elem.text = text
                self._store_import(value._meta_info().pmodule_name)
                self.app += _get_value_assignment_statement(entity, member, value)
            else:
                if member.mtype == REFERENCE_ENUM_CLASS:
                    self._store_import(value._meta_info().pmodule_name)
                text = self.encode_value(member, NSMAP, value)
                member_elem.text = text
                self.app += _get_value_assignment_statement(entity, member, value)
        return elem

    def encode_filter(self, f, root, optype):
        self.encode_to_xml(f, root , optype, True)

    def _encode_union_member(self, entity, contained_member, value, elem, NSMAP):
        member_elem = None
        if contained_member.mtype == REFERENCE_UNION:
            for sub_member in contained_member.members:
                if self._encode_union_member(entity, sub_member, value, elem, NSMAP):
                    return True
        elif contained_member.mtype == REFERENCE_LEAFLIST:
            for child in value:
                t = self.encode_value(contained_member, NSMAP, child.item)
                if len(t) == 0:
                    continue
                self.app += _get_value_append_statement(entity, contained_member, t)
                member_elem = etree.SubElement(elem, contained_member.name, nsmap=NSMAP)
                if entity.i_meta.namespace is not None and entity.i_meta.namespace != _yang_ns._namespaces[contained_member.module_name]:
                    NSMAP[None] = _yang_ns._namespaces[contained_member.module_name]
                member_elem.text = t
            if member_elem is not None and len(member_elem.text) > 0:
                return True
        else:
            t = self.encode_value(contained_member, NSMAP, value)
            if len(t) == 0:
                    return
            member_elem = etree.SubElement(elem, contained_member.name, nsmap=NSMAP)
            if contained_member.mtype == REFERENCE_ENUM_CLASS:
                self._store_import(value._meta_info().pmodule_name)
            self.app += _get_value_assignment_statement(entity, contained_member, value)
            member_elem.text = t
            if len(member_elem.text) > 0:
                return True
        return False

    def _add_imports(self):
        import_statements = ''
        for import_statement in self.python_imports.keys():
            import_statements += import_statement + '\n'
        import_statements += '    from ydk.types import Empty\n\n'
        self.app = import_statements + self.app

    def _store_import(self, pmodule_name):
        import_from = '.'.join(pmodule_name.split('.')[:-1])
        import_module = pmodule_name.split('.')[-1]
        import_statement = '    from ' + import_from + ' import ' + import_module
        if import_statement in self.python_imports:
            return
        self.python_imports[import_statement] = True


def entity_is_rpc_input(entity):
    return hasattr(entity, 'parent') and \
        entity.parent is not None and \
        hasattr(entity.parent, 'is_rpc') and \
        entity.parent.is_rpc and \
        entity._meta_info().yang_name == 'input'


def _enclose_function_definition(entity, app):
    return '\ndef _create_' + _dash_to_underscore(entity.i_meta.yang_name) + '_ydk_object():\n' + \
        app + '\n    return ' + _dash_to_underscore(entity.i_meta.yang_name) + '\n'


def _get_object_declaration_statement(entity):
    return '\n    ' + _dash_to_underscore(entity.i_meta.yang_name) + ' = ' + _get_module_name(entity.i_meta.pmodule_name) + '.' + entity.i_meta.name + '()\n'


def _get_value_assignment_statement(entity, member, value):
    if member.ptype == 'Empty':
        return '    ' + _dash_to_underscore(entity.i_meta.yang_name) + '.' + member.presentation_name + ' = Empty()' + '\n'
    return '    ' + _dash_to_underscore(entity.i_meta.yang_name) + '.' + member.presentation_name + ' = ' + _get_encoded_value(member, value) + '\n'


def _get_value_append_statement(entity, member, value):
    return '    ' + _dash_to_underscore(entity.i_meta.yang_name) + '.' + member.presentation_name + '.append(' + _get_encoded_value(member, value) + ')\n'


def _get_member_assignment_statement(entity, member):
    return '    ' + _dash_to_underscore(entity.i_meta.yang_name) + '.' + member.presentation_name + ' = ' + '' + member.presentation_name + '\n'


def _get_member_append_statement(entity, member):
    return '    ' + _dash_to_underscore(entity.i_meta.yang_name) + '.' + member.presentation_name + '.append(' + '' + member.presentation_name + ')\n'


def _get_encoded_value(member, value):
    if member.mtype == REFERENCE_ENUM_CLASS:
        value = _dash_to_underscore(value._meta_info().module_name) + _get_class_name(member) + '.' + str(value)
        return value
    elif member.mtype == REFERENCE_IDENTITY_CLASS:
        value = _dash_to_underscore(value._meta_info().module_name) + _get_class_name(member) + '.' + value.__class__.__name__ + '()'
        return value
    else:
        return _escape_value(value)


def _get_class_name(member):
    clazz_name = '.'.join(member.clazz_name.split('.')[:-1])
    if clazz_name == '':
        clazz_name = ''
    else:
        clazz_name = '.' + clazz_name
    return clazz_name


def _dash_to_underscore(name):
    import keyword
    if keyword.iskeyword(name) or name in ('None', 'parent'):
        return name.replace('-', '_') + '_'
    return name.replace('-', '_')


def _escape_value(value):
    if isinstance(value, str):
        return "'" + str(value) + "'"
    return str(value)


def _get_module_name(full_name):
    return full_name.split('.')[-1]
