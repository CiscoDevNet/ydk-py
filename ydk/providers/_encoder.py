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
""" providers.py 
 
   Service Providers module. Current implementation supports the NetconfServiceProvider which
   uses ncclient (a Netconf client library) to provide CRUD services.
   
"""
from ydk.errors import YPYDataValidationError, YPYError
from ydk.types import Empty, DELETE, READ, Decimal64
from ._validator import validate_entity

class _NetconfEncodeDecodeService(object):
    def __init__(self):
        pass

    def _encode_filter(self, filter, root, optype):
        self._encode(filter, root, optype, True)

    def _encode_value(self, member, member_elem, NSMAP, value):
        import ydk.models._yang_ns as _yang_ns
        from ydk._core._dm_meta_info import REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS

        encoded = True
        if member.mtype == REFERENCE_IDENTITY_CLASS:
            exec 'from %s import %s' % (member.pmodule_name, member.clazz_name.split('.')[0])

            if issubclass(type(value), eval(member.clazz_name)):
                identity_inst = value
                if _yang_ns._namespaces[member.module_name] == _yang_ns._namespaces[identity_inst._meta_info().module_name]:
                    # no need for prefix in this case
                    member_elem.text = identity_inst._meta_info().yang_name
                else:
                    NSMAP['idx'] = _yang_ns._namespaces[identity_inst._meta_info().module_name]
                    member_elem.text = 'idx:%s' % identity_inst._meta_info().yang_name
            else:
                encoded = False

        elif member.mtype == REFERENCE_BITS:
            exec 'from %s import %s' % (member.pmodule_name, member.clazz_name.split('.')[0])

            if isinstance(value, eval(member.clazz_name)):
                bits_value = value
                value = " ".join([k for k in bits_value._dictionary if bits_value._dictionary[k] == True])
                if (len(value) > 1):
                    member_elem.text = value
                else:
                    encoded = False
            else:
                encoded = False
        elif member.mtype == REFERENCE_ENUM_CLASS:
            enum_value = value
            exec_import = 'from ' + member.pmodule_name + ' import ' + member.clazz_name.split('.')[0]
            exec exec_import
            enum_clazz = eval(member.clazz_name)
            literal_map = enum_clazz._meta_info().literal_map
            enum_found = False
            for yang_enum_name in literal_map:
                literal = literal_map[yang_enum_name]
                if enum_value == getattr(enum_clazz, literal) \
                    or enum_value == literal:
                    member_elem.text = yang_enum_name
                    enum_found = True
                    break
            if not enum_found:
                encoded = False
        elif member.ptype == 'bool' and isinstance(value, bool):
            if value is True:
                member_elem.text = 'true'
            else:
                member_elem.text = 'false'
        elif member.ptype == 'Empty' and isinstance(value, Empty):
            pass
        elif member.ptype == 'Decimal64' and isinstance(value, Decimal64):
            member_elem.text = value.s
        elif member.ptype == 'str' and isinstance(value, str):
            member_elem.text = value
        elif member.ptype == 'int' and isinstance(value, int):
            member_elem.text = str(value)
        elif member.ptype == 'long' and isinstance(value, long):
            member_elem.text = str(value)
        else:
            encoded = False

        return encoded


    def _encode(self, entity, root, optype, is_filter=False):
        import ydk.models._yang_ns as _yang_ns
        from lxml import etree
        from ydk._core._dm_meta_info import REFERENCE_CLASS, REFERENCE_LIST , REFERENCE_LEAFLIST, REFERENCE_UNION

        ''' Convert the entity to an xml payload '''
        # if the entity has a parent hierarchy use that to get
        # the parent related envelope that we need
        if not is_filter and hasattr(entity, '_has_data') and not entity._has_data():
            return

        validate_entity(entity, optype)

        elem = etree.SubElement(root, entity._meta_info().yang_name)
        parent_ns = None
        current_parent = root
        while current_parent != None and parent_ns is None:
            parent_ns = current_parent.get('xmlns')
            current_parent = current_parent.getparent()

        if entity._meta_info().namespace is not None and parent_ns != entity._meta_info().namespace:
            elem.set('xmlns', entity._meta_info().namespace)

        for member in entity._meta_info().meta_info_class_members:
            value = eval('entity.%s' % member.presentation_name)
            if value is None or isinstance(value, list) and value == []:
                continue
            # bits
            if hasattr(value, '_has_data') and not value._has_data():
                continue

            member_elem = None
            NSMAP = {}
            if member.mtype not in [REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST] or isinstance(value, DELETE) or isinstance(value, READ):
                member_elem = etree.SubElement(elem, member.name, nsmap=NSMAP)
                if entity._meta_info().namespace is not None and entity._meta_info().namespace != _yang_ns._namespaces[member.module_name]:
                    NSMAP[None] = _yang_ns._namespaces[member.module_name]

            if isinstance(value, DELETE) and not is_filter:
                xc = 'urn:ietf:params:xml:ns:netconf:base:1.0'
                member_elem.set('{' + xc + '}operation', 'delete')
            elif isinstance(value, READ):
                continue
            elif member.mtype == REFERENCE_CLASS:
                self._encode(value, elem, optype)
            elif member.mtype == REFERENCE_LIST:
                child_list = value
                for child in child_list:
                    self._encode(child, elem, optype)
            elif member.mtype == REFERENCE_LEAFLIST and isinstance(value, list):
                for child in value:
                    member_elem = etree.SubElement(elem, member.name, nsmap=NSMAP)
                    if entity._meta_info().namespace is not None and entity._meta_info().namespace != _yang_ns._namespaces[member.module_name]:
                        NSMAP[None] = _yang_ns._namespaces[member.module_name]
                    self._encode_value(member, member_elem, NSMAP, child)
            elif member.mtype == REFERENCE_UNION:
                for contained_member in member.members:
                    # determine what kind of encoding is needed here
                    if self._encode_value(contained_member, member_elem, NSMAP, value):
                        break
                # if not encoded:
                #     raise YPYError('Cannot translate union value')
            else:
                if not self._encode_value(member, member_elem, NSMAP, value):
                    # raise YPYError('Cannot encode value')
                    pass
