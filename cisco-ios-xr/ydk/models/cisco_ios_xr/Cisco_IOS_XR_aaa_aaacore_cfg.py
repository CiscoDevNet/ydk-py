""" Cisco_IOS_XR_aaa_aaacore_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR aaa\-aaacore package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-aaa\-lib\-cfg,
  Cisco\-IOS\-XR\-ifmgr\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AaaServiceAccounting(Enum):
    """
    AaaServiceAccounting (Enum Class)

    Aaa service accounting

    .. data:: none = 0

    	None

    .. data:: extended = 1

    	Extended

    .. data:: brief = 2

    	Brief

    """

    none = Enum.YLeaf(0, "none")

    extended = Enum.YLeaf(1, "extended")

    brief = Enum.YLeaf(2, "brief")


class NasPortValue(Enum):
    """
    NasPortValue (Enum Class)

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

    async = Enum.YLeaf(0, "async")

    sync = Enum.YLeaf(1, "sync")

    isdn = Enum.YLeaf(2, "isdn")

    isdn_async_v120 = Enum.YLeaf(3, "isdn-async-v120")

    isdn_async_v110 = Enum.YLeaf(4, "isdn-async-v110")

    virtual = Enum.YLeaf(5, "virtual")

    isdn_async_piafs = Enum.YLeaf(6, "isdn-async-piafs")

    x75 = Enum.YLeaf(9, "x75")

    ethernet = Enum.YLeaf(15, "ethernet")

    pppoa = Enum.YLeaf(30, "pppoa")

    pppoeoa = Enum.YLeaf(31, "pppoeoa")

    pppoeoe = Enum.YLeaf(32, "pppoeoe")

    pppoeovlan = Enum.YLeaf(33, "pppoeovlan")

    pppoeoqinq = Enum.YLeaf(34, "pppoeoqinq")

    virtual_pppoeoe = Enum.YLeaf(35, "virtual-pppoeoe")

    virtual_pppoeovlan = Enum.YLeaf(36, "virtual-pppoeovlan")

    virtual_pppoeoqinaq = Enum.YLeaf(37, "virtual-pppoeoqinaq")

    ipsec = Enum.YLeaf(38, "ipsec")

    ipoeoe = Enum.YLeaf(39, "ipoeoe")

    ipoeovlan = Enum.YLeaf(40, "ipoeovlan")

    ipoeoqinq = Enum.YLeaf(41, "ipoeoqinq")

    virtual_ipoeoe = Enum.YLeaf(42, "virtual-ipoeoe")

    virtual_ipoeovlan = Enum.YLeaf(43, "virtual-ipoeovlan")

    virtual_ipoeoqinq = Enum.YLeaf(44, "virtual-ipoeoqinq")



