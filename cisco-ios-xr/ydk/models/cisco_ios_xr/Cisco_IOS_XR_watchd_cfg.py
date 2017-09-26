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

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {}
        self._child_list_classes = {}

        self.timeout = YLeaf(YType.uint32, "timeout")
        self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchd"

    def __setattr__(self, name, value):
        self._perform_setattr(Watchd, ['timeout'], name, value)

    def clone_ptr(self):
        self._top_entity = Watchd()
        return self._top_entity

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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"threshold-memory" : ("threshold_memory", Watchdog.ThresholdMemory)}
        self._child_list_classes = {}

        self.overload_notification = YLeaf(YType.empty, "overload-notification")

        self.overload_throttle_timeout = YLeaf(YType.uint32, "overload-throttle-timeout")

        self.restart_deadlock_disable = YLeaf(YType.empty, "restart-deadlock-disable")

        self.restart_memoryhog_disable = YLeaf(YType.empty, "restart-memoryhog-disable")

        self.threshold_memory = Watchdog.ThresholdMemory()
        self.threshold_memory.parent = self
        self._children_name_map["threshold_memory"] = "threshold-memory"
        self._children_yang_names.add("threshold-memory")
        self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog"

    def __setattr__(self, name, value):
        self._perform_setattr(Watchdog, ['overload_notification', 'overload_throttle_timeout', 'restart_deadlock_disable', 'restart_memoryhog_disable'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.critical = YLeaf(YType.uint32, "critical")

            self.minor = YLeaf(YType.uint32, "minor")

            self.severe = YLeaf(YType.uint32, "severe")
            self._segment_path = lambda: "threshold-memory"
            self._absolute_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Watchdog.ThresholdMemory, ['critical', 'minor', 'severe'], name, value)

    def clone_ptr(self):
        self._top_entity = Watchdog()
        return self._top_entity

