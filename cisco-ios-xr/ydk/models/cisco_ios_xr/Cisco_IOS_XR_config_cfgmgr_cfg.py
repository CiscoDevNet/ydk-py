""" Cisco_IOS_XR_config_cfgmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr package configuration.

This module contains definitions
for the following management objects\:
  cfgmgr\: Cfgmgr configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Cfgmgr(Entity):
    """
    Cfgmgr configuration
    
    .. attribute:: mode_exclusive
    
    	Enabled or Disabled
    	**type**\:  bool
    
    	**default value**\: true
    
    

    """

    _prefix = 'config-cfgmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Cfgmgr, self).__init__()
        self._top_entity = None

        self.yang_name = "cfgmgr"
        self.yang_parent_name = "Cisco-IOS-XR-config-cfgmgr-cfg"

        self.mode_exclusive = YLeaf(YType.boolean, "mode-exclusive")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("mode_exclusive") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Cfgmgr, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Cfgmgr, self).__setattr__(name, value)

    def has_data(self):
        return self.mode_exclusive.is_set

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.mode_exclusive.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-config-cfgmgr-cfg:cfgmgr" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.mode_exclusive.is_set or self.mode_exclusive.yfilter != YFilter.not_set):
            leaf_name_data.append(self.mode_exclusive.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "mode-exclusive"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "mode-exclusive"):
            self.mode_exclusive = value
            self.mode_exclusive.value_namespace = name_space
            self.mode_exclusive.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Cfgmgr()
        return self._top_entity

