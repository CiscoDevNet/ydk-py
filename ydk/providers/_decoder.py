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
            REFERENCE_BITS, REFERENCE_UNION
from ydk.types import Empty, Decimal64, YLeafList, YListItem
from ydk.models import _yang_ns
from ydk.services.meta_service import MetaService

import logging
import re


class XmlDecoder(object):

    def decode(self, payload):
        payload_tree = etree.fromstring(payload)
        top_entity = self._get_top_entity(payload_tree)
        rt = payload_tree.getroottree().getroot()
        curr_rt = get_root(rt, top_entity._common_path, _yang_ns._namespaces)
        XmlDecoder._bind_to_object_helper(curr_rt, top_entity)
        return top_entity

    def get_top_container_for_namespace(self, namespace, text):
        entity_import = _yang_ns._namespace_package_map[(namespace, text)]
        exec entity_import
        top_entity = eval('%s()' % entity_import.split()[-1])
        return top_entity

    def _get_top_entity(self, payload_tree):
        root = payload_tree.getroottree().getroot()
        namespace = root.tag.split('}')[0][1:]
        return self.get_top_container_for_namespace(namespace, root.tag.split('}')[1])

    @classmethod
    def _to_real_union_type_helper(self, rt, member, entity):
        potential_str_value = ''
        for contained_member in member.members:
            if contained_member.mtype == REFERENCE_UNION:
                return XmlDecoder._to_real_union_type_helper(rt, contained_member, entity)
            elif contained_member.mtype == REFERENCE_LEAFLIST:
                return XmlDecoder._to_real_list_type(rt, contained_member, entity)
            elif contained_member.mtype == REFERENCE_ENUM_CLASS:
                exec_import = 'from ' + contained_member.pmodule_name + ' import ' + contained_member.clazz_name.split('.')[0]
                exec exec_import
                # first get the enum_class
                meta_info = eval('%s._meta_info()' % contained_member.clazz_name)
                enum_literal_key = rt[0].text
                if enum_literal_key in meta_info.literal_map:
                    enum_literal = meta_info.literal_map[enum_literal_key]
                    return eval('%s.%s' % (contained_member.clazz_name, enum_literal))
            elif contained_member.mtype == REFERENCE_IDENTITY_CLASS:
                identity_mod_name = None
                identity_name = None

                if ':' in rt[0]:
                    (prefix, identity_name) = rt[0].text.split(':')
                    identity_ns = rt[0].nsmap[prefix]
                    identity_mod_name = None
                    # find the module name corresponding to this identity_ns
                    for mod_name in _yang_ns._namespaces:
                        if identity_ns == _yang_ns._namespaces[mod_name]:
                            identity_mod_name = mod_name
                            break
                else:
                    identity_mod_name = entity.i_meta.module_name
                    identity_name = rt[0].text

                if (identity_mod_name, identity_name) in _yang_ns._identity_map:
                    (py_mod_name, identity_clazz_name) = _yang_ns._identity_map[(identity_mod_name, identity_name)]
                    exec_import = 'from ' + py_mod_name + ' import ' + identity_clazz_name
                    exec exec_import
                    eval_getinstance = identity_clazz_name + '()'
                    instance = eval(eval_getinstance)
                    return instance

            elif contained_member.mtype == REFERENCE_BITS:
                exec_import = 'from ' + contained_member.pmodule_name + ' import ' + contained_member.clazz_name.split('.')[0]
                exec exec_import
                keys = rt[0].text.split(" ")
                for key in keys:
                    entity.__dict__[member.presentation_name][key] = True
                    return entity.__dict__[member.presentation_name]
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
            elif contained_member.ptype == 'long' and rt[0].text is not None and is_digit(rt[0].text):
                return long(rt[0].text)
            elif contained_member.ptype == 'int' and rt[0].text is not None and is_digit(rt[0].text):
                return int(rt[0].text)
            elif contained_member.ptype == 'Decimal64' and rt[0].text is not None:
                try:
                    float(rt[0].text)
                    return Decimal64(rt[0].text)
                except ValueError:
                    ydk_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')
                    ydk_logger.error('Got a ValueError converting a Decimal64 type to float')
                pass
            elif contained_member.ptype == 'Empty' and rt[0].text is None:
                return Empty()

        if len(potential_str_value) > 0:
            return potential_str_value

        return None

    @classmethod
    def _to_real_type_helper(self, elem, member, entity):
        _type = member.ptype
        text = elem.text
        if text is None:
            return Empty()
        elif _type == 'int':
            if is_digit(text):
                return int(text)
            else:
                return text
            return int(text)
        elif _type == 'long':
            return long(text)
        elif _type == 'str':
            return text
        elif _type == 'bool':
            if text == 'false':
                return False
            else:
                return True
        elif _type == 'Decimal64':
            return Decimal64(text)
        elif _type == 'bits':
            pass
        else:
            pass

    @classmethod
    def _to_real_list_type(self, elems, member, entity):

        if isinstance(elems, list):
            results = YLeafList()
            results.parent = entity
            results.name = member.presentation_name
            for elem in elems:
                result = None
                if 'Enum' in member.ptype:
                    result = XmlDecoder._bind_to_enum_helper(member, elem)
                else:
                    result = XmlDecoder._to_real_type_helper(elem, member, entity)
                results.append(result)
            return results
        else:
            return XmlDecoder._to_real_type_helper(elems[0], member, entity)

    @classmethod
    def _to_real_type(self, elems, member, entity):
        return XmlDecoder._to_real_type_helper(elems[0], member, entity)

    @staticmethod
    def _bind_to_object(payload, entity, capabilities, pretty_p='|-'):
        active_deviation_tables = MetaService.get_active_deviation_tables(capabilities, entity)
        payload = payload_convert(payload)
        if payload is None:
            return entity
        rt = etree.fromstring(payload).getroottree().getroot()
        curr_rt = get_root(rt, entity._common_path, _yang_ns._namespaces)
        XmlDecoder._bind_to_object_helper(curr_rt, entity, active_deviation_tables, pretty_p='|-')

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
            elif (member.mtype == REFERENCE_CLASS):
                instance = entity.__dict__[member.presentation_name]
                if instance is None:
                    exec_import = 'from ' + member.pmodule_name + ' import ' + member.clazz_name.split('.')[0]
                    exec exec_import
                    eval_getinstance = member.clazz_name + '()'
                    instance = eval(eval_getinstance)
                    entity.__dict__[member.presentation_name] = instance
                    instance.parent = entity
                XmlDecoder._bind_to_object_helper(rt[0], instance, deviation_tables, pretty_p + '-|')
            elif member.mtype == REFERENCE_LIST:
                instance = entity.__dict__[member.presentation_name]
                if instance is None:
                    instance = []
                    entity.__dict__[member] = instance
                exec_import = 'from ' + member.pmodule_name + ' import ' + member.clazz_name.split('.')[0]
                exec exec_import
                for rtchild in rt:
                    child = eval(member.clazz_name + '()')
                    child.parent = entity
                    instance.append(child)
                    XmlDecoder._bind_to_object_helper(rtchild, child, deviation_tables, pretty_p + '-l')
            elif member.mtype == REFERENCE_IDENTITY_CLASS:
                identity_mod_name = None
                identity_name = None

                if ':' in rt[0].text:
                    (prefix, identity_name) = rt[0].text.split(':')
                    identity_ns = rt[0].nsmap[prefix]
                    identity_mod_name = None
                    # find the module name corresponding to this identity_ns
                    for mod_name in _yang_ns._namespaces:
                        if identity_ns == _yang_ns._namespaces[mod_name]:
                            identity_mod_name = mod_name
                            break
                else:
                    identity_mod_name = entity.i_meta.module_name
                    identity_name = rt[0].text
                py_mod_name = None
                if not (identity_mod_name, identity_name) in _yang_ns._identity_map:
                    # this is a hack on some platforms the identity mod_name is not available
                    sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')
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
                    exec_import = 'from ' + py_mod_name + ' import ' + identity_clazz_name
                    exec exec_import

                    eval_getinstance = identity_clazz_name + '()'
                    instance = eval(eval_getinstance)
                    entity.__dict__[member.presentation_name] = instance
            elif member.mtype == REFERENCE_ENUM_CLASS:
                entity.__dict__[member.presentation_name] = XmlDecoder._bind_to_enum_helper(member, rt[0])
            elif member.mtype == REFERENCE_BITS:
                exec_import = 'from ' + member.pmodule_name + ' import ' + member.clazz_name.split('.')[0]
                exec exec_import
                keys = rt[0].text.split(" ")
                for key in keys:
                    entity.__dict__[member.presentation_name][key] = True
            elif member.mtype == REFERENCE_UNION:
                entity.__dict__[member.presentation_name] = XmlDecoder._to_real_union_type_helper(rt, member, entity)
    
    @staticmethod
    def _bind_to_enum_helper(member, elem):
        exec_import = 'from ' + member.pmodule_name + ' import ' + member.clazz_name.split('.')[0]
        exec exec_import
        # first get the enum_class
        meta_info = eval('%s._meta_info()' % member.clazz_name)
        enum_literal_key = elem.text
        if enum_literal_key not in meta_info.literal_map:
            sp_logger = logging.getLogger('ydk.providers.NetconfServiceProvider')
            values = ','.join(meta_info.literal_map)
            sp_logger.error('Cannot find enum literal with name %s in enum clazz %s(%s) trying with different case',
                            enum_literal_key, member.clazz_name, values)
            # hack change the case and check
            if enum_literal_key.upper() in meta_info.literal_map:
                sp_logger.debug('Found literal using secondary mechanism')
                enum_literal = meta_info.literal_map[enum_literal_key.upper()]
                return eval('%s.%s' % (member.clazz_name, enum_literal))
            elif enum_literal_key.lower() in meta_info.literal_map:
                sp_logger.debug('Found literal using secondary mechanism')
                enum_literal = meta_info.literal_map[enum_literal_key.lower()]
                return eval('%s.%s' % (member.clazz_name, enum_literal))
        else:
            enum_literal = meta_info.literal_map[enum_literal_key]
            return eval('%s.%s' % (member.clazz_name, enum_literal))


def get_root(root, common_path, module_nmsp):
    common_path = common_path[1:]
    pathlist = []
    while len(common_path) > 0:
        i_l = common_path.find('[')
        if i_l == -1:
            break
        elif i_l != 0:
            pathlist += common_path[:i_l].split('/')
        common_path = common_path[i_l + 1:]
        i_r = common_path.find(']')
        # append it to last path element
        pathlist[-1] += '[' + common_path[:i_r] + ']'
        common_path = common_path[i_r + 1:]
    if len(common_path):
        pathlist += common_path.split('/')
    pathlist = [path for path in pathlist if path != '']

    # XXX:YYY[XXX:ZZZ = abc] => (XXX, YYY[XXX:ZZZ = abc])
    pathlist = [tuple(path.split(':', 1)) for path in pathlist]
    def update_prefix(tu):
        return (module_nmsp[tu[0]],) + tu[1:]
    # replace prefix with actual namespace
    pathlist = map(lambda tu: update_prefix(tu), pathlist)
    # tuple have multiple keys
    def update_tuple(tu):
        if not '[' in tu[1]:
            return tu
        else:
            segs = re.split('[\[\]]', tu[1])
            segs = [seg for seg in segs if seg != '']
            tag_name, key_vals = segs[0], segs[1:]
            key_vals = map(lambda s: s.replace(' ', '').split('='), key_vals)
            key_vals = map(lambda lst: [lst[0].split(':')[1], lst[1]], key_vals)
            _dict = {}
            for k, v in key_vals:
                _dict[k] = v
            return tuple((tu[0], tag_name, _dict))
    # (XXX, YYY[XXX:ZZZ = abc]) => (XXX, YYY, ZZZ, abc)
    # unpack key_val to a key_val dict (prefix, tag_name, key_val_dict)
    pathlist = map(lambda tu: update_tuple(tu), pathlist)
    return get_root_helper(root, pathlist)


def get_root_helper(curr_rt, pathlist):
    while pathlist != []:
        _hd, _tl = pathlist[0], pathlist[1:]
        tag_name = '{' + _hd[0] + '}' + _hd[1]
        if len(_hd) == 2:
            rt_new = [rt for rt in curr_rt.getchildren() if rt.tag == tag_name]
        else:
            # match each key
            for ch in curr_rt.getchildren():
                # multiple ch candidates,
                # return the ch which its ch matches dict specific
                _dict = _hd[2]

                def matches(chch):
                    t = chch.tag.split('}')[1]
                    if t in _dict.keys() and chch.text != _dict[t]:
                        return False
                    else:
                        return True
                _match = reduce(lambda init, chch: matches(chch) and init, ch.getchildren(), True)

                if _match:
                    break
            rt_new = [ch]
        if len(rt_new) == 0:
            return curr_rt
        if len(rt_new) == 1:
            curr_rt = rt_new[0]
        pathlist = _tl
    return curr_rt


def payload_convert(payload):
    # TODO add feature to detect types of payload: JSON or xml
    # drop namespaces and key_val pairs
    rt_new = etree.Element('rpc-reply')
    rt = etree.fromstring(payload)
    chchs = rt.getchildren()[0].getchildren()
    for ch in chchs:
        rt_new.append(ch)

    return etree.tostring(rt_new, pretty_print=True)

def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return  False

