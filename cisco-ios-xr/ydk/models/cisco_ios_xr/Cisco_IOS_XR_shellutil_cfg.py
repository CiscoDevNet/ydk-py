""" Cisco_IOS_XR_shellutil_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR shellutil package configuration.

This module contains definitions
for the following management objects\:
  host\-names\: Container Schema for hostname configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class HostNames(object):
    """
    Container Schema for hostname configuration
    
    .. attribute:: host_name
    
    	Configure system's hostname
    	**type**\:  str
    
    

    """

    _prefix = 'shellutil-cfg'
    _revision = '2015-10-12'

    def __init__(self):
        self.host_name = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-shellutil-cfg:host-names'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.host_name is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_shellutil_cfg as meta
        return meta._meta_table['HostNames']['meta_info']


