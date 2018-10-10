""" Cisco_IOS_XR_ipv4_bgp_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BgpAddressFamily(Enum):
    """
    BgpAddressFamily (Enum Class)

    Bgp address family

    .. data:: ipv4_unicast = 0

    	IPv4 unicast

    .. data:: ipv4_multicast = 1

    	IPv4 multicast

    .. data:: ipv4_labeled_unicast = 2

    	IPv4 labeled-unicast

    .. data:: ipv4_tunnel = 3

    	IPv4 tunnel

    .. data:: vpnv4_unicast = 4

    	VPNv4 unicast

    .. data:: ipv6_unicast = 5

    	IPv6 unicast

    .. data:: ipv6_multicast = 6

    	IPv6 multicast

    .. data:: ipv6_labeled_unicast = 7

    	IPv6 labeled-unicast

    .. data:: vpnv6_unicast = 8

    	VPNv6 unicast

    .. data:: ipv4_mdt = 9

    	IPv4 MDT

    .. data:: l2vpn_vpls = 10

    	L2VPN VPLS-VPWS

    .. data:: ipv4rt_constraint = 11

    	IPv4 rt-filter

    .. data:: ipv4_mvpn = 12

    	IPv4 MVPN

    .. data:: ipv6_mvpn = 13

    	IPv6 MVPN

    .. data:: l2vpn_evpn = 14

    	L2VPN EVPN

    .. data:: lsls = 15

    	Link-state link-state

    .. data:: vpnv4_multicast = 16

    	VPNv4 Multicast

    .. data:: vpnv6_multicast = 17

    	VPNv6 Multicast

    .. data:: ipv4_flowspec = 18

    	IPv4 flowspec

    .. data:: ipv6_flowspec = 19

    	IPv6 flowspec

    .. data:: vpnv4_flowspec = 20

    	VPNv4 flowspec

    .. data:: vpnv6_flowspec = 21

    	VPNv6 flowspec

    .. data:: l2vpn_mspw = 22

    	L2VPN MSPW

    .. data:: ipv4_sr_policy = 23

    	IPv4 SRPolicy

    .. data:: ipv6_sr_policy = 24

    	IPv6 SRPolicy

    .. data:: all_address_family = 25

    	All Address Families

    """

    ipv4_unicast = Enum.YLeaf(0, "ipv4-unicast")

    ipv4_multicast = Enum.YLeaf(1, "ipv4-multicast")

    ipv4_labeled_unicast = Enum.YLeaf(2, "ipv4-labeled-unicast")

    ipv4_tunnel = Enum.YLeaf(3, "ipv4-tunnel")

    vpnv4_unicast = Enum.YLeaf(4, "vpnv4-unicast")

    ipv6_unicast = Enum.YLeaf(5, "ipv6-unicast")

    ipv6_multicast = Enum.YLeaf(6, "ipv6-multicast")

    ipv6_labeled_unicast = Enum.YLeaf(7, "ipv6-labeled-unicast")

    vpnv6_unicast = Enum.YLeaf(8, "vpnv6-unicast")

    ipv4_mdt = Enum.YLeaf(9, "ipv4-mdt")

    l2vpn_vpls = Enum.YLeaf(10, "l2vpn-vpls")

    ipv4rt_constraint = Enum.YLeaf(11, "ipv4rt-constraint")

    ipv4_mvpn = Enum.YLeaf(12, "ipv4-mvpn")

    ipv6_mvpn = Enum.YLeaf(13, "ipv6-mvpn")

    l2vpn_evpn = Enum.YLeaf(14, "l2vpn-evpn")

    lsls = Enum.YLeaf(15, "lsls")

    vpnv4_multicast = Enum.YLeaf(16, "vpnv4-multicast")

    vpnv6_multicast = Enum.YLeaf(17, "vpnv6-multicast")

    ipv4_flowspec = Enum.YLeaf(18, "ipv4-flowspec")

    ipv6_flowspec = Enum.YLeaf(19, "ipv6-flowspec")

    vpnv4_flowspec = Enum.YLeaf(20, "vpnv4-flowspec")

    vpnv6_flowspec = Enum.YLeaf(21, "vpnv6-flowspec")

    l2vpn_mspw = Enum.YLeaf(22, "l2vpn-mspw")

    ipv4_sr_policy = Enum.YLeaf(23, "ipv4-sr-policy")

    ipv6_sr_policy = Enum.YLeaf(24, "ipv6-sr-policy")

    all_address_family = Enum.YLeaf(25, "all-address-family")


class BgpAdvertiseLocalLabeledRouteCfg(Enum):
    """
    BgpAdvertiseLocalLabeledRouteCfg (Enum Class)

    Bgp advertise local labeled route cfg

    .. data:: enable = 1

    	Enable

    .. data:: disable = 2

    	Disable

    """

    enable = Enum.YLeaf(1, "enable")

    disable = Enum.YLeaf(2, "disable")


class BgpAfAdditionalPathsCfg(Enum):
    """
    BgpAfAdditionalPathsCfg (Enum Class)

    Bgp af additional paths cfg

    .. data:: enable = 1

    	Enable

    .. data:: disable = 2

    	Disable

    """

    enable = Enum.YLeaf(1, "enable")

    disable = Enum.YLeaf(2, "disable")


class BgpNbrCapAdditionalPathsCfg(Enum):
    """
    BgpNbrCapAdditionalPathsCfg (Enum Class)

    Bgp nbr cap additional paths cfg

    .. data:: enable = 1

    	Enable

    .. data:: disable = 2

    	Disable

    """

    enable = Enum.YLeaf(1, "enable")

    disable = Enum.YLeaf(2, "disable")


class BgpOfficialAddressFamily(Enum):
    """
    BgpOfficialAddressFamily (Enum Class)

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

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")

    l2vpn = Enum.YLeaf(25, "l2vpn")

    ls = Enum.YLeaf(16388, "ls")

    all = Enum.YLeaf(65534, "all")


class BgpPrecedenceDscp(Enum):
    """
    BgpPrecedenceDscp (Enum Class)

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

    af11 = Enum.YLeaf(10, "af11")

    af12 = Enum.YLeaf(12, "af12")

    af13 = Enum.YLeaf(14, "af13")

    af21 = Enum.YLeaf(18, "af21")

    af22 = Enum.YLeaf(20, "af22")

    af23 = Enum.YLeaf(22, "af23")

    af31 = Enum.YLeaf(26, "af31")

    af32 = Enum.YLeaf(28, "af32")

    af33 = Enum.YLeaf(30, "af33")

    af41 = Enum.YLeaf(34, "af41")

    af42 = Enum.YLeaf(36, "af42")

    af43 = Enum.YLeaf(38, "af43")

    cs1 = Enum.YLeaf(8, "cs1")

    cs2 = Enum.YLeaf(16, "cs2")

    cs3 = Enum.YLeaf(24, "cs3")

    cs4 = Enum.YLeaf(32, "cs4")

    cs5 = Enum.YLeaf(40, "cs5")

    cs6 = Enum.YLeaf(48, "cs6")

    cs7 = Enum.YLeaf(56, "cs7")

    ef = Enum.YLeaf(46, "ef")

    critical = Enum.YLeaf(5, "critical")

    flash = Enum.YLeaf(3, "flash")

    flash_override = Enum.YLeaf(4, "flash-override")

    immediate = Enum.YLeaf(2, "immediate")

    internet = Enum.YLeaf(6, "internet")

    network = Enum.YLeaf(7, "network")

    priority = Enum.YLeaf(1, "priority")

    default_or_routine = Enum.YLeaf(0, "default-or-routine")


class BgpSubsequentAddressFamily(Enum):
    """
    BgpSubsequentAddressFamily (Enum Class)

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

    unicast = Enum.YLeaf(1, "unicast")

    multicast = Enum.YLeaf(2, "multicast")

    labeled_unicast = Enum.YLeaf(4, "labeled-unicast")

    mvpn = Enum.YLeaf(5, "mvpn")

    mspw = Enum.YLeaf(6, "mspw")

    tunnel = Enum.YLeaf(64, "tunnel")

    vpls = Enum.YLeaf(65, "vpls")

    mdt = Enum.YLeaf(66, "mdt")

    vpws = Enum.YLeaf(68, "vpws")

    evpn = Enum.YLeaf(70, "evpn")

    ls = Enum.YLeaf(71, "ls")

    sr_policy = Enum.YLeaf(73, "sr-policy")

    vpn = Enum.YLeaf(128, "vpn")

    vpn_mcast = Enum.YLeaf(129, "vpn-mcast")

    rt_filter = Enum.YLeaf(132, "rt-filter")

    flowspec = Enum.YLeaf(133, "flowspec")

    vpn_flowspec = Enum.YLeaf(134, "vpn-flowspec")

    all = Enum.YLeaf(254, "all")


class BgpTos(Enum):
    """
    BgpTos (Enum Class)

    Bgp tos

    .. data:: precedence = 0

    	Precedence

    .. data:: dscp = 1

    	DSCP

    """

    precedence = Enum.YLeaf(0, "precedence")

    dscp = Enum.YLeaf(1, "dscp")


class BgpUpdateFilterAction(Enum):
    """
    BgpUpdateFilterAction (Enum Class)

    Bgp update filter action

    .. data:: treat_as_withdraw = 1

    	Treat as withdraw

    .. data:: discard_attibute = 2

    	Discard attribute

    """

    treat_as_withdraw = Enum.YLeaf(1, "treat-as-withdraw")

    discard_attibute = Enum.YLeaf(2, "discard-attibute")



