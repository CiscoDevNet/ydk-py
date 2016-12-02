""" Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN\-subscriber package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SpanMirrorIntervalEnum(Enum):
    """
    SpanMirrorIntervalEnum

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

    Y_512 = 1

    Y_1k = 2

    Y_2k = 3

    Y_4k = 4

    Y_8k = 5

    Y_16k = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg as meta
        return meta._meta_table['SpanMirrorIntervalEnum']


class SpanTrafficDirectionEnum(Enum):
    """
    SpanTrafficDirectionEnum

    Span traffic direction

    .. data:: rx_only = 1

    	Replicate only received (ingress) traffic

    .. data:: tx_only = 2

    	Replicate only transmitted (egress) traffic

    """

    rx_only = 1

    tx_only = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg as meta
        return meta._meta_table['SpanTrafficDirectionEnum']



