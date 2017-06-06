""" Cisco_IOS_XR_wd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR wd package configuration.

This module contains definitions
for the following management objects\:
  watchdog\: watchdog

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Watchdog(object):
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
        self.monitor_cpuhog_timeout = None
        self.monitor_procnto_timeout = None
        self.monitor_qnet_timeout = None
        self.overload_notification = None
        self.overload_throttle_timeout = None
        self.restart_cpuhog_disable = None
        self.restart_deadlock_disable = None
        self.restart_memoryhog_disable = None
        self.threshold_memory = Watchdog.ThresholdMemory()
        self.threshold_memory.parent = self
        self.threshold_memory_switchover = None


    class ThresholdMemory(object):
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
            self.parent = None
            self.critical = None
            self.minor = None
            self.severe = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-wd-cfg:watchdog/Cisco-IOS-XR-wd-cfg:threshold-memory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.critical is not None:
                return True

            if self.minor is not None:
                return True

            if self.severe is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_cfg as meta
            return meta._meta_table['Watchdog.ThresholdMemory']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-wd-cfg:watchdog'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.monitor_cpuhog_timeout is not None:
            return True

        if self.monitor_procnto_timeout is not None:
            return True

        if self.monitor_qnet_timeout is not None:
            return True

        if self.overload_notification is not None:
            return True

        if self.overload_throttle_timeout is not None:
            return True

        if self.restart_cpuhog_disable is not None:
            return True

        if self.restart_deadlock_disable is not None:
            return True

        if self.restart_memoryhog_disable is not None:
            return True

        if self.threshold_memory is not None and self.threshold_memory._has_data():
            return True

        if self.threshold_memory_switchover is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_wd_cfg as meta
        return meta._meta_table['Watchdog']['meta_info']


