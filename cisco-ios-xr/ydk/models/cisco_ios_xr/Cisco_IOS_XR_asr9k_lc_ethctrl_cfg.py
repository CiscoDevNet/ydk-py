""" Cisco_IOS_XR_asr9k_lc_ethctrl_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR asr9k\-lc\-ethctrl package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EtherCtrlTransportModeEnum(Enum):
    """
    EtherCtrlTransportModeEnum

    Ether ctrl transport mode

    .. data:: wan = 1

    	WAN

    .. data:: otnopu1e = 2

    	OTNOPUle

    .. data:: otnopu2e = 3

    	OTNOPU2e

    """

    wan = 1

    otnopu1e = 2

    otnopu2e = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_cfg as meta
        return meta._meta_table['EtherCtrlTransportModeEnum']


class PermitPluggableEnum(Enum):
    """
    PermitPluggableEnum

    Permit pluggable

    .. data:: all = 1

    	ALL types

    """

    all = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_cfg as meta
        return meta._meta_table['PermitPluggableEnum']


class PermitPluggablePidEnum(Enum):
    """
    PermitPluggablePidEnum

    Permit pluggable pid

    .. data:: all = 1

    	ALL PIDs

    """

    all = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_lc_ethctrl_cfg as meta
        return meta._meta_table['PermitPluggablePidEnum']



