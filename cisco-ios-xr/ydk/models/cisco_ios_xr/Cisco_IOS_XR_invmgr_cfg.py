""" Cisco_IOS_XR_invmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR invmgr package configuration.

This module contains definitions
for the following management objects\:
  inventory\-configurations\: Configuration for inventory entities

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InventoryConfigurations(Entity):
    """
    Configuration for inventory entities
    
    .. attribute:: entity_
    
    	Entity name
    	**type**\: list of    :py:class:`Entity_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_invmgr_cfg.InventoryConfigurations.Entity_>`
    
    

    """

    _prefix = 'invmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(InventoryConfigurations, self).__init__()
        self._top_entity = None

        self.yang_name = "inventory-configurations"
        self.yang_parent_name = "Cisco-IOS-XR-invmgr-cfg"

        self.entity_ = YList(self)

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in () and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(InventoryConfigurations, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(InventoryConfigurations, self).__setattr__(name, value)


    class Entity_(Entity):
        """
        Entity name
        
        .. attribute:: name  <key>
        
        	Entity name
        	**type**\:  str
        
        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
        
        .. attribute:: name_xr
        
        	Entity name
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'invmgr-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(InventoryConfigurations.Entity_, self).__init__()

            self.yang_name = "entity"
            self.yang_parent_name = "inventory-configurations"

            self.name = YLeaf(YType.str, "name")

            self.name_xr = YLeaf(YType.str, "name-xr")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("name",
                            "name_xr") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(InventoryConfigurations.Entity_, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(InventoryConfigurations.Entity_, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.name.is_set or
                self.name_xr.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.name.yfilter != YFilter.not_set or
                self.name_xr.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "entity" + "[name='" + self.name.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-invmgr-cfg:inventory-configurations/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name.get_name_leafdata())
            if (self.name_xr.is_set or self.name_xr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.name_xr.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "name" or name == "name-xr"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "name"):
                self.name = value
                self.name.value_namespace = name_space
                self.name.value_namespace_prefix = name_space_prefix
            if(value_path == "name-xr"):
                self.name_xr = value
                self.name_xr.value_namespace = name_space
                self.name_xr.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.entity_:
            if (c.has_data()):
                return True
        return False

    def has_operation(self):
        for c in self.entity_:
            if (c.has_operation()):
                return True
        return self.yfilter != YFilter.not_set

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-invmgr-cfg:inventory-configurations" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "entity"):
            for c in self.entity_:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = InventoryConfigurations.Entity_()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.entity_.append(c)
            return c

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "entity"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = InventoryConfigurations()
        return self._top_entity

