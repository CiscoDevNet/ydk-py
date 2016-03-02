""" Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN\-subscriber package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-subscriber\-infra\-tmplmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SpanMirrorInterval_Enum(Enum):
    """
    SpanMirrorInterval_Enum

    Span mirror interval

    """

    """

    Mirror 1 in every 512 packets

    """
    Y_512 = 1

    """

    Mirror 1 in every 1024 packets

    """
    Y_1K = 2

    """

    Mirror 1 in every 2048 packets

    """
    Y_2K = 3

    """

    Mirror 1 in every 4096 packets

    """
    Y_4K = 4

    """

    Mirror 1 in every 8192 packets

    """
    Y_8K = 5

    """

    Mirror 1 in every 16384 packets

    """
    Y_16K = 6


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg as meta
        return meta._meta_table['SpanMirrorInterval_Enum']


class SpanTrafficDirection_Enum(Enum):
    """
    SpanTrafficDirection_Enum

    Span traffic direction

    """

    """

    Replicate only received (ingress) traffic

    """
    RX_ONLY = 1

    """

    Replicate only transmitted (egress) traffic

    """
    TX_ONLY = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ethernet._meta import _Cisco_IOS_XR_Ethernet_SPAN_subscriber_cfg as meta
        return meta._meta_table['SpanTrafficDirection_Enum']



