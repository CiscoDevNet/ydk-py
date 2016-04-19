""" Cisco_IOS_XR_atm_vcm_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR atm\-vcm package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg,
  Cisco\-IOS\-XR\-l2vpn\-cfg
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AtmPvcTestModeEnum(Enum):
    """
    AtmPvcTestModeEnum

    Atm pvc test mode

    .. data:: LOOP = 1

    	Loop mode applicable to L2/L3 PVC

    .. data:: RESERVED = 2

    	Reserved mode applicable to L2 PVC

    """

    LOOP = 1

    RESERVED = 2


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _Cisco_IOS_XR_atm_vcm_cfg as meta
        return meta._meta_table['AtmPvcTestModeEnum']


class AtmPvpTestModeEnum(Enum):
    """
    AtmPvpTestModeEnum

    Atm pvp test mode

    .. data:: LOOP = 1

    	Loop mode

    """

    LOOP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _Cisco_IOS_XR_atm_vcm_cfg as meta
        return meta._meta_table['AtmPvpTestModeEnum']


class AtmVpiBitsModeEnum(Enum):
    """
    AtmVpiBitsModeEnum

    Atm vpi bits mode

    .. data:: TWELVE = 12

    	12-bits VPI cell format

    """

    TWELVE = 12


    @staticmethod
    def _meta_info():
        from ydk.models.atm._meta import _Cisco_IOS_XR_atm_vcm_cfg as meta
        return meta._meta_table['AtmVpiBitsModeEnum']



