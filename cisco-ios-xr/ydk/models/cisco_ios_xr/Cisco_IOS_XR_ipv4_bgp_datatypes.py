""" Cisco_IOS_XR_ipv4_bgp_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpAddressFamilyEnum(Enum):
    """
    BgpAddressFamilyEnum

    Bgp address family

    .. data:: IPV4_UNICAST = 0

    	IPv4 unicast

    .. data:: IPV4_MULTICAST = 1

    	IPv4 multicast

    .. data:: IPV4_LABELED_UNICAST = 2

    	IPv4 labeled-unicast

    .. data:: IPV4_TUNNEL = 3

    	IPv4 tunnel

    .. data:: VP_NV4_UNICAST = 4

    	VPNv4 unicast

    .. data:: IPV6_UNICAST = 5

    	IPv6 unicast

    .. data:: IPV6_MULTICAST = 6

    	IPv6 multicast

    .. data:: IPV6_LABELED_UNICAST = 7

    	IPv6 labeled-unicast

    .. data:: VP_NV6_UNICAST = 8

    	VPNv6 unicast

    .. data:: IPV4MDT = 9

    	IPv4 MDT

    .. data:: L2VPNVPLS = 10

    	L2VPN VPLS-VPWS

    .. data:: IPV4RT_CONSTRAINT = 11

    	IPv4 rt-filter

    .. data:: IPV4MVPN = 12

    	IPv4 MVPN

    .. data:: IPV6MVPN = 13

    	IPv6 MVPN

    .. data:: L2VPNEVPN = 14

    	L2VPN EVPN

    .. data:: LSLS = 15

    	Link-state link-state

    .. data:: VP_NV4_MULTICAST = 16

    	VPNv4 Multicast

    .. data:: VP_NV6_MULTICAST = 17

    	VPNv6 Multicast

    .. data:: IPV4_FLOWSPEC = 18

    	IPv4 flowspec

    .. data:: IPV6_FLOWSPEC = 19

    	IPv6 flowspec

    .. data:: VP_NV4_FLOWSPEC = 20

    	VPNv4 flowspec

    .. data:: VP_NV6_FLOWSPEC = 21

    	VPNv6 flowspec

    .. data:: L2VPNMSPW = 22

    	L2VPN MSPW

    .. data:: ALL_ADDRESS_FAMILY = 23

    	All Address Families

    """

    IPV4_UNICAST = 0

    IPV4_MULTICAST = 1

    IPV4_LABELED_UNICAST = 2

    IPV4_TUNNEL = 3

    VP_NV4_UNICAST = 4

    IPV6_UNICAST = 5

    IPV6_MULTICAST = 6

    IPV6_LABELED_UNICAST = 7

    VP_NV6_UNICAST = 8

    IPV4MDT = 9

    L2VPNVPLS = 10

    IPV4RT_CONSTRAINT = 11

    IPV4MVPN = 12

    IPV6MVPN = 13

    L2VPNEVPN = 14

    LSLS = 15

    VP_NV4_MULTICAST = 16

    VP_NV6_MULTICAST = 17

    IPV4_FLOWSPEC = 18

    IPV6_FLOWSPEC = 19

    VP_NV4_FLOWSPEC = 20

    VP_NV6_FLOWSPEC = 21

    L2VPNMSPW = 22

    ALL_ADDRESS_FAMILY = 23


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpAddressFamilyEnum']


class BgpNbrCapAdditionalPathsCfgEnum(Enum):
    """
    BgpNbrCapAdditionalPathsCfgEnum

    Bgp nbr cap additional paths cfg

    .. data:: ENABLE = 1

    	Enable

    .. data:: DISABLE = 2

    	Disable

    """

    ENABLE = 1

    DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpNbrCapAdditionalPathsCfgEnum']


class BgpOfficialAddressFamilyEnum(Enum):
    """
    BgpOfficialAddressFamilyEnum

    Bgp official address family

    .. data:: IPV4 = 1

    	IPv4

    .. data:: IPV6 = 2

    	IPv6

    .. data:: L2VPN = 25

    	L2VPN

    .. data:: LS = 16388

    	LS

    .. data:: ALL = 65534

    	All

    """

    IPV4 = 1

    IPV6 = 2

    L2VPN = 25

    LS = 16388

    ALL = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpOfficialAddressFamilyEnum']


class BgpPrecedenceDscpEnum(Enum):
    """
    BgpPrecedenceDscpEnum

    Bgp precedence dscp

    .. data:: AF11 = 10

    	AF11 dscp (001010)

    .. data:: AF12 = 12

    	AF12 dscp (001100)

    .. data:: AF13 = 14

    	AF13 dscp (001110)

    .. data:: AF21 = 18

    	AF21 dscp (010010)

    .. data:: AF22 = 20

    	AF22 dscp (010100)

    .. data:: AF23 = 22

    	AF23 dscp (010110)

    .. data:: AF31 = 26

    	AF31 dscp (011010)

    .. data:: AF32 = 28

    	AF32 dscp (011100)

    .. data:: AF33 = 30

    	AF33 dscp (011110)

    .. data:: AF41 = 34

    	AF41 dscp (100010)

    .. data:: AF42 = 36

    	AF42 dscp (100100)

    .. data:: AF43 = 38

    	AF43 dscp (100110)

    .. data:: CS1 = 8

    	CS1 dscp (001000)

    .. data:: CS2 = 16

    	CS2 dscp (010000)

    .. data:: CS3 = 24

    	CS3 dscp (011000)

    .. data:: CS4 = 32

    	CS4 dscp (100000)

    .. data:: CS5 = 40

    	CS5 dscp (101000)

    .. data:: CS6 = 48

    	CS6 dscp (110000)

    .. data:: CS7 = 56

    	CS7 dscp (111000)

    .. data:: EF = 46

    	EF dscp (101110)

    .. data:: CRITICAL = 5

    	critical precedence (5)

    .. data:: FLASH = 3

    	flash precedence (3)

    .. data:: FLASH_OVERRIDE = 4

    	flash override precedence (4)

    .. data:: IMMEDIATE = 2

    	immediate precedence (2)

    .. data:: INTERNET = 6

    	internetwork control precedence (6)

    .. data:: NETWORK = 7

    	network control precedence (7)

    .. data:: PRIORITY = 1

    	priority precedence (1)

    .. data:: DEFAULT_OR_ROUTINE = 0

    	default dscp or routine precedence (0)

    """

    AF11 = 10

    AF12 = 12

    AF13 = 14

    AF21 = 18

    AF22 = 20

    AF23 = 22

    AF31 = 26

    AF32 = 28

    AF33 = 30

    AF41 = 34

    AF42 = 36

    AF43 = 38

    CS1 = 8

    CS2 = 16

    CS3 = 24

    CS4 = 32

    CS5 = 40

    CS6 = 48

    CS7 = 56

    EF = 46

    CRITICAL = 5

    FLASH = 3

    FLASH_OVERRIDE = 4

    IMMEDIATE = 2

    INTERNET = 6

    NETWORK = 7

    PRIORITY = 1

    DEFAULT_OR_ROUTINE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpPrecedenceDscpEnum']


class BgpSubsequentAddressFamilyEnum(Enum):
    """
    BgpSubsequentAddressFamilyEnum

    Bgp subsequent address family

    .. data:: UNICAST = 1

    	Unicast

    .. data:: MULTICAST = 2

    	Multicast

    .. data:: LABELED_UNICAST = 4

    	Labeled unicast

    .. data:: MVPN = 5

    	MVPN

    .. data:: MSPW = 6

    	MSPW

    .. data:: TUNNEL = 64

    	Tunnel

    .. data:: VPLS = 65

    	VPLS

    .. data:: MDT = 66

    	MDT

    .. data:: VPWS = 68

    	VPWS

    .. data:: EVPN = 70

    	EVPN

    .. data:: LS = 71

    	LS

    .. data:: VPN = 128

    	VPN

    .. data:: VPN_MCAST = 129

    	VPN MCAST

    .. data:: RT_FILTER = 132

    	Rt filter

    .. data:: FLOWSPEC = 133

    	Flowspec

    .. data:: VPN_FLOWSPEC = 134

    	VPN Flowspec

    .. data:: ALL = 254

    	All

    """

    UNICAST = 1

    MULTICAST = 2

    LABELED_UNICAST = 4

    MVPN = 5

    MSPW = 6

    TUNNEL = 64

    VPLS = 65

    MDT = 66

    VPWS = 68

    EVPN = 70

    LS = 71

    VPN = 128

    VPN_MCAST = 129

    RT_FILTER = 132

    FLOWSPEC = 133

    VPN_FLOWSPEC = 134

    ALL = 254


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpSubsequentAddressFamilyEnum']


class BgpTosEnum(Enum):
    """
    BgpTosEnum

    Bgp tos

    .. data:: PRECEDENCE = 0

    	Precedence

    .. data:: DSCP = 1

    	DSCP

    """

    PRECEDENCE = 0

    DSCP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpTosEnum']


class BgpUpdateFilterActionEnum(Enum):
    """
    BgpUpdateFilterActionEnum

    Bgp update filter action

    .. data:: TREAT_AS_WITHDRAW = 1

    	Treat as withdraw

    .. data:: DISCARD_ATTIBUTE = 2

    	Discard attribute

    """

    TREAT_AS_WITHDRAW = 1

    DISCARD_ATTIBUTE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpUpdateFilterActionEnum']


class BgpafAdditionalPathsCfgEnum(Enum):
    """
    BgpafAdditionalPathsCfgEnum

    Bgpaf additional paths cfg

    .. data:: ENABLE = 1

    	Enable

    .. data:: DISABLE = 2

    	Disable

    """

    ENABLE = 1

    DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpafAdditionalPathsCfgEnum']



