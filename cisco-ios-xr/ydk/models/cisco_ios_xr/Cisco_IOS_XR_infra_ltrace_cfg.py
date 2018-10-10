""" Cisco_IOS_XR_infra_ltrace_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR infra\-ltrace package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-config\-mda\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class InfraLtraceMode(Enum):
    """
    InfraLtraceMode (Enum Class)

    Infra ltrace mode

    .. data:: static = 1

    	Set ltrace memory allocation to static mode

    .. data:: dynamic = 2

    	Set ltrace memory allocation to dynamic mode

    """

    static = Enum.YLeaf(1, "static")

    dynamic = Enum.YLeaf(2, "dynamic")


class InfraLtraceScale(Enum):
    """
    InfraLtraceScale (Enum Class)

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

    Y_0 = Enum.YLeaf(0, "0")

    Y_1 = Enum.YLeaf(1, "1")

    Y_2 = Enum.YLeaf(2, "2")

    Y_4 = Enum.YLeaf(4, "4")

    Y_8 = Enum.YLeaf(8, "8")

    Y_16 = Enum.YLeaf(16, "16")



