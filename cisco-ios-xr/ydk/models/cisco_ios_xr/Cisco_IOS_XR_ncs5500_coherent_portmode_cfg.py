""" Cisco_IOS_XR_ncs5500_coherent_portmode_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ncs5500\-coherent\-portmode package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DiffSel(Enum):
    """
    DiffSel (Enum Class)

    Diff sel

    .. data:: disable = 0

    	disable differential

    .. data:: enable = 1

    	enable differential

    """

    disable = Enum.YLeaf(0, "disable")

    enable = Enum.YLeaf(1, "enable")


class FecSel(Enum):
    """
    FecSel (Enum Class)

    Fec sel

    .. data:: Y_15percent = 0

    	FEC 15

    .. data:: Y_25percent = 1

    	FEC 25

    """

    Y_15percent = Enum.YLeaf(0, "15percent")

    Y_25percent = Enum.YLeaf(1, "25percent")


class SpeedSel(Enum):
    """
    SpeedSel (Enum Class)

    Speed sel

    .. data:: Y_100g = 100000000

    	Speed 100

    .. data:: Y_150g = 150000000

    	Speed 150

    .. data:: Y_200g = 200000000

    	Speed 200

    """

    Y_100g = Enum.YLeaf(100000000, "100g")

    Y_150g = Enum.YLeaf(150000000, "150g")

    Y_200g = Enum.YLeaf(200000000, "200g")



