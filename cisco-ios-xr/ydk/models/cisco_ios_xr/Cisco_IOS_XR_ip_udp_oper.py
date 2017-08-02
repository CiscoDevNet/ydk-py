""" Cisco_IOS_XR_ip_udp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-udp package operational data.

This module contains definitions
for the following management objects\:
  udp\: IP UDP Operational Data
  udp\-connection\: udp connection

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AddrFamily(Enum):
    """
    AddrFamily

    Address Family Types

    .. data:: unspecified = 0

    	Unspecified

    .. data:: local = 1

    	Local to host (pipes, portals)

    .. data:: inet = 2

    	Internetwork: UDP, TCP, etc.

    .. data:: implink = 3

    	arpanet imp addresses

    .. data:: pup = 4

    	Pup protocols: e.g. BSP

    .. data:: chaos = 5

    	mit CHAOS protocols

    .. data:: ns = 6

    	XEROX NS protocols

    .. data:: iso = 7

    	ISO protocols

    .. data:: ecma = 8

    	European computer manufacturers

    .. data:: data_kit = 9

    	Datakit protocols

    .. data:: ccitt = 10

    	CCITT protocols, X.25 etc

    .. data:: sna = 11

    	IBM SNA

    .. data:: de_cnet = 12

    	DECnet

    .. data:: dli = 13

    	DEC Direct data link interface

    .. data:: lat = 14

    	LAT

    .. data:: hylink = 15

    	NSC Hyperchannel

    .. data:: appletalk = 16

    	Apple Talk

    .. data:: route = 17

    	Internal Routing Protocol

    .. data:: link = 18

    	Link layer interface

    .. data:: pseudo_xtp = 19

    	eXpress Transfer Protocol (no AF)

    .. data:: coip = 20

    	Connection-oriented IP, aka ST II

    .. data:: cnt = 21

    	Computer Network Technology

    .. data:: pseudo_rtip = 22

    	Help Identify RTIP packets

    .. data:: ipx = 23

    	Novell Internet Protocol

    .. data:: sip = 24

    	Simple Internet Protocol

    .. data:: pseudo_pip = 25

    	Help Identify PIP packets

    .. data:: inet6 = 26

    	IP version 6

    .. data:: snap = 27

    	802.2 SNAP sockets

    .. data:: clnl = 28

    	SAP_CLNS + nlpid encaps

    .. data:: chdlc = 29

    	cisco HDLC on serial

    .. data:: ppp = 30

    	PPP sockets

    .. data:: host_cas = 31

    	Host-based CAS signaling

    .. data:: dsp = 32

    	DSP messaging

    .. data:: sap = 33

    	SAP Sockets

    .. data:: atm = 34

    	ATM Sockets

    .. data:: fr = 35

    	Frame Relay sockets

    .. data:: mso = 36

    	Voice Media Stream Sockets

    .. data:: dchan = 37

    	ISDN D Channel Sockets

    .. data:: cas = 38

    	Trunk Framer media IF Sockets

    .. data:: nat = 39

    	Network Address Translation Sockets

    .. data:: ether = 40

    	Generic Ethernet Sockets

    .. data:: srp = 41

    	Spatial Reuse Protocol Sockets

    """

    unspecified = Enum.YLeaf(0, "unspecified")

    local = Enum.YLeaf(1, "local")

    inet = Enum.YLeaf(2, "inet")

    implink = Enum.YLeaf(3, "implink")

    pup = Enum.YLeaf(4, "pup")

    chaos = Enum.YLeaf(5, "chaos")

    ns = Enum.YLeaf(6, "ns")

    iso = Enum.YLeaf(7, "iso")

    ecma = Enum.YLeaf(8, "ecma")

    data_kit = Enum.YLeaf(9, "data-kit")

    ccitt = Enum.YLeaf(10, "ccitt")

    sna = Enum.YLeaf(11, "sna")

    de_cnet = Enum.YLeaf(12, "de-cnet")

    dli = Enum.YLeaf(13, "dli")

    lat = Enum.YLeaf(14, "lat")

    hylink = Enum.YLeaf(15, "hylink")

    appletalk = Enum.YLeaf(16, "appletalk")

    route = Enum.YLeaf(17, "route")

    link = Enum.YLeaf(18, "link")

    pseudo_xtp = Enum.YLeaf(19, "pseudo-xtp")

    coip = Enum.YLeaf(20, "coip")

    cnt = Enum.YLeaf(21, "cnt")

    pseudo_rtip = Enum.YLeaf(22, "pseudo-rtip")

    ipx = Enum.YLeaf(23, "ipx")

    sip = Enum.YLeaf(24, "sip")

    pseudo_pip = Enum.YLeaf(25, "pseudo-pip")

    inet6 = Enum.YLeaf(26, "inet6")

    snap = Enum.YLeaf(27, "snap")

    clnl = Enum.YLeaf(28, "clnl")

    chdlc = Enum.YLeaf(29, "chdlc")

    ppp = Enum.YLeaf(30, "ppp")

    host_cas = Enum.YLeaf(31, "host-cas")

    dsp = Enum.YLeaf(32, "dsp")

    sap = Enum.YLeaf(33, "sap")

    atm = Enum.YLeaf(34, "atm")

    fr = Enum.YLeaf(35, "fr")

    mso = Enum.YLeaf(36, "mso")

    dchan = Enum.YLeaf(37, "dchan")

    cas = Enum.YLeaf(38, "cas")

    nat = Enum.YLeaf(39, "nat")

    ether = Enum.YLeaf(40, "ether")

    srp = Enum.YLeaf(41, "srp")


class LptsPcbQuery(Enum):
    """
    LptsPcbQuery

    Lpts pcb query

    .. data:: all = 0

    	No filter

    .. data:: static_policy = 1

    	Static policy filter

    .. data:: interface = 2

    	Interface filter

    .. data:: packet = 3

    	Packet type filter

    """

    all = Enum.YLeaf(0, "all")

    static_policy = Enum.YLeaf(1, "static-policy")

    interface = Enum.YLeaf(2, "interface")

    packet = Enum.YLeaf(3, "packet")


class MessageTypeIcmp(Enum):
    """
    MessageTypeIcmp

    LPTS ICMP message types

    .. data:: echo_reply = 0

    	ICMP Packet type: Echo reply

    .. data:: destination_unreachable = 3

    	ICMP Packet type: Destination unreachable

    .. data:: source_quench = 4

    	ICMP Packet type: Source quench

    .. data:: redirect = 5

    	ICMP Packet type: Redirect

    .. data:: alternate_host_address = 6

    	ICMP Packet type: Alternate host address

    .. data:: echo = 8

    	ICMP Packet type: Echo

    .. data:: router_advertisement = 9

    	ICMP Packet type: Router advertisement

    .. data:: router_selection = 10

    	ICMP Packet type: Router selection

    .. data:: time_exceeded = 11

    	ICMP Packet type: Time exceeded

    .. data:: parameter_problem = 12

    	ICMP Packet type: Parameter problem

    .. data:: time_stamp = 13

    	ICMP Packet type: Time stamp

    .. data:: time_stamp_reply = 14

    	ICMP Packet type: Time stamp reply

    .. data:: information_request = 15

    	ICMP Packet type: Information request

    .. data:: information_reply = 16

    	ICMP Packet type: Information reply

    .. data:: address_mask_request = 17

    	ICMP Packet type: Address mask request

    .. data:: address_mask_reply = 18

    	ICMP Packet type: Address mask reply

    .. data:: trace_route = 30

    	ICMP Packet type: Trace route

    .. data:: datagram_conversion_error = 31

    	ICMP Packet type: Datagram Conversion error

    .. data:: mobile_host_redirect = 32

    	ICMP Packet type: Mobile host redirect

    .. data:: where_are_you = 33

    	ICMP Packet type: IPv6 where-are-you

    .. data:: iam_here = 34

    	ICMP Packet type: IPv6 i-am-here

    .. data:: mobile_registration_request = 35

    	ICMP Packet type: Mobile registration request

    .. data:: mobile_registration_reply = 36

    	ICMP Packet type: Mobile registration reply

    .. data:: domain_name_request = 37

    	ICMP Packet type: Domain name request

    """

    echo_reply = Enum.YLeaf(0, "echo-reply")

    destination_unreachable = Enum.YLeaf(3, "destination-unreachable")

    source_quench = Enum.YLeaf(4, "source-quench")

    redirect = Enum.YLeaf(5, "redirect")

    alternate_host_address = Enum.YLeaf(6, "alternate-host-address")

    echo = Enum.YLeaf(8, "echo")

    router_advertisement = Enum.YLeaf(9, "router-advertisement")

    router_selection = Enum.YLeaf(10, "router-selection")

    time_exceeded = Enum.YLeaf(11, "time-exceeded")

    parameter_problem = Enum.YLeaf(12, "parameter-problem")

    time_stamp = Enum.YLeaf(13, "time-stamp")

    time_stamp_reply = Enum.YLeaf(14, "time-stamp-reply")

    information_request = Enum.YLeaf(15, "information-request")

    information_reply = Enum.YLeaf(16, "information-reply")

    address_mask_request = Enum.YLeaf(17, "address-mask-request")

    address_mask_reply = Enum.YLeaf(18, "address-mask-reply")

    trace_route = Enum.YLeaf(30, "trace-route")

    datagram_conversion_error = Enum.YLeaf(31, "datagram-conversion-error")

    mobile_host_redirect = Enum.YLeaf(32, "mobile-host-redirect")

    where_are_you = Enum.YLeaf(33, "where-are-you")

    iam_here = Enum.YLeaf(34, "iam-here")

    mobile_registration_request = Enum.YLeaf(35, "mobile-registration-request")

    mobile_registration_reply = Enum.YLeaf(36, "mobile-registration-reply")

    domain_name_request = Enum.YLeaf(37, "domain-name-request")


class MessageTypeIcmp(Enum):
    """
    MessageTypeIcmp

    LPTS ICMP message types

    .. data:: echo_reply = 0

    	ICMP Packet type: Echo reply

    .. data:: destination_unreachable = 3

    	ICMP Packet type: Destination unreachable

    .. data:: source_quench = 4

    	ICMP Packet type: Source quench

    .. data:: redirect = 5

    	ICMP Packet type: Redirect

    .. data:: alternate_host_address = 6

    	ICMP Packet type: Alternate host address

    .. data:: echo = 8

    	ICMP Packet type: Echo

    .. data:: router_advertisement = 9

    	ICMP Packet type: Router advertisement

    .. data:: router_selection = 10

    	ICMP Packet type: Router selection

    .. data:: time_exceeded = 11

    	ICMP Packet type: Time exceeded

    .. data:: parameter_problem = 12

    	ICMP Packet type: Parameter problem

    .. data:: time_stamp = 13

    	ICMP Packet type: Time stamp

    .. data:: time_stamp_reply = 14

    	ICMP Packet type: Time stamp reply

    .. data:: information_request = 15

    	ICMP Packet type: Information request

    .. data:: information_reply = 16

    	ICMP Packet type: Information reply

    .. data:: address_mask_request = 17

    	ICMP Packet type: Address mask request

    .. data:: address_mask_reply = 18

    	ICMP Packet type: Address mask reply

    .. data:: trace_route = 30

    	ICMP Packet type: Trace route

    .. data:: datagram_conversion_error = 31

    	ICMP Packet type: Datagram Conversion error

    .. data:: mobile_host_redirect = 32

    	ICMP Packet type: Mobile host redirect

    .. data:: where_are_you = 33

    	ICMP Packet type: IPv6 where-are-you

    .. data:: iam_here = 34

    	ICMP Packet type: IPv6 i-am-here

    .. data:: mobile_registration_request = 35

    	ICMP Packet type: Mobile registration request

    .. data:: mobile_registration_reply = 36

    	ICMP Packet type: Mobile registration reply

    .. data:: domain_name_request = 37

    	ICMP Packet type: Domain name request

    """

    echo_reply = Enum.YLeaf(0, "echo-reply")

    destination_unreachable = Enum.YLeaf(3, "destination-unreachable")

    source_quench = Enum.YLeaf(4, "source-quench")

    redirect = Enum.YLeaf(5, "redirect")

    alternate_host_address = Enum.YLeaf(6, "alternate-host-address")

    echo = Enum.YLeaf(8, "echo")

    router_advertisement = Enum.YLeaf(9, "router-advertisement")

    router_selection = Enum.YLeaf(10, "router-selection")

    time_exceeded = Enum.YLeaf(11, "time-exceeded")

    parameter_problem = Enum.YLeaf(12, "parameter-problem")

    time_stamp = Enum.YLeaf(13, "time-stamp")

    time_stamp_reply = Enum.YLeaf(14, "time-stamp-reply")

    information_request = Enum.YLeaf(15, "information-request")

    information_reply = Enum.YLeaf(16, "information-reply")

    address_mask_request = Enum.YLeaf(17, "address-mask-request")

    address_mask_reply = Enum.YLeaf(18, "address-mask-reply")

    trace_route = Enum.YLeaf(30, "trace-route")

    datagram_conversion_error = Enum.YLeaf(31, "datagram-conversion-error")

    mobile_host_redirect = Enum.YLeaf(32, "mobile-host-redirect")

    where_are_you = Enum.YLeaf(33, "where-are-you")

    iam_here = Enum.YLeaf(34, "iam-here")

    mobile_registration_request = Enum.YLeaf(35, "mobile-registration-request")

    mobile_registration_reply = Enum.YLeaf(36, "mobile-registration-reply")

    domain_name_request = Enum.YLeaf(37, "domain-name-request")


class MessageTypeIcmpv6(Enum):
    """
    MessageTypeIcmpv6

    LPTS ICMPv6 message types

    .. data:: destination_unreachable = 1

    	ICMPv6 Packet type: Destination unreachable

    .. data:: packet_too_big = 2

    	ICMPv6 Packet type: packet too big

    .. data:: time_exceeded = 3

    	ICMPv6 Packet type: Time exceeded

    .. data:: parameter_problem = 4

    	ICMPv6 Packet type: Parameter problem

    .. data:: echo_request = 128

    	ICMPv6 Packet type: Echo request

    .. data:: echo_reply = 129

    	ICMPv6 Packet type: Echo reply

    .. data:: multicast_listener_query = 130

    	ICMPv6 Packet type: Multicast listener query

    .. data:: multicast_listener_report = 131

    	ICMPv6 Packet type: Multicast listener report

    .. data:: multicast_listener_done = 132

    	ICMPv6 Packet type: Multicast listener done

    .. data:: router_solicitation = 133

    	ICMPv6 Packet type: Router solicitation

    .. data:: router_advertisement = 134

    	ICMPv6 Packet type: Router advertisement

    .. data:: neighbor_solicitation = 135

    	ICMPv6 Packet type: Neighbor solicitation

    .. data:: neighbor_advertisement = 136

    	ICMPv6 Packet type: Neighbor advertisement

    .. data:: redirect_message = 137

    	ICMPv6 Packet type: Redirect message

    .. data:: router_renumbering = 138

    	ICMPv6 Packet type: Router renumbering

    .. data:: node_information_query = 139

    	ICMPv6 Packet type: Node information query

    .. data:: node_information_reply = 140

    	ICMPv6 Packet type: Node information reply

    .. data:: inverse_neighbor_discovery_solicitaion = 141

    	ICMPv6 Packet type: Inverse neighbor discovery

    	solicitation message

    .. data:: inverse_neighbor_discover_advertisement = 142

    	ICMPv6 Packet type: Inverse neighbor discovery

    	advertisement message

    .. data:: v2_multicast_listener_report = 143

    	ICMPv6 Packet type: Version 2 multicast

    	listener report

    .. data:: home_agent_address_discovery_request = 144

    	ICMPv6 Packet type: Home agent address

    	discovery request message

    .. data:: home_agent_address_discovery_reply = 145

    	ICMPv6 Packet type: Home agent address

    	discovery reply message

    .. data:: mobile_prefix_solicitation = 146

    	ICMPv6 Packet type: Mobile prefix solicitation

    .. data:: mobile_prefix_advertisement = 147

    	ICMPv6 Packet type: Mobile prefix advertisement

    .. data:: certification_path_solicitation_message = 148

    	ICMPv6 Packet type: Certification path

    	solicitation message

    .. data:: certification_path_advertisement_message = 149

    	ICMPv6 Packet type: Certification path

    	advertisement message

    .. data:: experimental_mobility_protocols = 150

    	ICMPv6 Packet type: ICMP messages utilized by

    	experimental mobility  protocols such as

    	seamoby

    .. data:: multicast_router_advertisement = 151

    	ICMPv6 Packet type: Multicast router

    	advertisement

    .. data:: multicast_router_solicitation = 152

    	ICMPv6 Packet type: Multicast router

    	solicitation

    .. data:: multicast_router_termination = 153

    	ICMPv6 Packet type: Multicast router

    	termination

    .. data:: fmipv6_messages = 154

    	ICMPv6 Packet type: FMIPv6 messages

    """

    destination_unreachable = Enum.YLeaf(1, "destination-unreachable")

    packet_too_big = Enum.YLeaf(2, "packet-too-big")

    time_exceeded = Enum.YLeaf(3, "time-exceeded")

    parameter_problem = Enum.YLeaf(4, "parameter-problem")

    echo_request = Enum.YLeaf(128, "echo-request")

    echo_reply = Enum.YLeaf(129, "echo-reply")

    multicast_listener_query = Enum.YLeaf(130, "multicast-listener-query")

    multicast_listener_report = Enum.YLeaf(131, "multicast-listener-report")

    multicast_listener_done = Enum.YLeaf(132, "multicast-listener-done")

    router_solicitation = Enum.YLeaf(133, "router-solicitation")

    router_advertisement = Enum.YLeaf(134, "router-advertisement")

    neighbor_solicitation = Enum.YLeaf(135, "neighbor-solicitation")

    neighbor_advertisement = Enum.YLeaf(136, "neighbor-advertisement")

    redirect_message = Enum.YLeaf(137, "redirect-message")

    router_renumbering = Enum.YLeaf(138, "router-renumbering")

    node_information_query = Enum.YLeaf(139, "node-information-query")

    node_information_reply = Enum.YLeaf(140, "node-information-reply")

    inverse_neighbor_discovery_solicitaion = Enum.YLeaf(141, "inverse-neighbor-discovery-solicitaion")

    inverse_neighbor_discover_advertisement = Enum.YLeaf(142, "inverse-neighbor-discover-advertisement")

    v2_multicast_listener_report = Enum.YLeaf(143, "v2-multicast-listener-report")

    home_agent_address_discovery_request = Enum.YLeaf(144, "home-agent-address-discovery-request")

    home_agent_address_discovery_reply = Enum.YLeaf(145, "home-agent-address-discovery-reply")

    mobile_prefix_solicitation = Enum.YLeaf(146, "mobile-prefix-solicitation")

    mobile_prefix_advertisement = Enum.YLeaf(147, "mobile-prefix-advertisement")

    certification_path_solicitation_message = Enum.YLeaf(148, "certification-path-solicitation-message")

    certification_path_advertisement_message = Enum.YLeaf(149, "certification-path-advertisement-message")

    experimental_mobility_protocols = Enum.YLeaf(150, "experimental-mobility-protocols")

    multicast_router_advertisement = Enum.YLeaf(151, "multicast-router-advertisement")

    multicast_router_solicitation = Enum.YLeaf(152, "multicast-router-solicitation")

    multicast_router_termination = Enum.YLeaf(153, "multicast-router-termination")

    fmipv6_messages = Enum.YLeaf(154, "fmipv6-messages")


class MessageTypeIcmpv6(Enum):
    """
    MessageTypeIcmpv6

    LPTS ICMPv6 message types

    .. data:: destination_unreachable = 1

    	ICMPv6 Packet type: Destination unreachable

    .. data:: packet_too_big = 2

    	ICMPv6 Packet type: packet too big

    .. data:: time_exceeded = 3

    	ICMPv6 Packet type: Time exceeded

    .. data:: parameter_problem = 4

    	ICMPv6 Packet type: Parameter problem

    .. data:: echo_request = 128

    	ICMPv6 Packet type: Echo request

    .. data:: echo_reply = 129

    	ICMPv6 Packet type: Echo reply

    .. data:: multicast_listener_query = 130

    	ICMPv6 Packet type: Multicast listener query

    .. data:: multicast_listener_report = 131

    	ICMPv6 Packet type: Multicast listener report

    .. data:: multicast_listener_done = 132

    	ICMPv6 Packet type: Multicast listener done

    .. data:: router_solicitation = 133

    	ICMPv6 Packet type: Router solicitation

    .. data:: router_advertisement = 134

    	ICMPv6 Packet type: Router advertisement

    .. data:: neighbor_solicitation = 135

    	ICMPv6 Packet type: Neighbor solicitation

    .. data:: neighbor_advertisement = 136

    	ICMPv6 Packet type: Neighbor advertisement

    .. data:: redirect_message = 137

    	ICMPv6 Packet type: Redirect message

    .. data:: router_renumbering = 138

    	ICMPv6 Packet type: Router renumbering

    .. data:: node_information_query = 139

    	ICMPv6 Packet type: Node information query

    .. data:: node_information_reply = 140

    	ICMPv6 Packet type: Node information reply

    .. data:: inverse_neighbor_discovery_solicitaion = 141

    	ICMPv6 Packet type: Inverse neighbor discovery

    	solicitation message

    .. data:: inverse_neighbor_discover_advertisement = 142

    	ICMPv6 Packet type: Inverse neighbor discovery

    	advertisement message

    .. data:: v2_multicast_listener_report = 143

    	ICMPv6 Packet type: Version 2 multicast

    	listener report

    .. data:: home_agent_address_discovery_request = 144

    	ICMPv6 Packet type: Home agent address

    	discovery request message

    .. data:: home_agent_address_discovery_reply = 145

    	ICMPv6 Packet type: Home agent address

    	discovery reply message

    .. data:: mobile_prefix_solicitation = 146

    	ICMPv6 Packet type: Mobile prefix solicitation

    .. data:: mobile_prefix_advertisement = 147

    	ICMPv6 Packet type: Mobile prefix advertisement

    .. data:: certification_path_solicitation_message = 148

    	ICMPv6 Packet type: Certification path

    	solicitation message

    .. data:: certification_path_advertisement_message = 149

    	ICMPv6 Packet type: Certification path

    	advertisement message

    .. data:: experimental_mobility_protocols = 150

    	ICMPv6 Packet type: ICMP messages utilized by

    	experimental mobility  protocols such as

    	seamoby

    .. data:: multicast_router_advertisement = 151

    	ICMPv6 Packet type: Multicast router

    	advertisement

    .. data:: multicast_router_solicitation = 152

    	ICMPv6 Packet type: Multicast router

    	solicitation

    .. data:: multicast_router_termination = 153

    	ICMPv6 Packet type: Multicast router

    	termination

    .. data:: fmipv6_messages = 154

    	ICMPv6 Packet type: FMIPv6 messages

    """

    destination_unreachable = Enum.YLeaf(1, "destination-unreachable")

    packet_too_big = Enum.YLeaf(2, "packet-too-big")

    time_exceeded = Enum.YLeaf(3, "time-exceeded")

    parameter_problem = Enum.YLeaf(4, "parameter-problem")

    echo_request = Enum.YLeaf(128, "echo-request")

    echo_reply = Enum.YLeaf(129, "echo-reply")

    multicast_listener_query = Enum.YLeaf(130, "multicast-listener-query")

    multicast_listener_report = Enum.YLeaf(131, "multicast-listener-report")

    multicast_listener_done = Enum.YLeaf(132, "multicast-listener-done")

    router_solicitation = Enum.YLeaf(133, "router-solicitation")

    router_advertisement = Enum.YLeaf(134, "router-advertisement")

    neighbor_solicitation = Enum.YLeaf(135, "neighbor-solicitation")

    neighbor_advertisement = Enum.YLeaf(136, "neighbor-advertisement")

    redirect_message = Enum.YLeaf(137, "redirect-message")

    router_renumbering = Enum.YLeaf(138, "router-renumbering")

    node_information_query = Enum.YLeaf(139, "node-information-query")

    node_information_reply = Enum.YLeaf(140, "node-information-reply")

    inverse_neighbor_discovery_solicitaion = Enum.YLeaf(141, "inverse-neighbor-discovery-solicitaion")

    inverse_neighbor_discover_advertisement = Enum.YLeaf(142, "inverse-neighbor-discover-advertisement")

    v2_multicast_listener_report = Enum.YLeaf(143, "v2-multicast-listener-report")

    home_agent_address_discovery_request = Enum.YLeaf(144, "home-agent-address-discovery-request")

    home_agent_address_discovery_reply = Enum.YLeaf(145, "home-agent-address-discovery-reply")

    mobile_prefix_solicitation = Enum.YLeaf(146, "mobile-prefix-solicitation")

    mobile_prefix_advertisement = Enum.YLeaf(147, "mobile-prefix-advertisement")

    certification_path_solicitation_message = Enum.YLeaf(148, "certification-path-solicitation-message")

    certification_path_advertisement_message = Enum.YLeaf(149, "certification-path-advertisement-message")

    experimental_mobility_protocols = Enum.YLeaf(150, "experimental-mobility-protocols")

    multicast_router_advertisement = Enum.YLeaf(151, "multicast-router-advertisement")

    multicast_router_solicitation = Enum.YLeaf(152, "multicast-router-solicitation")

    multicast_router_termination = Enum.YLeaf(153, "multicast-router-termination")

    fmipv6_messages = Enum.YLeaf(154, "fmipv6-messages")


class MessageTypeIgmp(Enum):
    """
    MessageTypeIgmp

    LPTS IGMP message types

    .. data:: membership_query = 17

    	IGMP Packet type: Membership query

    .. data:: v1_membership_report = 18

    	IGMP Packet type: V1 membership report

    .. data:: dvmrp = 19

    	IGMP Packet type: DVMRP

    .. data:: pi_mv1 = 20

    	IGMP Packet type: PIM version 1

    .. data:: cisco_trace_messages = 21

    	IGMP Packet type: Cisco Trace Messages

    .. data:: v2_membership_report = 22

    	IGMP Packet type: V2 membership report

    .. data:: v2_leave_group = 23

    	IGMP Packet type: V2 leave group

    .. data:: multicast_traceroute_response = 30

    	IGMP Packet type: Multicast traceroute response

    .. data:: multicast_traceroute = 31

    	IGMP Packet type: MulticastTraceroute

    .. data:: v3_membership_report = 34

    	IGMP Packet type: V3 membership report

    .. data:: multicast_router_advertisement = 48

    	IGMP Packet type: Multicast router

    	advertisement

    .. data:: multicast_router_solicitation = 49

    	IGMP Packet type: Multicast router solicitation

    .. data:: multicast_router_termination = 50

    	IGMP Packet type: Multicast router termination

    """

    membership_query = Enum.YLeaf(17, "membership-query")

    v1_membership_report = Enum.YLeaf(18, "v1-membership-report")

    dvmrp = Enum.YLeaf(19, "dvmrp")

    pi_mv1 = Enum.YLeaf(20, "pi-mv1")

    cisco_trace_messages = Enum.YLeaf(21, "cisco-trace-messages")

    v2_membership_report = Enum.YLeaf(22, "v2-membership-report")

    v2_leave_group = Enum.YLeaf(23, "v2-leave-group")

    multicast_traceroute_response = Enum.YLeaf(30, "multicast-traceroute-response")

    multicast_traceroute = Enum.YLeaf(31, "multicast-traceroute")

    v3_membership_report = Enum.YLeaf(34, "v3-membership-report")

    multicast_router_advertisement = Enum.YLeaf(48, "multicast-router-advertisement")

    multicast_router_solicitation = Enum.YLeaf(49, "multicast-router-solicitation")

    multicast_router_termination = Enum.YLeaf(50, "multicast-router-termination")


class MessageTypeIgmp(Enum):
    """
    MessageTypeIgmp

    LPTS IGMP message types

    .. data:: membership_query = 17

    	IGMP Packet type: Membership query

    .. data:: v1_membership_report = 18

    	IGMP Packet type: V1 membership report

    .. data:: dvmrp = 19

    	IGMP Packet type: DVMRP

    .. data:: pi_mv1 = 20

    	IGMP Packet type: PIM version 1

    .. data:: cisco_trace_messages = 21

    	IGMP Packet type: Cisco Trace Messages

    .. data:: v2_membership_report = 22

    	IGMP Packet type: V2 membership report

    .. data:: v2_leave_group = 23

    	IGMP Packet type: V2 leave group

    .. data:: multicast_traceroute_response = 30

    	IGMP Packet type: Multicast traceroute response

    .. data:: multicast_traceroute = 31

    	IGMP Packet type: MulticastTraceroute

    .. data:: v3_membership_report = 34

    	IGMP Packet type: V3 membership report

    .. data:: multicast_router_advertisement = 48

    	IGMP Packet type: Multicast router

    	advertisement

    .. data:: multicast_router_solicitation = 49

    	IGMP Packet type: Multicast router solicitation

    .. data:: multicast_router_termination = 50

    	IGMP Packet type: Multicast router termination

    """

    membership_query = Enum.YLeaf(17, "membership-query")

    v1_membership_report = Enum.YLeaf(18, "v1-membership-report")

    dvmrp = Enum.YLeaf(19, "dvmrp")

    pi_mv1 = Enum.YLeaf(20, "pi-mv1")

    cisco_trace_messages = Enum.YLeaf(21, "cisco-trace-messages")

    v2_membership_report = Enum.YLeaf(22, "v2-membership-report")

    v2_leave_group = Enum.YLeaf(23, "v2-leave-group")

    multicast_traceroute_response = Enum.YLeaf(30, "multicast-traceroute-response")

    multicast_traceroute = Enum.YLeaf(31, "multicast-traceroute")

    v3_membership_report = Enum.YLeaf(34, "v3-membership-report")

    multicast_router_advertisement = Enum.YLeaf(48, "multicast-router-advertisement")

    multicast_router_solicitation = Enum.YLeaf(49, "multicast-router-solicitation")

    multicast_router_termination = Enum.YLeaf(50, "multicast-router-termination")


class Packet(Enum):
    """
    Packet

    Packet type

    .. data:: icmp = 0

    	ICMP packet type

    .. data:: icm_pv6 = 1

    	ICMPv6 packet type

    .. data:: igmp = 2

    	IGMP packet type

    .. data:: unknown = 3

    	Packet type unknown

    """

    icmp = Enum.YLeaf(0, "icmp")

    icm_pv6 = Enum.YLeaf(1, "icm-pv6")

    igmp = Enum.YLeaf(2, "igmp")

    unknown = Enum.YLeaf(3, "unknown")


class UdpAddressFamily(Enum):
    """
    UdpAddressFamily

    Address Family Type

    .. data:: ipv4 = 2

    	IPv4

    .. data:: ipv6 = 10

    	IPv6

    """

    ipv4 = Enum.YLeaf(2, "ipv4")

    ipv6 = Enum.YLeaf(10, "ipv6")



class Udp(Entity):
    """
    IP UDP Operational Data
    
    .. attribute:: nodes
    
    	Node\-specific UDP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2016-02-26'

    def __init__(self):
        super(Udp, self).__init__()
        self._top_entity = None

        self.yang_name = "udp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-udp-oper"

        self.nodes = Udp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        Node\-specific UDP operational data
        
        .. attribute:: node
        
        	UDP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2016-02-26'

        def __init__(self):
            super(Udp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "udp"

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Udp.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Udp.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            UDP operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistical UDP operational data for a node
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2016-02-26'

            def __init__(self):
                super(Udp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.statistics = Udp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Udp.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Udp.Nodes.Node, self).__setattr__(name, value)


            class Statistics(Entity):
                """
                Statistical UDP operational data for a node
                
                .. attribute:: ipv4_traffic
                
                	UDP Traffic statistics for IPv4
                	**type**\:   :py:class:`Ipv4Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv4Traffic>`
                
                .. attribute:: ipv6_traffic
                
                	UDP Traffic statistics for IPv6
                	**type**\:   :py:class:`Ipv6Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv6Traffic>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2016-02-26'

                def __init__(self):
                    super(Udp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"

                    self.ipv4_traffic = Udp.Nodes.Node.Statistics.Ipv4Traffic()
                    self.ipv4_traffic.parent = self
                    self._children_name_map["ipv4_traffic"] = "ipv4-traffic"
                    self._children_yang_names.add("ipv4-traffic")

                    self.ipv6_traffic = Udp.Nodes.Node.Statistics.Ipv6Traffic()
                    self.ipv6_traffic.parent = self
                    self._children_name_map["ipv6_traffic"] = "ipv6-traffic"
                    self._children_yang_names.add("ipv6-traffic")


                class Ipv4Traffic(Entity):
                    """
                    UDP Traffic statistics for IPv4
                    
                    .. attribute:: udp_bad_length_packets
                    
                    	UDP bad length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_checksum_error_packets
                    
                    	UDP Checksum Errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_dropped_packets
                    
                    	UDP drop for other reason
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_input_packets
                    
                    	UDP Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_no_port_packets
                    
                    	UDP No Port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_output_packets
                    
                    	UDP Transmitted
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(Udp.Nodes.Node.Statistics.Ipv4Traffic, self).__init__()

                        self.yang_name = "ipv4-traffic"
                        self.yang_parent_name = "statistics"

                        self.udp_bad_length_packets = YLeaf(YType.uint32, "udp-bad-length-packets")

                        self.udp_checksum_error_packets = YLeaf(YType.uint32, "udp-checksum-error-packets")

                        self.udp_dropped_packets = YLeaf(YType.uint32, "udp-dropped-packets")

                        self.udp_input_packets = YLeaf(YType.uint32, "udp-input-packets")

                        self.udp_no_port_packets = YLeaf(YType.uint32, "udp-no-port-packets")

                        self.udp_output_packets = YLeaf(YType.uint32, "udp-output-packets")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("udp_bad_length_packets",
                                        "udp_checksum_error_packets",
                                        "udp_dropped_packets",
                                        "udp_input_packets",
                                        "udp_no_port_packets",
                                        "udp_output_packets") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Udp.Nodes.Node.Statistics.Ipv4Traffic, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Udp.Nodes.Node.Statistics.Ipv4Traffic, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.udp_bad_length_packets.is_set or
                            self.udp_checksum_error_packets.is_set or
                            self.udp_dropped_packets.is_set or
                            self.udp_input_packets.is_set or
                            self.udp_no_port_packets.is_set or
                            self.udp_output_packets.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.udp_bad_length_packets.yfilter != YFilter.not_set or
                            self.udp_checksum_error_packets.yfilter != YFilter.not_set or
                            self.udp_dropped_packets.yfilter != YFilter.not_set or
                            self.udp_input_packets.yfilter != YFilter.not_set or
                            self.udp_no_port_packets.yfilter != YFilter.not_set or
                            self.udp_output_packets.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv4-traffic" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.udp_bad_length_packets.is_set or self.udp_bad_length_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_bad_length_packets.get_name_leafdata())
                        if (self.udp_checksum_error_packets.is_set or self.udp_checksum_error_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_checksum_error_packets.get_name_leafdata())
                        if (self.udp_dropped_packets.is_set or self.udp_dropped_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_dropped_packets.get_name_leafdata())
                        if (self.udp_input_packets.is_set or self.udp_input_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_input_packets.get_name_leafdata())
                        if (self.udp_no_port_packets.is_set or self.udp_no_port_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_no_port_packets.get_name_leafdata())
                        if (self.udp_output_packets.is_set or self.udp_output_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_output_packets.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "udp-bad-length-packets" or name == "udp-checksum-error-packets" or name == "udp-dropped-packets" or name == "udp-input-packets" or name == "udp-no-port-packets" or name == "udp-output-packets"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "udp-bad-length-packets"):
                            self.udp_bad_length_packets = value
                            self.udp_bad_length_packets.value_namespace = name_space
                            self.udp_bad_length_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-checksum-error-packets"):
                            self.udp_checksum_error_packets = value
                            self.udp_checksum_error_packets.value_namespace = name_space
                            self.udp_checksum_error_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-dropped-packets"):
                            self.udp_dropped_packets = value
                            self.udp_dropped_packets.value_namespace = name_space
                            self.udp_dropped_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-input-packets"):
                            self.udp_input_packets = value
                            self.udp_input_packets.value_namespace = name_space
                            self.udp_input_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-no-port-packets"):
                            self.udp_no_port_packets = value
                            self.udp_no_port_packets.value_namespace = name_space
                            self.udp_no_port_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-output-packets"):
                            self.udp_output_packets = value
                            self.udp_output_packets.value_namespace = name_space
                            self.udp_output_packets.value_namespace_prefix = name_space_prefix


                class Ipv6Traffic(Entity):
                    """
                    UDP Traffic statistics for IPv6
                    
                    .. attribute:: udp_bad_length_packets
                    
                    	UDP bad length
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_checksum_error_packets
                    
                    	UDP Checksum Errors
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_dropped_packets
                    
                    	UDP drop for other reason
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_input_packets
                    
                    	UDP Received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_no_port_packets
                    
                    	UDP No Port
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_output_packets
                    
                    	UDP Transmitted
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(Udp.Nodes.Node.Statistics.Ipv6Traffic, self).__init__()

                        self.yang_name = "ipv6-traffic"
                        self.yang_parent_name = "statistics"

                        self.udp_bad_length_packets = YLeaf(YType.uint32, "udp-bad-length-packets")

                        self.udp_checksum_error_packets = YLeaf(YType.uint32, "udp-checksum-error-packets")

                        self.udp_dropped_packets = YLeaf(YType.uint32, "udp-dropped-packets")

                        self.udp_input_packets = YLeaf(YType.uint32, "udp-input-packets")

                        self.udp_no_port_packets = YLeaf(YType.uint32, "udp-no-port-packets")

                        self.udp_output_packets = YLeaf(YType.uint32, "udp-output-packets")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("udp_bad_length_packets",
                                        "udp_checksum_error_packets",
                                        "udp_dropped_packets",
                                        "udp_input_packets",
                                        "udp_no_port_packets",
                                        "udp_output_packets") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Udp.Nodes.Node.Statistics.Ipv6Traffic, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Udp.Nodes.Node.Statistics.Ipv6Traffic, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.udp_bad_length_packets.is_set or
                            self.udp_checksum_error_packets.is_set or
                            self.udp_dropped_packets.is_set or
                            self.udp_input_packets.is_set or
                            self.udp_no_port_packets.is_set or
                            self.udp_output_packets.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.udp_bad_length_packets.yfilter != YFilter.not_set or
                            self.udp_checksum_error_packets.yfilter != YFilter.not_set or
                            self.udp_dropped_packets.yfilter != YFilter.not_set or
                            self.udp_input_packets.yfilter != YFilter.not_set or
                            self.udp_no_port_packets.yfilter != YFilter.not_set or
                            self.udp_output_packets.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ipv6-traffic" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.udp_bad_length_packets.is_set or self.udp_bad_length_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_bad_length_packets.get_name_leafdata())
                        if (self.udp_checksum_error_packets.is_set or self.udp_checksum_error_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_checksum_error_packets.get_name_leafdata())
                        if (self.udp_dropped_packets.is_set or self.udp_dropped_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_dropped_packets.get_name_leafdata())
                        if (self.udp_input_packets.is_set or self.udp_input_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_input_packets.get_name_leafdata())
                        if (self.udp_no_port_packets.is_set or self.udp_no_port_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_no_port_packets.get_name_leafdata())
                        if (self.udp_output_packets.is_set or self.udp_output_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.udp_output_packets.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "udp-bad-length-packets" or name == "udp-checksum-error-packets" or name == "udp-dropped-packets" or name == "udp-input-packets" or name == "udp-no-port-packets" or name == "udp-output-packets"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "udp-bad-length-packets"):
                            self.udp_bad_length_packets = value
                            self.udp_bad_length_packets.value_namespace = name_space
                            self.udp_bad_length_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-checksum-error-packets"):
                            self.udp_checksum_error_packets = value
                            self.udp_checksum_error_packets.value_namespace = name_space
                            self.udp_checksum_error_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-dropped-packets"):
                            self.udp_dropped_packets = value
                            self.udp_dropped_packets.value_namespace = name_space
                            self.udp_dropped_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-input-packets"):
                            self.udp_input_packets = value
                            self.udp_input_packets.value_namespace = name_space
                            self.udp_input_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-no-port-packets"):
                            self.udp_no_port_packets = value
                            self.udp_no_port_packets.value_namespace = name_space
                            self.udp_no_port_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "udp-output-packets"):
                            self.udp_output_packets = value
                            self.udp_output_packets.value_namespace = name_space
                            self.udp_output_packets.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.ipv4_traffic is not None and self.ipv4_traffic.has_data()) or
                        (self.ipv6_traffic is not None and self.ipv6_traffic.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.ipv4_traffic is not None and self.ipv4_traffic.has_operation()) or
                        (self.ipv6_traffic is not None and self.ipv6_traffic.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "ipv4-traffic"):
                        if (self.ipv4_traffic is None):
                            self.ipv4_traffic = Udp.Nodes.Node.Statistics.Ipv4Traffic()
                            self.ipv4_traffic.parent = self
                            self._children_name_map["ipv4_traffic"] = "ipv4-traffic"
                        return self.ipv4_traffic

                    if (child_yang_name == "ipv6-traffic"):
                        if (self.ipv6_traffic is None):
                            self.ipv6_traffic = Udp.Nodes.Node.Statistics.Ipv6Traffic()
                            self.ipv6_traffic.parent = self
                            self._children_name_map["ipv6_traffic"] = "ipv6-traffic"
                        return self.ipv6_traffic

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ipv4-traffic" or name == "ipv6-traffic"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.statistics is not None and self.statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.statistics is not None and self.statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-udp-oper:udp/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = Udp.Nodes.Node.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "statistics" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-udp-oper:udp/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Udp.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-udp-oper:udp" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = Udp.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = Udp()
        return self._top_entity

class UdpConnection(Entity):
    """
    udp connection
    
    .. attribute:: nodes
    
    	List of UDP connections nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2016-02-26'

    def __init__(self):
        super(UdpConnection, self).__init__()
        self._top_entity = None

        self.yang_name = "udp-connection"
        self.yang_parent_name = "Cisco-IOS-XR-ip-udp-oper"

        self.nodes = UdpConnection.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Nodes(Entity):
        """
        List of UDP connections nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2016-02-26'

        def __init__(self):
            super(UdpConnection.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "udp-connection"

            self.node = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(UdpConnection.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(UdpConnection.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: lpts
            
            	LPTS statistical data
            	**type**\:   :py:class:`Lpts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts>`
            
            .. attribute:: pcb_briefs
            
            	Brief information for list of UDP connections
            	**type**\:   :py:class:`PcbBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs>`
            
            .. attribute:: pcb_details
            
            	Detail information for list of UDP connections 
            	**type**\:   :py:class:`PcbDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails>`
            
            .. attribute:: statistics
            
            	Statistics of UDP connections
            	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2016-02-26'

            def __init__(self):
                super(UdpConnection.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node_name = YLeaf(YType.str, "node-name")

                self.lpts = UdpConnection.Nodes.Node.Lpts()
                self.lpts.parent = self
                self._children_name_map["lpts"] = "lpts"
                self._children_yang_names.add("lpts")

                self.pcb_briefs = UdpConnection.Nodes.Node.PcbBriefs()
                self.pcb_briefs.parent = self
                self._children_name_map["pcb_briefs"] = "pcb-briefs"
                self._children_yang_names.add("pcb-briefs")

                self.pcb_details = UdpConnection.Nodes.Node.PcbDetails()
                self.pcb_details.parent = self
                self._children_name_map["pcb_details"] = "pcb-details"
                self._children_yang_names.add("pcb-details")

                self.statistics = UdpConnection.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(UdpConnection.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(UdpConnection.Nodes.Node, self).__setattr__(name, value)


            class Statistics(Entity):
                """
                Statistics of UDP connections
                
                .. attribute:: clients
                
                	Table listing clients
                	**type**\:   :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients>`
                
                .. attribute:: pcb_statistics
                
                	Table listing the UDP connections for which statistics are provided
                	**type**\:   :py:class:`PcbStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics>`
                
                .. attribute:: summary
                
                	Summary statistics across all UDP connections
                	**type**\:   :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Summary>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2016-02-26'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"

                    self.clients = UdpConnection.Nodes.Node.Statistics.Clients()
                    self.clients.parent = self
                    self._children_name_map["clients"] = "clients"
                    self._children_yang_names.add("clients")

                    self.pcb_statistics = UdpConnection.Nodes.Node.Statistics.PcbStatistics()
                    self.pcb_statistics.parent = self
                    self._children_name_map["pcb_statistics"] = "pcb-statistics"
                    self._children_yang_names.add("pcb-statistics")

                    self.summary = UdpConnection.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")


                class Clients(Entity):
                    """
                    Table listing clients
                    
                    .. attribute:: client
                    
                    	Describing Client ID
                    	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients.Client>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Statistics.Clients, self).__init__()

                        self.yang_name = "clients"
                        self.yang_parent_name = "statistics"

                        self.client = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(UdpConnection.Nodes.Node.Statistics.Clients, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(UdpConnection.Nodes.Node.Statistics.Clients, self).__setattr__(name, value)


                    class Client(Entity):
                        """
                        Describing Client ID
                        
                        .. attribute:: client_id  <key>
                        
                        	Displaying client's aggregated statistics
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: client_jid
                        
                        	Job ID of the transport client
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: client_name
                        
                        	Transport client name
                        	**type**\:  str
                        
                        	**length:** 0..21
                        
                        .. attribute:: ipv4_received_packets
                        
                        	Total IPv4 packets received from client
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_sent_packets
                        
                        	Total IPv4 packets sent to client
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv6_received_packets
                        
                        	Total IPv6 packets received from app
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv6_sent_packets
                        
                        	Total IPv6 packets sent to app
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.Statistics.Clients.Client, self).__init__()

                            self.yang_name = "client"
                            self.yang_parent_name = "clients"

                            self.client_id = YLeaf(YType.uint32, "client-id")

                            self.client_jid = YLeaf(YType.int32, "client-jid")

                            self.client_name = YLeaf(YType.str, "client-name")

                            self.ipv4_received_packets = YLeaf(YType.uint32, "ipv4-received-packets")

                            self.ipv4_sent_packets = YLeaf(YType.uint32, "ipv4-sent-packets")

                            self.ipv6_received_packets = YLeaf(YType.uint32, "ipv6-received-packets")

                            self.ipv6_sent_packets = YLeaf(YType.uint32, "ipv6-sent-packets")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("client_id",
                                            "client_jid",
                                            "client_name",
                                            "ipv4_received_packets",
                                            "ipv4_sent_packets",
                                            "ipv6_received_packets",
                                            "ipv6_sent_packets") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(UdpConnection.Nodes.Node.Statistics.Clients.Client, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(UdpConnection.Nodes.Node.Statistics.Clients.Client, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.client_id.is_set or
                                self.client_jid.is_set or
                                self.client_name.is_set or
                                self.ipv4_received_packets.is_set or
                                self.ipv4_sent_packets.is_set or
                                self.ipv6_received_packets.is_set or
                                self.ipv6_sent_packets.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.client_id.yfilter != YFilter.not_set or
                                self.client_jid.yfilter != YFilter.not_set or
                                self.client_name.yfilter != YFilter.not_set or
                                self.ipv4_received_packets.yfilter != YFilter.not_set or
                                self.ipv4_sent_packets.yfilter != YFilter.not_set or
                                self.ipv6_received_packets.yfilter != YFilter.not_set or
                                self.ipv6_sent_packets.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "client" + "[client-id='" + self.client_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.client_id.is_set or self.client_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.client_id.get_name_leafdata())
                            if (self.client_jid.is_set or self.client_jid.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.client_jid.get_name_leafdata())
                            if (self.client_name.is_set or self.client_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.client_name.get_name_leafdata())
                            if (self.ipv4_received_packets.is_set or self.ipv4_received_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_received_packets.get_name_leafdata())
                            if (self.ipv4_sent_packets.is_set or self.ipv4_sent_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_sent_packets.get_name_leafdata())
                            if (self.ipv6_received_packets.is_set or self.ipv6_received_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_received_packets.get_name_leafdata())
                            if (self.ipv6_sent_packets.is_set or self.ipv6_sent_packets.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_sent_packets.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "client-id" or name == "client-jid" or name == "client-name" or name == "ipv4-received-packets" or name == "ipv4-sent-packets" or name == "ipv6-received-packets" or name == "ipv6-sent-packets"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "client-id"):
                                self.client_id = value
                                self.client_id.value_namespace = name_space
                                self.client_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "client-jid"):
                                self.client_jid = value
                                self.client_jid.value_namespace = name_space
                                self.client_jid.value_namespace_prefix = name_space_prefix
                            if(value_path == "client-name"):
                                self.client_name = value
                                self.client_name.value_namespace = name_space
                                self.client_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-received-packets"):
                                self.ipv4_received_packets = value
                                self.ipv4_received_packets.value_namespace = name_space
                                self.ipv4_received_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-sent-packets"):
                                self.ipv4_sent_packets = value
                                self.ipv4_sent_packets.value_namespace = name_space
                                self.ipv4_sent_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-received-packets"):
                                self.ipv6_received_packets = value
                                self.ipv6_received_packets.value_namespace = name_space
                                self.ipv6_received_packets.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-sent-packets"):
                                self.ipv6_sent_packets = value
                                self.ipv6_sent_packets.value_namespace = name_space
                                self.ipv6_sent_packets.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.client:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.client:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "clients" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "client"):
                            for c in self.client:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = UdpConnection.Nodes.Node.Statistics.Clients.Client()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.client.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "client"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


                class Summary(Entity):
                    """
                    Summary statistics across all UDP connections
                    
                    .. attribute:: cloned_packets
                    
                    	Total cloned packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failed_clone_packets
                    
                    	Total failed cloned packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forward_broadcast_packets
                    
                    	Total forwarding broadcast packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_bad_checksum_packets
                    
                    	Packets received has bad checksum
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_drop_packets
                    
                    	Packets dropped for other reasons
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_no_port_packets
                    
                    	Packets received when no wild listener
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_too_short_packets
                    
                    	Packets received is too short
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_total_packets
                    
                    	Total packets received
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_error_packets
                    
                    	Total send erorr packets
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_total_packets
                    
                    	Total packets sent
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Statistics.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "statistics"

                        self.cloned_packets = YLeaf(YType.uint32, "cloned-packets")

                        self.failed_clone_packets = YLeaf(YType.uint32, "failed-clone-packets")

                        self.forward_broadcast_packets = YLeaf(YType.uint32, "forward-broadcast-packets")

                        self.received_bad_checksum_packets = YLeaf(YType.uint32, "received-bad-checksum-packets")

                        self.received_drop_packets = YLeaf(YType.uint32, "received-drop-packets")

                        self.received_no_port_packets = YLeaf(YType.uint32, "received-no-port-packets")

                        self.received_too_short_packets = YLeaf(YType.uint32, "received-too-short-packets")

                        self.received_total_packets = YLeaf(YType.uint32, "received-total-packets")

                        self.sent_error_packets = YLeaf(YType.uint32, "sent-error-packets")

                        self.sent_total_packets = YLeaf(YType.uint32, "sent-total-packets")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cloned_packets",
                                        "failed_clone_packets",
                                        "forward_broadcast_packets",
                                        "received_bad_checksum_packets",
                                        "received_drop_packets",
                                        "received_no_port_packets",
                                        "received_too_short_packets",
                                        "received_total_packets",
                                        "sent_error_packets",
                                        "sent_total_packets") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(UdpConnection.Nodes.Node.Statistics.Summary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(UdpConnection.Nodes.Node.Statistics.Summary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.cloned_packets.is_set or
                            self.failed_clone_packets.is_set or
                            self.forward_broadcast_packets.is_set or
                            self.received_bad_checksum_packets.is_set or
                            self.received_drop_packets.is_set or
                            self.received_no_port_packets.is_set or
                            self.received_too_short_packets.is_set or
                            self.received_total_packets.is_set or
                            self.sent_error_packets.is_set or
                            self.sent_total_packets.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cloned_packets.yfilter != YFilter.not_set or
                            self.failed_clone_packets.yfilter != YFilter.not_set or
                            self.forward_broadcast_packets.yfilter != YFilter.not_set or
                            self.received_bad_checksum_packets.yfilter != YFilter.not_set or
                            self.received_drop_packets.yfilter != YFilter.not_set or
                            self.received_no_port_packets.yfilter != YFilter.not_set or
                            self.received_too_short_packets.yfilter != YFilter.not_set or
                            self.received_total_packets.yfilter != YFilter.not_set or
                            self.sent_error_packets.yfilter != YFilter.not_set or
                            self.sent_total_packets.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "summary" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cloned_packets.is_set or self.cloned_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cloned_packets.get_name_leafdata())
                        if (self.failed_clone_packets.is_set or self.failed_clone_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.failed_clone_packets.get_name_leafdata())
                        if (self.forward_broadcast_packets.is_set or self.forward_broadcast_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.forward_broadcast_packets.get_name_leafdata())
                        if (self.received_bad_checksum_packets.is_set or self.received_bad_checksum_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_bad_checksum_packets.get_name_leafdata())
                        if (self.received_drop_packets.is_set or self.received_drop_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_drop_packets.get_name_leafdata())
                        if (self.received_no_port_packets.is_set or self.received_no_port_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_no_port_packets.get_name_leafdata())
                        if (self.received_too_short_packets.is_set or self.received_too_short_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_too_short_packets.get_name_leafdata())
                        if (self.received_total_packets.is_set or self.received_total_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.received_total_packets.get_name_leafdata())
                        if (self.sent_error_packets.is_set or self.sent_error_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent_error_packets.get_name_leafdata())
                        if (self.sent_total_packets.is_set or self.sent_total_packets.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.sent_total_packets.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cloned-packets" or name == "failed-clone-packets" or name == "forward-broadcast-packets" or name == "received-bad-checksum-packets" or name == "received-drop-packets" or name == "received-no-port-packets" or name == "received-too-short-packets" or name == "received-total-packets" or name == "sent-error-packets" or name == "sent-total-packets"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cloned-packets"):
                            self.cloned_packets = value
                            self.cloned_packets.value_namespace = name_space
                            self.cloned_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "failed-clone-packets"):
                            self.failed_clone_packets = value
                            self.failed_clone_packets.value_namespace = name_space
                            self.failed_clone_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "forward-broadcast-packets"):
                            self.forward_broadcast_packets = value
                            self.forward_broadcast_packets.value_namespace = name_space
                            self.forward_broadcast_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-bad-checksum-packets"):
                            self.received_bad_checksum_packets = value
                            self.received_bad_checksum_packets.value_namespace = name_space
                            self.received_bad_checksum_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-drop-packets"):
                            self.received_drop_packets = value
                            self.received_drop_packets.value_namespace = name_space
                            self.received_drop_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-no-port-packets"):
                            self.received_no_port_packets = value
                            self.received_no_port_packets.value_namespace = name_space
                            self.received_no_port_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-too-short-packets"):
                            self.received_too_short_packets = value
                            self.received_too_short_packets.value_namespace = name_space
                            self.received_too_short_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "received-total-packets"):
                            self.received_total_packets = value
                            self.received_total_packets.value_namespace = name_space
                            self.received_total_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent-error-packets"):
                            self.sent_error_packets = value
                            self.sent_error_packets.value_namespace = name_space
                            self.sent_error_packets.value_namespace_prefix = name_space_prefix
                        if(value_path == "sent-total-packets"):
                            self.sent_total_packets = value
                            self.sent_total_packets.value_namespace = name_space
                            self.sent_total_packets.value_namespace_prefix = name_space_prefix


                class PcbStatistics(Entity):
                    """
                    Table listing the UDP connections for which
                    statistics are provided
                    
                    .. attribute:: pcb_statistic
                    
                    	Satistics associated with a particular PCB
                    	**type**\: list of    :py:class:`PcbStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Statistics.PcbStatistics, self).__init__()

                        self.yang_name = "pcb-statistics"
                        self.yang_parent_name = "statistics"

                        self.pcb_statistic = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(UdpConnection.Nodes.Node.Statistics.PcbStatistics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(UdpConnection.Nodes.Node.Statistics.PcbStatistics, self).__setattr__(name, value)


                    class PcbStatistic(Entity):
                        """
                        Satistics associated with a particular PCB
                        
                        .. attribute:: pcb_address  <key>
                        
                        	Protocol Control Block address
                        	**type**\:  int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: is_paw_socket
                        
                        	True if paw socket
                        	**type**\:  bool
                        
                        .. attribute:: receive
                        
                        	UDP receive statistics
                        	**type**\:   :py:class:`Receive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive>`
                        
                        .. attribute:: send
                        
                        	UDP send statistics
                        	**type**\:   :py:class:`Send <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send>`
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic, self).__init__()

                            self.yang_name = "pcb-statistic"
                            self.yang_parent_name = "pcb-statistics"

                            self.pcb_address = YLeaf(YType.int32, "pcb-address")

                            self.is_paw_socket = YLeaf(YType.boolean, "is-paw-socket")

                            self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                            self.receive = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive()
                            self.receive.parent = self
                            self._children_name_map["receive"] = "receive"
                            self._children_yang_names.add("receive")

                            self.send = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send()
                            self.send.parent = self
                            self._children_name_map["send"] = "send"
                            self._children_yang_names.add("send")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pcb_address",
                                            "is_paw_socket",
                                            "vrf_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic, self).__setattr__(name, value)


                        class Send(Entity):
                            """
                            UDP send statistics
                            
                            .. attribute:: failed_queued_net_io_packets
                            
                            	Packets failed getting queued to network (NetIO)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: failed_queued_network_packets
                            
                            	Packets failed getting queued to network (v4/v6 IO)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: received_application_bytes
                            
                            	Bytes received from application
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: received_xipc_pulses
                            
                            	XIPC pulses received from application
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_net_io_packets
                            
                            	Packets sent to network (NetIO)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_network_packets
                            
                            	Packets sent to network (v4/v6 IO)
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2016-02-26'

                            def __init__(self):
                                super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send, self).__init__()

                                self.yang_name = "send"
                                self.yang_parent_name = "pcb-statistic"

                                self.failed_queued_net_io_packets = YLeaf(YType.uint32, "failed-queued-net-io-packets")

                                self.failed_queued_network_packets = YLeaf(YType.uint32, "failed-queued-network-packets")

                                self.received_application_bytes = YLeaf(YType.uint64, "received-application-bytes")

                                self.received_xipc_pulses = YLeaf(YType.uint64, "received-xipc-pulses")

                                self.sent_net_io_packets = YLeaf(YType.uint64, "sent-net-io-packets")

                                self.sent_network_packets = YLeaf(YType.uint64, "sent-network-packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("failed_queued_net_io_packets",
                                                "failed_queued_network_packets",
                                                "received_application_bytes",
                                                "received_xipc_pulses",
                                                "sent_net_io_packets",
                                                "sent_network_packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.failed_queued_net_io_packets.is_set or
                                    self.failed_queued_network_packets.is_set or
                                    self.received_application_bytes.is_set or
                                    self.received_xipc_pulses.is_set or
                                    self.sent_net_io_packets.is_set or
                                    self.sent_network_packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.failed_queued_net_io_packets.yfilter != YFilter.not_set or
                                    self.failed_queued_network_packets.yfilter != YFilter.not_set or
                                    self.received_application_bytes.yfilter != YFilter.not_set or
                                    self.received_xipc_pulses.yfilter != YFilter.not_set or
                                    self.sent_net_io_packets.yfilter != YFilter.not_set or
                                    self.sent_network_packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "send" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.failed_queued_net_io_packets.is_set or self.failed_queued_net_io_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.failed_queued_net_io_packets.get_name_leafdata())
                                if (self.failed_queued_network_packets.is_set or self.failed_queued_network_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.failed_queued_network_packets.get_name_leafdata())
                                if (self.received_application_bytes.is_set or self.received_application_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_application_bytes.get_name_leafdata())
                                if (self.received_xipc_pulses.is_set or self.received_xipc_pulses.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_xipc_pulses.get_name_leafdata())
                                if (self.sent_net_io_packets.is_set or self.sent_net_io_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sent_net_io_packets.get_name_leafdata())
                                if (self.sent_network_packets.is_set or self.sent_network_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.sent_network_packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "failed-queued-net-io-packets" or name == "failed-queued-network-packets" or name == "received-application-bytes" or name == "received-xipc-pulses" or name == "sent-net-io-packets" or name == "sent-network-packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "failed-queued-net-io-packets"):
                                    self.failed_queued_net_io_packets = value
                                    self.failed_queued_net_io_packets.value_namespace = name_space
                                    self.failed_queued_net_io_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "failed-queued-network-packets"):
                                    self.failed_queued_network_packets = value
                                    self.failed_queued_network_packets.value_namespace = name_space
                                    self.failed_queued_network_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-application-bytes"):
                                    self.received_application_bytes = value
                                    self.received_application_bytes.value_namespace = name_space
                                    self.received_application_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-xipc-pulses"):
                                    self.received_xipc_pulses = value
                                    self.received_xipc_pulses.value_namespace = name_space
                                    self.received_xipc_pulses.value_namespace_prefix = name_space_prefix
                                if(value_path == "sent-net-io-packets"):
                                    self.sent_net_io_packets = value
                                    self.sent_net_io_packets.value_namespace = name_space
                                    self.sent_net_io_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "sent-network-packets"):
                                    self.sent_network_packets = value
                                    self.sent_network_packets.value_namespace = name_space
                                    self.sent_network_packets.value_namespace_prefix = name_space_prefix


                        class Receive(Entity):
                            """
                            UDP receive statistics
                            
                            .. attribute:: failed_queued_application_packets
                            
                            	Packets failed queued to application
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: failed_queued_application_socket_packets
                            
                            	Packet that couldn't be queued to application.on socket
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: queued_application_packets
                            
                            	Packets queued to application
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: queued_application_socket_packets
                            
                            	Packets queued to application on socket
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_network_packets
                            
                            	Packets received from network
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2016-02-26'

                            def __init__(self):
                                super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive, self).__init__()

                                self.yang_name = "receive"
                                self.yang_parent_name = "pcb-statistic"

                                self.failed_queued_application_packets = YLeaf(YType.uint32, "failed-queued-application-packets")

                                self.failed_queued_application_socket_packets = YLeaf(YType.uint32, "failed-queued-application-socket-packets")

                                self.queued_application_packets = YLeaf(YType.uint64, "queued-application-packets")

                                self.queued_application_socket_packets = YLeaf(YType.uint64, "queued-application-socket-packets")

                                self.received_network_packets = YLeaf(YType.uint64, "received-network-packets")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("failed_queued_application_packets",
                                                "failed_queued_application_socket_packets",
                                                "queued_application_packets",
                                                "queued_application_socket_packets",
                                                "received_network_packets") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.failed_queued_application_packets.is_set or
                                    self.failed_queued_application_socket_packets.is_set or
                                    self.queued_application_packets.is_set or
                                    self.queued_application_socket_packets.is_set or
                                    self.received_network_packets.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.failed_queued_application_packets.yfilter != YFilter.not_set or
                                    self.failed_queued_application_socket_packets.yfilter != YFilter.not_set or
                                    self.queued_application_packets.yfilter != YFilter.not_set or
                                    self.queued_application_socket_packets.yfilter != YFilter.not_set or
                                    self.received_network_packets.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "receive" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.failed_queued_application_packets.is_set or self.failed_queued_application_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.failed_queued_application_packets.get_name_leafdata())
                                if (self.failed_queued_application_socket_packets.is_set or self.failed_queued_application_socket_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.failed_queued_application_socket_packets.get_name_leafdata())
                                if (self.queued_application_packets.is_set or self.queued_application_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.queued_application_packets.get_name_leafdata())
                                if (self.queued_application_socket_packets.is_set or self.queued_application_socket_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.queued_application_socket_packets.get_name_leafdata())
                                if (self.received_network_packets.is_set or self.received_network_packets.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.received_network_packets.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "failed-queued-application-packets" or name == "failed-queued-application-socket-packets" or name == "queued-application-packets" or name == "queued-application-socket-packets" or name == "received-network-packets"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "failed-queued-application-packets"):
                                    self.failed_queued_application_packets = value
                                    self.failed_queued_application_packets.value_namespace = name_space
                                    self.failed_queued_application_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "failed-queued-application-socket-packets"):
                                    self.failed_queued_application_socket_packets = value
                                    self.failed_queued_application_socket_packets.value_namespace = name_space
                                    self.failed_queued_application_socket_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "queued-application-packets"):
                                    self.queued_application_packets = value
                                    self.queued_application_packets.value_namespace = name_space
                                    self.queued_application_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "queued-application-socket-packets"):
                                    self.queued_application_socket_packets = value
                                    self.queued_application_socket_packets.value_namespace = name_space
                                    self.queued_application_socket_packets.value_namespace_prefix = name_space_prefix
                                if(value_path == "received-network-packets"):
                                    self.received_network_packets = value
                                    self.received_network_packets.value_namespace = name_space
                                    self.received_network_packets.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.pcb_address.is_set or
                                self.is_paw_socket.is_set or
                                self.vrf_id.is_set or
                                (self.receive is not None and self.receive.has_data()) or
                                (self.send is not None and self.send.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pcb_address.yfilter != YFilter.not_set or
                                self.is_paw_socket.yfilter != YFilter.not_set or
                                self.vrf_id.yfilter != YFilter.not_set or
                                (self.receive is not None and self.receive.has_operation()) or
                                (self.send is not None and self.send.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pcb-statistic" + "[pcb-address='" + self.pcb_address.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pcb_address.is_set or self.pcb_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pcb_address.get_name_leafdata())
                            if (self.is_paw_socket.is_set or self.is_paw_socket.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_paw_socket.get_name_leafdata())
                            if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "receive"):
                                if (self.receive is None):
                                    self.receive = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive()
                                    self.receive.parent = self
                                    self._children_name_map["receive"] = "receive"
                                return self.receive

                            if (child_yang_name == "send"):
                                if (self.send is None):
                                    self.send = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send()
                                    self.send.parent = self
                                    self._children_name_map["send"] = "send"
                                return self.send

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "receive" or name == "send" or name == "pcb-address" or name == "is-paw-socket" or name == "vrf-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pcb-address"):
                                self.pcb_address = value
                                self.pcb_address.value_namespace = name_space
                                self.pcb_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "is-paw-socket"):
                                self.is_paw_socket = value
                                self.is_paw_socket.value_namespace = name_space
                                self.is_paw_socket.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-id"):
                                self.vrf_id = value
                                self.vrf_id.value_namespace = name_space
                                self.vrf_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.pcb_statistic:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.pcb_statistic:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pcb-statistics" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "pcb-statistic"):
                            for c in self.pcb_statistic:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.pcb_statistic.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pcb-statistic"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        (self.clients is not None and self.clients.has_data()) or
                        (self.pcb_statistics is not None and self.pcb_statistics.has_data()) or
                        (self.summary is not None and self.summary.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.clients is not None and self.clients.has_operation()) or
                        (self.pcb_statistics is not None and self.pcb_statistics.has_operation()) or
                        (self.summary is not None and self.summary.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistics" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "clients"):
                        if (self.clients is None):
                            self.clients = UdpConnection.Nodes.Node.Statistics.Clients()
                            self.clients.parent = self
                            self._children_name_map["clients"] = "clients"
                        return self.clients

                    if (child_yang_name == "pcb-statistics"):
                        if (self.pcb_statistics is None):
                            self.pcb_statistics = UdpConnection.Nodes.Node.Statistics.PcbStatistics()
                            self.pcb_statistics.parent = self
                            self._children_name_map["pcb_statistics"] = "pcb-statistics"
                        return self.pcb_statistics

                    if (child_yang_name == "summary"):
                        if (self.summary is None):
                            self.summary = UdpConnection.Nodes.Node.Statistics.Summary()
                            self.summary.parent = self
                            self._children_name_map["summary"] = "summary"
                        return self.summary

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "clients" or name == "pcb-statistics" or name == "summary"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Lpts(Entity):
                """
                LPTS statistical data
                
                .. attribute:: queries
                
                	List of query options
                	**type**\:   :py:class:`Queries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2016-02-26'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.Lpts, self).__init__()

                    self.yang_name = "lpts"
                    self.yang_parent_name = "node"

                    self.queries = UdpConnection.Nodes.Node.Lpts.Queries()
                    self.queries.parent = self
                    self._children_name_map["queries"] = "queries"
                    self._children_yang_names.add("queries")


                class Queries(Entity):
                    """
                    List of query options
                    
                    .. attribute:: query
                    
                    	Query option
                    	**type**\: list of    :py:class:`Query <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Lpts.Queries, self).__init__()

                        self.yang_name = "queries"
                        self.yang_parent_name = "lpts"

                        self.query = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in () and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(UdpConnection.Nodes.Node.Lpts.Queries, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(UdpConnection.Nodes.Node.Lpts.Queries, self).__setattr__(name, value)


                    class Query(Entity):
                        """
                        Query option
                        
                        .. attribute:: query_name  <key>
                        
                        	Query option
                        	**type**\:   :py:class:`LptsPcbQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.LptsPcbQuery>`
                        
                        .. attribute:: pcbs
                        
                        	List of PCBs
                        	**type**\:   :py:class:`Pcbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs>`
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query, self).__init__()

                            self.yang_name = "query"
                            self.yang_parent_name = "queries"

                            self.query_name = YLeaf(YType.enumeration, "query-name")

                            self.pcbs = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs()
                            self.pcbs.parent = self
                            self._children_name_map["pcbs"] = "pcbs"
                            self._children_yang_names.add("pcbs")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("query_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query, self).__setattr__(name, value)


                        class Pcbs(Entity):
                            """
                            List of PCBs
                            
                            .. attribute:: pcb
                            
                            	A PCB information
                            	**type**\: list of    :py:class:`Pcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb>`
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2016-02-26'

                            def __init__(self):
                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs, self).__init__()

                                self.yang_name = "pcbs"
                                self.yang_parent_name = "query"

                                self.pcb = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in () and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs, self).__setattr__(name, value)


                            class Pcb(Entity):
                                """
                                A PCB information
                                
                                .. attribute:: pcb_address  <key>
                                
                                	PCB address
                                	**type**\:  int
                                
                                	**range:** \-2147483648..2147483647
                                
                                .. attribute:: common
                                
                                	Common PCB information
                                	**type**\:   :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common>`
                                
                                .. attribute:: foreign_address
                                
                                	Remote IP address
                                	**type**\:   :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress>`
                                
                                .. attribute:: foreign_port
                                
                                	Remote port
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: l4_protocol
                                
                                	Layer 4 protocol
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: local_address
                                
                                	Local IP address
                                	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress>`
                                
                                .. attribute:: local_port
                                
                                	Local port
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ip-udp-oper'
                                _revision = '2016-02-26'

                                def __init__(self):
                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb, self).__init__()

                                    self.yang_name = "pcb"
                                    self.yang_parent_name = "pcbs"

                                    self.pcb_address = YLeaf(YType.int32, "pcb-address")

                                    self.foreign_port = YLeaf(YType.uint16, "foreign-port")

                                    self.l4_protocol = YLeaf(YType.uint32, "l4-protocol")

                                    self.local_port = YLeaf(YType.uint16, "local-port")

                                    self.common = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common()
                                    self.common.parent = self
                                    self._children_name_map["common"] = "common"
                                    self._children_yang_names.add("common")

                                    self.foreign_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress()
                                    self.foreign_address.parent = self
                                    self._children_name_map["foreign_address"] = "foreign-address"
                                    self._children_yang_names.add("foreign-address")

                                    self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress()
                                    self.local_address.parent = self
                                    self._children_name_map["local_address"] = "local-address"
                                    self._children_yang_names.add("local-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("pcb_address",
                                                    "foreign_port",
                                                    "l4_protocol",
                                                    "local_port") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb, self).__setattr__(name, value)


                                class LocalAddress(Entity):
                                    """
                                    Local IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2016-02-26'

                                    def __init__(self):
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress, self).__init__()

                                        self.yang_name = "local-address"
                                        self.yang_parent_name = "pcb"

                                        self.af_name = YLeaf(YType.enumeration, "af-name")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("af_name",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.af_name.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.af_name.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "local-address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.af_name.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "af-name"):
                                            self.af_name = value
                                            self.af_name.value_namespace = name_space
                                            self.af_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix


                                class ForeignAddress(Entity):
                                    """
                                    Remote IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\:  str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\:  str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2016-02-26'

                                    def __init__(self):
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress, self).__init__()

                                        self.yang_name = "foreign-address"
                                        self.yang_parent_name = "pcb"

                                        self.af_name = YLeaf(YType.enumeration, "af-name")

                                        self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                        self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("af_name",
                                                        "ipv4_address",
                                                        "ipv6_address") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.af_name.is_set or
                                            self.ipv4_address.is_set or
                                            self.ipv6_address.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.af_name.yfilter != YFilter.not_set or
                                            self.ipv4_address.yfilter != YFilter.not_set or
                                            self.ipv6_address.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "foreign-address" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.af_name.get_name_leafdata())
                                        if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                        if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "af-name"):
                                            self.af_name = value
                                            self.af_name.value_namespace = name_space
                                            self.af_name.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv4-address"):
                                            self.ipv4_address = value
                                            self.ipv4_address.value_namespace = name_space
                                            self.ipv4_address.value_namespace_prefix = name_space_prefix
                                        if(value_path == "ipv6-address"):
                                            self.ipv6_address = value
                                            self.ipv6_address.value_namespace = name_space
                                            self.ipv6_address.value_namespace_prefix = name_space_prefix


                                class Common(Entity):
                                    """
                                    Common PCB information
                                    
                                    .. attribute:: af_name
                                    
                                    	Address Family
                                    	**type**\:   :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                    
                                    .. attribute:: lpts_pcb
                                    
                                    	LPTS PCB information
                                    	**type**\:   :py:class:`LptsPcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb>`
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2016-02-26'

                                    def __init__(self):
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common, self).__init__()

                                        self.yang_name = "common"
                                        self.yang_parent_name = "pcb"

                                        self.af_name = YLeaf(YType.enumeration, "af-name")

                                        self.lpts_pcb = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb()
                                        self.lpts_pcb.parent = self
                                        self._children_name_map["lpts_pcb"] = "lpts-pcb"
                                        self._children_yang_names.add("lpts-pcb")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("af_name") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common, self).__setattr__(name, value)


                                    class LptsPcb(Entity):
                                        """
                                        LPTS PCB information
                                        
                                        .. attribute:: accept_mask
                                        
                                        	AcceptMask
                                        	**type**\:   :py:class:`AcceptMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask>`
                                        
                                        .. attribute:: filter
                                        
                                        	Interface Filters
                                        	**type**\: list of    :py:class:`Filter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter>`
                                        
                                        .. attribute:: flow_types_info
                                        
                                        	flow information
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lpts_flags
                                        
                                        	LPTS flags
                                        	**type**\:   :py:class:`LptsFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags>`
                                        
                                        .. attribute:: options
                                        
                                        	Receive options
                                        	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options>`
                                        
                                        .. attribute:: ttl
                                        
                                        	Minimum TTL
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ip-udp-oper'
                                        _revision = '2016-02-26'

                                        def __init__(self):
                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb, self).__init__()

                                            self.yang_name = "lpts-pcb"
                                            self.yang_parent_name = "common"

                                            self.flow_types_info = YLeaf(YType.uint32, "flow-types-info")

                                            self.ttl = YLeaf(YType.uint8, "ttl")

                                            self.accept_mask = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask()
                                            self.accept_mask.parent = self
                                            self._children_name_map["accept_mask"] = "accept-mask"
                                            self._children_yang_names.add("accept-mask")

                                            self.lpts_flags = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags()
                                            self.lpts_flags.parent = self
                                            self._children_name_map["lpts_flags"] = "lpts-flags"
                                            self._children_yang_names.add("lpts-flags")

                                            self.options = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options()
                                            self.options.parent = self
                                            self._children_name_map["options"] = "options"
                                            self._children_yang_names.add("options")

                                            self.filter = YList(self)

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("flow_types_info",
                                                            "ttl") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb, self).__setattr__(name, value)


                                        class Options(Entity):
                                            """
                                            Receive options
                                            
                                            .. attribute:: is_ip_sla
                                            
                                            	IP SLA
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_receive_filter
                                            
                                            	Receive filter enabled
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2016-02-26'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options, self).__init__()

                                                self.yang_name = "options"
                                                self.yang_parent_name = "lpts-pcb"

                                                self.is_ip_sla = YLeaf(YType.boolean, "is-ip-sla")

                                                self.is_receive_filter = YLeaf(YType.boolean, "is-receive-filter")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("is_ip_sla",
                                                                "is_receive_filter") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.is_ip_sla.is_set or
                                                    self.is_receive_filter.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.is_ip_sla.yfilter != YFilter.not_set or
                                                    self.is_receive_filter.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "options" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.is_ip_sla.is_set or self.is_ip_sla.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_ip_sla.get_name_leafdata())
                                                if (self.is_receive_filter.is_set or self.is_receive_filter.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_receive_filter.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "is-ip-sla" or name == "is-receive-filter"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "is-ip-sla"):
                                                    self.is_ip_sla = value
                                                    self.is_ip_sla.value_namespace = name_space
                                                    self.is_ip_sla.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-receive-filter"):
                                                    self.is_receive_filter = value
                                                    self.is_receive_filter.value_namespace = name_space
                                                    self.is_receive_filter.value_namespace_prefix = name_space_prefix


                                        class LptsFlags(Entity):
                                            """
                                            LPTS flags
                                            
                                            .. attribute:: is_ignore_vrf_filter
                                            
                                            	Ignore VRF Filter
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_local_address_ignore
                                            
                                            	Sent drop packets
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_pcb_bound
                                            
                                            	PCB bound
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2016-02-26'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags, self).__init__()

                                                self.yang_name = "lpts-flags"
                                                self.yang_parent_name = "lpts-pcb"

                                                self.is_ignore_vrf_filter = YLeaf(YType.boolean, "is-ignore-vrf-filter")

                                                self.is_local_address_ignore = YLeaf(YType.boolean, "is-local-address-ignore")

                                                self.is_pcb_bound = YLeaf(YType.boolean, "is-pcb-bound")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("is_ignore_vrf_filter",
                                                                "is_local_address_ignore",
                                                                "is_pcb_bound") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.is_ignore_vrf_filter.is_set or
                                                    self.is_local_address_ignore.is_set or
                                                    self.is_pcb_bound.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.is_ignore_vrf_filter.yfilter != YFilter.not_set or
                                                    self.is_local_address_ignore.yfilter != YFilter.not_set or
                                                    self.is_pcb_bound.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "lpts-flags" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.is_ignore_vrf_filter.is_set or self.is_ignore_vrf_filter.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_ignore_vrf_filter.get_name_leafdata())
                                                if (self.is_local_address_ignore.is_set or self.is_local_address_ignore.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_local_address_ignore.get_name_leafdata())
                                                if (self.is_pcb_bound.is_set or self.is_pcb_bound.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_pcb_bound.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "is-ignore-vrf-filter" or name == "is-local-address-ignore" or name == "is-pcb-bound"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "is-ignore-vrf-filter"):
                                                    self.is_ignore_vrf_filter = value
                                                    self.is_ignore_vrf_filter.value_namespace = name_space
                                                    self.is_ignore_vrf_filter.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-local-address-ignore"):
                                                    self.is_local_address_ignore = value
                                                    self.is_local_address_ignore.value_namespace = name_space
                                                    self.is_local_address_ignore.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-pcb-bound"):
                                                    self.is_pcb_bound = value
                                                    self.is_pcb_bound.value_namespace = name_space
                                                    self.is_pcb_bound.value_namespace_prefix = name_space_prefix


                                        class AcceptMask(Entity):
                                            """
                                            AcceptMask
                                            
                                            .. attribute:: is_interface
                                            
                                            	Set interface
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_local_address
                                            
                                            	Set Local Address
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_local_port
                                            
                                            	Set Local Port
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_packet_type
                                            
                                            	Set packet type
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_remote_address
                                            
                                            	Set Remote address
                                            	**type**\:  bool
                                            
                                            .. attribute:: is_remote_port
                                            
                                            	Set Remote Port
                                            	**type**\:  bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2016-02-26'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask, self).__init__()

                                                self.yang_name = "accept-mask"
                                                self.yang_parent_name = "lpts-pcb"

                                                self.is_interface = YLeaf(YType.boolean, "is-interface")

                                                self.is_local_address = YLeaf(YType.boolean, "is-local-address")

                                                self.is_local_port = YLeaf(YType.boolean, "is-local-port")

                                                self.is_packet_type = YLeaf(YType.boolean, "is-packet-type")

                                                self.is_remote_address = YLeaf(YType.boolean, "is-remote-address")

                                                self.is_remote_port = YLeaf(YType.boolean, "is-remote-port")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("is_interface",
                                                                "is_local_address",
                                                                "is_local_port",
                                                                "is_packet_type",
                                                                "is_remote_address",
                                                                "is_remote_port") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.is_interface.is_set or
                                                    self.is_local_address.is_set or
                                                    self.is_local_port.is_set or
                                                    self.is_packet_type.is_set or
                                                    self.is_remote_address.is_set or
                                                    self.is_remote_port.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.is_interface.yfilter != YFilter.not_set or
                                                    self.is_local_address.yfilter != YFilter.not_set or
                                                    self.is_local_port.yfilter != YFilter.not_set or
                                                    self.is_packet_type.yfilter != YFilter.not_set or
                                                    self.is_remote_address.yfilter != YFilter.not_set or
                                                    self.is_remote_port.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "accept-mask" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.is_interface.is_set or self.is_interface.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_interface.get_name_leafdata())
                                                if (self.is_local_address.is_set or self.is_local_address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_local_address.get_name_leafdata())
                                                if (self.is_local_port.is_set or self.is_local_port.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_local_port.get_name_leafdata())
                                                if (self.is_packet_type.is_set or self.is_packet_type.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_packet_type.get_name_leafdata())
                                                if (self.is_remote_address.is_set or self.is_remote_address.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_remote_address.get_name_leafdata())
                                                if (self.is_remote_port.is_set or self.is_remote_port.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.is_remote_port.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "is-interface" or name == "is-local-address" or name == "is-local-port" or name == "is-packet-type" or name == "is-remote-address" or name == "is-remote-port"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "is-interface"):
                                                    self.is_interface = value
                                                    self.is_interface.value_namespace = name_space
                                                    self.is_interface.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-local-address"):
                                                    self.is_local_address = value
                                                    self.is_local_address.value_namespace = name_space
                                                    self.is_local_address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-local-port"):
                                                    self.is_local_port = value
                                                    self.is_local_port.value_namespace = name_space
                                                    self.is_local_port.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-packet-type"):
                                                    self.is_packet_type = value
                                                    self.is_packet_type.value_namespace = name_space
                                                    self.is_packet_type.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-remote-address"):
                                                    self.is_remote_address = value
                                                    self.is_remote_address.value_namespace = name_space
                                                    self.is_remote_address.value_namespace_prefix = name_space_prefix
                                                if(value_path == "is-remote-port"):
                                                    self.is_remote_port = value
                                                    self.is_remote_port.value_namespace = name_space
                                                    self.is_remote_port.value_namespace_prefix = name_space_prefix


                                        class Filter(Entity):
                                            """
                                            Interface Filters
                                            
                                            .. attribute:: flow_types_info
                                            
                                            	flow information
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: interface_name
                                            
                                            	Interface name
                                            	**type**\:  str
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: local_address
                                            
                                            	Local address
                                            	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress>`
                                            
                                            .. attribute:: local_length
                                            
                                            	Local address length
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: packet_type
                                            
                                            	Protocol\-specific packet type
                                            	**type**\:   :py:class:`PacketType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType>`
                                            
                                            .. attribute:: priority
                                            
                                            	Priority
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: receive_local_port
                                            
                                            	Receive Local port
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: receive_remote_port
                                            
                                            	Receive Remote port
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: remote_address
                                            
                                            	Remote address
                                            	**type**\:   :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress>`
                                            
                                            .. attribute:: remote_length
                                            
                                            	Remote address length
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: ttl
                                            
                                            	Minimum TTL
                                            	**type**\:  int
                                            
                                            	**range:** 0..255
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2016-02-26'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter, self).__init__()

                                                self.yang_name = "filter"
                                                self.yang_parent_name = "lpts-pcb"

                                                self.flow_types_info = YLeaf(YType.uint32, "flow-types-info")

                                                self.interface_name = YLeaf(YType.str, "interface-name")

                                                self.local_length = YLeaf(YType.uint16, "local-length")

                                                self.priority = YLeaf(YType.uint8, "priority")

                                                self.receive_local_port = YLeaf(YType.uint16, "receive-local-port")

                                                self.receive_remote_port = YLeaf(YType.uint16, "receive-remote-port")

                                                self.remote_length = YLeaf(YType.uint16, "remote-length")

                                                self.ttl = YLeaf(YType.uint8, "ttl")

                                                self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress()
                                                self.local_address.parent = self
                                                self._children_name_map["local_address"] = "local-address"
                                                self._children_yang_names.add("local-address")

                                                self.packet_type = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType()
                                                self.packet_type.parent = self
                                                self._children_name_map["packet_type"] = "packet-type"
                                                self._children_yang_names.add("packet-type")

                                                self.remote_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress()
                                                self.remote_address.parent = self
                                                self._children_name_map["remote_address"] = "remote-address"
                                                self._children_yang_names.add("remote-address")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("flow_types_info",
                                                                "interface_name",
                                                                "local_length",
                                                                "priority",
                                                                "receive_local_port",
                                                                "receive_remote_port",
                                                                "remote_length",
                                                                "ttl") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter, self).__setattr__(name, value)


                                            class PacketType(Entity):
                                                """
                                                Protocol\-specific packet type
                                                
                                                .. attribute:: icm_pv6_message_type
                                                
                                                	ICMPv6 message type
                                                	**type**\:   :py:class:`MessageTypeIcmpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmpv6>`
                                                
                                                .. attribute:: icmp_message_type
                                                
                                                	ICMP message type
                                                	**type**\:   :py:class:`MessageTypeIcmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmp>`
                                                
                                                .. attribute:: igmp_message_type
                                                
                                                	IGMP message type
                                                	**type**\:   :py:class:`MessageTypeIgmp <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIgmp>`
                                                
                                                .. attribute:: message_id
                                                
                                                	Message type in number
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: type
                                                
                                                	Type
                                                	**type**\:   :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Packet>`
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2016-02-26'

                                                def __init__(self):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType, self).__init__()

                                                    self.yang_name = "packet-type"
                                                    self.yang_parent_name = "filter"

                                                    self.icm_pv6_message_type = YLeaf(YType.enumeration, "icm-pv6-message-type")

                                                    self.icmp_message_type = YLeaf(YType.enumeration, "icmp-message-type")

                                                    self.igmp_message_type = YLeaf(YType.enumeration, "igmp-message-type")

                                                    self.message_id = YLeaf(YType.uint32, "message-id")

                                                    self.type = YLeaf(YType.enumeration, "type")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("icm_pv6_message_type",
                                                                    "icmp_message_type",
                                                                    "igmp_message_type",
                                                                    "message_id",
                                                                    "type") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.icm_pv6_message_type.is_set or
                                                        self.icmp_message_type.is_set or
                                                        self.igmp_message_type.is_set or
                                                        self.message_id.is_set or
                                                        self.type.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.icm_pv6_message_type.yfilter != YFilter.not_set or
                                                        self.icmp_message_type.yfilter != YFilter.not_set or
                                                        self.igmp_message_type.yfilter != YFilter.not_set or
                                                        self.message_id.yfilter != YFilter.not_set or
                                                        self.type.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "packet-type" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.icm_pv6_message_type.is_set or self.icm_pv6_message_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.icm_pv6_message_type.get_name_leafdata())
                                                    if (self.icmp_message_type.is_set or self.icmp_message_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.icmp_message_type.get_name_leafdata())
                                                    if (self.igmp_message_type.is_set or self.igmp_message_type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.igmp_message_type.get_name_leafdata())
                                                    if (self.message_id.is_set or self.message_id.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.message_id.get_name_leafdata())
                                                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.type.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "icm-pv6-message-type" or name == "icmp-message-type" or name == "igmp-message-type" or name == "message-id" or name == "type"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "icm-pv6-message-type"):
                                                        self.icm_pv6_message_type = value
                                                        self.icm_pv6_message_type.value_namespace = name_space
                                                        self.icm_pv6_message_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "icmp-message-type"):
                                                        self.icmp_message_type = value
                                                        self.icmp_message_type.value_namespace = name_space
                                                        self.icmp_message_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "igmp-message-type"):
                                                        self.igmp_message_type = value
                                                        self.igmp_message_type.value_namespace = name_space
                                                        self.igmp_message_type.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "message-id"):
                                                        self.message_id = value
                                                        self.message_id.value_namespace = name_space
                                                        self.message_id.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "type"):
                                                        self.type = value
                                                        self.type.value_namespace = name_space
                                                        self.type.value_namespace_prefix = name_space_prefix


                                            class RemoteAddress(Entity):
                                                """
                                                Remote address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\:   :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 address
                                                	**type**\:  str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2016-02-26'

                                                def __init__(self):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress, self).__init__()

                                                    self.yang_name = "remote-address"
                                                    self.yang_parent_name = "filter"

                                                    self.af_name = YLeaf(YType.enumeration, "af-name")

                                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("af_name",
                                                                    "ipv4_address",
                                                                    "ipv6_address") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.af_name.is_set or
                                                        self.ipv4_address.is_set or
                                                        self.ipv6_address.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.af_name.yfilter != YFilter.not_set or
                                                        self.ipv4_address.yfilter != YFilter.not_set or
                                                        self.ipv6_address.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "remote-address" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.af_name.get_name_leafdata())
                                                    if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                                    if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "af-name"):
                                                        self.af_name = value
                                                        self.af_name.value_namespace = name_space
                                                        self.af_name.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "ipv4-address"):
                                                        self.ipv4_address = value
                                                        self.ipv4_address.value_namespace = name_space
                                                        self.ipv4_address.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "ipv6-address"):
                                                        self.ipv6_address = value
                                                        self.ipv6_address.value_namespace = name_space
                                                        self.ipv6_address.value_namespace_prefix = name_space_prefix


                                            class LocalAddress(Entity):
                                                """
                                                Local address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\:   :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 address
                                                	**type**\:  str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 address
                                                	**type**\:  str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2016-02-26'

                                                def __init__(self):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress, self).__init__()

                                                    self.yang_name = "local-address"
                                                    self.yang_parent_name = "filter"

                                                    self.af_name = YLeaf(YType.enumeration, "af-name")

                                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("af_name",
                                                                    "ipv4_address",
                                                                    "ipv6_address") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.af_name.is_set or
                                                        self.ipv4_address.is_set or
                                                        self.ipv6_address.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.af_name.yfilter != YFilter.not_set or
                                                        self.ipv4_address.yfilter != YFilter.not_set or
                                                        self.ipv6_address.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "local-address" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.af_name.get_name_leafdata())
                                                    if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                                                    if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "af-name"):
                                                        self.af_name = value
                                                        self.af_name.value_namespace = name_space
                                                        self.af_name.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "ipv4-address"):
                                                        self.ipv4_address = value
                                                        self.ipv4_address.value_namespace = name_space
                                                        self.ipv4_address.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "ipv6-address"):
                                                        self.ipv6_address = value
                                                        self.ipv6_address.value_namespace = name_space
                                                        self.ipv6_address.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.flow_types_info.is_set or
                                                    self.interface_name.is_set or
                                                    self.local_length.is_set or
                                                    self.priority.is_set or
                                                    self.receive_local_port.is_set or
                                                    self.receive_remote_port.is_set or
                                                    self.remote_length.is_set or
                                                    self.ttl.is_set or
                                                    (self.local_address is not None and self.local_address.has_data()) or
                                                    (self.packet_type is not None and self.packet_type.has_data()) or
                                                    (self.remote_address is not None and self.remote_address.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.flow_types_info.yfilter != YFilter.not_set or
                                                    self.interface_name.yfilter != YFilter.not_set or
                                                    self.local_length.yfilter != YFilter.not_set or
                                                    self.priority.yfilter != YFilter.not_set or
                                                    self.receive_local_port.yfilter != YFilter.not_set or
                                                    self.receive_remote_port.yfilter != YFilter.not_set or
                                                    self.remote_length.yfilter != YFilter.not_set or
                                                    self.ttl.yfilter != YFilter.not_set or
                                                    (self.local_address is not None and self.local_address.has_operation()) or
                                                    (self.packet_type is not None and self.packet_type.has_operation()) or
                                                    (self.remote_address is not None and self.remote_address.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "filter" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.flow_types_info.is_set or self.flow_types_info.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.flow_types_info.get_name_leafdata())
                                                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.interface_name.get_name_leafdata())
                                                if (self.local_length.is_set or self.local_length.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.local_length.get_name_leafdata())
                                                if (self.priority.is_set or self.priority.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.priority.get_name_leafdata())
                                                if (self.receive_local_port.is_set or self.receive_local_port.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.receive_local_port.get_name_leafdata())
                                                if (self.receive_remote_port.is_set or self.receive_remote_port.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.receive_remote_port.get_name_leafdata())
                                                if (self.remote_length.is_set or self.remote_length.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.remote_length.get_name_leafdata())
                                                if (self.ttl.is_set or self.ttl.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.ttl.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "local-address"):
                                                    if (self.local_address is None):
                                                        self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress()
                                                        self.local_address.parent = self
                                                        self._children_name_map["local_address"] = "local-address"
                                                    return self.local_address

                                                if (child_yang_name == "packet-type"):
                                                    if (self.packet_type is None):
                                                        self.packet_type = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType()
                                                        self.packet_type.parent = self
                                                        self._children_name_map["packet_type"] = "packet-type"
                                                    return self.packet_type

                                                if (child_yang_name == "remote-address"):
                                                    if (self.remote_address is None):
                                                        self.remote_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress()
                                                        self.remote_address.parent = self
                                                        self._children_name_map["remote_address"] = "remote-address"
                                                    return self.remote_address

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "local-address" or name == "packet-type" or name == "remote-address" or name == "flow-types-info" or name == "interface-name" or name == "local-length" or name == "priority" or name == "receive-local-port" or name == "receive-remote-port" or name == "remote-length" or name == "ttl"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "flow-types-info"):
                                                    self.flow_types_info = value
                                                    self.flow_types_info.value_namespace = name_space
                                                    self.flow_types_info.value_namespace_prefix = name_space_prefix
                                                if(value_path == "interface-name"):
                                                    self.interface_name = value
                                                    self.interface_name.value_namespace = name_space
                                                    self.interface_name.value_namespace_prefix = name_space_prefix
                                                if(value_path == "local-length"):
                                                    self.local_length = value
                                                    self.local_length.value_namespace = name_space
                                                    self.local_length.value_namespace_prefix = name_space_prefix
                                                if(value_path == "priority"):
                                                    self.priority = value
                                                    self.priority.value_namespace = name_space
                                                    self.priority.value_namespace_prefix = name_space_prefix
                                                if(value_path == "receive-local-port"):
                                                    self.receive_local_port = value
                                                    self.receive_local_port.value_namespace = name_space
                                                    self.receive_local_port.value_namespace_prefix = name_space_prefix
                                                if(value_path == "receive-remote-port"):
                                                    self.receive_remote_port = value
                                                    self.receive_remote_port.value_namespace = name_space
                                                    self.receive_remote_port.value_namespace_prefix = name_space_prefix
                                                if(value_path == "remote-length"):
                                                    self.remote_length = value
                                                    self.remote_length.value_namespace = name_space
                                                    self.remote_length.value_namespace_prefix = name_space_prefix
                                                if(value_path == "ttl"):
                                                    self.ttl = value
                                                    self.ttl.value_namespace = name_space
                                                    self.ttl.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.filter:
                                                if (c.has_data()):
                                                    return True
                                            return (
                                                self.flow_types_info.is_set or
                                                self.ttl.is_set or
                                                (self.accept_mask is not None and self.accept_mask.has_data()) or
                                                (self.lpts_flags is not None and self.lpts_flags.has_data()) or
                                                (self.options is not None and self.options.has_data()))

                                        def has_operation(self):
                                            for c in self.filter:
                                                if (c.has_operation()):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.flow_types_info.yfilter != YFilter.not_set or
                                                self.ttl.yfilter != YFilter.not_set or
                                                (self.accept_mask is not None and self.accept_mask.has_operation()) or
                                                (self.lpts_flags is not None and self.lpts_flags.has_operation()) or
                                                (self.options is not None and self.options.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "lpts-pcb" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.flow_types_info.is_set or self.flow_types_info.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.flow_types_info.get_name_leafdata())
                                            if (self.ttl.is_set or self.ttl.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.ttl.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "accept-mask"):
                                                if (self.accept_mask is None):
                                                    self.accept_mask = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask()
                                                    self.accept_mask.parent = self
                                                    self._children_name_map["accept_mask"] = "accept-mask"
                                                return self.accept_mask

                                            if (child_yang_name == "filter"):
                                                for c in self.filter:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.filter.append(c)
                                                return c

                                            if (child_yang_name == "lpts-flags"):
                                                if (self.lpts_flags is None):
                                                    self.lpts_flags = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags()
                                                    self.lpts_flags.parent = self
                                                    self._children_name_map["lpts_flags"] = "lpts-flags"
                                                return self.lpts_flags

                                            if (child_yang_name == "options"):
                                                if (self.options is None):
                                                    self.options = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options()
                                                    self.options.parent = self
                                                    self._children_name_map["options"] = "options"
                                                return self.options

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "accept-mask" or name == "filter" or name == "lpts-flags" or name == "options" or name == "flow-types-info" or name == "ttl"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "flow-types-info"):
                                                self.flow_types_info = value
                                                self.flow_types_info.value_namespace = name_space
                                                self.flow_types_info.value_namespace_prefix = name_space_prefix
                                            if(value_path == "ttl"):
                                                self.ttl = value
                                                self.ttl.value_namespace = name_space
                                                self.ttl.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.af_name.is_set or
                                            (self.lpts_pcb is not None and self.lpts_pcb.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.af_name.yfilter != YFilter.not_set or
                                            (self.lpts_pcb is not None and self.lpts_pcb.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "common" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.af_name.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "lpts-pcb"):
                                            if (self.lpts_pcb is None):
                                                self.lpts_pcb = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb()
                                                self.lpts_pcb.parent = self
                                                self._children_name_map["lpts_pcb"] = "lpts-pcb"
                                            return self.lpts_pcb

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "lpts-pcb" or name == "af-name"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "af-name"):
                                            self.af_name = value
                                            self.af_name.value_namespace = name_space
                                            self.af_name.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (
                                        self.pcb_address.is_set or
                                        self.foreign_port.is_set or
                                        self.l4_protocol.is_set or
                                        self.local_port.is_set or
                                        (self.common is not None and self.common.has_data()) or
                                        (self.foreign_address is not None and self.foreign_address.has_data()) or
                                        (self.local_address is not None and self.local_address.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.pcb_address.yfilter != YFilter.not_set or
                                        self.foreign_port.yfilter != YFilter.not_set or
                                        self.l4_protocol.yfilter != YFilter.not_set or
                                        self.local_port.yfilter != YFilter.not_set or
                                        (self.common is not None and self.common.has_operation()) or
                                        (self.foreign_address is not None and self.foreign_address.has_operation()) or
                                        (self.local_address is not None and self.local_address.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "pcb" + "[pcb-address='" + self.pcb_address.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.pcb_address.is_set or self.pcb_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pcb_address.get_name_leafdata())
                                    if (self.foreign_port.is_set or self.foreign_port.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.foreign_port.get_name_leafdata())
                                    if (self.l4_protocol.is_set or self.l4_protocol.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.l4_protocol.get_name_leafdata())
                                    if (self.local_port.is_set or self.local_port.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.local_port.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "common"):
                                        if (self.common is None):
                                            self.common = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common()
                                            self.common.parent = self
                                            self._children_name_map["common"] = "common"
                                        return self.common

                                    if (child_yang_name == "foreign-address"):
                                        if (self.foreign_address is None):
                                            self.foreign_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress()
                                            self.foreign_address.parent = self
                                            self._children_name_map["foreign_address"] = "foreign-address"
                                        return self.foreign_address

                                    if (child_yang_name == "local-address"):
                                        if (self.local_address is None):
                                            self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress()
                                            self.local_address.parent = self
                                            self._children_name_map["local_address"] = "local-address"
                                        return self.local_address

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "common" or name == "foreign-address" or name == "local-address" or name == "pcb-address" or name == "foreign-port" or name == "l4-protocol" or name == "local-port"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "pcb-address"):
                                        self.pcb_address = value
                                        self.pcb_address.value_namespace = name_space
                                        self.pcb_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "foreign-port"):
                                        self.foreign_port = value
                                        self.foreign_port.value_namespace = name_space
                                        self.foreign_port.value_namespace_prefix = name_space_prefix
                                    if(value_path == "l4-protocol"):
                                        self.l4_protocol = value
                                        self.l4_protocol.value_namespace = name_space
                                        self.l4_protocol.value_namespace_prefix = name_space_prefix
                                    if(value_path == "local-port"):
                                        self.local_port = value
                                        self.local_port.value_namespace = name_space
                                        self.local_port.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.pcb:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.pcb:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "pcbs" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "pcb"):
                                    for c in self.pcb:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.pcb.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "pcb"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.query_name.is_set or
                                (self.pcbs is not None and self.pcbs.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.query_name.yfilter != YFilter.not_set or
                                (self.pcbs is not None and self.pcbs.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "query" + "[query-name='" + self.query_name.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.query_name.is_set or self.query_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.query_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "pcbs"):
                                if (self.pcbs is None):
                                    self.pcbs = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs()
                                    self.pcbs.parent = self
                                    self._children_name_map["pcbs"] = "pcbs"
                                return self.pcbs

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "pcbs" or name == "query-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "query-name"):
                                self.query_name = value
                                self.query_name.value_namespace = name_space
                                self.query_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.query:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.query:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "queries" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "query"):
                            for c in self.query:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = UdpConnection.Nodes.Node.Lpts.Queries.Query()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.query.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "query"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.queries is not None and self.queries.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.queries is not None and self.queries.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "lpts" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "queries"):
                        if (self.queries is None):
                            self.queries = UdpConnection.Nodes.Node.Lpts.Queries()
                            self.queries.parent = self
                            self._children_name_map["queries"] = "queries"
                        return self.queries

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "queries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PcbDetails(Entity):
                """
                Detail information for list of UDP connections
                .
                
                .. attribute:: pcb_detail
                
                	Detail information about a UDP connection
                	**type**\: list of    :py:class:`PcbDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2016-02-26'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.PcbDetails, self).__init__()

                    self.yang_name = "pcb-details"
                    self.yang_parent_name = "node"

                    self.pcb_detail = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(UdpConnection.Nodes.Node.PcbDetails, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(UdpConnection.Nodes.Node.PcbDetails, self).__setattr__(name, value)


                class PcbDetail(Entity):
                    """
                    Detail information about a UDP connection
                    
                    .. attribute:: pcb_address  <key>
                    
                    	Protocol Control Block address
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\:   :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:   :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress>`
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress>`
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_process_id
                    
                    	ID of local process
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_queue
                    
                    	Receive queue count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_queue
                    
                    	Send queue count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_id
                    
                    	VRF ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail, self).__init__()

                        self.yang_name = "pcb-detail"
                        self.yang_parent_name = "pcb-details"

                        self.pcb_address = YLeaf(YType.int32, "pcb-address")

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.foreign_port = YLeaf(YType.uint16, "foreign-port")

                        self.local_port = YLeaf(YType.uint16, "local-port")

                        self.local_process_id = YLeaf(YType.uint32, "local-process-id")

                        self.receive_queue = YLeaf(YType.uint32, "receive-queue")

                        self.send_queue = YLeaf(YType.uint32, "send-queue")

                        self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                        self.foreign_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress()
                        self.foreign_address.parent = self
                        self._children_name_map["foreign_address"] = "foreign-address"
                        self._children_yang_names.add("foreign-address")

                        self.local_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("pcb_address",
                                        "af_name",
                                        "foreign_port",
                                        "local_port",
                                        "local_process_id",
                                        "receive_queue",
                                        "send_queue",
                                        "vrf_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail, self).__setattr__(name, value)


                    class LocalAddress(Entity):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "pcb-detail"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "local-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix


                    class ForeignAddress(Entity):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress, self).__init__()

                            self.yang_name = "foreign-address"
                            self.yang_parent_name = "pcb-detail"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "foreign-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.pcb_address.is_set or
                            self.af_name.is_set or
                            self.foreign_port.is_set or
                            self.local_port.is_set or
                            self.local_process_id.is_set or
                            self.receive_queue.is_set or
                            self.send_queue.is_set or
                            self.vrf_id.is_set or
                            (self.foreign_address is not None and self.foreign_address.has_data()) or
                            (self.local_address is not None and self.local_address.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pcb_address.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.foreign_port.yfilter != YFilter.not_set or
                            self.local_port.yfilter != YFilter.not_set or
                            self.local_process_id.yfilter != YFilter.not_set or
                            self.receive_queue.yfilter != YFilter.not_set or
                            self.send_queue.yfilter != YFilter.not_set or
                            self.vrf_id.yfilter != YFilter.not_set or
                            (self.foreign_address is not None and self.foreign_address.has_operation()) or
                            (self.local_address is not None and self.local_address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pcb-detail" + "[pcb-address='" + self.pcb_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pcb_address.is_set or self.pcb_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pcb_address.get_name_leafdata())
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.foreign_port.is_set or self.foreign_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.foreign_port.get_name_leafdata())
                        if (self.local_port.is_set or self.local_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_port.get_name_leafdata())
                        if (self.local_process_id.is_set or self.local_process_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_process_id.get_name_leafdata())
                        if (self.receive_queue.is_set or self.receive_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_queue.get_name_leafdata())
                        if (self.send_queue.is_set or self.send_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_queue.get_name_leafdata())
                        if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "foreign-address"):
                            if (self.foreign_address is None):
                                self.foreign_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress()
                                self.foreign_address.parent = self
                                self._children_name_map["foreign_address"] = "foreign-address"
                            return self.foreign_address

                        if (child_yang_name == "local-address"):
                            if (self.local_address is None):
                                self.local_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress()
                                self.local_address.parent = self
                                self._children_name_map["local_address"] = "local-address"
                            return self.local_address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "foreign-address" or name == "local-address" or name == "pcb-address" or name == "af-name" or name == "foreign-port" or name == "local-port" or name == "local-process-id" or name == "receive-queue" or name == "send-queue" or name == "vrf-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pcb-address"):
                            self.pcb_address = value
                            self.pcb_address.value_namespace = name_space
                            self.pcb_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "foreign-port"):
                            self.foreign_port = value
                            self.foreign_port.value_namespace = name_space
                            self.foreign_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-port"):
                            self.local_port = value
                            self.local_port.value_namespace = name_space
                            self.local_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-process-id"):
                            self.local_process_id = value
                            self.local_process_id.value_namespace = name_space
                            self.local_process_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-queue"):
                            self.receive_queue = value
                            self.receive_queue.value_namespace = name_space
                            self.receive_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-queue"):
                            self.send_queue = value
                            self.send_queue.value_namespace = name_space
                            self.send_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-id"):
                            self.vrf_id = value
                            self.vrf_id.value_namespace = name_space
                            self.vrf_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.pcb_detail:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.pcb_detail:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "pcb-details" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "pcb-detail"):
                        for c in self.pcb_detail:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = UdpConnection.Nodes.Node.PcbDetails.PcbDetail()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.pcb_detail.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pcb-detail"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class PcbBriefs(Entity):
                """
                Brief information for list of UDP connections.
                
                .. attribute:: pcb_brief
                
                	Brief information about a UDP connection
                	**type**\: list of    :py:class:`PcbBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2016-02-26'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.PcbBriefs, self).__init__()

                    self.yang_name = "pcb-briefs"
                    self.yang_parent_name = "node"

                    self.pcb_brief = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in () and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(UdpConnection.Nodes.Node.PcbBriefs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(UdpConnection.Nodes.Node.PcbBriefs, self).__setattr__(name, value)


                class PcbBrief(Entity):
                    """
                    Brief information about a UDP connection
                    
                    .. attribute:: pcb_address  <key>
                    
                    	Protocol Control Block address
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\:   :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:   :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress>`
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:   :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress>`
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: receive_queue
                    
                    	Receive queue count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_queue
                    
                    	Send queue count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_id
                    
                    	VRF ID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief, self).__init__()

                        self.yang_name = "pcb-brief"
                        self.yang_parent_name = "pcb-briefs"

                        self.pcb_address = YLeaf(YType.int32, "pcb-address")

                        self.af_name = YLeaf(YType.enumeration, "af-name")

                        self.foreign_port = YLeaf(YType.uint16, "foreign-port")

                        self.local_port = YLeaf(YType.uint16, "local-port")

                        self.receive_queue = YLeaf(YType.uint32, "receive-queue")

                        self.send_queue = YLeaf(YType.uint32, "send-queue")

                        self.vrf_id = YLeaf(YType.uint32, "vrf-id")

                        self.foreign_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress()
                        self.foreign_address.parent = self
                        self._children_name_map["foreign_address"] = "foreign-address"
                        self._children_yang_names.add("foreign-address")

                        self.local_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("pcb_address",
                                        "af_name",
                                        "foreign_port",
                                        "local_port",
                                        "receive_queue",
                                        "send_queue",
                                        "vrf_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief, self).__setattr__(name, value)


                    class LocalAddress(Entity):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "pcb-brief"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "local-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix


                    class ForeignAddress(Entity):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress, self).__init__()

                            self.yang_name = "foreign-address"
                            self.yang_parent_name = "pcb-brief"

                            self.af_name = YLeaf(YType.enumeration, "af-name")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("af_name",
                                            "ipv4_address",
                                            "ipv6_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.af_name.is_set or
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.af_name.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "foreign-address" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.af_name.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "af-name" or name == "ipv4-address" or name == "ipv6-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "af-name"):
                                self.af_name = value
                                self.af_name.value_namespace = name_space
                                self.af_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.pcb_address.is_set or
                            self.af_name.is_set or
                            self.foreign_port.is_set or
                            self.local_port.is_set or
                            self.receive_queue.is_set or
                            self.send_queue.is_set or
                            self.vrf_id.is_set or
                            (self.foreign_address is not None and self.foreign_address.has_data()) or
                            (self.local_address is not None and self.local_address.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pcb_address.yfilter != YFilter.not_set or
                            self.af_name.yfilter != YFilter.not_set or
                            self.foreign_port.yfilter != YFilter.not_set or
                            self.local_port.yfilter != YFilter.not_set or
                            self.receive_queue.yfilter != YFilter.not_set or
                            self.send_queue.yfilter != YFilter.not_set or
                            self.vrf_id.yfilter != YFilter.not_set or
                            (self.foreign_address is not None and self.foreign_address.has_operation()) or
                            (self.local_address is not None and self.local_address.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pcb-brief" + "[pcb-address='" + self.pcb_address.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pcb_address.is_set or self.pcb_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pcb_address.get_name_leafdata())
                        if (self.af_name.is_set or self.af_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.af_name.get_name_leafdata())
                        if (self.foreign_port.is_set or self.foreign_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.foreign_port.get_name_leafdata())
                        if (self.local_port.is_set or self.local_port.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_port.get_name_leafdata())
                        if (self.receive_queue.is_set or self.receive_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.receive_queue.get_name_leafdata())
                        if (self.send_queue.is_set or self.send_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.send_queue.get_name_leafdata())
                        if (self.vrf_id.is_set or self.vrf_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vrf_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "foreign-address"):
                            if (self.foreign_address is None):
                                self.foreign_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress()
                                self.foreign_address.parent = self
                                self._children_name_map["foreign_address"] = "foreign-address"
                            return self.foreign_address

                        if (child_yang_name == "local-address"):
                            if (self.local_address is None):
                                self.local_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress()
                                self.local_address.parent = self
                                self._children_name_map["local_address"] = "local-address"
                            return self.local_address

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "foreign-address" or name == "local-address" or name == "pcb-address" or name == "af-name" or name == "foreign-port" or name == "local-port" or name == "receive-queue" or name == "send-queue" or name == "vrf-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pcb-address"):
                            self.pcb_address = value
                            self.pcb_address.value_namespace = name_space
                            self.pcb_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "af-name"):
                            self.af_name = value
                            self.af_name.value_namespace = name_space
                            self.af_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "foreign-port"):
                            self.foreign_port = value
                            self.foreign_port.value_namespace = name_space
                            self.foreign_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-port"):
                            self.local_port = value
                            self.local_port.value_namespace = name_space
                            self.local_port.value_namespace_prefix = name_space_prefix
                        if(value_path == "receive-queue"):
                            self.receive_queue = value
                            self.receive_queue.value_namespace = name_space
                            self.receive_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "send-queue"):
                            self.send_queue = value
                            self.send_queue.value_namespace = name_space
                            self.send_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "vrf-id"):
                            self.vrf_id = value
                            self.vrf_id.value_namespace = name_space
                            self.vrf_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.pcb_brief:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.pcb_brief:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "pcb-briefs" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "pcb-brief"):
                        for c in self.pcb_brief:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.pcb_brief.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "pcb-brief"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node_name.is_set or
                    (self.lpts is not None and self.lpts.has_data()) or
                    (self.pcb_briefs is not None and self.pcb_briefs.has_data()) or
                    (self.pcb_details is not None and self.pcb_details.has_data()) or
                    (self.statistics is not None and self.statistics.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node_name.yfilter != YFilter.not_set or
                    (self.lpts is not None and self.lpts.has_operation()) or
                    (self.pcb_briefs is not None and self.pcb_briefs.has_operation()) or
                    (self.pcb_details is not None and self.pcb_details.has_operation()) or
                    (self.statistics is not None and self.statistics.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node-name='" + self.node_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ip-udp-oper:udp-connection/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node_name.is_set or self.node_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "lpts"):
                    if (self.lpts is None):
                        self.lpts = UdpConnection.Nodes.Node.Lpts()
                        self.lpts.parent = self
                        self._children_name_map["lpts"] = "lpts"
                    return self.lpts

                if (child_yang_name == "pcb-briefs"):
                    if (self.pcb_briefs is None):
                        self.pcb_briefs = UdpConnection.Nodes.Node.PcbBriefs()
                        self.pcb_briefs.parent = self
                        self._children_name_map["pcb_briefs"] = "pcb-briefs"
                    return self.pcb_briefs

                if (child_yang_name == "pcb-details"):
                    if (self.pcb_details is None):
                        self.pcb_details = UdpConnection.Nodes.Node.PcbDetails()
                        self.pcb_details.parent = self
                        self._children_name_map["pcb_details"] = "pcb-details"
                    return self.pcb_details

                if (child_yang_name == "statistics"):
                    if (self.statistics is None):
                        self.statistics = UdpConnection.Nodes.Node.Statistics()
                        self.statistics.parent = self
                        self._children_name_map["statistics"] = "statistics"
                    return self.statistics

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "lpts" or name == "pcb-briefs" or name == "pcb-details" or name == "statistics" or name == "node-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node-name"):
                    self.node_name = value
                    self.node_name.value_namespace = name_space
                    self.node_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ip-udp-oper:udp-connection/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = UdpConnection.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.nodes is not None and self.nodes.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ip-udp-oper:udp-connection" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = UdpConnection.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = UdpConnection()
        return self._top_entity

