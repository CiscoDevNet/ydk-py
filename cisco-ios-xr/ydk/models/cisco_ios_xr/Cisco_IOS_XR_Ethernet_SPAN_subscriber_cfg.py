""" Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN\-subscriber package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SpanMirrorInterval(Enum):
    """
    SpanMirrorInterval

    Span mirror interval

    .. data:: Y_512 = 1

    	Mirror 1 in every 512 packets

    .. data:: Y_1k = 2

    	Mirror 1 in every 1024 packets

    .. data:: Y_2k = 3

    	Mirror 1 in every 2048 packets

    .. data:: Y_4k = 4

    	Mirror 1 in every 4096 packets

    .. data:: Y_8k = 5

    	Mirror 1 in every 8192 packets

    .. data:: Y_16k = 6

    	Mirror 1 in every 16384 packets

    """

    Y_512 = Enum.YLeaf(1, "512")

    Y_1k = Enum.YLeaf(2, "1k")

    Y_2k = Enum.YLeaf(3, "2k")

    Y_4k = Enum.YLeaf(4, "4k")

    Y_8k = Enum.YLeaf(5, "8k")

    Y_16k = Enum.YLeaf(6, "16k")


class SpanTrafficDirection(Enum):
    """
    SpanTrafficDirection

    Span traffic direction

    .. data:: rx_only = 1

    	Replicate only received (ingress) traffic

    .. data:: tx_only = 2

    	Replicate only transmitted (egress) traffic

    """

    rx_only = Enum.YLeaf(1, "rx-only")

    tx_only = Enum.YLeaf(2, "tx-only")



