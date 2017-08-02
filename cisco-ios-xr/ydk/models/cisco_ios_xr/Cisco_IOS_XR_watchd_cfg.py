""" Cisco_IOS_XR_watchd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR watchd package configuration.

This module contains definitions
for the following management objects\:
  watchdog\: Watchdog configuration commands
  watchd\: watchd

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Watchdog(Entity):
    """
    Watchdog configuration commands
    
    .. attribute:: overload_notification
    
    	Disable critical event notification
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: overload_throttle_timeout
    
    	Watchdog overload throttle timeout configuration
    	**type**\:  int
    
    	**range:** 5..120
    
    	**units**\: second
    
    .. attribute:: restart_deadlock_disable
    
    	Disable watchdog restart deadlock
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: restart_memoryhog_disable
    
    	Disable watchdog restart memory\-hog
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: threshold_memory
    
    	Memory thresholds
    	**type**\:   :py:class:`ThresholdMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg.Watchdog.ThresholdMemory>`
    
    

    """

    _prefix = 'watchd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Watchdog, self).__init__()
        self._top_entity = None

        self.yang_name = "watchdog"
        self.yang_parent_name = "Cisco-IOS-XR-watchd-cfg"

        self.overload_notification = YLeaf(YType.empty, "overload-notification")

        self.overload_throttle_timeout = YLeaf(YType.uint32, "overload-throttle-timeout")

        self.restart_deadlock_disable = YLeaf(YType.empty, "restart-deadlock-disable")

        self.restart_memoryhog_disable = YLeaf(YType.empty, "restart-memoryhog-disable")

        self.threshold_memory = Watchdog.ThresholdMemory()
        self.threshold_memory.parent = self
        self._children_name_map["threshold_memory"] = "threshold-memory"
        self._children_yang_names.add("threshold-memory")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("overload_notification",
                        "overload_throttle_timeout",
                        "restart_deadlock_disable",
                        "restart_memoryhog_disable") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Watchdog, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Watchdog, self).__setattr__(name, value)


    class ThresholdMemory(Entity):
        """
        Memory thresholds
        
        .. attribute:: critical
        
        	Threshold, Range (3, severe)
        	**type**\:  int
        
        	**range:** 3..40
        
        .. attribute:: minor
        
        	Threshold, Range (5, 40)
        	**type**\:  int
        
        	**range:** 5..40
        
        .. attribute:: severe
        
        	Threshold, Range (4, minor)
        	**type**\:  int
        
        	**range:** 4..40
        
        

        """

        _prefix = 'watchd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Watchdog.ThresholdMemory, self).__init__()

            self.yang_name = "threshold-memory"
            self.yang_parent_name = "watchdog"

            self.critical = YLeaf(YType.uint32, "critical")

            self.minor = YLeaf(YType.uint32, "minor")

            self.severe = YLeaf(YType.uint32, "severe")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("critical",
                            "minor",
                            "severe") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Watchdog.ThresholdMemory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Watchdog.ThresholdMemory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.critical.is_set or
                self.minor.is_set or
                self.severe.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.critical.yfilter != YFilter.not_set or
                self.minor.yfilter != YFilter.not_set or
                self.severe.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "threshold-memory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-watchd-cfg:watchdog/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.critical.is_set or self.critical.yfilter != YFilter.not_set):
                leaf_name_data.append(self.critical.get_name_leafdata())
            if (self.minor.is_set or self.minor.yfilter != YFilter.not_set):
                leaf_name_data.append(self.minor.get_name_leafdata())
            if (self.severe.is_set or self.severe.yfilter != YFilter.not_set):
                leaf_name_data.append(self.severe.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "critical" or name == "minor" or name == "severe"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "critical"):
                self.critical = value
                self.critical.value_namespace = name_space
                self.critical.value_namespace_prefix = name_space_prefix
            if(value_path == "minor"):
                self.minor = value
                self.minor.value_namespace = name_space
                self.minor.value_namespace_prefix = name_space_prefix
            if(value_path == "severe"):
                self.severe = value
                self.severe.value_namespace = name_space
                self.severe.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.overload_notification.is_set or
            self.overload_throttle_timeout.is_set or
            self.restart_deadlock_disable.is_set or
            self.restart_memoryhog_disable.is_set or
            (self.threshold_memory is not None and self.threshold_memory.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.overload_notification.yfilter != YFilter.not_set or
            self.overload_throttle_timeout.yfilter != YFilter.not_set or
            self.restart_deadlock_disable.yfilter != YFilter.not_set or
            self.restart_memoryhog_disable.yfilter != YFilter.not_set or
            (self.threshold_memory is not None and self.threshold_memory.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-watchd-cfg:watchdog" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.overload_notification.is_set or self.overload_notification.yfilter != YFilter.not_set):
            leaf_name_data.append(self.overload_notification.get_name_leafdata())
        if (self.overload_throttle_timeout.is_set or self.overload_throttle_timeout.yfilter != YFilter.not_set):
            leaf_name_data.append(self.overload_throttle_timeout.get_name_leafdata())
        if (self.restart_deadlock_disable.is_set or self.restart_deadlock_disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.restart_deadlock_disable.get_name_leafdata())
        if (self.restart_memoryhog_disable.is_set or self.restart_memoryhog_disable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.restart_memoryhog_disable.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "threshold-memory"):
            if (self.threshold_memory is None):
                self.threshold_memory = Watchdog.ThresholdMemory()
                self.threshold_memory.parent = self
                self._children_name_map["threshold_memory"] = "threshold-memory"
            return self.threshold_memory

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "threshold-memory" or name == "overload-notification" or name == "overload-throttle-timeout" or name == "restart-deadlock-disable" or name == "restart-memoryhog-disable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "overload-notification"):
            self.overload_notification = value
            self.overload_notification.value_namespace = name_space
            self.overload_notification.value_namespace_prefix = name_space_prefix
        if(value_path == "overload-throttle-timeout"):
            self.overload_throttle_timeout = value
            self.overload_throttle_timeout.value_namespace = name_space
            self.overload_throttle_timeout.value_namespace_prefix = name_space_prefix
        if(value_path == "restart-deadlock-disable"):
            self.restart_deadlock_disable = value
            self.restart_deadlock_disable.value_namespace = name_space
            self.restart_deadlock_disable.value_namespace_prefix = name_space_prefix
        if(value_path == "restart-memoryhog-disable"):
            self.restart_memoryhog_disable = value
            self.restart_memoryhog_disable.value_namespace = name_space
            self.restart_memoryhog_disable.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Watchdog()
        return self._top_entity

class Watchd(Entity):
    """
    watchd
    
    .. attribute:: timeout
    
    	Length of timeout in seconds
    	**type**\:  int
    
    	**range:** 1..10
    
    	**units**\: second
    
    

    """

    _prefix = 'watchd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Watchd, self).__init__()
        self._top_entity = None

        self.yang_name = "watchd"
        self.yang_parent_name = "Cisco-IOS-XR-watchd-cfg"

        self.timeout = YLeaf(YType.uint32, "timeout")

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("timeout") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Watchd, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Watchd, self).__setattr__(name, value)

    def has_data(self):
        return self.timeout.is_set

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.timeout.yfilter != YFilter.not_set)

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-watchd-cfg:watchd" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
            leaf_name_data.append(self.timeout.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "timeout"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "timeout"):
            self.timeout = value
            self.timeout.value_namespace = name_space
            self.timeout.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Watchd()
        return self._top_entity

