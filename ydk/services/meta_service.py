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
""" meta_services.py 
 
   The MetaService class. Inject i_meta to entity
   
"""
from ydk.errors import YPYModelError
from ydk.types import YList, READ, DELETE, YListItem, YLeafList
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST, \
    REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS
from .service import Service


class MetaService(Service):
    """ Meta Service class to modify enttiy meta at run time """

    @classmethod
    def normalize_meta(cls, capabilities, entity):
        """ Get meta information from entity._meta_info(), modify and inject i_meta attribute back to entity.

            Args:
                cls: First argument for class method
                capabilities: List of capabilities get from provider
                entity: An instance of YDK object

            Returns:
                entity: An instance of YDK object

            Raises:
                `YPYModelError <ydk.errors.html#ydk.errors.YPYModelError>`_ if try to access an unsupported feature.

        """
        deviation_tables = MetaService.get_active_deviation_tables(capabilities, entity)
        MetaService.inject_imeta(entity, deviation_tables)
        return entity

    @classmethod
    def get_active_deviation_tables(cls, capabilities, entity):
        """ Return active deviation tables

            Args:
                cls: First argument for class method
                capabilities: List of capabilities get from provider
                enttiy: An instance of YDk object

            Returns:
                deviation_tables: A dictionary for deviation tables

        """
        active_dmodule_names = get_active_deviation_module_names(capabilities, entity)
        deviation_tables = {}
        active_pmodule_names = [name.replace('-', '_') for name in active_dmodule_names]
        for pname in active_pmodule_names:
            import_stmt = 'from ydk.models._deviate import _%s as %s' % (pname, pname)
            exec import_stmt
            deviation_table = eval(pname + '._deviation_table')
            deviation_tables[pname] = deviation_table

        return deviation_tables

    @classmethod
    def inject_imeta(cls, entity, deviation_tables):
        """ Inject i_meta to entity using existing deviation table

            Args:
                cls: First argument for class method
                deviation_tables: A dictionary of existing deviation tables

        """

        if hasattr(entity, 'parent'):
            set_parent_imeta(entity)

        if isinstance(entity, YList) or isinstance(entity, YLeafList):
            entity = entity.parent
            MetaService.inject_imeta(entity, deviation_tables)
        else:
            if len(deviation_tables) == 0:
                inject_imeta_helper(entity, deviation_tables)
            else:
                for deviation_table in deviation_tables.values():
                    inject_imeta_helper(entity, deviation_table)


def set_parent_imeta(entity, child_meta=None):
    if isinstance(entity, YList) or isinstance(entity, YLeafList) or isinstance(entity, YListItem):
        set_parent_imeta(entity.parent, child_meta)
    elif entity:
        entity.i_meta = entity._meta_info()
        if hasattr(entity, 'parent'):
            set_parent_imeta(entity.parent, entity.i_meta)

def get_active_deviation_module_names(capabilities, entity):
    """ Return active deviation module names """
    # entity could be a list
    active_dmodule_names = []
    if isinstance(entity, YList) or isinstance(entity, YLeafList) or isinstance(entity, YListItem):
        if entity and hasattr(entity, '_meta_info'):
            entity_module_name = entity[0]._meta_info().module_name
        else:
            return active_dmodule_names
    else:
        entity_module_name = entity._meta_info().module_name


    def parse_uri(uri):
        if "?" in uri:
            id, params = uri.split("?")
        else:
            id, params = uri, None
        return id, params

    def parse_params(params):
        parameters = {}
        for p in params.split("&"):
            name, value = p.split("=")
            parameters[name] = value
        return parameters

    for uri in capabilities:
        id, params = parse_uri(uri)
        if params is not None:
            parameters = parse_params(params)
            if 'module' in parameters and 'deviations' in parameters and \
                parameters['module'] == entity_module_name:
                active_dmodule_names.extend(parameters['deviations'].split(','))

    return active_dmodule_names

def modify_member_meta(full_name, deviation_table, member):
    """ Return modified member meta """
    deviation_typ = deviation_table[full_name]['deviation_typ']
    if deviation_typ  == 'not_supported':
        return None
    key_vals = deviation_table[full_name]['keyword_value']
    for key, val in key_vals:
        if key == 'config':
            # ignore config change
            raise YPYModelError("Ignore config change at the moment")
        if key == 'type' and deviation_typ == 'replace':
            # should only appear once per deviation
            member = val
            break
        if deviation_typ in ('add', 'replace'):
            try:
                setattr(member, '_%s' % key, val)
            except:
                raise YPYModelError(
                    "Key {} not found in {}".format(member.presentation_name))
        elif key != 'default':
            # TODO: other keyword not necessary to modify in client side
            try:
                delattr(member, '_%s' % key)
            except:
                raise YPYModelError(
                    "Key {} not found in {}".format(member.presentation_name))
    return member


def inject_imeta_helper(entity, deviation_table, parent=None):
    """ Inject i_meta field to entity """
    # leaflist could be a lsit a primitive types
    if isinstance(entity, YListItem):
        entity = entity.item
        if not hasattr(entity, '_meta_info'):
            return

    if not hasattr(entity, 'i_meta'):
        meta = entity._meta_info()
        new_meta = copy_meta(meta)
        entity.i_meta = new_meta
        entity.i_meta.parent = parent

    new_members = []
    for idx, member in enumerate(entity.i_meta.meta_info_class_members):
        value = eval('entity.%s' % member.presentation_name)
        if member.mtype not in (REFERENCE_LIST, REFERENCE_CLASS):
            name = member.presentation_name
        else:
            snake_segs = member.presentation_name.split('_')
            name = ''.join([word.title() for word in snake_segs])

        full_name = '.'.join([entity.i_meta.name, name])
        if full_name in deviation_table:
            new_member = modify_member_meta(full_name, deviation_table, member)
            if new_member is None:
                # not supported
                if value is None or isinstance(value, list) and value == [] or \
                    hasattr(value, '_has_data') and not value._has_data() or \
                    isinstance(value, READ) or isinstance(value, DELETE):
                    pass
                else:
                    raise YPYModelError("Attempt to configure not supported node")
        else:
            new_member = member
        if new_member is not None:
            new_members.append(new_member)

    entity.i_meta.meta_info_class_members = new_members
    for idx, member in enumerate(entity.i_meta.meta_info_class_members):
        value = eval('entity.%s' % member.presentation_name)
        if value is None or isinstance(value, list) and value == []:
            continue
        elif isinstance(value, READ) or isinstance(value, DELETE):
            continue
        elif member.mtype == REFERENCE_LIST:
            for v in value:
                inject_imeta_helper(v, deviation_table, entity.i_meta)
        elif member.mtype in (REFERENCE_CLASS, ANYXML_CLASS):
            inject_imeta_helper(value, deviation_table, entity.i_meta)

def copy_meta(meta):
    """ Return a copy of the meta, an instance of MetaInfoClass"""
    import copy
    # need to copy members in union type if it contains union type
    def copy_union_meta(meta):
        new_meta = copy.copy(meta)
        if meta.members is None:
            return new_meta
        new_members = []
        for member in meta.members:
            new_member = copy_union_meta(member)
            new_members.append(new_member)
        if new_members != []:
            new_meta._members = new_members
        return new_meta

    new_meta = copy.copy(meta)
    new_members = []
    for member in meta.meta_info_class_members:
        if member.mtype == REFERENCE_UNION:
            new_member = copy_union_meta(member)
        else:
            new_member = copy.copy(member)
        new_members.append(new_member)

    new_meta.meta_info_class_members = new_members
    return new_meta
