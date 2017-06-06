""" Cisco_IOS_XR_cdp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR cdp package configuration.

This module contains definitions
for the following management objects\:
  cdp\: Global CDP configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Cdp(object):
    """
    Global CDP configuration data
    
    .. attribute:: advertise_v1_only
    
    	Enable CDPv1 only advertisements
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: enable
    
    	Enable or disable CDP globally
    	**type**\:  bool
    
    	**default value**\: true
    
    .. attribute:: hold_time
    
    	Length of time (in sec) that the receiver must keep a CDP packet
    	**type**\:  int
    
    	**range:** 10..255
    
    	**default value**\: 180
    
    .. attribute:: log_adjacency
    
    	Enable logging of adjacency changes
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: timer
    
    	Specify the rate at which CDP packets are sent
    	**type**\:  int
    
    	**range:** 5..255
    
    	**default value**\: 60
    
    

    """

    _prefix = 'cdp-cfg'
    _revision = '2015-07-30'

    def __init__(self):
        self.advertise_v1_only = None
        self.enable = None
        self.hold_time = None
        self.log_adjacency = None
        self.timer = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-cdp-cfg:cdp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.advertise_v1_only is not None:
            return True

        if self.enable is not None:
            return True

        if self.hold_time is not None:
            return True

        if self.log_adjacency is not None:
            return True

        if self.timer is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_cdp_cfg as meta
        return meta._meta_table['Cdp']['meta_info']


