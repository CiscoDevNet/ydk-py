""" Cisco_IOS_XR_ncs5500_qos_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-qos package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class QosFieldNotSupportedEnum(Enum):
    """
    QosFieldNotSupportedEnum

    Qos field not supported

    .. data:: NOT_SUPPORTED = 0

    	Dummy data type leave unspecified

    """

    NOT_SUPPORTED = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_cfg as meta
        return meta._meta_table['QosFieldNotSupportedEnum']


class QosPolicyAccountEnum(Enum):
    """
    QosPolicyAccountEnum

    Qos policy account

    .. data:: NO_PREFERENCE = 0

    	No account turn off preference

    .. data:: LAYER2 = 1

    	Turn on layer 2 accounting

    .. data:: NO_LAYER2 = 2

    	Turn off layer 2 accounting

    .. data:: USER_DEFINED = 4

    	User defined accounting

    .. data:: LAYER1 = 8

    	Turn on layer 1 accounting

    """

    NO_PREFERENCE = 0

    LAYER2 = 1

    NO_LAYER2 = 2

    USER_DEFINED = 4

    LAYER1 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_cfg as meta
        return meta._meta_table['QosPolicyAccountEnum']



