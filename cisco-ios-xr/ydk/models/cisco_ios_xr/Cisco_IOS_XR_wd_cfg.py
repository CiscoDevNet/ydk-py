""" Cisco_IOS_XR_wd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wd package configuration.

This module contains definitions
for the following management objects\:
  watchdog\: watchdog

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



class Watchdog(Entity):
    """
    watchdog
    
    .. attribute:: monitor_cpuhog_timeout
    
    	Watchdog monitor cpu\-hog persistent timeout configuration
    	**type**\:  int
    
    	**range:** 10..3600
    
    	**units**\: second
    
    .. attribute:: monitor_procnto_timeout
    
    	Watchdog monitor procnto timeout configuration
    	**type**\:  int
    
    	**range:** 60..3600
    
    	**units**\: second
    
    .. attribute:: monitor_qnet_timeout
    
    	Watchdog monitor transport qnet timeout
    	**type**\:  int
    
    	**range:** 10..3600
    
    	**units**\: second
    
    .. attribute:: overload_notification
    
    	Disable critical event notification
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: overload_throttle_timeout
    
    	Watchdog overload throttle timeout configuration
    	**type**\:  int
    
    	**range:** 5..120
    
    	**units**\: second
    
    .. attribute:: restart_cpuhog_disable
    
    	Disable watchdog restart cpu\-hog
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: restart_deadlock_disable
    
    	Disable watchdog restart deadlock
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: restart_memoryhog_disable
    
    	Disable watchdog restart memory\-hog
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: threshold_memory
    
    	Memory thresholds
    	**type**\:   :py:class:`ThresholdMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_cfg.Watchdog.ThresholdMemory>`
    
    .. attribute:: threshold_memory_switchover
    
    	switchover the RP at configured memory state
    	**type**\:  int
    
    	**range:** 2..4
    
    

    """

    _prefix = 'wd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Watchdog, self).__init__()
        self._top_entity = None

        self.yang_name = "watchdog"
        self.yang_parent_name = "Cisco-IOS-XR-wd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"threshold-memory" : ("threshold_memory", Watchdog.ThresholdMemory)}
        self._child_list_classes = {}

        self.monitor_cpuhog_timeout = YLeaf(YType.uint32, "monitor-cpuhog-timeout")

        self.monitor_procnto_timeout = YLeaf(YType.uint32, "monitor-procnto-timeout")

        self.monitor_qnet_timeout = YLeaf(YType.uint32, "monitor-qnet-timeout")

        self.overload_notification = YLeaf(YType.empty, "overload-notification")

        self.overload_throttle_timeout = YLeaf(YType.uint32, "overload-throttle-timeout")

        self.restart_cpuhog_disable = YLeaf(YType.empty, "restart-cpuhog-disable")

        self.restart_deadlock_disable = YLeaf(YType.empty, "restart-deadlock-disable")

        self.restart_memoryhog_disable = YLeaf(YType.empty, "restart-memoryhog-disable")

        self.threshold_memory_switchover = YLeaf(YType.uint32, "threshold-memory-switchover")

        self.threshold_memory = Watchdog.ThresholdMemory()
        self.threshold_memory.parent = self
        self._children_name_map["threshold_memory"] = "threshold-memory"
        self._children_yang_names.add("threshold-memory")
        self._segment_path = lambda: "Cisco-IOS-XR-wd-cfg:watchdog"

    def __setattr__(self, name, value):
        self._perform_setattr(Watchdog, ['monitor_cpuhog_timeout', 'monitor_procnto_timeout', 'monitor_qnet_timeout', 'overload_notification', 'overload_throttle_timeout', 'restart_cpuhog_disable', 'restart_deadlock_disable', 'restart_memoryhog_disable', 'threshold_memory_switchover'], name, value)


    class ThresholdMemory(Entity):
        """
        Memory thresholds
        
        .. attribute:: critical
        
        	Threshold, Range(3, severe)
        	**type**\:  int
        
        	**range:** 3..40
        
        .. attribute:: minor
        
        	Threshold, Range(5, 40)
        	**type**\:  int
        
        	**range:** 5..40
        
        .. attribute:: severe
        
        	Threshold, Range(4, minor)
        	**type**\:  int
        
        	**range:** 4..40
        
        

        """

        _prefix = 'wd-cfg'
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
            self._absolute_path = lambda: "Cisco-IOS-XR-wd-cfg:watchdog/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Watchdog.ThresholdMemory, ['critical', 'minor', 'severe'], name, value)

    def clone_ptr(self):
        self._top_entity = Watchdog()
        return self._top_entity

