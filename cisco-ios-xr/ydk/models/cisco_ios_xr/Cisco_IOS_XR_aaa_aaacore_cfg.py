""" Cisco_IOS_XR_aaa_aaacore_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-aaacore package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-lib\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AaaServiceAccountingEnum(Enum):
    """
    AaaServiceAccountingEnum

    Aaa service accounting

    .. data:: none = 0

    	None

    .. data:: extended = 1

    	Extended

    .. data:: brief = 2

    	Brief

    """

    none = 0

    extended = 1

    brief = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_aaacore_cfg as meta
        return meta._meta_table['AaaServiceAccountingEnum']


class NasPortValueEnum(Enum):
    """
    NasPortValueEnum

    Nas port value

    .. data:: async = 0

    	Async(0)

    .. data:: sync = 1

    	Sync(1)

    .. data:: isdn = 2

    	ISDN(2)

    .. data:: isdn_async_v120 = 3

    	ISDN Async V120(3)

    .. data:: isdn_async_v110 = 4

    	ISDN Async V110(4)

    .. data:: virtual = 5

    	Virtual(5)

    .. data:: isdn_async_piafs = 6

    	ISDN Async PIAFS(6)

    .. data:: x75 = 9

    	X75(9)

    .. data:: ethernet = 15

    	Ethernet(15)

    .. data:: pppoa = 30

    	PPPoA(30)

    .. data:: pppoeoa = 31

    	PPPoEoA(31)

    .. data:: pppoeoe = 32

    	PPPoEoE(32)

    .. data:: pppoeovlan = 33

    	PPPoEoVLAN(33)

    .. data:: pppoeoqinq = 34

    	PPPoEoQinQ(34)

    .. data:: virtual_pppoeoe = 35

    	Virtual PPPoEoE(35)

    .. data:: virtual_pppoeovlan = 36

    	Virtual PPPoEoVLAN(36)

    .. data:: virtual_pppoeoqinaq = 37

    	Virtual PPPoEoQinQ(37)

    .. data:: ipsec = 38

    	IPSEC(38)

    .. data:: ipoeoe = 39

    	IPOEOE(39)

    .. data:: ipoeovlan = 40

    	IPOEOVLAN(40)

    .. data:: ipoeoqinq = 41

    	IPOEOQINQ(41)

    .. data:: virtual_ipoeoe = 42

    	VIRTUAL IPOEOE(42)

    .. data:: virtual_ipoeovlan = 43

    	VIRTUAL IPOEOVLAN(43)

    .. data:: virtual_ipoeoqinq = 44

    	VIRTUAL IPOEOQINQ(44)

    """

    async = 0

    sync = 1

    isdn = 2

    isdn_async_v120 = 3

    isdn_async_v110 = 4

    virtual = 5

    isdn_async_piafs = 6

    x75 = 9

    ethernet = 15

    pppoa = 30

    pppoeoa = 31

    pppoeoe = 32

    pppoeovlan = 33

    pppoeoqinq = 34

    virtual_pppoeoe = 35

    virtual_pppoeovlan = 36

    virtual_pppoeoqinaq = 37

    ipsec = 38

    ipoeoe = 39

    ipoeovlan = 40

    ipoeoqinq = 41

    virtual_ipoeoe = 42

    virtual_ipoeovlan = 43

    virtual_ipoeoqinq = 44


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_aaa_aaacore_cfg as meta
        return meta._meta_table['NasPortValueEnum']



