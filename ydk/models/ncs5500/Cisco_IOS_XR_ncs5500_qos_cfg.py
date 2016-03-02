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



class QosFieldNotSupported_Enum(Enum):
    """
    QosFieldNotSupported_Enum

    Qos field not supported

    """

    """

    Dummy data type leave unspecified

    """
    NOT_SUPPORTED = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_cfg as meta
        return meta._meta_table['QosFieldNotSupported_Enum']


class QosPolicyAccount_Enum(Enum):
    """
    QosPolicyAccount_Enum

    Qos policy account

    """

    """

    No account turn off preference

    """
    NO_PREFERENCE = 0

    """

    Turn on layer 2 accounting

    """
    LAYER2 = 1

    """

    Turn off layer 2 accounting

    """
    NO_LAYER2 = 2

    """

    User defined accounting

    """
    USER_DEFINED = 4

    """

    Turn on layer 1 accounting

    """
    LAYER1 = 8


    @staticmethod
    def _meta_info():
        from ydk.models.ncs5500._meta import _Cisco_IOS_XR_ncs5500_qos_cfg as meta
        return meta._meta_table['QosPolicyAccount_Enum']



