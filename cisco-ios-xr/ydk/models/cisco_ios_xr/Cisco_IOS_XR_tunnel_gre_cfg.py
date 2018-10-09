""" Cisco_IOS_XR_tunnel_gre_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-gre package configuration.

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



class TunnelModeDirection(Enum):
    """
    TunnelModeDirection (Enum Class)

    Tunnel mode direction

    .. data:: decap = 1

    	Decap-only tunnel

    .. data:: encap = 2

    	Encap-only tunnel

    """

    decap = Enum.YLeaf(1, "decap")

    encap = Enum.YLeaf(2, "encap")



