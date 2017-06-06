""" Cisco_IOS_XR_config_cfgmgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR config\-cfgmgr package configuration.

This module contains definitions
for the following management objects\:
  cfgmgr\: Cfgmgr configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Cfgmgr(object):
    """
    Cfgmgr configuration
    
    .. attribute:: mode_exclusive
    
    	Enabled or Disabled
    	**type**\:  bool
    
    	**default value**\: true
    
    

    """

    _prefix = 'config-cfgmgr-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.mode_exclusive = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-config-cfgmgr-cfg:cfgmgr'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.mode_exclusive is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_config_cfgmgr_cfg as meta
        return meta._meta_table['Cfgmgr']['meta_info']


