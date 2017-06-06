""" Cisco_IOS_XR_patch_panel_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR patch\-panel package configuration.

This module contains definitions
for the following management objects\:
  patch\-panel\: patch\-panel service submode

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class PatchPanel(object):
    """
    patch\-panel service submode
    
    .. attribute:: enable
    
    	Enable patch\-panel service
    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: ipv4
    
    	IP address for patch\-panel
    	**type**\:  str
    
    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
    
    .. attribute:: password
    
    	Password name to be used for Authentication with Patch\-Panel
    	**type**\:  str
    
    	**pattern:** (!.+)\|([^!].+)
    
    .. attribute:: user_name
    
    	User name to be used for Authentication with Patch\-Panel
    	**type**\:  str
    
    .. attribute:: _is_presence
    
    	Is present if this instance represents presence container else not
    	**type**\: bool
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'patch-panel-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self._is_presence = True
        self.enable = None
        self.ipv4 = None
        self.password = None
        self.user_name = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-patch-panel-cfg:patch-panel'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self._is_presence:
            return True
        if self.enable is not None:
            return True

        if self.ipv4 is not None:
            return True

        if self.password is not None:
            return True

        if self.user_name is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_patch_panel_cfg as meta
        return meta._meta_table['PatchPanel']['meta_info']


