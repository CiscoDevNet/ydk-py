""" Cisco_IOS_XR_ipv4_bgp_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class BgpAddressFamily_Enum(Enum):
    """
    BgpAddressFamily_Enum

    Bgp address family

    """

    """

    IPv4 unicast

    """
    IPV4_UNICAST = 0

    """

    IPv4 multicast

    """
    IPV4_MULTICAST = 1

    """

    IPv4 labeled\-unicast

    """
    IPV4_LABELED_UNICAST = 2

    """

    IPv4 tunnel

    """
    IPV4_TUNNEL = 3

    """

    VPNv4 unicast

    """
    VP_NV4_UNICAST = 4

    """

    IPv6 unicast

    """
    IPV6_UNICAST = 5

    """

    IPv6 multicast

    """
    IPV6_MULTICAST = 6

    """

    IPv6 labeled\-unicast

    """
    IPV6_LABELED_UNICAST = 7

    """

    VPNv6 unicast

    """
    VP_NV6_UNICAST = 8

    """

    IPv4 MDT

    """
    IPV4MDT = 9

    """

    L2VPN VPLS\-VPWS

    """
    L2VPNVPLS = 10

    """

    IPv4 rt\-filter

    """
    IPV4RT_CONSTRAINT = 11

    """

    IPv4 MVPN

    """
    IPV4MVPN = 12

    """

    IPv6 MVPN

    """
    IPV6MVPN = 13

    """

    L2VPN EVPN

    """
    L2VPNEVPN = 14

    """

    Link\-state link\-state

    """
    LSLS = 15

    """

    VPNv4 Multicast

    """
    VP_NV4_MULTICAST = 16

    """

    VPNv6 Multicast

    """
    VP_NV6_MULTICAST = 17

    """

    IPv4 flowspec

    """
    IPV4_FLOWSPEC = 18

    """

    IPv6 flowspec

    """
    IPV6_FLOWSPEC = 19

    """

    VPNv4 flowspec

    """
    VP_NV4_FLOWSPEC = 20

    """

    VPNv6 flowspec

    """
    VP_NV6_FLOWSPEC = 21

    """

    L2VPN MSPW

    """
    L2VPNMSPW = 22

    """

    All Address Families

    """
    ALL_ADDRESS_FAMILY = 23


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpAddressFamily_Enum']


class BgpNbrCapAdditionalPathsCfg_Enum(Enum):
    """
    BgpNbrCapAdditionalPathsCfg_Enum

    Bgp nbr cap additional paths cfg

    """

    """

    Enable

    """
    ENABLE = 1

    """

    Disable

    """
    DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpNbrCapAdditionalPathsCfg_Enum']


class BgpOfficialAddressFamily_Enum(Enum):
    """
    BgpOfficialAddressFamily_Enum

    Bgp official address family

    """

    """

    IPv4

    """
    IPV4 = 1

    """

    IPv6

    """
    IPV6 = 2

    """

    L2VPN

    """
    L2VPN = 25

    """

    LS

    """
    LS = 16388

    """

    All

    """
    ALL = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpOfficialAddressFamily_Enum']


class BgpPrecedenceDscp_Enum(Enum):
    """
    BgpPrecedenceDscp_Enum

    Bgp precedence dscp

    """

    """

    AF11 dscp (001010)

    """
    AF11 = 10

    """

    AF12 dscp (001100)

    """
    AF12 = 12

    """

    AF13 dscp (001110)

    """
    AF13 = 14

    """

    AF21 dscp (010010)

    """
    AF21 = 18

    """

    AF22 dscp (010100)

    """
    AF22 = 20

    """

    AF23 dscp (010110)

    """
    AF23 = 22

    """

    AF31 dscp (011010)

    """
    AF31 = 26

    """

    AF32 dscp (011100)

    """
    AF32 = 28

    """

    AF33 dscp (011110)

    """
    AF33 = 30

    """

    AF41 dscp (100010)

    """
    AF41 = 34

    """

    AF42 dscp (100100)

    """
    AF42 = 36

    """

    AF43 dscp (100110)

    """
    AF43 = 38

    """

    CS1 dscp (001000)

    """
    CS1 = 8

    """

    CS2 dscp (010000)

    """
    CS2 = 16

    """

    CS3 dscp (011000)

    """
    CS3 = 24

    """

    CS4 dscp (100000)

    """
    CS4 = 32

    """

    CS5 dscp (101000)

    """
    CS5 = 40

    """

    CS6 dscp (110000)

    """
    CS6 = 48

    """

    CS7 dscp (111000)

    """
    CS7 = 56

    """

    EF dscp (101110)

    """
    EF = 46

    """

    critical precedence (5)

    """
    CRITICAL = 5

    """

    flash precedence (3)

    """
    FLASH = 3

    """

    flash override precedence (4)

    """
    FLASH_OVERRIDE = 4

    """

    immediate precedence (2)

    """
    IMMEDIATE = 2

    """

    internetwork control precedence (6)

    """
    INTERNET = 6

    """

    network control precedence (7)

    """
    NETWORK = 7

    """

    priority precedence (1)

    """
    PRIORITY = 1

    """

    default dscp or routine precedence (0)

    """
    DEFAULT_OR_ROUTINE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpPrecedenceDscp_Enum']


class BgpSubsequentAddressFamily_Enum(Enum):
    """
    BgpSubsequentAddressFamily_Enum

    Bgp subsequent address family

    """

    """

    Unicast

    """
    UNICAST = 1

    """

    Multicast

    """
    MULTICAST = 2

    """

    Labeled unicast

    """
    LABELED_UNICAST = 4

    """

    MVPN

    """
    MVPN = 5

    """

    MSPW

    """
    MSPW = 6

    """

    Tunnel

    """
    TUNNEL = 64

    """

    VPLS

    """
    VPLS = 65

    """

    MDT

    """
    MDT = 66

    """

    VPWS

    """
    VPWS = 68

    """

    EVPN

    """
    EVPN = 70

    """

    LS

    """
    LS = 71

    """

    VPN

    """
    VPN = 128

    """

    VPN MCAST

    """
    VPN_MCAST = 129

    """

    Rt filter

    """
    RT_FILTER = 132

    """

    Flowspec

    """
    FLOWSPEC = 133

    """

    VPN Flowspec

    """
    VPN_FLOWSPEC = 134

    """

    All

    """
    ALL = 254


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpSubsequentAddressFamily_Enum']


class BgpTos_Enum(Enum):
    """
    BgpTos_Enum

    Bgp tos

    """

    """

    Precedence

    """
    PRECEDENCE = 0

    """

    DSCP

    """
    DSCP = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpTos_Enum']


class BgpUpdateFilterAction_Enum(Enum):
    """
    BgpUpdateFilterAction_Enum

    Bgp update filter action

    """

    """

    Treat as withdraw

    """
    TREAT_AS_WITHDRAW = 1

    """

    Discard attribute

    """
    DISCARD_ATTIBUTE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpUpdateFilterAction_Enum']


class BgpafAdditionalPathsCfg_Enum(Enum):
    """
    BgpafAdditionalPathsCfg_Enum

    Bgpaf additional paths cfg

    """

    """

    Enable

    """
    ENABLE = 1

    """

    Disable

    """
    DISABLE = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpafAdditionalPathsCfg_Enum']



