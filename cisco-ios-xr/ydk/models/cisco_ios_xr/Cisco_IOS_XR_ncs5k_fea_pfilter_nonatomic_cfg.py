""" Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5k\-fea\-pfilter\-nonatomic package configuration.

This module contains definitions
for the following management objects\:
  hardware\: Hardware

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AtomicDisableDfltActnEnum(Enum):
    """
    AtomicDisableDfltActnEnum

    Atomic disable dflt actn

    .. data:: default_action_deny = 1

    	Drops traffic during modification

    .. data:: default_action_permit = 2

    	Forward traffic during modification

    """

    default_action_deny = 1

    default_action_permit = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg as meta
        return meta._meta_table['AtomicDisableDfltActnEnum']



class Hardware(object):
    """
    Hardware
    
    .. attribute:: access_list
    
    	Access\-list option
    	**type**\:   :py:class:`AccessList <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg.Hardware.AccessList>`
    
    

    """

    _prefix = 'ncs5k-fea-pfilter-nonatomic-cfg'
    _revision = '2016-09-01'

    def __init__(self):
        self.access_list = Hardware.AccessList()
        self.access_list.parent = self


    class AccessList(object):
        """
        Access\-list option
        
        .. attribute:: atomic_disable
        
        	Specify Option for Atomic disable
        	**type**\:   :py:class:`AtomicDisableDfltActnEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg.AtomicDisableDfltActnEnum>`
        
        

        """

        _prefix = 'ncs5k-fea-pfilter-nonatomic-cfg'
        _revision = '2016-09-01'

        def __init__(self):
            self.parent = None
            self.atomic_disable = None

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg:hardware/Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg:access-list'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.atomic_disable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg as meta
            return meta._meta_table['Hardware.AccessList']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ncs5k-fea-pfilter-nonatomic-cfg:hardware'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.access_list is not None and self.access_list._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ncs5k_fea_pfilter_nonatomic_cfg as meta
        return meta._meta_table['Hardware']['meta_info']


