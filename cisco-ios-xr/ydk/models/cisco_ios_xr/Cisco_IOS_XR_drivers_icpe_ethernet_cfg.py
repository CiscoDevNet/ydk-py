""" Cisco_IOS_XR_drivers_icpe_ethernet_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR drivers\-icpe\-ethernet package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class ExtendedEthernetLoopback(Enum):
    """
    ExtendedEthernetLoopback (Enum Class)

    Extended ethernet loopback

    .. data:: internal = 1

    	Internal loopback

    .. data:: line = 2

    	Line loopback

    """

    internal = Enum.YLeaf(1, "internal")

    line = Enum.YLeaf(2, "line")



