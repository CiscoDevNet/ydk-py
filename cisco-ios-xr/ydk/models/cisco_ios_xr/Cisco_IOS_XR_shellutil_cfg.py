""" Cisco_IOS_XR_shellutil_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil package configuration.

This module contains definitions
for the following management objects\:
  host\-names\: Container Schema for hostname configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class HostNames(Entity):
    """
    Container Schema for hostname configuration
    
    .. attribute:: host_name
    
    	Configure system's hostname
    	**type**\:  str
    
    

    """

    _prefix = 'shellutil-cfg'
    _revision = '2015-10-12'

    def __init__(self):
        super(HostNames, self).__init__()
        self._top_entity = None

        self.yang_name = "host-names"
        self.yang_parent_name = "Cisco-IOS-XR-shellutil-cfg"

        self.host_name = YLeaf(YType.str, "host-name")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("host_name") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(HostNames, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(HostNames, self).__setattr__(name, value)

    def has_data(self):
        return self.host_name.is_set

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.host_name.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-shellutil-cfg:host-names" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.host_name.is_set or self.host_name.yfilter != YFilter.not_set):
            leaf_name_data.append(self.host_name.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "host-name"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "host-name"):
            self.host_name = value
            self.host_name.value_namespace = name_space
            self.host_name.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = HostNames()
        return self._top_entity

