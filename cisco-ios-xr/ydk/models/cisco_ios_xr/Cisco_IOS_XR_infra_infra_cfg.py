""" Cisco_IOS_XR_infra_infra_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-infra package configuration.

This module contains definitions
for the following management objects\:
  banners\: Schema for Banner configuration commands

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BannerEnum(Enum):
    """
    BannerEnum

    Banner

    .. data:: exec_ = 0

    	Set EXEC process creation banner

    .. data:: incoming = 1

    	Set incoming terminal line banner

    .. data:: motd = 2

    	Set Message of the Day banner

    .. data:: login = 3

    	Set login banner

    .. data:: slip_ppp = 4

    	Set Message for SLIP/PPP

    .. data:: prompt_timeout = 5

    	Set Message for login authentication timeout

    """

    exec_ = 0

    incoming = 1

    motd = 2

    login = 3

    slip_ppp = 4

    prompt_timeout = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_cfg as meta
        return meta._meta_table['BannerEnum']



class Banners(object):
    """
    Schema for Banner configuration commands
    
    .. attribute:: banner
    
    	Select a Banner Type
    	**type**\: list of    :py:class:`Banner <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg.Banners.Banner>`
    
    

    """

    _prefix = 'infra-infra-cfg'
    _revision = '2016-06-16'

    def __init__(self):
        self.banner = YList()
        self.banner.parent = self
        self.banner.name = 'banner'


    class Banner(object):
        """
        Select a Banner Type
        
        .. attribute:: banner_name  <key>
        
        	Banner Type
        	**type**\:   :py:class:`BannerEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_infra_cfg.BannerEnum>`
        
        .. attribute:: banner_text
        
        	Banner text message
        	**type**\:  str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'infra-infra-cfg'
        _revision = '2016-06-16'

        def __init__(self):
            self.parent = None
            self.banner_name = None
            self.banner_text = None

        @property
        def _common_path(self):
            if self.banner_name is None:
                raise YPYModelError('Key property banner_name is None')

            return '/Cisco-IOS-XR-infra-infra-cfg:banners/Cisco-IOS-XR-infra-infra-cfg:banner[Cisco-IOS-XR-infra-infra-cfg:banner-name = ' + str(self.banner_name) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.banner_name is not None:
                return True

            if self.banner_text is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_cfg as meta
            return meta._meta_table['Banners.Banner']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-infra-infra-cfg:banners'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.banner is not None:
            for child_ref in self.banner:
                if child_ref._has_data():
                    return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_infra_cfg as meta
        return meta._meta_table['Banners']['meta_info']


