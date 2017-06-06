""" Cisco_IOS_XR_shellutil_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil package operational data.

This module contains definitions
for the following management objects\:
  system\-time\: System time information

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class TimeSourceEnum(Enum):
    """
    TimeSourceEnum

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

    error = 0

    none = 1

    ntp = 2

    manual = 3

    calendar = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_oper as meta
        return meta._meta_table['TimeSourceEnum']



class SystemTime(object):
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
        self.clock = SystemTime.Clock()
        self.clock.parent = self
        self.uptime = SystemTime.Uptime()
        self.uptime.parent = self


    class Clock(object):
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
        	**type**\:   :py:class:`TimeSourceEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_shellutil_oper.TimeSourceEnum>`
        
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
            self.parent = None
            self.day = None
            self.hour = None
            self.millisecond = None
            self.minute = None
            self.month = None
            self.second = None
            self.time_source = None
            self.time_zone = None
            self.wday = None
            self.year = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-shellutil-oper:system-time/Cisco-IOS-XR-shellutil-oper:clock'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.day is not None:
                return True

            if self.hour is not None:
                return True

            if self.millisecond is not None:
                return True

            if self.minute is not None:
                return True

            if self.month is not None:
                return True

            if self.second is not None:
                return True

            if self.time_source is not None:
                return True

            if self.time_zone is not None:
                return True

            if self.wday is not None:
                return True

            if self.year is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_oper as meta
            return meta._meta_table['SystemTime.Clock']['meta_info']


    class Uptime(object):
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
            self.parent = None
            self.host_name = None
            self.uptime = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-shellutil-oper:system-time/Cisco-IOS-XR-shellutil-oper:uptime'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.host_name is not None:
                return True

            if self.uptime is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_oper as meta
            return meta._meta_table['SystemTime.Uptime']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-shellutil-oper:system-time'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.clock is not None and self.clock._has_data():
            return True

        if self.uptime is not None and self.uptime._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_oper as meta
        return meta._meta_table['SystemTime']['meta_info']


