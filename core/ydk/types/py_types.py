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

""" py_types.py

    Contains python-cpp glue code for:
        - YList
        - YLeafList
        - Entity
"""
from collections import OrderedDict
from functools import reduce

import importlib
import logging

import sys
if sys.version_info > (3,):
    long = int
    unicode = str

from ydk_ import is_set
from ydk.ext.types import Bits
from ydk.ext.types import ChildrenMap
from ydk.ext.types import Enum as _Enum
from ydk.ext.types import YLeaf as _YLeaf
from ydk.ext.types import YLeafList as _YLeafList
from ydk.ext.types import YType
from ydk.ext.types import Empty
from ydk.ext.types import Decimal64 # Do not remove. Used in eval()
from ydk.ext.types import Entity as _Entity
from ydk.ext.types import LeafDataList
from ydk.filters import YFilter as _YFilter
from ydk.errors import YModelError as _YModelError
from ydk.errors import YInvalidArgumentError
from ydk.errors.error_handler import handle_type_error as _handle_type_error

class YLeafList(_YLeafList):
    """ Wrapper class for YLeafList, add __repr__ and get list slice
    functionalities.
    """
    def __init__(self, ytype, leaf_name):
        super(YLeafList, self).__init__(ytype, leaf_name)
        self.ytype = ytype
        self.leaf_name = leaf_name

    def append(self, item):
        if isinstance(item, _YLeaf):
            item = item.get()
        super(YLeafList, self).append(item)

    def extend(self, items):
        for item in items:
            self.append(item)

    def set(self, other):
        if not isinstance(other, YLeafList):
            raise _YModelError("Invalid value '{}' in '{}'"
                            .format(other, self.leaf_name))
        else:
            super(YLeafList, self).clear()
            for item in other:
                self.append(item)

    def __getitem__(self, arg):
        if isinstance(arg, slice):
            indices = arg.indices(len(self))
            ret = YLeafList(self.ytype, self.leaf_name)
            values = [self.__getitem__(i).get() for i in range(*indices)]
            ret.extend(values)
            return ret
        else:
            arg = len(self) + arg if arg < 0 else arg
            return super(YLeafList, self).__getitem__(arg)

    def __str__(self):
        rep = [i for i in self.getYLeafs()]
        return "%s('%s', %r)" % (self.__class__.__name__, self.leaf_name, rep)


class Entity(_Entity):
    """ Entity wrapper class overrides some of the ydk::Entity methods.
    """
    def __init__(self):
        super(Entity, self).__init__()
        self._is_frozen = False
        self.parent = None
        self.ylist_key = None
        self.logger = logging.getLogger("ydk.types.Entity")
        self._local_refs = {}
        self._children_name_map = OrderedDict()
        self._children_yang_names = set()
        self._child_classes = OrderedDict()
        self._leafs = OrderedDict()
        self._segment_path = lambda : ''
        self._absolute_path = lambda : ''
        self._python_type_validation_enabled = True

    def __eq__(self, other):
        if not isinstance(other, Entity):
            return False
        return super(Entity, self).__eq__(other)

    def __ne__(self, other):
        if not isinstance(other, Entity):
            return True
        return super(Entity, self).__ne__(other)

    def children(self):
        return self.get_children()

    def get_children(self):
        children = ChildrenMap()

        for name in self.__dict__:
            value = self.__dict__[name]
            if isinstance(value, Entity) and name != '_top_entity':
                if name not in self._children_name_map:
                    continue
                children[name] = value
            elif isinstance(value, YList):
                count=0
                for v in value:
                    if isinstance(v, Entity):
                        if v.get_segment_path() not in children:
                            children[v.get_segment_path()] = v
                        else:
                            children['%s%s' % (v.get_segment_path(), count)] = v
                            count += 1
        # store local refs so that pybind11 does not free the object. See https://github.com/pybind/pybind11/issues/673
        self._local_refs["ydk::children"] = children
        return children

    def get_order_of_children(self):
        order = []
        for yang_name in self._child_classes:
            name = self._child_classes[yang_name][0]
            value = self.__dict__[name]
            if isinstance(value, YList):
                for v in value:
                    if isinstance(v, Entity):
                        order.append(v.get_segment_path())
            elif isinstance(value, Entity):
                order.append(name)
        return order

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        found = False
        self.logger.debug("Looking for '%s'" % (child_yang_name))
        if child_yang_name in self._child_classes:
            found = True
        else:
            self.logger.debug("Could not find child '%s' in '%s'" % (child_yang_name, self._child_classes))
        if found:
            attr, clazz = self._child_classes[child_yang_name]
            is_list = isinstance(getattr(self, attr), YList)
            child = clazz()
            child.parent = self
            if not is_list:
                self._children_name_map[attr] = child_yang_name
                setattr(self, attr, child)
            else:
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = child
                getattr(self, attr).append(child)

            return child

        return None

    def has_data(self):
        if hasattr(self, 'is_presence_container') and self.is_presence_container:
            return True

        for name, value in vars(self).items():
            if isinstance(value, _YFilter):
                return True
            if name in self._leafs:
                leaf = _get_leaf_object(self._leafs[name])
                if _is_yleaf(leaf):
                    if value is not None:
                        if not isinstance(value, Bits) or len(value.get_bitmap()) > 0:
                            return True
                elif _is_yleaflist(leaf) and len(value) > 0:
                    return True
            if isinstance(value, Entity) and value.has_data():
                return True
            elif isinstance(value, YList):
                for l in value:
                    if l.has_data():
                        return True
        return False

    def has_operation(self):
        if hasattr(self, 'yfilter') and is_set(self.yfilter):
            return True

        for name, value in vars(self).items():
            if value is not None:
                if name in self._leafs:
                    leaf = _get_leaf_object(self._leafs[name])
                    isYLeaf = isinstance(leaf, _YLeaf)
                    isYLeafList = isinstance(leaf, _YLeafList)
                    isBits = isinstance(value, Bits)

                    if type(value) is _YFilter:
                        return True
                    if isYLeaf and (not isBits or len(value.get_bitmap()) > 0):
                        return True
                    if isYLeafList and len(value) > 0:
                        return True
                elif isinstance(value, Entity):
                    if is_set(value.yfilter) or value.has_operation():
                        return True
                elif isinstance(value, YList):
                    for v in value:
                        isEntity = isinstance(v, Entity)
                        if isEntity and (is_set(v.yfilter) or v.has_operation()):
                            return True
        return False

    def set_value(self, path, value, name_space='', name_space_prefix=''):
        for name, leaf in self._leafs.items():
            leaf = _get_leaf_object(leaf)
            if _leaf_name_matches(leaf, path):
                v = _get_decoded_value_object(self._leafs[name], self, value)
                if _is_yleaf(leaf):
                    self._assign_yleaf(name, value, v)
                elif isinstance(leaf, _YLeafList):
                    self._assign_yleaflist(name, value, v)

    def set_filter(self, path, yfilter):
        if hasattr(self, path):
            setattr(self, path, yfilter)

    def has_leaf_or_child_of_name(self, name):
        for _, leaf in self._leafs.items():
            if name == _get_leaf_object(leaf).name:
                return True

        if name in self._child_classes:
            return True

        return False

    def get_name_leaf_data(self):
        leaf_name_data = LeafDataList()
        for name in self._leafs:
            value = self.__dict__[name]
            leaf = _get_leaf_object(self._leafs[name])

            if isinstance(value, _YFilter):
                self.logger.debug('YFilter assigned to "%s", "%s"' % (name, value))
                leaf.yfilter = value
                if isinstance(leaf, _YLeaf):
                    leaf_name_data.append(leaf.get_name_leafdata())
                elif isinstance(leaf, _YLeafList):
                    leaf_name_data.extend(leaf.get_name_leafdata())
            elif (type(value) not in (list, type(None), Bits)
                or (isinstance(value, Bits) and len(value.get_bitmap()) > 0)):
                leaf.set(value)
                leaf_name_data.append(leaf.get_name_leafdata())
            elif isinstance(value, list) and len(value) > 0:
                l = _YLeafList(YType.str, leaf.name)
                # l = self._leafs[name]
                # Above results in YModelError:
                #     Duplicate leaf-list item detected:
                #     /ydktest-sanity:runner/ytypes/built-in-t/enum-llist[.='local'] :
                #     No resolvents found for leafref "../config/id"..
                #     Path: /ydktest-sanity:runner/one-list/identity-list/id-ref
                for item in value:
                    l.append(item)
                leaf_name_data.extend(l.get_name_leafdata())
        self.logger.debug('Get name leaf data for "%s". Count: %s'%(self.yang_name, len(leaf_name_data)))
        for l in leaf_name_data:
            leaf_value = l[1].value
            if "'" in leaf_value:
                leaf_value.replace("'", "\'")
            self.logger.debug('Leaf data name: "%s", value: "%s", yfilter: "%s", is_set: "%s"' % (
            l[0], leaf_value, l[1].yfilter, l[1].is_set))
        return leaf_name_data

    def get_segment_path(self):
        path = self._segment_path()
        if ("[" in path) and hasattr(self, 'ylist_key_names') and len(self.ylist_key_names) > 0:
            path = path.split('[')[0]
            for attr_name in self.ylist_key_names:
                leaf = _get_leaf_object(self._leafs[attr_name])
                if leaf is not None:
                    attr_str = format(self.__dict__[attr_name])
                    if "'" in attr_str:
                        path += '[{}="{}"]'.format(leaf.name, attr_str)
                    else:
                        path += "[{}='{}']".format(leaf.name, attr_str)
                else:
                    # should never get here
                    return self._segment_path()
        elif self.ylist_key is not None:
            # the entity is member of keyless YList
            try:
                index = int(self.ylist_key) % 1000000
            except:
                index = self.ylist_key
            path += '[%s]' % index
        return path

    def path(self):
        return self.get_segment_path()

    def get_absolute_path(self):
        path = self._absolute_path()
        if len(path) == 0 and self.is_top_level_class:
            path = self.get_segment_path()
            if '[' in path:
                path = path.split('[')[0]
        return path

    def _get_child_by_seg_name(self, segs):
        for seg in segs:
            for name in self._children_name_map:
                if seg == self._children_name_map[name]:
                    return self.__dict__[name]
        return None

    def _perform_setattr(self, clazz, leaf_names, name, value):
        with _handle_type_error():
            if name != 'yfilter' and name != 'parent' and name != 'ignore_validation' \
                                 and hasattr(self, '_is_frozen') and self._is_frozen \
                                 and name not in self.__dict__:
                raise _YModelError("Attempt to assign unknown attribute '{0}' to '{1}'.".format(name,
                                                                                            self.__class__.__name__))
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise _YModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if name in leaf_names and name in self.__dict__:
                if self._python_type_validation_enabled:
                    _validate_value(self._leafs[name], name, value, self.logger)
                leaf = _get_leaf_object(self._leafs[name])
                prev_value = self.__dict__[name]
                self.__dict__[name] = value

                if not isinstance(value, _YFilter):
                    if isinstance(leaf, _YLeaf):
                        leaf.set(value)
                    elif isinstance(leaf, _YLeafList):
                        for item in value:
                            leaf.append(item)
                else:
                    self.logger.debug('Setting "%s" to "%s"' % (value, name))
                    leaf.yfilter = value
                    if prev_value is not None:
                        self.logger.debug('Storing previous value "%s" to "%s"' % (prev_value, name))
                        if isinstance(leaf, _YLeaf):
                            leaf.set(prev_value)
                        elif isinstance(leaf, _YLeafList):
                            for item in prev_value:
                                leaf.append(item)

            else:
                if isinstance(value, Entity):
                    if hasattr(value, "parent") and name != "parent":
                        if not value.is_top_level_class:
                            value.parent = self
                super(Entity, self).__setattr__(name, value)

    def _assign_yleaf(self, name, value, v):
        if isinstance(self.__dict__[name], Bits):
            self.__dict__[name][value] = True
        else:
            if v is not None:
                self.__dict__[name] = v
            else:
                self.__dict__[name] = value

    def _assign_yleaflist(self, name, value, v):
        if v is not None:
            self.__dict__[name].append(v)
        else:
            self.__dict__[name].append(value)

    def __str__(self):
        return "{}.{}".format(self.__class__.__module__, self.__class__.__name__)


def _name_matches_yang_name(name, yang_name):
    return name == yang_name or yang_name.endswith(':'+name)


class EntityCollection(object):
    """ EntityCollection is a wrapper class around ordered dictionary collection of type OrderedDict.
    It is created specifically to collect Entity class instances,
    Each Entity instance has unique segment path value, which is used as a key in the dictionary.
    """
    def __init__(self, *entities):
        self.logger = logging.getLogger("ydk.types.EntityCollection")
        self._entity_map = OrderedDict()
        for entity in entities:
            self.append(entity)

    def __eq__(self, other):
        if not isinstance(other, EntityCollection):
            return False
        return self._entity_map.__eq__(other._entity_map)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return self._entity_map.__len__()

    def _key(self, entity):
        return entity.path();

    def append(self, entities):
        """
        Adds new elements to the end of the dictionary. Allowed entries:
          - instance of Entity class
          - list of Entity class instances
        """
        if entities is None:
            self.logger.debug("Cannot add None object to the EntityCollection")
        elif isinstance(entities, Entity):
            key = self._key(entities)
            self._entity_map[key] = entities
        elif isinstance(entities, list):
            for entity in entities:
                if isinstance(entity, Entity):
                    key = self._key(entity)
                    self._entity_map[key] = entity
                elif entity is None:
                    self.logger.debug("Cannot add None object to the EntityCollection")
                else:
                    msg = "Argument %s is not supported by EntityCollection class; data ignored"%type(entity)
                    self._log_error_and_raise_exception(msg, YInvalidArgumentError)
        else:
            msg = "Argument %s is not supported by EntityCollection class; data ignored"%type(entities)
            self._log_error_and_raise_exception(msg, YInvalidArgumentError)

    def _log_error_and_raise_exception(self, msg, exception_class):
        self.logger.error(msg)
        raise exception_class(msg)

    def entities(self):
        """
        Returns list of all entities in the collection.
        If collection is empty, it returns an empty list.
        """
        return list(self._entity_map.values())

    def keys(self):
        """
        Returns list of keys for the collection entities.
        If collection is empty, it returns an empty list.
        """
        return list(self._entity_map.keys())

    def has_key(self, key):
        return key in self.keys()

    def get(self, item):
        return self.__getitem__(item)

    def __getitem__(self, item):
        """
        Returns entity store in the collection.
        Parameter 'item' could be:
         - a type of int (ordered number of entity)
         - type of str (segment path of entity)
         - instance of Entity class
        """
        entity = None
        if isinstance(item, int):
            if 0 <= item < len(self):
                entity = self.entities()[item]
        elif isinstance(item, str):
            if item in self.keys():
                entity = self._entity_map[item]
        elif isinstance(item, Entity):
            key = self._key(item)
            if key in self.keys():
                entity = self._entity_map[key]
        else:
            msg = "Argument %s is not supported by EntityCollection class; data ignored"%type(item)
            self._log_error_and_raise_exception(msg, YInvalidArgumentError)
        return entity

    def clear(self):
        """Deletes all the members of collection"""
        self._entity_map.clear()

    def pop(self, item=None):
        """
        Deletes collection item.
        Parameter 'item' could be:
         - type of int (ordered number of entity)
         - type of str (segment path of entity)
         - instance of Entity class
        Returns entity of deleted instance or None if item is not found.
        """
        entity = None
        if len(self) == 0:
            pass
        elif item is None:
            key, entity = self._entity_map.popitem()
        elif isinstance(item, int):
            entity = self.__getitem__(item)
            if entity is not None:
                key = self._key(entity)
                entity = self._entity_map.pop(key)
        elif isinstance(item, str):
            if item in self.keys():
                entity = self._entity_map.pop(item)
        elif isinstance(item, Entity):
            key = self._key(item)
            if key in self.keys():
                entity = self._entity_map.pop(key)
        return entity

    def __delitem__(self, item):
        return self.pop(item)

    def __iter__(self):
        return iter(self.entities())

    def __str__(self):
        ent_strs = list();
        for entity in self.entities():
            ent_strs.append(format(entity))
        return "Entities in {}: {}".format(self.__class__.__name__, ent_strs)


class Filter(EntityCollection):
    pass


class Config(EntityCollection):
    pass


class YList(EntityCollection):
    """ Represents a list with support for hanging a parent

        All YANG based entity classes that have lists in them use YList
        to represent the list.

        The "list" statement is used to define an interior data node in the
        schema tree.  A list node may exist in multiple instances in the data
        tree.  Each such instance is known as a list entry.  The "list"
        statement takes one argument, which is an identifier, followed by a
        block of sub-statements that holds detailed list information.

        A list entry is uniquely identified by the values of the list's keys, if defined.
        The keys then could be used to get entities from the YList.
    """
    def __init__(self, parent):
        super(YList, self).__init__()
        self.parent = parent
        self.counter = 1000000
        self._cache_dict = OrderedDict()

    def __setattr__(self, name, value):
        if name == 'yfilter' and isinstance(value, _YFilter):
            for e in self:
                e.yfilter = value
        super(YList, self).__setattr__(name, value)

    def _key(self, entity):
        key_list = []
        if hasattr(entity, 'ylist_key_names'):
            for key in entity.ylist_key_names:
                if hasattr(entity, key):
                    attr = entity.__dict__[key]
                    if attr is None:
                        key_list = []
                        break
                    key_list.append(attr)
        if len(key_list) == 0:
            self.counter += 1
            key = format(self.counter)
        elif len(key_list) == 1:
            key = key_list[0]
            if not isinstance(key, str):
                key = format(key)
        else:
            key = tuple(key_list)
        return key

    def _flush_cache(self):
        for _ in range(len(self._cache_dict)):
            _, entity = self._cache_dict.popitem(False)
            self._entity_map[self._key(entity)] = entity

    def append(self, entities):
        entities.parent = self.parent
        if entities is None:
            self._log_error_and_raise_exception("Cannot add None object to the YList", YInvalidArgumentError)
        elif isinstance(entities, Entity):
            key = self._key(entities)
            self._cache_dict[key] = entities
            entities.ylist_key = key
        else:
            msg = "Argument %s is not supported by YList class; data ignored"%type(entities)
            self._log_error_and_raise_exception(msg, YInvalidArgumentError)

    def extend(self, entity_list):
        for entity in entity_list:
            self.append(entity)

    def clear(self):
        """Deletes all the members of collection"""
        self._entity_map.clear()
        self._cache_dict.clear()

    def keys(self):
        self._flush_cache()
        return super(YList, self).keys()

    def entities(self):
        self._flush_cache()
        return super(YList, self).entities()

    def pop(self, item=None):
        self._flush_cache()
        return super(YList, self).pop(item)

    def __getitem__(self, item):
        entity = None
        if isinstance(item, int) and 0 <= item < len(self):
            entity = self.entities()[item]
        elif self.has_key(item):
            entity = self._entity_map[item]
        elif not isinstance(item, str):
            entity = self._entity_map[format(item)]
        return entity

    def __len__(self):
        return self._entity_map.__len__() + self._cache_dict.__len__()


def _get_bundle_name(entity):
    mod_name = str(getattr(entity, '__module__'))
    return mod_name.split('.')[2]


def _get_bundle_yang_ns(bundle_name):
    mod_yang_ns = None
    from ydk import models
    import pkgutil
    for (_, name, ispkg) in pkgutil.iter_modules(models.__path__):
        if ispkg and name == bundle_name:
            try:
                mod_yang_ns = importlib.import_module('ydk.models.{}._yang_ns'.format(name))
                break
            except ImportError:
                continue
    return mod_yang_ns


def _get_class(py_mod_name, clazz_name):
    module = importlib.import_module(py_mod_name)
    return reduce(getattr, clazz_name.split('.'), module)


def _get_class_instance(py_mod_name, clazz_name):
    return _get_class(py_mod_name, clazz_name)()


def _get_decoded_value_object(leaf_tuple, entity, value):
    if not isinstance(leaf_tuple, tuple):
        return None
    typs = leaf_tuple[1]
    value_object = None
    for typ in typs:
        if _is_identity(typ):
            value_object = _decode_identity_value_object(entity, value)
        elif _is_enum(typ):
            value_object = _decode_enum_value_object(typ, value)
        else:
            value_object = _decode_other_type_value_object(typ, value)
        if value_object is not None:
            return value_object


def _validate_value(leaf_tuple, name, value, logger):
    if not isinstance(leaf_tuple, tuple):
        return
    if isinstance(value, _YFilter):
        return
    typs = leaf_tuple[1]
    for typ in typs:
        if _is_identity(typ):
            if _validate_identity_value_object(typ, value):
                return
        elif _is_enum(typ):
            if _validate_enum_value_object(typ, value):
                return
        else:
            if _validate_other_type_value_object(typ, value):
                return
    err_msg = "Invalid value {0} for '{1}'. Got type: '{2}'. Expected types: {3}".format(value, name,
                                                                                         type(value).__name__,
                                                                                         _get_types_string(typs))
    logger.error(err_msg)
    raise _YModelError(err_msg)


def _get_types_string(typs):
    typs_string = []
    for typ in typs:
        if isinstance(typ, tuple):
            s = '.'.join(typ)
            if s.endswith('.'):
                s = s[:-1]
            typs_string.append("'%s'" % s)
        else:
            typs_string.append("'%s'" % typ)
    return ' or '.join(typs_string)


def _is_identity(typ):
    return isinstance(typ, tuple) and len(typ) == 2


def _is_enum(typ):
    return isinstance(typ, tuple) and len(typ) == 3


def _validate_identity_value_object(typ, value):
    if not _is_identity(typ):
        return False
    mod = importlib.import_module(typ[0])
    base_identity_class = getattr(mod, typ[1])
    return isinstance(value, base_identity_class)


def _decode_identity_value_object(entity, value):
    bundle_yang_ns = _get_bundle_yang_ns(_get_bundle_name(entity))
    if 'IDENTITY_LOOKUP' in bundle_yang_ns.__dict__:
        identity_lookup = bundle_yang_ns.__dict__['IDENTITY_LOOKUP']
        if value in identity_lookup:
            (py_mod_name, identity_clazz_name) = identity_lookup[value]
            return _get_class_instance(py_mod_name, identity_clazz_name)
    return None


def _get_enum_class(module_name, class_name, nested_class_name):
    mod = importlib.import_module(module_name)
    clazz_name = '%s%s' % (class_name, '' if len(nested_class_name) == 0 else '.%s' % (nested_class_name))
    enum_clazz = None
    for c in clazz_name.split('.'):
        if enum_clazz is None:
            enum_clazz = getattr(mod, c)
        else:
            enum_clazz = getattr(enum_clazz, c)
    return enum_clazz


def _validate_enum_value_object(typ, value):
    if not isinstance(value, _Enum.YLeaf):
        return False
    if not _is_enum(typ):
        return False
    enum_clazz = _get_enum_class(typ[0], typ[1], typ[2])
    for _, v in enum_clazz.__dict__.items():
        if isinstance(v, _Enum.YLeaf) and value.name == v.name:
            return True
    return False


def _decode_enum_value_object(typ, value):
    if not _is_enum(typ):
        return None
    enum_clazz = _get_enum_class(typ[0], typ[1], typ[2])
    for _, v in enum_clazz.__dict__.items():
        if isinstance(v, _Enum.YLeaf) and value == v.name:
            return v
    return None


def _validate_other_type_value_object(typ, value):
    if typ == 'Empty':
        return isinstance(value, Empty)
    if typ == 'str' and (isinstance(value, bytes) or isinstance(value, unicode)):
        return True
    if typ == 'int' and (isinstance(value, int) or isinstance(value, long)):
        return True
    typ = eval(typ)
    return isinstance(value, typ)


def _decode_other_type_value_object(typ, value):
    value_object = None
    if typ == 'bool':
        return True if value == 'true' else False
    elif typ == 'Empty':
        return Empty()
    typ = eval(typ)
    try:
        value_object = typ(value)
    except:
        pass
    return value_object


def _get_leaf_object(leaf):
    # Backward compatibility
    if isinstance(leaf, tuple):
        return leaf[0]
    return leaf


def _leaf_name_matches(leaf, path):
    return leaf.name == path


def _is_yleaf(leaf):
    return isinstance(leaf, _YLeaf)


def _is_yleaflist(leaf):
    return isinstance(leaf, _YLeafList)
