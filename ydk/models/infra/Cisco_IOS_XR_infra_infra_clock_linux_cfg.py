""" Cisco_IOS_XR_infra_infra_clock_linux_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra\-clock\-linux package configuration.

This module contains definitions
for the following management objects\:
  clock\: Configure time\-of\-day clock

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError




class Clock(object):
    """
    Configure time\-of\-day clock
    
    .. attribute:: time_zone
    
    	Configure time zone
    	**type**\: :py:class:`TimeZone <ydk.models.infra.Cisco_IOS_XR_infra_infra_clock_linux_cfg.Clock.TimeZone>`
    
    

    """

    _prefix = 'infra-infra-clock-linux-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.time_zone = None


    class TimeZone(object):
        """
        Configure time zone
        
        .. attribute:: area_name
        
        	Area File in zoneinfo package
        	**type**\: str
        
        .. attribute:: time_zone_name
        
        	Name of time zone
        	**type**\: str
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'infra-infra-clock-linux-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.area_name = None
            self.time_zone_name = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock/Cisco-IOS-XR-infra-infra-clock-linux-cfg:time-zone'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.area_name is not None:
                return True

            if self.time_zone_name is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return True

        @staticmethod
        def _meta_info():
            from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_clock_linux_cfg as meta
            return meta._meta_table['Clock.TimeZone']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-infra-clock-linux-cfg:clock'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.time_zone is not None and self.time_zone._has_data():
            return True

        if self.time_zone is not None and self.time_zone.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.infra._meta import _Cisco_IOS_XR_infra_infra_clock_linux_cfg as meta
        return meta._meta_table['Clock']['meta_info']


