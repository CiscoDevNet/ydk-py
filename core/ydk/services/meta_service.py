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
import copy
import importlib
from ydk.errors import YPYModelError, YPYServiceError
from ydk.types import YList, READ, DELETE, YListItem, YLeafList
from ydk._core._dm_meta_info import (REFERENCE_CLASS, REFERENCE_LIST,
                                     REFERENCE_LEAFLIST, REFERENCE_UNION,
                                     ANYXML_CLASS)
from .service import Service

_ERR_ARG_CHK = "'capabilities' and 'entity' cannot be None"
_ERR_META_IGNORE_CONFIG = "Ignore config change at the moment"
_ERR_META_MISSING_KEY = "Key {} not found in {}"
_ERR_USER_NOT_SUPPORTED = "Attempt to configure not supported node"
_TYPE_MISMATCH_LLIST = ("Attempt to assign object of type {} to YLeafList {}. "
                        "Please use list append or extend method.")
_TYPE_MISMATCH_LIST = ("Attempt to assign object of type {} to YList {}. "
                       "Please use list append or extend method.")
_TYPE_MISMATCH_CLASS = ("Attempt to assign non YDK entity object"
                        " of type {} to {}")
_ERR_USER_PPOINTER = ("YDK object is not created correctly,"
                      "parent pointer should not point to itself.")


class MetaService(Service):
    """ Meta Service class to modify enttiy meta at run time """

    @classmethod
    def normalize_meta(cls, capabilities, entity):
        """ Get meta information from entity._meta_info(), modify and inject
        i_meta attribute back to entity.

            Args:
                cls: First argument for class method
                capabilities: List of capabilities get from provider
                entity: An instance of YDK object

            Returns:
                entity: An instance of YDK object

            Raises:
                `YPYModelError <ydk.errors.html#ydk.errors.YPYModelError>`_ if
                try to access an unsupported feature.

        """
        if None in (capabilities, entity):
            raise YPYServiceError(error_msg=_ERR_ARG_CHK)
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
        active_pmodule_names = _get_active_deviation_module_names(capabilities, entity)
        deviation_tables = {}
        for pname in active_pmodule_names:
            module = importlib.import_module('ydk.models._deviate._%s' % pname)
            deviation_table = getattr(module, '_deviation_table')
            deviation_tables[pname] = deviation_table

        return deviation_tables

    @classmethod
    def inject_imeta(cls, entity, deviation_tables):
        """ Inject i_meta to entity using existing deviation table

            Args:
                cls: First argument for class method
                deviation_tables: A dictionary of existing deviation tables

        """
        _set_parent_imeta(entity)

        if isinstance(entity, (YList, YLeafList)):
            entity = entity.parent
            MetaService.inject_imeta(entity, deviation_tables.values())
        elif not deviation_tables:
            _inject_imeta_helper(entity)
        else:
            for deviation_table in deviation_tables.values():
                _inject_imeta_helper(entity, deviation_table)


def _set_parent_imeta(entity, child_imeta=None):
    if isinstance(entity, (YList, YLeafList, YListItem)):
        _set_parent_imeta(entity.parent)
    elif entity:
        entity.i_meta = _copy_meta(entity._meta_info())
        if child_imeta:
            child_imeta.parent = entity.i_meta
        if hasattr(entity, 'parent'):
            if entity.parent is entity:
                raise YPYServiceError(error_msg=_ERR_USER_PPOINTER)
            else:
                _set_parent_imeta(entity.parent, entity.i_meta)


def _get_active_deviation_module_names(capabilities, entity):
    """ Return active deviation module names """
    # entity could be a list
    active_dmodule_names = []
    mname = _get_module_name_from_entity(entity)

    if not mname:
        return active_dmodule_names

    for cap in capabilities:
        params = _get_params(cap)
        if params:
            params = _parse_params(params)
            if all(('module' in params and params['module'] == mname,
                    'deviations' in params)):
                active_dmodule_names.extend(params['deviations'].split(','))

    return [name.replace('-', '_') for name in active_dmodule_names]


def _modify_member_meta(full_name, deviation_table, member):
    """ Return modified member meta """
    deviation_typ = deviation_table[full_name]['deviation_typ']

    if deviation_typ == 'not_supported':
        return None

    key_vals = deviation_table[full_name]['keyword_value']
    for key, val in key_vals:
        if key == 'config':
            raise YPYModelError(error_msg=_ERR_META_IGNORE_CONFIG)
        elif key == 'type' and deviation_typ == 'replace':
            member = val
            break
        elif deviation_typ in ('add', 'replace'):
            setattr(member, '_%s' % key, val)
        elif key != 'default':
            try:
                delattr(member, '_%s' % key)
            except:
                raise YPYModelError(error_msg=_ERR_META_MISSING_KEY.format(
                                    key, member.presentation_name))
            delattr(member, '_%s' % key)

    return member


def _inject_imeta_helper(entity, deviation_table={}, parent=None):
    """ Inject i_meta field to entity """
    # leaflist could be a list of primitive types
    if isinstance(entity, YListItem):
        entity = entity.item
        if not hasattr(entity, '_meta_info'):
            return

    if not hasattr(entity, 'i_meta'):
        meta = entity._meta_info()
        new_meta = _copy_meta(meta)
        entity.i_meta = new_meta
        entity.i_meta.parent = parent

    new_members = []
    for idx, member in enumerate(entity.i_meta.meta_info_class_members):
        value = getattr(entity, member.presentation_name)
        if member.mtype not in (REFERENCE_LIST, REFERENCE_CLASS):
            name = member.presentation_name
        else:
            snake_segs = member.presentation_name.split('_')
            name = ''.join([word.title() for word in snake_segs])

        full_name = '.'.join([entity.i_meta.name, name])
        if full_name in deviation_table:
            new_member = _modify_member_meta(full_name, deviation_table, member)
            if new_member is None:
                # not supported
                if any((value is None,
                        isinstance(value, list) and value == [],
                        hasattr(value, '_has_data') and not value._has_data(),
                        isinstance(value, READ),
                        isinstance(value, DELETE))):
                    pass
                else:
                    raise YPYModelError(error_msg=_ERR_USER_NOT_SUPPORTED)
        else:
            new_member = member

        if new_member is not None:
            new_members.append(new_member)

    entity.i_meta.meta_info_class_members = new_members
    for idx, member in enumerate(entity.i_meta.meta_info_class_members):
        value = getattr(entity, member.presentation_name)

        if any((value is None,
                isinstance(value, list) and value == [],
                isinstance(value, (READ, DELETE)))):
            continue
        else:
            _check_type_mismatch(value, member)

        if member.mtype == REFERENCE_LIST:
            for v in value:
                _inject_imeta_helper(v, deviation_table, entity.i_meta)
        elif member.mtype in (REFERENCE_CLASS, ANYXML_CLASS):
            _inject_imeta_helper(value, deviation_table, entity.i_meta)


def _check_type_mismatch(value, member):
    # type mismatches for ATTRIBUTE, REFERENCE_ENUM, REFERENCE_IDENTITY,
    # REFREENCE_BITS and REFREENCE_ANYXML are covered by validation
    if member.mtype == REFERENCE_CLASS:
        value_clazz_name = value.__class__.__name__
        member_clazz_name = member.clazz_name.split('.')[-1]
        if any((# not value.__class__.__module__.startswith('ydk.models'),
                isinstance(value, list),
                value_clazz_name != member_clazz_name)):
            raise YPYServiceError(error_msg=_TYPE_MISMATCH_CLASS.format(
                                  value_clazz_name, member_clazz_name))
    elif member.mtype == REFERENCE_LIST:
        if not type(value) == YList:
            raise YPYServiceError(error_msg=_TYPE_MISMATCH_LIST.format(
                                  value.__class__.__name__, member.name))
    elif member.mtype == REFERENCE_LEAFLIST:
        if not type(value) == YLeafList:
            raise YPYServiceError(error_msg=_TYPE_MISMATCH_LLIST.format(
                                  value.__class__.__name__, member.name))


def _copy_meta(old_meta):
    meta = copy.copy(old_meta)
    members = []

    for old_member in old_meta.meta_info_class_members:
        if old_member.mtype == REFERENCE_UNION:
            member = _copy_union_meta(old_member)
        else:
            member = copy.copy(old_member)
        members.append(member)
    meta.meta_info_class_members = members

    return meta


def _copy_union_meta(old_meta):
    meta = copy.copy(old_meta)

    if old_meta.members is None:
        return old_meta

    members = []
    for old_member in old_meta.members:
        member = _copy_union_meta(old_member)
        members.append(member)
    meta._members = members

    return meta


def _get_module_name_from_entity(entity):
    module_name = None
    if entity and hasattr(entity, '_meta_info'):
        if isinstance(entity, (YList, YLeafList, YListItem)):
            module_name = entity[0]._meta_info().module_name
        else:
            module_name = entity._meta_info().module_name
    return module_name


def _get_params(cap):
    params = None
    if '?' in cap:
        _, params = cap.split('?')
    return params


def _parse_params(raw_params):
    params = {}
    for p in raw_params.split('&'):
        name, value = p.split('=')
        params[name] = value
    return params
