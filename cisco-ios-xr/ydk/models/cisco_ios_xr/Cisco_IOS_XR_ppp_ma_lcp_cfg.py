""" Cisco_IOS_XR_ppp_ma_lcp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-lcp package configuration.

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



class PppAuthenticationMethod(Enum):
    """
    PppAuthenticationMethod (Enum Class)

    Ppp authentication method

    .. data:: pap = 1

    	PAP

    .. data:: chap = 2

    	CHAP

    .. data:: ms_chap = 3

    	MS CHAP

    """

    pap = Enum.YLeaf(1, "pap")

    chap = Enum.YLeaf(2, "chap")

    ms_chap = Enum.YLeaf(3, "ms-chap")



