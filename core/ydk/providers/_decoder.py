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
""" _decoder.py

   Decoder.

"""
from lxml import etree
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LEAFLIST, \
            REFERENCE_LIST, REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, \
            REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS
from ydk.types import Empty, Decimal64, YLeafList
from ._importer import _yang_ns
from ydk.services.meta_service import MetaService
from ydk.errors import YPYServiceProviderError, YPYErrorCode

import logging
import importlib
from functools import reduce


class XmlDecoder(object):

    def decode(self, payload):
        payload_tree = etree.fromstring(payload.encode('utf-8'))
        top_entity = self._get_top_entity(payload_tree)
        rt = payload_tree.getroottree().getroot()

        curr_rt = get_root(rt, top_entity, _yang_ns._namespaces)
        try:
            XmlDecoder._bind_to_object_helper(curr_rt, top_entity)
        except Exception as e:
            e.payload = payload
            raise e
        return top_entity

    def get_top_container_for_namespace(self, namespace, text):
        entity_import = _yang_ns._namespace_package_map[(namespace, text)]
        exec(entity_import)
        top_entity = eval('%s()' % entity_import.split()[-1])
        return top_entity

    def _get_top_entity(self, payload_tree):
        root = payload_tree.getroottree().getroot()
        namespace = root.tag.split('}')[0][1:]
        prefix = root.tag.split('}')[1]
        return self.get_top_container_for_namespace(namespace, prefix)

    @staticmethod
    def _bind_to_object(payload, top_entity, capabilities, pretty_p='|-'):
        active_deviation_tables = MetaService.get_active_deviation_tables(capabilities, top_entity)
        if hasattr(top_entity, 'parent') and top_entity.parent is not None and XmlDecoder()._is_rpc_reply(top_entity.parent):
            prefix = top_entity._meta_info().module_name
            NSMAP = _yang_ns._namespaces
            payload = payload_convert(payload, NSMAP[prefix], 'output')
        else:
            payload = payload_convert(payload, '', '')
        if payload is None:
            return top_entity
        rt = etree.fromstring(payload.encode('utf-8')).getroottree().getroot()
        curr_rt = get_root(rt, top_entity, _yang_ns._namespaces)
        try:
            XmlDecoder._bind_to_object_helper(curr_rt, top_entity, active_deviation_tables, pretty_p='|-')
        except Exception as e:
            e.payload = payload
            raise e

    @staticmethod
    def _bind_to_object_helper(root, entity, deviation_tables={}, pretty_p='|-'):
        if root is None:
            return
        MetaService.inject_imeta(entity, deviation_tables)
        entity_members = entity.i_meta.meta_info_class_members
        for member in entity_members:
            module_name = member.module_name
            nmsp = _yang_ns._namespaces[module_name]
            tag_name = '{' + nmsp + '}' + member.name
            rt = [rt for rt in root.getchildren() if rt.tag == tag_name]
            if rt == []:
                continue

            if member.mtype == ATTRIBUTE:
                entity.__dict__[member.presentation_name] = XmlDecoder._to_real_type(rt, member, entity)
            elif member.mtype == REFERENCE_LEAFLIST:
                entity.__dict__[member.presentation_name] = XmlDecoder._to_real_list_type(rt, member, entity)
            elif member.mtype == REFERENCE_CLASS:
                instance = entity.__dict__[member.presentation_name]
                if instance is None:
                    instance = get_class_instance(member.pmodule_name, member.clazz_name)
                    entity.__dict__[member.presentation_name] = instance
                    instance.parent = entity
                XmlDecoder._bind_to_object_helper(rt[0], instance, deviation_tables, pretty_p + '-|')
            elif member.mtype == REFERENCE_LIST:
                instance = entity.__dict__[member.presentation_name]
                if instance is None:
                    instance = []
                    entity.__dict__[member] = instance
                importlib.import_module(member.pmodule_name)
                for rtchild in rt:
                    # get nested class
                    child = get_class_instance(member.pmodule_name, member.clazz_name)
                    child.parent = entity
                    instance.append(child)
                    XmlDecoder._bind_to_object_helper(rtchild, child, deviation_tables, pretty_p + '-l')
            elif member.mtype == REFERENCE_IDENTITY_CLASS:
                instance = XmlDecoder._bind_to_identity_helper(rt[0], member, entity)
                entity.__dict__[member.presentation_name] = instance
            elif member.mtype == REFERENCE_ENUM_CLASS:
                entity.__dict__[member.presentation_name] = XmlDecoder._bind_to_enum_helper(rt[0], member)
            elif member.mtype == REFERENCE_BITS:
                entity.__dict__[member.presentation_name] = XmlDecoder._bind_to_bits_helper(rt[0], member, entity)
            elif member.mtype == REFERENCE_UNION:
                entity.__dict__[member.presentation_name] = XmlDecoder._to_real_union_type_helper(rt, member, entity)
            elif member.mtype == ANYXML_CLASS:
                for rtchild in rt:
                    for ch in rtchild:
                        namespace = ch.tag.split('}')[0][1:]
                        prefix = ch.tag.split('}')[1]
                        child = XmlDecoder().get_top_container_for_namespace(namespace, prefix)
                        entity.__dict__[child._meta_info().yang_name.replace('-', '_')] = child
                        child.parent = entity
                        XmlDecoder._bind_to_object_helper(ch, child, deviation_tables, pretty_p + '-l')


    @classmethod
    def _to_real_type(cls, elems, member, entity):
        return XmlDecoder._to_real_type_helper(elems[0], member, entity)

    @classmethod
    def _to_real_type_helper(cls, elem, member, entity):
        if elem.text is None:
            return Empty()
        elif member.ptype == 'int' and is_digit(elem.text):
            return int(elem.text)
        elif member.ptype == 'str':
            return elem.text
        elif member.ptype == 'bool':
            return False if elem.text == 'false' else True
        elif member.ptype == 'Decimal64':
            return Decimal64(elem.text)
        elif member.ptype == 'bits':
            return XmlDecoder._bind_to_bits_helper(elem, member, entity)
        elif 'Enum' in member.ptype:
            return XmlDecoder._bind_to_enum_helper(elem, member)
        elif 'Identity' in member.ptype:
            return XmlDecoder._bind_to_identity_helper(elem, member, entity)
        return None

    @classmethod
    def _to_real_list_type(cls, elems, member, entity):

        if isinstance(elems, list):
            results = YLeafList()
            results.parent = entity
            results.name = member.presentation_name
            for elem in elems:
                result = XmlDecoder._to_real_type_helper(elem, member, entity)
                if result is None:
                    return None
                results.append(result)
            results.parent = entity
            return results
        else:
            return XmlDecoder._to_real_type_helper(elems[0], member, entity)

    @classmethod
    def _to_real_union_type_helper(cls, rt, member, entity):
        potential_str_value = ''
        for contained_member in member.members:
            if contained_member.mtype == REFERENCE_UNION:
                return XmlDecoder._to_real_union_type_helper(rt, contained_member, entity)
            elif contained_member.mtype == REFERENCE_LEAFLIST:
                result = XmlDecoder._to_real_list_type(rt, contained_member, entity)
                if result is not None:
                    return result
                else:
                    continue
            elif contained_member.mtype == REFERENCE_ENUM_CLASS:
                clazz = get_class(contained_member.pmodule_name, contained_member.clazz_name)
                meta_info = getattr(clazz, '_meta_info')()
                enum_literal_key = rt[0].text
                if enum_literal_key in meta_info.literal_map:
                    enum_literal = meta_info.literal_map[enum_literal_key]
                    return getattr(clazz, enum_literal)
            elif contained_member.mtype == REFERENCE_IDENTITY_CLASS:
                return XmlDecoder._bind_to_identity_helper(rt[0], member, entity)

            elif contained_member.mtype == REFERENCE_BITS:
                return XmlDecoder._bind_to_bits_helper(rt[0], member, entity)
            elif contained_member.ptype == 'bool' and rt[0] in ['false', 'true']:
                if rt[0] == 'false':
                    return False
                else:
                    return True
            elif contained_member.ptype == 'str':
                if is_digit(rt[0].text):
                    potential_str_value = rt[0].text
                    continue
                return rt[0].text
            elif contained_member.ptype == 'int' and rt[0].text is not None and is_digit(rt[0].text):
                return int(rt[0].text)
            elif contained_member.ptype == 'Decimal64' and rt[0].text is not None:
                try:
                    float(rt[0].text)
                    return Decimal64(rt[0].text)
                except ValueError:
                    ydk_logger = logging.getLogger(__name__)
                    ydk_logger.error('Got a ValueError converting a Decimal64 type to float')
                pass
            elif contained_member.ptype == 'Empty' and rt[0].text is None:
                return Empty()

        if len(potential_str_value) > 0:
            return potential_str_value

        return None

    @staticmethod
    def _bind_to_bits_helper(elem, member, entity):
        keys = elem.text.split(" ")
        for key in keys:
            entity.__dict__[member.presentation_name][key] = True
        return entity.__dict__[member.presentation_name]

    @staticmethod
    def _bind_to_enum_helper(elem, member):
        enum_clazz = get_class(member.pmodule_name, member.clazz_name)
        meta_info = enum_clazz._meta_info()
        enum_literal_key = elem.text
        if enum_literal_key not in meta_info.literal_map:
            sp_logger = logging.getLogger(__name__)
            values = ','.join(meta_info.literal_map)
            sp_logger.error('Cannot find enum literal with name %s in enum clazz %s(%s) trying with different case',
                            enum_literal_key, member.clazz_name, values)
            # hack change the case and check
            if enum_literal_key.upper() in meta_info.literal_map:
                sp_logger.debug('Found literal using secondary mechanism')
                enum_literal = meta_info.literal_map[enum_literal_key.upper()]
                return getattr(enum_clazz, enum_literal)

            elif enum_literal_key.lower() in meta_info.literal_map:
                sp_logger.debug('Found literal using secondary mechanism')
                enum_literal = meta_info.literal_map[enum_literal_key.lower()]
                return getattr(enum_clazz, enum_literal)
        else:
            enum_literal = meta_info.literal_map[enum_literal_key]
            return getattr(enum_clazz, enum_literal)

    @staticmethod
    def _bind_to_identity_helper(elem, member, entity):
        identity_mod_name = None
        identity_name = None
        if ':' in elem.text:
            (prefix, identity_name) = elem.text.split(':')
            identity_ns = elem.nsmap[prefix]
            identity_mod_name = None
            # find the module name corresponding to this identity_ns
            for mod_name in _yang_ns._namespaces:
                if identity_ns == _yang_ns._namespaces[mod_name]:
                    identity_mod_name = mod_name
                    break
        else:
            identity_mod_name = entity.i_meta.module_name
            identity_name = elem.text
        py_mod_name = None
        if not (identity_mod_name, identity_name) in _yang_ns._identity_map:
            # this is a hack on some platforms the identity mod_name is not available
            sp_logger = logging.getLogger(__name__)
            sp_logger.error('Could not find identity tuple (%s, %s) in identity_map, trying secondary mechanism', identity_mod_name, identity_name)
            identities_with_name = [(x, y) for (x, y) in _yang_ns._identity_map if y == identity_name]
            if len(identities_with_name) == 0:
                sp_logger.error('Secondary mechanism failed no identity with name %s found', identity_name)
            elif len(identities_with_name) > 1:
                sp_logger.error('Secondary mechanism failed more than one identity with name %s found', identity_name)
            else:
                (py_mod_name, identity_clazz_name) = _yang_ns._identity_map[identities_with_name[0]]
                sp_logger.debug('Secondary mechanism succeeded identity with name %s found in module %s', identity_name, py_mod_name)
        else:
            (py_mod_name, identity_clazz_name) = _yang_ns._identity_map[(identity_mod_name, identity_name)]
        if py_mod_name is not None:
            instance = get_class_instance(py_mod_name, identity_clazz_name)
            return instance

    def _is_rpc_reply(self, top_entity):
        return hasattr(top_entity, 'is_rpc') and top_entity.is_rpc


def get_class(py_mod_name, clazz_name):
    module = importlib.import_module(py_mod_name)
    return reduce(getattr, clazz_name.split('.'), module)


def get_class_instance(py_mod_name, clazz_name):
    return get_class(py_mod_name, clazz_name)()


def get_root(payload_root, top_entity, NSMAP):
    prefix = top_entity._meta_info().module_name
    tag = top_entity._meta_info().yang_name
    namespace = NSMAP[prefix]
    if payload_root.tag == 'rpc-reply':
        root = payload_root.find('{}:{}'.format(prefix, tag), namespaces=NSMAP)
    elif payload_root.tag == '{{{}}}{}'.format(namespace, tag):
        root = payload_root
    else:
        raise YPYServiceProviderError(error_code=YPYErrorCode.INVALID_DECODE_VALUE)

    return root


def payload_convert(payload, namespace, prefix):
    # TODO add feature to detect types of payload: JSON or xml
    # drop namespaces and key_val pairs
    rt_new = etree.Element('rpc-reply')
    rt = etree.fromstring(payload.encode('utf-8'))
    if len(namespace) > 0 and  len(prefix) > 0:
        rt_new = etree.Element(prefix, attrib={'xmlns':namespace})
        chchs = rt.getchildren()
        for ch in chchs:
            rt_new.append(ch)
    else:
        chchs = rt.getchildren()[0].getchildren()
        for ch in chchs:
            rt_new.append(ch)
    return etree.tostring(rt_new, pretty_print=True, encoding='utf-8').decode('utf-8')


def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False
