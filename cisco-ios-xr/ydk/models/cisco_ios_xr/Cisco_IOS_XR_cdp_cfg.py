""" Cisco_IOS_XR_cdp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cdp package configuration.

This module contains definitions
for the following management objects\:
  cdp\: Global CDP configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Cdp(Entity):
    """
    Global CDP configuration data
    
    .. attribute:: advertise_v1_only
    
    	Enable CDPv1 only advertisements
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable or disable CDP globally
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: hold_time
    
    	Length of time (in sec) that the receiver must keep a CDP packet
    	**type**\:  int
    
    	**range:** 10..255
    
    	**default value**\: 180
    
    .. attribute:: log_adjacency
    
    	Enable logging of adjacency changes
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: timer
    
    	Specify the rate at which CDP packets are sent
    	**type**\:  int
    
    	**range:** 5..255
    
    	**default value**\: 60
    
    

    """

    _prefix = 'cdp-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        super(Cdp, self).__init__()
        self._top_entity = None

        self.yang_name = "cdp"
        self.yang_parent_name = "Cisco-IOS-XR-cdp-cfg"

        self.advertise_v1_only = YLeaf(YType.empty, "advertise-v1-only")

        self.enable = YLeaf(YType.boolean, "enable")

        self.hold_time = YLeaf(YType.uint32, "hold-time")

        self.log_adjacency = YLeaf(YType.empty, "log-adjacency")

        self.timer = YLeaf(YType.uint32, "timer")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("advertise_v1_only",
                        "enable",
                        "hold_time",
                        "log_adjacency",
                        "timer") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Cdp, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Cdp, self).__setattr__(name, value)

    def has_data(self):
        return (
            self.advertise_v1_only.is_set or
            self.enable.is_set or
            self.hold_time.is_set or
            self.log_adjacency.is_set or
            self.timer.is_set)

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.advertise_v1_only.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.hold_time.yfilter != YFilter.not_set or
            self.log_adjacency.yfilter != YFilter.not_set or
            self.timer.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-cdp-cfg:cdp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.advertise_v1_only.is_set or self.advertise_v1_only.yfilter != YFilter.not_set):
            leaf_name_data.append(self.advertise_v1_only.get_name_leafdata())
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
            leaf_name_data.append(self.hold_time.get_name_leafdata())
        if (self.log_adjacency.is_set or self.log_adjacency.yfilter != YFilter.not_set):
            leaf_name_data.append(self.log_adjacency.get_name_leafdata())
        if (self.timer.is_set or self.timer.yfilter != YFilter.not_set):
            leaf_name_data.append(self.timer.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "advertise-v1-only" or name == "enable" or name == "hold-time" or name == "log-adjacency" or name == "timer"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "advertise-v1-only"):
            self.advertise_v1_only = value
            self.advertise_v1_only.value_namespace = name_space
            self.advertise_v1_only.value_namespace_prefix = name_space_prefix
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "hold-time"):
            self.hold_time = value
            self.hold_time.value_namespace = name_space
            self.hold_time.value_namespace_prefix = name_space_prefix
        if(value_path == "log-adjacency"):
            self.log_adjacency = value
            self.log_adjacency.value_namespace = name_space
            self.log_adjacency.value_namespace_prefix = name_space_prefix
        if(value_path == "timer"):
            self.timer = value
            self.timer.value_namespace = name_space
            self.timer.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Cdp()
        return self._top_entity

