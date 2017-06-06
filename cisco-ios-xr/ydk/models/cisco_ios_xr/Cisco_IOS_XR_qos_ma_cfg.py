""" Cisco_IOS_XR_qos_ma_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR qos package configuration.

This module contains definitions
for the following management objects\:
  qos\: Global QOS configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg,
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class QosFieldNotSupportedEnum(Enum):
    """
    QosFieldNotSupportedEnum

    Qos field not supported

    .. data:: not_supported = 0

    	Dummy data type leave unspecified

    """

    not_supported = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_qos_ma_cfg as meta
        return meta._meta_table['QosFieldNotSupportedEnum']


class QosPolicyAccountEnum(Enum):
    """
    QosPolicyAccountEnum

    Qos policy account

    .. data:: layer1 = 8

    	Turn on Layer 1 accounting

    .. data:: layer2 = 1

    	Turn on Layer 2 accounting

    .. data:: nolayer2 = 2

    	Turn on Layer 2 accounting

    .. data:: user_defined = 4

    	User defined accounting

    """

    layer1 = 8

    layer2 = 1

    nolayer2 = 2

    user_defined = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_qos_ma_cfg as meta
        return meta._meta_table['QosPolicyAccountEnum']



class Qos(object):
    """
    Global QOS configuration.
    
    .. attribute:: fabric_service_policy
    
    	Name of the fabric service policy
    	**type**\:  str
    
    	**length:** 0..63
    
    

    """

    _prefix = 'qos-ma-cfg'
    _revision = '2016-12-23'

    def __init__(self):
        self.fabric_service_policy = None

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-qos-ma-cfg:qos'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.fabric_service_policy is not None:
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_qos_ma_cfg as meta
        return meta._meta_table['Qos']['meta_info']


