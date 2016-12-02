""" Cisco_IOS_XR_infra_ltrace_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-ltrace package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class InfraLtraceModeEnum(Enum):
    """
    InfraLtraceModeEnum

    Infra ltrace mode

    .. data:: static = 1

    	Set ltrace memory allocation to static mode

    .. data:: dynamic = 2

    	Set ltrace memory allocation to dynamic mode

    """

    static = 1

    dynamic = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_ltrace_cfg as meta
        return meta._meta_table['InfraLtraceModeEnum']


class InfraLtraceScaleEnum(Enum):
    """
    InfraLtraceScaleEnum

    Infra ltrace scale

    .. data:: Y_0 = 0

    	Use platform-defined scale-factor

    .. data:: Y_1 = 1

    	Do not scale down ltrace memory request

    .. data:: Y_2 = 2

    	Scale down ltrace memory request by 2

    .. data:: Y_4 = 4

    	Scale down ltrace memory request by 4

    .. data:: Y_8 = 8

    	Scale down ltrace memory request by 8

    .. data:: Y_16 = 16

    	Scale down ltrace memory request by 16

    """

    Y_0 = 0

    Y_1 = 1

    Y_2 = 2

    Y_4 = 4

    Y_8 = 8

    Y_16 = 16


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_infra_ltrace_cfg as meta
        return meta._meta_table['InfraLtraceScaleEnum']



