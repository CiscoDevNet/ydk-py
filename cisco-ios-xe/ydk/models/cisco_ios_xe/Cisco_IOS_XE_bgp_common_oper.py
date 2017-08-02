""" Cisco_IOS_XE_bgp_common_oper 

This module contains a collection of YANG definitions
common for all bgp operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AfiSafi(Enum):
    """
    AfiSafi

    Base identity from which identities

    describing address families are derived.

    This identity represents IPv4 address family

    .. data:: ipv4_mdt = 0

    	IPv4 MDT address family

    .. data:: ipv4_multicast = 1

    	IPv4 Multicast address family

    .. data:: ipv4_unicast = 2

    	IPv4 Unicast address family

    .. data:: ipv4_mvpn = 3

    	IPV4 MVPN address family

    .. data:: ipv4_flowspec = 4

    	IPv4 Flowspec address family

    .. data:: ipv6_multicast = 5

    	IPv6 Multicast address family

    .. data:: ipv6_unicast = 6

    	IPv6 Unicast address family

    .. data:: ipv6_mvpn = 7

    	IPv6 MVPN address family

    .. data:: ipv6_flowspec = 8

    	IPv6 Flowspec address family

    .. data:: l2vpn_vpls = 9

    	L2VPN VPLS address family

    .. data:: l2vpn_e_vpn = 10

    	L2VPN EVPN address family

    .. data:: nsap_unicast = 11

    	NSAP Unicast address family

    .. data:: rtfilter_unicast = 12

    	RT Filter Unicast address family

    .. data:: vpnv4_multicast = 13

    	VPNv4 Multicast address family

    .. data:: vpnv4_unicast = 14

    	VPNv4 Unicast address family

    .. data:: vpnv6_unicast = 15

    	VPNv6 Unicast address family

    .. data:: vpnv6_multicast = 16

    	VPNv6 Multicast address family

    .. data:: vpnv4_flowspec = 17

    	VPNv4 Flowspec address family

    .. data:: vpnv6_flowspec = 18

    	VPNv6 Flowspec address family

    """

    ipv4_mdt = Enum.YLeaf(0, "ipv4-mdt")

    ipv4_multicast = Enum.YLeaf(1, "ipv4-multicast")

    ipv4_unicast = Enum.YLeaf(2, "ipv4-unicast")

    ipv4_mvpn = Enum.YLeaf(3, "ipv4-mvpn")

    ipv4_flowspec = Enum.YLeaf(4, "ipv4-flowspec")

    ipv6_multicast = Enum.YLeaf(5, "ipv6-multicast")

    ipv6_unicast = Enum.YLeaf(6, "ipv6-unicast")

    ipv6_mvpn = Enum.YLeaf(7, "ipv6-mvpn")

    ipv6_flowspec = Enum.YLeaf(8, "ipv6-flowspec")

    l2vpn_vpls = Enum.YLeaf(9, "l2vpn-vpls")

    l2vpn_e_vpn = Enum.YLeaf(10, "l2vpn-e-vpn")

    nsap_unicast = Enum.YLeaf(11, "nsap-unicast")

    rtfilter_unicast = Enum.YLeaf(12, "rtfilter-unicast")

    vpnv4_multicast = Enum.YLeaf(13, "vpnv4-multicast")

    vpnv4_unicast = Enum.YLeaf(14, "vpnv4-unicast")

    vpnv6_unicast = Enum.YLeaf(15, "vpnv6-unicast")

    vpnv6_multicast = Enum.YLeaf(16, "vpnv6-multicast")

    vpnv4_flowspec = Enum.YLeaf(17, "vpnv4-flowspec")

    vpnv6_flowspec = Enum.YLeaf(18, "vpnv6-flowspec")


class TcpFsmState(Enum):
    """
    TcpFsmState

    TCP state machine states

    .. data:: closed = 0

    	no connection

    .. data:: listen = 1

    	Waiting for a connection request from any remote TCP

    .. data:: synsent = 2

    	Waiting for a matching connection request

    	after having sent a connection request

    .. data:: synrcvd = 3

    	Waiting for a confirming connection request acknowledgment

    	after having both received and sent a connection request

    .. data:: established = 4

    	connection established

    .. data:: finwait1 = 5

    	Waiting for a connection termination request

    	from the remote TCP, or an acknowledgment of

    	the connection termination request previously sent

    .. data:: finwait2 = 6

    	Waiting for a connection termination request from the

    	remote TCP

    .. data:: closewait = 7

    	Waiting for a connection termination request from

    	the local use

    .. data:: lastack = 8

    	Waiting for an acknowledgment of the connection termination

    	request previously sent to the remote TCP

    .. data:: closing = 9

    	Waiting for a connection termination request acknowledgment

    	from the remote

    .. data:: timewait = 10

    	waiting for enough time to pass to be sure the remote TCP

    	received the acknowledgment of its connection termination request

    """

    closed = Enum.YLeaf(0, "closed")

    listen = Enum.YLeaf(1, "listen")

    synsent = Enum.YLeaf(2, "synsent")

    synrcvd = Enum.YLeaf(3, "synrcvd")

    established = Enum.YLeaf(4, "established")

    finwait1 = Enum.YLeaf(5, "finwait1")

    finwait2 = Enum.YLeaf(6, "finwait2")

    closewait = Enum.YLeaf(7, "closewait")

    lastack = Enum.YLeaf(8, "lastack")

    closing = Enum.YLeaf(9, "closing")

    timewait = Enum.YLeaf(10, "timewait")



