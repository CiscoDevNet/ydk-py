""" Cisco_IOS_XR_wd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wd package configuration.

This module contains definitions
for the following management objects\:
  watchdog\: watchdog

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class Watchdog(Entity):
    """
    watchdog
    
    .. attribute:: threshold_memory
    
    	Memory thresholds
    	**type**\:  :py:class:`ThresholdMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_wd_cfg.Watchdog.ThresholdMemory>`
    
    .. attribute:: threshold_memory_switchover
    
    	switchover the RP at configured memory state
    	**type**\: int
    
    	**range:** 2..4
    
    .. attribute:: restart_deadlock_disable
    
    	Disable watchdog restart deadlock
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: monitor_qnet_timeout
    
    	Watchdog monitor transport qnet timeout
    	**type**\: int
    
    	**range:** 10..3600
    
    	**units**\: second
    
    .. attribute:: monitor_cpuhog_timeout
    
    	Watchdog monitor cpu\-hog persistent timeout configuration
    	**type**\: int
    
    	**range:** 10..3600
    
    	**units**\: second
    
    .. attribute:: monitor_procnto_timeout
    
    	Watchdog monitor procnto timeout configuration
    	**type**\: int
    
    	**range:** 60..3600
    
    	**units**\: second
    
    .. attribute:: overload_notification
    
    	Disable critical event notification
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: restart_cpuhog_disable
    
    	Disable watchdog restart cpu\-hog
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: restart_memoryhog_disable
    
    	Disable watchdog restart memory\-hog
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: overload_throttle_timeout
    
    	Watchdog overload throttle timeout configuration
    	**type**\: int
    
    	**range:** 5..120
    
    	**units**\: second
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("threshold-memory", ("threshold_memory", Watchdog.ThresholdMemory))])
        self._leafs = OrderedDict([
            ('threshold_memory_switchover', (YLeaf(YType.uint32, 'threshold-memory-switchover'), ['int'])),
            ('restart_deadlock_disable', (YLeaf(YType.empty, 'restart-deadlock-disable'), ['Empty'])),
            ('monitor_qnet_timeout', (YLeaf(YType.uint32, 'monitor-qnet-timeout'), ['int'])),
            ('monitor_cpuhog_timeout', (YLeaf(YType.uint32, 'monitor-cpuhog-timeout'), ['int'])),
            ('monitor_procnto_timeout', (YLeaf(YType.uint32, 'monitor-procnto-timeout'), ['int'])),
            ('overload_notification', (YLeaf(YType.empty, 'overload-notification'), ['Empty'])),
            ('restart_cpuhog_disable', (YLeaf(YType.empty, 'restart-cpuhog-disable'), ['Empty'])),
            ('restart_memoryhog_disable', (YLeaf(YType.empty, 'restart-memoryhog-disable'), ['Empty'])),
            ('overload_throttle_timeout', (YLeaf(YType.uint32, 'overload-throttle-timeout'), ['int'])),
        ])
        self.threshold_memory_switchover = None
        self.restart_deadlock_disable = None
        self.monitor_qnet_timeout = None
        self.monitor_cpuhog_timeout = None
        self.monitor_procnto_timeout = None
        self.overload_notification = None
        self.restart_cpuhog_disable = None
        self.restart_memoryhog_disable = None
        self.overload_throttle_timeout = None

        self.threshold_memory = Watchdog.ThresholdMemory()
        self.threshold_memory.parent = self
        self._children_name_map["threshold_memory"] = "threshold-memory"
        self._segment_path = lambda: "Cisco-IOS-XR-wd-cfg:watchdog"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Watchdog, ['threshold_memory_switchover', 'restart_deadlock_disable', 'monitor_qnet_timeout', 'monitor_cpuhog_timeout', 'monitor_procnto_timeout', 'overload_notification', 'restart_cpuhog_disable', 'restart_memoryhog_disable', 'overload_throttle_timeout'], name, value)


    class ThresholdMemory(Entity):
        """
        Memory thresholds
        
        .. attribute:: minor
        
        	Threshold, Range(5, 40)
        	**type**\: int
        
        	**range:** 5..40
        
        .. attribute:: severe
        
        	Threshold, Range(4, minor)
        	**type**\: int
        
        	**range:** 4..40
        
        .. attribute:: critical
        
        	Threshold, Range(3, severe)
        	**type**\: int
        
        	**range:** 3..40
        
        

        """

        _prefix = 'wd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Watchdog.ThresholdMemory, self).__init__()

            self.yang_name = "threshold-memory"
            self.yang_parent_name = "watchdog"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('minor', (YLeaf(YType.uint32, 'minor'), ['int'])),
                ('severe', (YLeaf(YType.uint32, 'severe'), ['int'])),
                ('critical', (YLeaf(YType.uint32, 'critical'), ['int'])),
            ])
            self.minor = None
            self.severe = None
            self.critical = None
            self._segment_path = lambda: "threshold-memory"
            self._absolute_path = lambda: "Cisco-IOS-XR-wd-cfg:watchdog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Watchdog.ThresholdMemory, ['minor', 'severe', 'critical'], name, value)


    def clone_ptr(self):
        self._top_entity = Watchdog()
        return self._top_entity



