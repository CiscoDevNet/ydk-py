""" Cisco_IOS_XR_infra_infra_clock_linux_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-clock\-linux package configuration.

This module contains definitions
for the following management objects\:
  clock\: Configure time\-of\-day clock

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Clock(Entity):
    """
    Configure time\-of\-day clock
    
    .. attribute:: time_zone
    
    	Configure time zone
    	**type**\:   :py:class:`TimeZone <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_clock_linux_cfg.Clock.TimeZone>`
    
    	**presence node**\: True
    
    

    """

    _prefix = 'infra-infra-clock-linux-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Clock, self).__init__()
        self._top_entity = None

        self.yang_name = "clock"
        self.yang_parent_name = "Cisco-IOS-XR-infra-infra-clock-linux-cfg"

        self.time_zone = None
        self._children_name_map["time_zone"] = "time-zone"
        self._children_yang_names.add("time-zone")


    class TimeZone(Entity):
        """
        Configure time zone
        
        .. attribute:: area_name
        
        	Area File in zoneinfo package
        	**type**\:  str
        
        	**mandatory**\: True
        
        .. attribute:: time_zone_name
        
        	Name of time zone
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-linux-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Clock.TimeZone, self).__init__()

            self.yang_name = "time-zone"
            self.yang_parent_name = "clock"
            self.is_presence_container = True

            self.area_name = YLeaf(YType.str, "area-name")

            self.time_zone_name = YLeaf(YType.str, "time-zone-name")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("area_name",
                            "time_zone_name") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Clock.TimeZone, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Clock.TimeZone, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.area_name.is_set or
                self.time_zone_name.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.area_name.yfilter != YFilter.not_set or
                self.time_zone_name.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "time-zone" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.area_name.is_set or self.area_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.area_name.get_name_leafdata())
            if (self.time_zone_name.is_set or self.time_zone_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.time_zone_name.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "area-name" or name == "time-zone-name"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "area-name"):
                self.area_name = value
                self.area_name.value_namespace = name_space
                self.area_name.value_namespace_prefix = name_space_prefix
            if(value_path == "time-zone-name"):
                self.time_zone_name = value
                self.time_zone_name.value_namespace = name_space
                self.time_zone_name.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (self.time_zone is not None)

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.time_zone is not None and self.time_zone.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock" + path_buffer

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

        if (child_yang_name == "time-zone"):
            if (self.time_zone is None):
                self.time_zone = Clock.TimeZone()
                self.time_zone.parent = self
                self._children_name_map["time_zone"] = "time-zone"
            return self.time_zone

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "time-zone"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Clock()
        return self._top_entity

