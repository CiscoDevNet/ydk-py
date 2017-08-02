""" Cisco_IOS_XR_shellutil_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil package operational data.

This module contains definitions
for the following management objects\:
  system\-time\: System time information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class TimeSource(Enum):
    """
    TimeSource

    Time source

    .. data:: error = 0

    	Error

    .. data:: none = 1

    	Unsynchronized time

    .. data:: ntp = 2

    	Network time protocol

    .. data:: manual = 3

    	User configured

    .. data:: calendar = 4

    	Hardware calendar

    """

    error = Enum.YLeaf(0, "error")

    none = Enum.YLeaf(1, "none")

    ntp = Enum.YLeaf(2, "ntp")

    manual = Enum.YLeaf(3, "manual")

    calendar = Enum.YLeaf(4, "calendar")



class SystemTime(Entity):
    """
    System time information
    
    .. attribute:: clock
    
    	System clock information
    	**type**\:   :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper.SystemTime.Clock>`
    
    .. attribute:: uptime
    
    	System uptime information
    	**type**\:   :py:class:`Uptime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper.SystemTime.Uptime>`
    
    

    """

    _prefix = 'shellutil-oper'
    _revision = '2015-01-07'

    def __init__(self):
        super(SystemTime, self).__init__()
        self._top_entity = None

        self.yang_name = "system-time"
        self.yang_parent_name = "Cisco-IOS-XR-shellutil-oper"

        self.clock = SystemTime.Clock()
        self.clock.parent = self
        self._children_name_map["clock"] = "clock"
        self._children_yang_names.add("clock")

        self.uptime = SystemTime.Uptime()
        self.uptime.parent = self
        self._children_name_map["uptime"] = "uptime"
        self._children_yang_names.add("uptime")


    class Clock(Entity):
        """
        System clock information
        
        .. attribute:: day
        
        	Day [1..31]
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: hour
        
        	Hour [0..23]
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: millisecond
        
        	Millisecond [0..999]
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: minute
        
        	Minute [0..59]
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: month
        
        	Month [1..12]
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: second
        
        	Second [0..60], use 60 for leap\-second
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: time_source
        
        	Time source
        	**type**\:   :py:class:`TimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper.TimeSource>`
        
        .. attribute:: time_zone
        
        	Time zone
        	**type**\:  str
        
        .. attribute:: wday
        
        	Week Day [0..6]
        	**type**\:  int
        
        	**range:** 0..65535
        
        .. attribute:: year
        
        	Year [0..65535]
        	**type**\:  int
        
        	**range:** 0..65535
        
        

        """

        _prefix = 'shellutil-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(SystemTime.Clock, self).__init__()

            self.yang_name = "clock"
            self.yang_parent_name = "system-time"

            self.day = YLeaf(YType.uint8, "day")

            self.hour = YLeaf(YType.uint8, "hour")

            self.millisecond = YLeaf(YType.uint16, "millisecond")

            self.minute = YLeaf(YType.uint8, "minute")

            self.month = YLeaf(YType.uint8, "month")

            self.second = YLeaf(YType.uint8, "second")

            self.time_source = YLeaf(YType.enumeration, "time-source")

            self.time_zone = YLeaf(YType.str, "time-zone")

            self.wday = YLeaf(YType.uint16, "wday")

            self.year = YLeaf(YType.uint16, "year")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("day",
                            "hour",
                            "millisecond",
                            "minute",
                            "month",
                            "second",
                            "time_source",
                            "time_zone",
                            "wday",
                            "year") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SystemTime.Clock, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SystemTime.Clock, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.day.is_set or
                self.hour.is_set or
                self.millisecond.is_set or
                self.minute.is_set or
                self.month.is_set or
                self.second.is_set or
                self.time_source.is_set or
                self.time_zone.is_set or
                self.wday.is_set or
                self.year.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.day.yfilter != YFilter.not_set or
                self.hour.yfilter != YFilter.not_set or
                self.millisecond.yfilter != YFilter.not_set or
                self.minute.yfilter != YFilter.not_set or
                self.month.yfilter != YFilter.not_set or
                self.second.yfilter != YFilter.not_set or
                self.time_source.yfilter != YFilter.not_set or
                self.time_zone.yfilter != YFilter.not_set or
                self.wday.yfilter != YFilter.not_set or
                self.year.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "clock" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-shellutil-oper:system-time/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.day.is_set or self.day.yfilter != YFilter.not_set):
                leaf_name_data.append(self.day.get_name_leafdata())
            if (self.hour.is_set or self.hour.yfilter != YFilter.not_set):
                leaf_name_data.append(self.hour.get_name_leafdata())
            if (self.millisecond.is_set or self.millisecond.yfilter != YFilter.not_set):
                leaf_name_data.append(self.millisecond.get_name_leafdata())
            if (self.minute.is_set or self.minute.yfilter != YFilter.not_set):
                leaf_name_data.append(self.minute.get_name_leafdata())
            if (self.month.is_set or self.month.yfilter != YFilter.not_set):
                leaf_name_data.append(self.month.get_name_leafdata())
            if (self.second.is_set or self.second.yfilter != YFilter.not_set):
                leaf_name_data.append(self.second.get_name_leafdata())
            if (self.time_source.is_set or self.time_source.yfilter != YFilter.not_set):
                leaf_name_data.append(self.time_source.get_name_leafdata())
            if (self.time_zone.is_set or self.time_zone.yfilter != YFilter.not_set):
                leaf_name_data.append(self.time_zone.get_name_leafdata())
            if (self.wday.is_set or self.wday.yfilter != YFilter.not_set):
                leaf_name_data.append(self.wday.get_name_leafdata())
            if (self.year.is_set or self.year.yfilter != YFilter.not_set):
                leaf_name_data.append(self.year.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "day" or name == "hour" or name == "millisecond" or name == "minute" or name == "month" or name == "second" or name == "time-source" or name == "time-zone" or name == "wday" or name == "year"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "day"):
                self.day = value
                self.day.value_namespace = name_space
                self.day.value_namespace_prefix = name_space_prefix
            if(value_path == "hour"):
                self.hour = value
                self.hour.value_namespace = name_space
                self.hour.value_namespace_prefix = name_space_prefix
            if(value_path == "millisecond"):
                self.millisecond = value
                self.millisecond.value_namespace = name_space
                self.millisecond.value_namespace_prefix = name_space_prefix
            if(value_path == "minute"):
                self.minute = value
                self.minute.value_namespace = name_space
                self.minute.value_namespace_prefix = name_space_prefix
            if(value_path == "month"):
                self.month = value
                self.month.value_namespace = name_space
                self.month.value_namespace_prefix = name_space_prefix
            if(value_path == "second"):
                self.second = value
                self.second.value_namespace = name_space
                self.second.value_namespace_prefix = name_space_prefix
            if(value_path == "time-source"):
                self.time_source = value
                self.time_source.value_namespace = name_space
                self.time_source.value_namespace_prefix = name_space_prefix
            if(value_path == "time-zone"):
                self.time_zone = value
                self.time_zone.value_namespace = name_space
                self.time_zone.value_namespace_prefix = name_space_prefix
            if(value_path == "wday"):
                self.wday = value
                self.wday.value_namespace = name_space
                self.wday.value_namespace_prefix = name_space_prefix
            if(value_path == "year"):
                self.year = value
                self.year.value_namespace = name_space
                self.year.value_namespace_prefix = name_space_prefix


    class Uptime(Entity):
        """
        System uptime information
        
        .. attribute:: host_name
        
        	Host name
        	**type**\:  str
        
        .. attribute:: uptime
        
        	Amount of time in seconds since this system     was last initialized
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: second
        
        

        """

        _prefix = 'shellutil-oper'
        _revision = '2015-01-07'

        def __init__(self):
            super(SystemTime.Uptime, self).__init__()

            self.yang_name = "uptime"
            self.yang_parent_name = "system-time"

            self.host_name = YLeaf(YType.str, "host-name")

            self.uptime = YLeaf(YType.uint32, "uptime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("host_name",
                            "uptime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(SystemTime.Uptime, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SystemTime.Uptime, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.host_name.is_set or
                self.uptime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.host_name.yfilter != YFilter.not_set or
                self.uptime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "uptime" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-shellutil-oper:system-time/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.host_name.is_set or self.host_name.yfilter != YFilter.not_set):
                leaf_name_data.append(self.host_name.get_name_leafdata())
            if (self.uptime.is_set or self.uptime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.uptime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "host-name" or name == "uptime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "host-name"):
                self.host_name = value
                self.host_name.value_namespace = name_space
                self.host_name.value_namespace_prefix = name_space_prefix
            if(value_path == "uptime"):
                self.uptime = value
                self.uptime.value_namespace = name_space
                self.uptime.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.clock is not None and self.clock.has_data()) or
            (self.uptime is not None and self.uptime.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.clock is not None and self.clock.has_operation()) or
            (self.uptime is not None and self.uptime.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-shellutil-oper:system-time" + path_buffer

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

        if (child_yang_name == "clock"):
            if (self.clock is None):
                self.clock = SystemTime.Clock()
                self.clock.parent = self
                self._children_name_map["clock"] = "clock"
            return self.clock

        if (child_yang_name == "uptime"):
            if (self.uptime is None):
                self.uptime = SystemTime.Uptime()
                self.uptime.parent = self
                self._children_name_map["uptime"] = "uptime"
            return self.uptime

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "clock" or name == "uptime"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SystemTime()
        return self._top_entity

