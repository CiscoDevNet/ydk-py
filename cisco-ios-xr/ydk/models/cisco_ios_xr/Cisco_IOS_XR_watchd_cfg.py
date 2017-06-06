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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Watchdog(object):
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
        self.overload_notification = None
        self.overload_throttle_timeout = None
        self.restart_deadlock_disable = None
        self.restart_memoryhog_disable = None
        self.threshold_memory = Watchdog.ThresholdMemory()
        self.threshold_memory.parent = self


    class ThresholdMemory(object):
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
            self.parent = None
            self.critical = None
            self.minor = None
            self.severe = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-watchd-cfg:watchdog/Cisco-IOS-XR-watchd-cfg:threshold-memory'

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
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_watchd_cfg as meta
            return meta._meta_table['Watchdog.ThresholdMemory']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-watchd-cfg:watchdog'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.overload_notification is not None:
            return True

        if self.overload_throttle_timeout is not None:
            return True

        if self.restart_deadlock_disable is not None:
            return True

        if self.restart_memoryhog_disable is not None:
            return True

        if self.threshold_memory is not None and self.threshold_memory._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_watchd_cfg as meta
        return meta._meta_table['Watchdog']['meta_info']


class Watchd(object):
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
        self.timeout = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-watchd-cfg:watchd'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.timeout is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_watchd_cfg as meta
        return meta._meta_table['Watchd']['meta_info']


