""" Cisco_IOS_XR_ipv4_bgp_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
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

    .. data:: ipv4_unicast = 0

    	IPv4 unicast

    .. data:: ipv4_multicast = 1

    	IPv4 multicast

    .. data:: ipv4_labeled_unicast = 2

    	IPv4 labeled-unicast

    .. data:: ipv4_tunnel = 3

    	IPv4 tunnel

    .. data:: vp_nv4_unicast = 4

    	VPNv4 unicast

    .. data:: ipv6_unicast = 5

    	IPv6 unicast

    .. data:: ipv6_multicast = 6

    	IPv6 multicast

    .. data:: ipv6_labeled_unicast = 7

    	IPv6 labeled-unicast

    .. data:: vp_nv6_unicast = 8

    	VPNv6 unicast

    .. data:: ipv4mdt = 9

    	IPv4 MDT

    .. data:: l2vpnvpls = 10

    	L2VPN VPLS-VPWS

    .. data:: ipv4rt_constraint = 11

    	IPv4 rt-filter

    .. data:: ipv4mvpn = 12

    	IPv4 MVPN

    .. data:: ipv6mvpn = 13

    	IPv6 MVPN

    .. data:: l2vpnevpn = 14

    	L2VPN EVPN

    .. data:: lsls = 15

    	Link-state link-state

    .. data:: vp_nv4_multicast = 16

    	VPNv4 Multicast

    .. data:: vp_nv6_multicast = 17

    	VPNv6 Multicast

    .. data:: ipv4_flowspec = 18

    	IPv4 flowspec

    .. data:: ipv6_flowspec = 19

    	IPv6 flowspec

    .. data:: vp_nv4_flowspec = 20

    	VPNv4 flowspec

    .. data:: vp_nv6_flowspec = 21

    	VPNv6 flowspec

    .. data:: l2vpnmspw = 22

    	L2VPN MSPW

    .. data:: ipv4sr_policy = 23

    	IPv4 SRPolicy

    .. data:: ipv6sr_policy = 24

    	IPv6 SRPolicy

    .. data:: all_address_family = 25

    	All Address Families

    """

    ipv4_unicast = 0

    ipv4_multicast = 1

    ipv4_labeled_unicast = 2

    ipv4_tunnel = 3

    vp_nv4_unicast = 4

    ipv6_unicast = 5

    ipv6_multicast = 6

    ipv6_labeled_unicast = 7

    vp_nv6_unicast = 8

    ipv4mdt = 9

    l2vpnvpls = 10

    ipv4rt_constraint = 11

    ipv4mvpn = 12

    ipv6mvpn = 13

    l2vpnevpn = 14

    lsls = 15

    vp_nv4_multicast = 16

    vp_nv6_multicast = 17

    ipv4_flowspec = 18

    ipv6_flowspec = 19

    vp_nv4_flowspec = 20

    vp_nv6_flowspec = 21

    l2vpnmspw = 22

    ipv4sr_policy = 23

    ipv6sr_policy = 24

    all_address_family = 25


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpAddressFamilyEnum']


class BgpAdvertiseLocalLabeledRouteCfgEnum(Enum):
    """
    BgpAdvertiseLocalLabeledRouteCfgEnum

    Bgp advertise local labeled route cfg

    .. data:: enable = 1

    	Enable

    .. data:: disable = 2

    	Disable

    """

    enable = 1

    disable = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpAdvertiseLocalLabeledRouteCfgEnum']


class BgpNbrCapAdditionalPathsCfgEnum(Enum):
    """
    BgpNbrCapAdditionalPathsCfgEnum

    Bgp nbr cap additional paths cfg

    .. data:: enable = 1

    	Enable

    .. data:: disable = 2

    	Disable

    """

    enable = 1

    disable = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpNbrCapAdditionalPathsCfgEnum']


class BgpOfficialAddressFamilyEnum(Enum):
    """
    BgpOfficialAddressFamilyEnum

    Bgp official address family

    .. data:: ipv4 = 1

    	IPv4

    .. data:: ipv6 = 2

    	IPv6

    .. data:: l2vpn = 25

    	L2VPN

    .. data:: ls = 16388

    	LS

    .. data:: all = 65534

    	All

    """

    ipv4 = 1

    ipv6 = 2

    l2vpn = 25

    ls = 16388

    all = 65534


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpOfficialAddressFamilyEnum']


class BgpPrecedenceDscpEnum(Enum):
    """
    BgpPrecedenceDscpEnum

    Bgp precedence dscp

    .. data:: af11 = 10

    	AF11 dscp (001010)

    .. data:: af12 = 12

    	AF12 dscp (001100)

    .. data:: af13 = 14

    	AF13 dscp (001110)

    .. data:: af21 = 18

    	AF21 dscp (010010)

    .. data:: af22 = 20

    	AF22 dscp (010100)

    .. data:: af23 = 22

    	AF23 dscp (010110)

    .. data:: af31 = 26

    	AF31 dscp (011010)

    .. data:: af32 = 28

    	AF32 dscp (011100)

    .. data:: af33 = 30

    	AF33 dscp (011110)

    .. data:: af41 = 34

    	AF41 dscp (100010)

    .. data:: af42 = 36

    	AF42 dscp (100100)

    .. data:: af43 = 38

    	AF43 dscp (100110)

    .. data:: cs1 = 8

    	CS1 dscp (001000)

    .. data:: cs2 = 16

    	CS2 dscp (010000)

    .. data:: cs3 = 24

    	CS3 dscp (011000)

    .. data:: cs4 = 32

    	CS4 dscp (100000)

    .. data:: cs5 = 40

    	CS5 dscp (101000)

    .. data:: cs6 = 48

    	CS6 dscp (110000)

    .. data:: cs7 = 56

    	CS7 dscp (111000)

    .. data:: ef = 46

    	EF dscp (101110)

    .. data:: critical = 5

    	critical precedence (5)

    .. data:: flash = 3

    	flash precedence (3)

    .. data:: flash_override = 4

    	flash override precedence (4)

    .. data:: immediate = 2

    	immediate precedence (2)

    .. data:: internet = 6

    	internetwork control precedence (6)

    .. data:: network = 7

    	network control precedence (7)

    .. data:: priority = 1

    	priority precedence (1)

    .. data:: default_or_routine = 0

    	default dscp or routine precedence (0)

    """

    af11 = 10

    af12 = 12

    af13 = 14

    af21 = 18

    af22 = 20

    af23 = 22

    af31 = 26

    af32 = 28

    af33 = 30

    af41 = 34

    af42 = 36

    af43 = 38

    cs1 = 8

    cs2 = 16

    cs3 = 24

    cs4 = 32

    cs5 = 40

    cs6 = 48

    cs7 = 56

    ef = 46

    critical = 5

    flash = 3

    flash_override = 4

    immediate = 2

    internet = 6

    network = 7

    priority = 1

    default_or_routine = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpPrecedenceDscpEnum']


class BgpSubsequentAddressFamilyEnum(Enum):
    """
    BgpSubsequentAddressFamilyEnum

    Bgp subsequent address family

    .. data:: unicast = 1

    	Unicast

    .. data:: multicast = 2

    	Multicast

    .. data:: labeled_unicast = 4

    	Labeled unicast

    .. data:: mvpn = 5

    	MVPN

    .. data:: mspw = 6

    	MSPW

    .. data:: tunnel = 64

    	Tunnel

    .. data:: vpls = 65

    	VPLS

    .. data:: mdt = 66

    	MDT

    .. data:: vpws = 68

    	VPWS

    .. data:: evpn = 70

    	EVPN

    .. data:: ls = 71

    	LS

    .. data:: sr_policy = 73

    	SRPolicy

    .. data:: vpn = 128

    	VPN

    .. data:: vpn_mcast = 129

    	VPN MCAST

    .. data:: rt_filter = 132

    	Rt filter

    .. data:: flowspec = 133

    	Flowspec

    .. data:: vpn_flowspec = 134

    	VPN Flowspec

    .. data:: all = 254

    	All

    """

    unicast = 1

    multicast = 2

    labeled_unicast = 4

    mvpn = 5

    mspw = 6

    tunnel = 64

    vpls = 65

    mdt = 66

    vpws = 68

    evpn = 70

    ls = 71

    sr_policy = 73

    vpn = 128

    vpn_mcast = 129

    rt_filter = 132

    flowspec = 133

    vpn_flowspec = 134

    all = 254


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpSubsequentAddressFamilyEnum']


class BgpTosEnum(Enum):
    """
    BgpTosEnum

    Bgp tos

    .. data:: precedence = 0

    	Precedence

    .. data:: dscp = 1

    	DSCP

    """

    precedence = 0

    dscp = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpTosEnum']


class BgpUpdateFilterActionEnum(Enum):
    """
    BgpUpdateFilterActionEnum

    Bgp update filter action

    .. data:: treat_as_withdraw = 1

    	Treat as withdraw

    .. data:: discard_attibute = 2

    	Discard attribute

    """

    treat_as_withdraw = 1

    discard_attibute = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpUpdateFilterActionEnum']


class BgpafAdditionalPathsCfgEnum(Enum):
    """
    BgpafAdditionalPathsCfgEnum

    Bgpaf additional paths cfg

    .. data:: enable = 1

    	Enable

    .. data:: disable = 2

    	Disable

    """

    enable = 1

    disable = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_bgp_datatypes as meta
        return meta._meta_table['BgpafAdditionalPathsCfgEnum']



