""" Cisco_IOS_XR_ppp_ma_ssrp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-ssrp package configuration.

This module contains definitions
for the following management objects\:
  ssrp\: Shared plane SSRP configuration data

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class Ssrp(object):
    """
    Shared plane SSRP configuration data
    
    .. attribute:: profiles
    
    	Table of SSRP Profiles
    	**type**\:   :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg.Ssrp.Profiles>`
    
    

    """

    _prefix = 'ppp-ma-ssrp-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        self.profiles = Ssrp.Profiles()
        self.profiles.parent = self


    class Profiles(object):
        """
        Table of SSRP Profiles
        
        .. attribute:: profile
        
        	SSRP Profile configuration
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg.Ssrp.Profiles.Profile>`
        
        

        """

        _prefix = 'ppp-ma-ssrp-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.profile = YList()
            self.profile.parent = self
            self.profile.name = 'profile'


        class Profile(object):
            """
            SSRP Profile configuration
            
            .. attribute:: name  <key>
            
            	The name of the profile
            	**type**\:  str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: max_hops
            
            	This specifies the maximum number of hops for packets on the SSO channel
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: peer_ipv4_address
            
            	This specifies the remote end's IPv4\-address for the SSO channel
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            

            """

            _prefix = 'ppp-ma-ssrp-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.name = None
                self.max_hops = None
                self.peer_ipv4_address = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp/Cisco-IOS-XR-ppp-ma-ssrp-cfg:profiles/Cisco-IOS-XR-ppp-ma-ssrp-cfg:profile[Cisco-IOS-XR-ppp-ma-ssrp-cfg:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.max_hops is not None:
                    return True

                if self.peer_ipv4_address is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_ssrp_cfg as meta
                return meta._meta_table['Ssrp.Profiles.Profile']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp/Cisco-IOS-XR-ppp-ma-ssrp-cfg:profiles'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.profile is not None:
                for child_ref in self.profile:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_ssrp_cfg as meta
            return meta._meta_table['Ssrp.Profiles']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ppp-ma-ssrp-cfg:ssrp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.profiles is not None and self.profiles._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_ssrp_cfg as meta
        return meta._meta_table['Ssrp']['meta_info']


