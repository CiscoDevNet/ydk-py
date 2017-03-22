""" Cisco_IOS_XR_ppp_ma_lcp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ppp\-ma\-lcp package configuration.

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



class PppAuthenticationMethodEnum(Enum):
    """
    PppAuthenticationMethodEnum

    Ppp authentication method

    .. data:: pap = 1

    	PAP

    .. data:: chap = 2

    	CHAP

    .. data:: ms_chap = 3

    	MS CHAP

    """

    pap = 1

    chap = 2

    ms_chap = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ppp_ma_lcp_cfg as meta
        return meta._meta_table['PppAuthenticationMethodEnum']



