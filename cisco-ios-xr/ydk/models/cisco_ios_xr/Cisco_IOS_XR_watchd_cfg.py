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
    Watchdog configuration commands
    
    .. attribute:: threshold_memory
    
    	Memory thresholds
    	**type**\:  :py:class:`ThresholdMemory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg.Watchdog.ThresholdMemory>`
    
    .. attribute:: disk_limit
    
    	Disk thresholds
    	**type**\:  :py:class:`DiskLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_watchd_cfg.Watchdog.DiskLimit>`
    
    .. attribute:: overload_notification
    
    	Disable critical event notification
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: restart_deadlock_disable
    
    	Disable watchdog restart deadlock
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

    _prefix = 'watchd-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(Watchdog, self).__init__()
        self._top_entity = None

        self.yang_name = "watchdog"
        self.yang_parent_name = "Cisco-IOS-XR-watchd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("threshold-memory", ("threshold_memory", Watchdog.ThresholdMemory)), ("disk-limit", ("disk_limit", Watchdog.DiskLimit))])
        self._leafs = OrderedDict([
            ('overload_notification', (YLeaf(YType.empty, 'overload-notification'), ['Empty'])),
            ('restart_deadlock_disable', (YLeaf(YType.empty, 'restart-deadlock-disable'), ['Empty'])),
            ('restart_memoryhog_disable', (YLeaf(YType.empty, 'restart-memoryhog-disable'), ['Empty'])),
            ('overload_throttle_timeout', (YLeaf(YType.uint32, 'overload-throttle-timeout'), ['int'])),
        ])
        self.overload_notification = None
        self.restart_deadlock_disable = None
        self.restart_memoryhog_disable = None
        self.overload_throttle_timeout = None

        self.threshold_memory = Watchdog.ThresholdMemory()
        self.threshold_memory.parent = self
        self._children_name_map["threshold_memory"] = "threshold-memory"

        self.disk_limit = Watchdog.DiskLimit()
        self.disk_limit.parent = self
        self._children_name_map["disk_limit"] = "disk-limit"
        self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Watchdog, ['overload_notification', 'restart_deadlock_disable', 'restart_memoryhog_disable', 'overload_throttle_timeout'], name, value)


    class ThresholdMemory(Entity):
        """
        Memory thresholds
        
        .. attribute:: minor
        
        	Threshold, Range (5, 40)
        	**type**\: int
        
        	**range:** 5..40
        
        .. attribute:: severe
        
        	Threshold, Range (4, minor)
        	**type**\: int
        
        	**range:** 4..40
        
        .. attribute:: critical
        
        	Threshold, Range (3, severe)
        	**type**\: int
        
        	**range:** 3..40
        
        

        """

        _prefix = 'watchd-cfg'
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
            self._absolute_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Watchdog.ThresholdMemory, ['minor', 'severe', 'critical'], name, value)


    class DiskLimit(Entity):
        """
        Disk thresholds
        
        .. attribute:: minor
        
        	Threshold, Range (5, 40)
        	**type**\: int
        
        	**range:** 5..40
        
        .. attribute:: severe
        
        	Threshold, Range (4, minor)
        	**type**\: int
        
        	**range:** 4..40
        
        .. attribute:: critical
        
        	Threshold, Range (3, severe)
        	**type**\: int
        
        	**range:** 3..40
        
        

        """

        _prefix = 'watchd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Watchdog.DiskLimit, self).__init__()

            self.yang_name = "disk-limit"
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
            self._segment_path = lambda: "disk-limit"
            self._absolute_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchdog/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Watchdog.DiskLimit, ['minor', 'severe', 'critical'], name, value)

    def clone_ptr(self):
        self._top_entity = Watchdog()
        return self._top_entity

class Watchd(Entity):
    """
    watchd
    
    .. attribute:: timeout
    
    	Length of timeout in seconds
    	**type**\: int
    
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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
        ])
        self.timeout = None
        self._segment_path = lambda: "Cisco-IOS-XR-watchd-cfg:watchd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Watchd, ['timeout'], name, value)

    def clone_ptr(self):
        self._top_entity = Watchd()
        return self._top_entity

