""" Cisco_IOS_XR_ip_udp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-udp package operational data.

This module contains definitions
for the following management objects\:
  udp\: IP UDP Operational Data
  udp\-connection\: udp connection

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AddrFamily(Enum):
    """
    AddrFamily (Enum Class)

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
    LptsPcbQuery (Enum Class)

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
    MessageTypeIcmp (Enum Class)

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


class MessageTypeIcmp_(Enum):
    """
    MessageTypeIcmp\_ (Enum Class)

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
    MessageTypeIcmpv6 (Enum Class)

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


class MessageTypeIcmpv6_(Enum):
    """
    MessageTypeIcmpv6\_ (Enum Class)

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
    MessageTypeIgmp (Enum Class)

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


class MessageTypeIgmp_(Enum):
    """
    MessageTypeIgmp\_ (Enum Class)

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
    Packet (Enum Class)

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
    UdpAddressFamily (Enum Class)

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
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2018-03-04'

    def __init__(self):
        super(Udp, self).__init__()
        self._top_entity = None

        self.yang_name = "udp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-udp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", Udp.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = Udp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-udp-oper:udp"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Udp, [], name, value)


    class Nodes(Entity):
        """
        Node\-specific UDP operational data
        
        .. attribute:: node
        
        	UDP operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2018-03-04'

        def __init__(self):
            super(Udp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "udp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", Udp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-udp-oper:udp/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Udp.Nodes, [], name, value)


        class Node(Entity):
            """
            UDP operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistical UDP operational data for a node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2018-03-04'

            def __init__(self):
                super(Udp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("statistics", ("statistics", Udp.Nodes.Node.Statistics))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.statistics = Udp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-udp-oper:udp/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Udp.Nodes.Node, ['node_name'], name, value)


            class Statistics(Entity):
                """
                Statistical UDP operational data for a node
                
                .. attribute:: ipv4_traffic
                
                	UDP Traffic statistics for IPv4
                	**type**\:  :py:class:`Ipv4Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv4Traffic>`
                
                .. attribute:: ipv6_traffic
                
                	UDP Traffic statistics for IPv6
                	**type**\:  :py:class:`Ipv6Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv6Traffic>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2018-03-04'

                def __init__(self):
                    super(Udp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("ipv4-traffic", ("ipv4_traffic", Udp.Nodes.Node.Statistics.Ipv4Traffic)), ("ipv6-traffic", ("ipv6_traffic", Udp.Nodes.Node.Statistics.Ipv6Traffic))])
                    self._leafs = OrderedDict()

                    self.ipv4_traffic = Udp.Nodes.Node.Statistics.Ipv4Traffic()
                    self.ipv4_traffic.parent = self
                    self._children_name_map["ipv4_traffic"] = "ipv4-traffic"

                    self.ipv6_traffic = Udp.Nodes.Node.Statistics.Ipv6Traffic()
                    self.ipv6_traffic.parent = self
                    self._children_name_map["ipv6_traffic"] = "ipv6-traffic"
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Udp.Nodes.Node.Statistics, [], name, value)


                class Ipv4Traffic(Entity):
                    """
                    UDP Traffic statistics for IPv4
                    
                    .. attribute:: udp_input_packets
                    
                    	UDP Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_checksum_error_packets
                    
                    	UDP Checksum Errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_no_port_packets
                    
                    	UDP No Port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_bad_length_packets
                    
                    	UDP bad length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_output_packets
                    
                    	UDP Transmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_dropped_packets
                    
                    	UDP drop for other reason
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(Udp.Nodes.Node.Statistics.Ipv4Traffic, self).__init__()

                        self.yang_name = "ipv4-traffic"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('udp_input_packets', (YLeaf(YType.uint32, 'udp-input-packets'), ['int'])),
                            ('udp_checksum_error_packets', (YLeaf(YType.uint32, 'udp-checksum-error-packets'), ['int'])),
                            ('udp_no_port_packets', (YLeaf(YType.uint32, 'udp-no-port-packets'), ['int'])),
                            ('udp_bad_length_packets', (YLeaf(YType.uint32, 'udp-bad-length-packets'), ['int'])),
                            ('udp_output_packets', (YLeaf(YType.uint32, 'udp-output-packets'), ['int'])),
                            ('udp_dropped_packets', (YLeaf(YType.uint32, 'udp-dropped-packets'), ['int'])),
                        ])
                        self.udp_input_packets = None
                        self.udp_checksum_error_packets = None
                        self.udp_no_port_packets = None
                        self.udp_bad_length_packets = None
                        self.udp_output_packets = None
                        self.udp_dropped_packets = None
                        self._segment_path = lambda: "ipv4-traffic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Udp.Nodes.Node.Statistics.Ipv4Traffic, ['udp_input_packets', 'udp_checksum_error_packets', 'udp_no_port_packets', 'udp_bad_length_packets', 'udp_output_packets', 'udp_dropped_packets'], name, value)


                class Ipv6Traffic(Entity):
                    """
                    UDP Traffic statistics for IPv6
                    
                    .. attribute:: udp_input_packets
                    
                    	UDP Received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_checksum_error_packets
                    
                    	UDP Checksum Errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_no_port_packets
                    
                    	UDP No Port
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_bad_length_packets
                    
                    	UDP bad length
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_output_packets
                    
                    	UDP Transmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: udp_dropped_packets
                    
                    	UDP drop for other reason
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(Udp.Nodes.Node.Statistics.Ipv6Traffic, self).__init__()

                        self.yang_name = "ipv6-traffic"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('udp_input_packets', (YLeaf(YType.uint32, 'udp-input-packets'), ['int'])),
                            ('udp_checksum_error_packets', (YLeaf(YType.uint32, 'udp-checksum-error-packets'), ['int'])),
                            ('udp_no_port_packets', (YLeaf(YType.uint32, 'udp-no-port-packets'), ['int'])),
                            ('udp_bad_length_packets', (YLeaf(YType.uint32, 'udp-bad-length-packets'), ['int'])),
                            ('udp_output_packets', (YLeaf(YType.uint32, 'udp-output-packets'), ['int'])),
                            ('udp_dropped_packets', (YLeaf(YType.uint32, 'udp-dropped-packets'), ['int'])),
                        ])
                        self.udp_input_packets = None
                        self.udp_checksum_error_packets = None
                        self.udp_no_port_packets = None
                        self.udp_bad_length_packets = None
                        self.udp_output_packets = None
                        self.udp_dropped_packets = None
                        self._segment_path = lambda: "ipv6-traffic"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Udp.Nodes.Node.Statistics.Ipv6Traffic, ['udp_input_packets', 'udp_checksum_error_packets', 'udp_no_port_packets', 'udp_bad_length_packets', 'udp_output_packets', 'udp_dropped_packets'], name, value)

    def clone_ptr(self):
        self._top_entity = Udp()
        return self._top_entity

class UdpConnection(Entity):
    """
    udp connection
    
    .. attribute:: nodes
    
    	List of UDP connections nodes
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2018-03-04'

    def __init__(self):
        super(UdpConnection, self).__init__()
        self._top_entity = None

        self.yang_name = "udp-connection"
        self.yang_parent_name = "Cisco-IOS-XR-ip-udp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", UdpConnection.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = UdpConnection.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-ip-udp-oper:udp-connection"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(UdpConnection, [], name, value)


    class Nodes(Entity):
        """
        List of UDP connections nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2018-03-04'

        def __init__(self):
            super(UdpConnection.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "udp-connection"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", UdpConnection.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-udp-oper:udp-connection/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(UdpConnection.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistics of UDP connections
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics>`
            
            .. attribute:: lpts
            
            	LPTS statistical data
            	**type**\:  :py:class:`Lpts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts>`
            
            .. attribute:: pcb_details
            
            	Detail information for list of UDP connections 
            	**type**\:  :py:class:`PcbDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails>`
            
            .. attribute:: pcb_briefs
            
            	Brief information for list of UDP connections
            	**type**\:  :py:class:`PcbBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2018-03-04'

            def __init__(self):
                super(UdpConnection.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_classes = OrderedDict([("statistics", ("statistics", UdpConnection.Nodes.Node.Statistics)), ("lpts", ("lpts", UdpConnection.Nodes.Node.Lpts)), ("pcb-details", ("pcb_details", UdpConnection.Nodes.Node.PcbDetails)), ("pcb-briefs", ("pcb_briefs", UdpConnection.Nodes.Node.PcbBriefs))])
                self._leafs = OrderedDict([
                    ('node_name', (YLeaf(YType.str, 'node-name'), ['str'])),
                ])
                self.node_name = None

                self.statistics = UdpConnection.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"

                self.lpts = UdpConnection.Nodes.Node.Lpts()
                self.lpts.parent = self
                self._children_name_map["lpts"] = "lpts"

                self.pcb_details = UdpConnection.Nodes.Node.PcbDetails()
                self.pcb_details.parent = self
                self._children_name_map["pcb_details"] = "pcb-details"

                self.pcb_briefs = UdpConnection.Nodes.Node.PcbBriefs()
                self.pcb_briefs.parent = self
                self._children_name_map["pcb_briefs"] = "pcb-briefs"
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-udp-oper:udp-connection/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(UdpConnection.Nodes.Node, ['node_name'], name, value)


            class Statistics(Entity):
                """
                Statistics of UDP connections
                
                .. attribute:: clients
                
                	Table listing clients
                	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients>`
                
                .. attribute:: summary
                
                	Summary statistics across all UDP connections
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Summary>`
                
                .. attribute:: pcb_statistics
                
                	Table listing the UDP connections for which statistics are provided
                	**type**\:  :py:class:`PcbStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2018-03-04'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("clients", ("clients", UdpConnection.Nodes.Node.Statistics.Clients)), ("summary", ("summary", UdpConnection.Nodes.Node.Statistics.Summary)), ("pcb-statistics", ("pcb_statistics", UdpConnection.Nodes.Node.Statistics.PcbStatistics))])
                    self._leafs = OrderedDict()

                    self.clients = UdpConnection.Nodes.Node.Statistics.Clients()
                    self.clients.parent = self
                    self._children_name_map["clients"] = "clients"

                    self.summary = UdpConnection.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"

                    self.pcb_statistics = UdpConnection.Nodes.Node.Statistics.PcbStatistics()
                    self.pcb_statistics.parent = self
                    self._children_name_map["pcb_statistics"] = "pcb-statistics"
                    self._segment_path = lambda: "statistics"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(UdpConnection.Nodes.Node.Statistics, [], name, value)


                class Clients(Entity):
                    """
                    Table listing clients
                    
                    .. attribute:: client
                    
                    	Describing Client ID
                    	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients.Client>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Statistics.Clients, self).__init__()

                        self.yang_name = "clients"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("client", ("client", UdpConnection.Nodes.Node.Statistics.Clients.Client))])
                        self._leafs = OrderedDict()

                        self.client = YList(self)
                        self._segment_path = lambda: "clients"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(UdpConnection.Nodes.Node.Statistics.Clients, [], name, value)


                    class Client(Entity):
                        """
                        Describing Client ID
                        
                        .. attribute:: client_id  (key)
                        
                        	Displaying client's aggregated statistics
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: client_jid
                        
                        	Job ID of the transport client
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: client_name
                        
                        	Transport client name
                        	**type**\: str
                        
                        	**length:** 0..21
                        
                        .. attribute:: ipv4_received_packets
                        
                        	Total IPv4 packets received from client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_sent_packets
                        
                        	Total IPv4 packets sent to client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv6_received_packets
                        
                        	Total IPv6 packets received from app
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv6_sent_packets
                        
                        	Total IPv6 packets sent to app
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2018-03-04'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.Statistics.Clients.Client, self).__init__()

                            self.yang_name = "client"
                            self.yang_parent_name = "clients"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['client_id']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                                ('client_jid', (YLeaf(YType.int32, 'client-jid'), ['int'])),
                                ('client_name', (YLeaf(YType.str, 'client-name'), ['str'])),
                                ('ipv4_received_packets', (YLeaf(YType.uint32, 'ipv4-received-packets'), ['int'])),
                                ('ipv4_sent_packets', (YLeaf(YType.uint32, 'ipv4-sent-packets'), ['int'])),
                                ('ipv6_received_packets', (YLeaf(YType.uint32, 'ipv6-received-packets'), ['int'])),
                                ('ipv6_sent_packets', (YLeaf(YType.uint32, 'ipv6-sent-packets'), ['int'])),
                            ])
                            self.client_id = None
                            self.client_jid = None
                            self.client_name = None
                            self.ipv4_received_packets = None
                            self.ipv4_sent_packets = None
                            self.ipv6_received_packets = None
                            self.ipv6_sent_packets = None
                            self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(UdpConnection.Nodes.Node.Statistics.Clients.Client, ['client_id', 'client_jid', 'client_name', 'ipv4_received_packets', 'ipv4_sent_packets', 'ipv6_received_packets', 'ipv6_sent_packets'], name, value)


                class Summary(Entity):
                    """
                    Summary statistics across all UDP connections
                    
                    .. attribute:: received_total_packets
                    
                    	Total packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_no_port_packets
                    
                    	Packets received when no wild listener
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_bad_checksum_packets
                    
                    	Packets received has bad checksum
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_too_short_packets
                    
                    	Packets received is too short
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_drop_packets
                    
                    	Packets dropped for other reasons
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_total_packets
                    
                    	Total packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sent_error_packets
                    
                    	Total send erorr packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: forward_broadcast_packets
                    
                    	Total forwarding broadcast packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cloned_packets
                    
                    	Total cloned packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: failed_clone_packets
                    
                    	Total failed cloned packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Statistics.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('received_total_packets', (YLeaf(YType.uint32, 'received-total-packets'), ['int'])),
                            ('received_no_port_packets', (YLeaf(YType.uint32, 'received-no-port-packets'), ['int'])),
                            ('received_bad_checksum_packets', (YLeaf(YType.uint32, 'received-bad-checksum-packets'), ['int'])),
                            ('received_too_short_packets', (YLeaf(YType.uint32, 'received-too-short-packets'), ['int'])),
                            ('received_drop_packets', (YLeaf(YType.uint32, 'received-drop-packets'), ['int'])),
                            ('sent_total_packets', (YLeaf(YType.uint32, 'sent-total-packets'), ['int'])),
                            ('sent_error_packets', (YLeaf(YType.uint32, 'sent-error-packets'), ['int'])),
                            ('forward_broadcast_packets', (YLeaf(YType.uint32, 'forward-broadcast-packets'), ['int'])),
                            ('cloned_packets', (YLeaf(YType.uint32, 'cloned-packets'), ['int'])),
                            ('failed_clone_packets', (YLeaf(YType.uint32, 'failed-clone-packets'), ['int'])),
                        ])
                        self.received_total_packets = None
                        self.received_no_port_packets = None
                        self.received_bad_checksum_packets = None
                        self.received_too_short_packets = None
                        self.received_drop_packets = None
                        self.sent_total_packets = None
                        self.sent_error_packets = None
                        self.forward_broadcast_packets = None
                        self.cloned_packets = None
                        self.failed_clone_packets = None
                        self._segment_path = lambda: "summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(UdpConnection.Nodes.Node.Statistics.Summary, ['received_total_packets', 'received_no_port_packets', 'received_bad_checksum_packets', 'received_too_short_packets', 'received_drop_packets', 'sent_total_packets', 'sent_error_packets', 'forward_broadcast_packets', 'cloned_packets', 'failed_clone_packets'], name, value)


                class PcbStatistics(Entity):
                    """
                    Table listing the UDP connections for which
                    statistics are provided
                    
                    .. attribute:: pcb_statistic
                    
                    	Satistics associated with a particular PCB
                    	**type**\: list of  		 :py:class:`PcbStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Statistics.PcbStatistics, self).__init__()

                        self.yang_name = "pcb-statistics"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("pcb-statistic", ("pcb_statistic", UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic))])
                        self._leafs = OrderedDict()

                        self.pcb_statistic = YList(self)
                        self._segment_path = lambda: "pcb-statistics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(UdpConnection.Nodes.Node.Statistics.PcbStatistics, [], name, value)


                    class PcbStatistic(Entity):
                        """
                        Satistics associated with a particular PCB
                        
                        .. attribute:: pcb_address  (key)
                        
                        	Protocol Control Block address
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: send
                        
                        	UDP send statistics
                        	**type**\:  :py:class:`Send <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send>`
                        
                        .. attribute:: receive
                        
                        	UDP receive statistics
                        	**type**\:  :py:class:`Receive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive>`
                        
                        .. attribute:: vrf_id
                        
                        	VRF ID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_paw_socket
                        
                        	True if paw socket
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2018-03-04'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic, self).__init__()

                            self.yang_name = "pcb-statistic"
                            self.yang_parent_name = "pcb-statistics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['pcb_address']
                            self._child_classes = OrderedDict([("send", ("send", UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send)), ("receive", ("receive", UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive))])
                            self._leafs = OrderedDict([
                                ('pcb_address', (YLeaf(YType.str, 'pcb-address'), ['str'])),
                                ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                                ('is_paw_socket', (YLeaf(YType.boolean, 'is-paw-socket'), ['bool'])),
                            ])
                            self.pcb_address = None
                            self.vrf_id = None
                            self.is_paw_socket = None

                            self.send = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send()
                            self.send.parent = self
                            self._children_name_map["send"] = "send"

                            self.receive = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive()
                            self.receive.parent = self
                            self._children_name_map["receive"] = "receive"
                            self._segment_path = lambda: "pcb-statistic" + "[pcb-address='" + str(self.pcb_address) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic, ['pcb_address', 'vrf_id', 'is_paw_socket'], name, value)


                        class Send(Entity):
                            """
                            UDP send statistics
                            
                            .. attribute:: received_application_bytes
                            
                            	Bytes received from application
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            	**units**\: byte
                            
                            .. attribute:: received_xipc_pulses
                            
                            	XIPC pulses received from application
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_network_packets
                            
                            	Packets sent to network (v4/v6 IO)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_net_io_packets
                            
                            	Packets sent to network (NetIO)
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: failed_queued_network_packets
                            
                            	Packets failed getting queued to network (v4/v6 IO)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: failed_queued_net_io_packets
                            
                            	Packets failed getting queued to network (NetIO)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2018-03-04'

                            def __init__(self):
                                super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send, self).__init__()

                                self.yang_name = "send"
                                self.yang_parent_name = "pcb-statistic"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_application_bytes', (YLeaf(YType.uint64, 'received-application-bytes'), ['int'])),
                                    ('received_xipc_pulses', (YLeaf(YType.uint64, 'received-xipc-pulses'), ['int'])),
                                    ('sent_network_packets', (YLeaf(YType.uint64, 'sent-network-packets'), ['int'])),
                                    ('sent_net_io_packets', (YLeaf(YType.uint64, 'sent-net-io-packets'), ['int'])),
                                    ('failed_queued_network_packets', (YLeaf(YType.uint32, 'failed-queued-network-packets'), ['int'])),
                                    ('failed_queued_net_io_packets', (YLeaf(YType.uint32, 'failed-queued-net-io-packets'), ['int'])),
                                ])
                                self.received_application_bytes = None
                                self.received_xipc_pulses = None
                                self.sent_network_packets = None
                                self.sent_net_io_packets = None
                                self.failed_queued_network_packets = None
                                self.failed_queued_net_io_packets = None
                                self._segment_path = lambda: "send"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send, ['received_application_bytes', 'received_xipc_pulses', 'sent_network_packets', 'sent_net_io_packets', 'failed_queued_network_packets', 'failed_queued_net_io_packets'], name, value)


                        class Receive(Entity):
                            """
                            UDP receive statistics
                            
                            .. attribute:: received_network_packets
                            
                            	Packets received from network
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: failed_queued_application_packets
                            
                            	Packets failed queued to application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: queued_application_packets
                            
                            	Packets queued to application
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: failed_queued_application_socket_packets
                            
                            	Packet that couldn't be queued to application.on socket
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: queued_application_socket_packets
                            
                            	Packets queued to application on socket
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2018-03-04'

                            def __init__(self):
                                super(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive, self).__init__()

                                self.yang_name = "receive"
                                self.yang_parent_name = "pcb-statistic"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('received_network_packets', (YLeaf(YType.uint64, 'received-network-packets'), ['int'])),
                                    ('failed_queued_application_packets', (YLeaf(YType.uint32, 'failed-queued-application-packets'), ['int'])),
                                    ('queued_application_packets', (YLeaf(YType.uint64, 'queued-application-packets'), ['int'])),
                                    ('failed_queued_application_socket_packets', (YLeaf(YType.uint32, 'failed-queued-application-socket-packets'), ['int'])),
                                    ('queued_application_socket_packets', (YLeaf(YType.uint64, 'queued-application-socket-packets'), ['int'])),
                                ])
                                self.received_network_packets = None
                                self.failed_queued_application_packets = None
                                self.queued_application_packets = None
                                self.failed_queued_application_socket_packets = None
                                self.queued_application_socket_packets = None
                                self._segment_path = lambda: "receive"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive, ['received_network_packets', 'failed_queued_application_packets', 'queued_application_packets', 'failed_queued_application_socket_packets', 'queued_application_socket_packets'], name, value)


            class Lpts(Entity):
                """
                LPTS statistical data
                
                .. attribute:: queries
                
                	List of query options
                	**type**\:  :py:class:`Queries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2018-03-04'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.Lpts, self).__init__()

                    self.yang_name = "lpts"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("queries", ("queries", UdpConnection.Nodes.Node.Lpts.Queries))])
                    self._leafs = OrderedDict()

                    self.queries = UdpConnection.Nodes.Node.Lpts.Queries()
                    self.queries.parent = self
                    self._children_name_map["queries"] = "queries"
                    self._segment_path = lambda: "lpts"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(UdpConnection.Nodes.Node.Lpts, [], name, value)


                class Queries(Entity):
                    """
                    List of query options
                    
                    .. attribute:: query
                    
                    	Query option
                    	**type**\: list of  		 :py:class:`Query <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.Lpts.Queries, self).__init__()

                        self.yang_name = "queries"
                        self.yang_parent_name = "lpts"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("query", ("query", UdpConnection.Nodes.Node.Lpts.Queries.Query))])
                        self._leafs = OrderedDict()

                        self.query = YList(self)
                        self._segment_path = lambda: "queries"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries, [], name, value)


                    class Query(Entity):
                        """
                        Query option
                        
                        .. attribute:: query_name  (key)
                        
                        	Query option
                        	**type**\:  :py:class:`LptsPcbQuery <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.LptsPcbQuery>`
                        
                        .. attribute:: pcbs
                        
                        	List of PCBs
                        	**type**\:  :py:class:`Pcbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs>`
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2018-03-04'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query, self).__init__()

                            self.yang_name = "query"
                            self.yang_parent_name = "queries"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['query_name']
                            self._child_classes = OrderedDict([("pcbs", ("pcbs", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs))])
                            self._leafs = OrderedDict([
                                ('query_name', (YLeaf(YType.enumeration, 'query-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'LptsPcbQuery', '')])),
                            ])
                            self.query_name = None

                            self.pcbs = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs()
                            self.pcbs.parent = self
                            self._children_name_map["pcbs"] = "pcbs"
                            self._segment_path = lambda: "query" + "[query-name='" + str(self.query_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query, ['query_name'], name, value)


                        class Pcbs(Entity):
                            """
                            List of PCBs
                            
                            .. attribute:: pcb
                            
                            	A PCB information
                            	**type**\: list of  		 :py:class:`Pcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb>`
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2018-03-04'

                            def __init__(self):
                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs, self).__init__()

                                self.yang_name = "pcbs"
                                self.yang_parent_name = "query"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("pcb", ("pcb", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb))])
                                self._leafs = OrderedDict()

                                self.pcb = YList(self)
                                self._segment_path = lambda: "pcbs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs, [], name, value)


                            class Pcb(Entity):
                                """
                                A PCB information
                                
                                .. attribute:: pcb_address  (key)
                                
                                	PCB address
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: local_address
                                
                                	Local IP address
                                	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress>`
                                
                                .. attribute:: foreign_address
                                
                                	Remote IP address
                                	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress>`
                                
                                .. attribute:: common
                                
                                	Common PCB information
                                	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common>`
                                
                                .. attribute:: l4_protocol
                                
                                	Layer 4 protocol
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: local_port
                                
                                	Local port
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                .. attribute:: foreign_port
                                
                                	Remote port
                                	**type**\: int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ip-udp-oper'
                                _revision = '2018-03-04'

                                def __init__(self):
                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb, self).__init__()

                                    self.yang_name = "pcb"
                                    self.yang_parent_name = "pcbs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['pcb_address']
                                    self._child_classes = OrderedDict([("local-address", ("local_address", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress)), ("foreign-address", ("foreign_address", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress)), ("common", ("common", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common))])
                                    self._leafs = OrderedDict([
                                        ('pcb_address', (YLeaf(YType.uint32, 'pcb-address'), ['int'])),
                                        ('l4_protocol', (YLeaf(YType.uint32, 'l4-protocol'), ['int'])),
                                        ('local_port', (YLeaf(YType.uint16, 'local-port'), ['int'])),
                                        ('foreign_port', (YLeaf(YType.uint16, 'foreign-port'), ['int'])),
                                    ])
                                    self.pcb_address = None
                                    self.l4_protocol = None
                                    self.local_port = None
                                    self.foreign_port = None

                                    self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress()
                                    self.local_address.parent = self
                                    self._children_name_map["local_address"] = "local-address"

                                    self.foreign_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress()
                                    self.foreign_address.parent = self
                                    self._children_name_map["foreign_address"] = "foreign-address"

                                    self.common = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common()
                                    self.common.parent = self
                                    self._children_name_map["common"] = "common"
                                    self._segment_path = lambda: "pcb" + "[pcb-address='" + str(self.pcb_address) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb, ['pcb_address', 'l4_protocol', 'local_port', 'foreign_port'], name, value)


                                class LocalAddress(Entity):
                                    """
                                    Local IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2018-03-04'

                                    def __init__(self):
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress, self).__init__()

                                        self.yang_name = "local-address"
                                        self.yang_parent_name = "pcb"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.af_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "local-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                                class ForeignAddress(Entity):
                                    """
                                    Remote IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                    
                                    .. attribute:: ipv4_address
                                    
                                    	IPv4 address
                                    	**type**\: str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    .. attribute:: ipv6_address
                                    
                                    	IPv6 address
                                    	**type**\: str
                                    
                                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2018-03-04'

                                    def __init__(self):
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress, self).__init__()

                                        self.yang_name = "foreign-address"
                                        self.yang_parent_name = "pcb"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily', '')])),
                                            ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                            ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ])
                                        self.af_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None
                                        self._segment_path = lambda: "foreign-address"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                                class Common(Entity):
                                    """
                                    Common PCB information
                                    
                                    .. attribute:: lpts_pcb
                                    
                                    	LPTS PCB information
                                    	**type**\:  :py:class:`LptsPcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb>`
                                    
                                    .. attribute:: af_name
                                    
                                    	Address Family
                                    	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2018-03-04'

                                    def __init__(self):
                                        super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common, self).__init__()

                                        self.yang_name = "common"
                                        self.yang_parent_name = "pcb"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("lpts-pcb", ("lpts_pcb", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb))])
                                        self._leafs = OrderedDict([
                                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily', '')])),
                                        ])
                                        self.af_name = None

                                        self.lpts_pcb = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb()
                                        self.lpts_pcb.parent = self
                                        self._children_name_map["lpts_pcb"] = "lpts-pcb"
                                        self._segment_path = lambda: "common"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common, ['af_name'], name, value)


                                    class LptsPcb(Entity):
                                        """
                                        LPTS PCB information
                                        
                                        .. attribute:: options
                                        
                                        	Receive options
                                        	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options>`
                                        
                                        .. attribute:: lpts_flags
                                        
                                        	LPTS flags
                                        	**type**\:  :py:class:`LptsFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags>`
                                        
                                        .. attribute:: accept_mask
                                        
                                        	AcceptMask
                                        	**type**\:  :py:class:`AcceptMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask>`
                                        
                                        .. attribute:: ttl
                                        
                                        	Minimum TTL
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: flow_types_info
                                        
                                        	flow information
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: filter
                                        
                                        	Interface Filters
                                        	**type**\: list of  		 :py:class:`Filter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter>`
                                        
                                        

                                        """

                                        _prefix = 'ip-udp-oper'
                                        _revision = '2018-03-04'

                                        def __init__(self):
                                            super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb, self).__init__()

                                            self.yang_name = "lpts-pcb"
                                            self.yang_parent_name = "common"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("options", ("options", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options)), ("lpts-flags", ("lpts_flags", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags)), ("accept-mask", ("accept_mask", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask)), ("filter", ("filter", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter))])
                                            self._leafs = OrderedDict([
                                                ('ttl', (YLeaf(YType.uint8, 'ttl'), ['int'])),
                                                ('flow_types_info', (YLeaf(YType.uint32, 'flow-types-info'), ['int'])),
                                            ])
                                            self.ttl = None
                                            self.flow_types_info = None

                                            self.options = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options()
                                            self.options.parent = self
                                            self._children_name_map["options"] = "options"

                                            self.lpts_flags = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags()
                                            self.lpts_flags.parent = self
                                            self._children_name_map["lpts_flags"] = "lpts-flags"

                                            self.accept_mask = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask()
                                            self.accept_mask.parent = self
                                            self._children_name_map["accept_mask"] = "accept-mask"

                                            self.filter = YList(self)
                                            self._segment_path = lambda: "lpts-pcb"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb, ['ttl', 'flow_types_info'], name, value)


                                        class Options(Entity):
                                            """
                                            Receive options
                                            
                                            .. attribute:: is_receive_filter
                                            
                                            	Receive filter enabled
                                            	**type**\: bool
                                            
                                            .. attribute:: is_ip_sla
                                            
                                            	IP SLA
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2018-03-04'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options, self).__init__()

                                                self.yang_name = "options"
                                                self.yang_parent_name = "lpts-pcb"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('is_receive_filter', (YLeaf(YType.boolean, 'is-receive-filter'), ['bool'])),
                                                    ('is_ip_sla', (YLeaf(YType.boolean, 'is-ip-sla'), ['bool'])),
                                                ])
                                                self.is_receive_filter = None
                                                self.is_ip_sla = None
                                                self._segment_path = lambda: "options"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options, ['is_receive_filter', 'is_ip_sla'], name, value)


                                        class LptsFlags(Entity):
                                            """
                                            LPTS flags
                                            
                                            .. attribute:: is_pcb_bound
                                            
                                            	PCB bound
                                            	**type**\: bool
                                            
                                            .. attribute:: is_local_address_ignore
                                            
                                            	Sent drop packets
                                            	**type**\: bool
                                            
                                            .. attribute:: is_ignore_vrf_filter
                                            
                                            	Ignore VRF Filter
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2018-03-04'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags, self).__init__()

                                                self.yang_name = "lpts-flags"
                                                self.yang_parent_name = "lpts-pcb"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('is_pcb_bound', (YLeaf(YType.boolean, 'is-pcb-bound'), ['bool'])),
                                                    ('is_local_address_ignore', (YLeaf(YType.boolean, 'is-local-address-ignore'), ['bool'])),
                                                    ('is_ignore_vrf_filter', (YLeaf(YType.boolean, 'is-ignore-vrf-filter'), ['bool'])),
                                                ])
                                                self.is_pcb_bound = None
                                                self.is_local_address_ignore = None
                                                self.is_ignore_vrf_filter = None
                                                self._segment_path = lambda: "lpts-flags"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags, ['is_pcb_bound', 'is_local_address_ignore', 'is_ignore_vrf_filter'], name, value)


                                        class AcceptMask(Entity):
                                            """
                                            AcceptMask
                                            
                                            .. attribute:: is_interface
                                            
                                            	Set interface
                                            	**type**\: bool
                                            
                                            .. attribute:: is_packet_type
                                            
                                            	Set packet type
                                            	**type**\: bool
                                            
                                            .. attribute:: is_remote_address
                                            
                                            	Set Remote address
                                            	**type**\: bool
                                            
                                            .. attribute:: is_remote_port
                                            
                                            	Set Remote Port
                                            	**type**\: bool
                                            
                                            .. attribute:: is_local_address
                                            
                                            	Set Local Address
                                            	**type**\: bool
                                            
                                            .. attribute:: is_local_port
                                            
                                            	Set Local Port
                                            	**type**\: bool
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2018-03-04'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask, self).__init__()

                                                self.yang_name = "accept-mask"
                                                self.yang_parent_name = "lpts-pcb"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('is_interface', (YLeaf(YType.boolean, 'is-interface'), ['bool'])),
                                                    ('is_packet_type', (YLeaf(YType.boolean, 'is-packet-type'), ['bool'])),
                                                    ('is_remote_address', (YLeaf(YType.boolean, 'is-remote-address'), ['bool'])),
                                                    ('is_remote_port', (YLeaf(YType.boolean, 'is-remote-port'), ['bool'])),
                                                    ('is_local_address', (YLeaf(YType.boolean, 'is-local-address'), ['bool'])),
                                                    ('is_local_port', (YLeaf(YType.boolean, 'is-local-port'), ['bool'])),
                                                ])
                                                self.is_interface = None
                                                self.is_packet_type = None
                                                self.is_remote_address = None
                                                self.is_remote_port = None
                                                self.is_local_address = None
                                                self.is_local_port = None
                                                self._segment_path = lambda: "accept-mask"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask, ['is_interface', 'is_packet_type', 'is_remote_address', 'is_remote_port', 'is_local_address', 'is_local_port'], name, value)


                                        class Filter(Entity):
                                            """
                                            Interface Filters
                                            
                                            .. attribute:: packet_type
                                            
                                            	Protocol\-specific packet type
                                            	**type**\:  :py:class:`PacketType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType>`
                                            
                                            .. attribute:: remote_address
                                            
                                            	Remote address
                                            	**type**\:  :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress>`
                                            
                                            .. attribute:: local_address
                                            
                                            	Local address
                                            	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress>`
                                            
                                            .. attribute:: interface_name
                                            
                                            	Interface name
                                            	**type**\: str
                                            
                                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                            
                                            .. attribute:: remote_length
                                            
                                            	Remote address length
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: local_length
                                            
                                            	Local address length
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: receive_remote_port
                                            
                                            	Receive Remote port
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: receive_local_port
                                            
                                            	Receive Local port
                                            	**type**\: int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: priority
                                            
                                            	Priority
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: ttl
                                            
                                            	Minimum TTL
                                            	**type**\: int
                                            
                                            	**range:** 0..255
                                            
                                            .. attribute:: flow_types_info
                                            
                                            	flow information
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ip-udp-oper'
                                            _revision = '2018-03-04'

                                            def __init__(self):
                                                super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter, self).__init__()

                                                self.yang_name = "filter"
                                                self.yang_parent_name = "lpts-pcb"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("packet-type", ("packet_type", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType)), ("remote-address", ("remote_address", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress)), ("local-address", ("local_address", UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress))])
                                                self._leafs = OrderedDict([
                                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                                    ('remote_length', (YLeaf(YType.uint16, 'remote-length'), ['int'])),
                                                    ('local_length', (YLeaf(YType.uint16, 'local-length'), ['int'])),
                                                    ('receive_remote_port', (YLeaf(YType.uint16, 'receive-remote-port'), ['int'])),
                                                    ('receive_local_port', (YLeaf(YType.uint16, 'receive-local-port'), ['int'])),
                                                    ('priority', (YLeaf(YType.uint8, 'priority'), ['int'])),
                                                    ('ttl', (YLeaf(YType.uint8, 'ttl'), ['int'])),
                                                    ('flow_types_info', (YLeaf(YType.uint32, 'flow-types-info'), ['int'])),
                                                ])
                                                self.interface_name = None
                                                self.remote_length = None
                                                self.local_length = None
                                                self.receive_remote_port = None
                                                self.receive_local_port = None
                                                self.priority = None
                                                self.ttl = None
                                                self.flow_types_info = None

                                                self.packet_type = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType()
                                                self.packet_type.parent = self
                                                self._children_name_map["packet_type"] = "packet-type"

                                                self.remote_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress()
                                                self.remote_address.parent = self
                                                self._children_name_map["remote_address"] = "remote-address"

                                                self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress()
                                                self.local_address.parent = self
                                                self._children_name_map["local_address"] = "local-address"
                                                self._segment_path = lambda: "filter"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter, ['interface_name', 'remote_length', 'local_length', 'receive_remote_port', 'receive_local_port', 'priority', 'ttl', 'flow_types_info'], name, value)


                                            class PacketType(Entity):
                                                """
                                                Protocol\-specific packet type
                                                
                                                .. attribute:: type
                                                
                                                	Type
                                                	**type**\:  :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Packet>`
                                                
                                                .. attribute:: icmp_message_type
                                                
                                                	ICMP message type
                                                	**type**\:  :py:class:`MessageTypeIcmp_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmp_>`
                                                
                                                .. attribute:: icm_pv6_message_type
                                                
                                                	ICMPv6 message type
                                                	**type**\:  :py:class:`MessageTypeIcmpv6_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmpv6_>`
                                                
                                                .. attribute:: igmp_message_type
                                                
                                                	IGMP message type
                                                	**type**\:  :py:class:`MessageTypeIgmp_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIgmp_>`
                                                
                                                .. attribute:: message_id
                                                
                                                	Message type in number
                                                	**type**\: int
                                                
                                                	**range:** 0..4294967295
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2018-03-04'

                                                def __init__(self):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType, self).__init__()

                                                    self.yang_name = "packet-type"
                                                    self.yang_parent_name = "filter"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'Packet', '')])),
                                                        ('icmp_message_type', (YLeaf(YType.enumeration, 'icmp-message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIcmp_', '')])),
                                                        ('icm_pv6_message_type', (YLeaf(YType.enumeration, 'icm-pv6-message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIcmpv6_', '')])),
                                                        ('igmp_message_type', (YLeaf(YType.enumeration, 'igmp-message-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'MessageTypeIgmp_', '')])),
                                                        ('message_id', (YLeaf(YType.uint32, 'message-id'), ['int'])),
                                                    ])
                                                    self.type = None
                                                    self.icmp_message_type = None
                                                    self.icm_pv6_message_type = None
                                                    self.igmp_message_type = None
                                                    self.message_id = None
                                                    self._segment_path = lambda: "packet-type"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType, ['type', 'icmp_message_type', 'icm_pv6_message_type', 'igmp_message_type', 'message_id'], name, value)


                                            class RemoteAddress(Entity):
                                                """
                                                Remote address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2018-03-04'

                                                def __init__(self):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress, self).__init__()

                                                    self.yang_name = "remote-address"
                                                    self.yang_parent_name = "filter"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily', '')])),
                                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                    ])
                                                    self.af_name = None
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None
                                                    self._segment_path = lambda: "remote-address"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                                            class LocalAddress(Entity):
                                                """
                                                Local address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamily>`
                                                
                                                .. attribute:: ipv4_address
                                                
                                                	IPv4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: ipv6_address
                                                
                                                	IPv6 address
                                                	**type**\: str
                                                
                                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2018-03-04'

                                                def __init__(self):
                                                    super(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress, self).__init__()

                                                    self.yang_name = "local-address"
                                                    self.yang_parent_name = "filter"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'AddrFamily', '')])),
                                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                                    ])
                                                    self.af_name = None
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None
                                                    self._segment_path = lambda: "local-address"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


            class PcbDetails(Entity):
                """
                Detail information for list of UDP connections
                .
                
                .. attribute:: pcb_detail
                
                	Detail information about a UDP connection
                	**type**\: list of  		 :py:class:`PcbDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2018-03-04'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.PcbDetails, self).__init__()

                    self.yang_name = "pcb-details"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pcb-detail", ("pcb_detail", UdpConnection.Nodes.Node.PcbDetails.PcbDetail))])
                    self._leafs = OrderedDict()

                    self.pcb_detail = YList(self)
                    self._segment_path = lambda: "pcb-details"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(UdpConnection.Nodes.Node.PcbDetails, [], name, value)


                class PcbDetail(Entity):
                    """
                    Detail information about a UDP connection
                    
                    .. attribute:: pcb_address  (key)
                    
                    	Protocol Control Block address
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress>`
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\:  :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                    
                    .. attribute:: local_process_id
                    
                    	ID of local process
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: receive_queue
                    
                    	Receive queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_queue
                    
                    	Send queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_id
                    
                    	VRF ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail, self).__init__()

                        self.yang_name = "pcb-detail"
                        self.yang_parent_name = "pcb-details"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pcb_address']
                        self._child_classes = OrderedDict([("local-address", ("local_address", UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress)), ("foreign-address", ("foreign_address", UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress))])
                        self._leafs = OrderedDict([
                            ('pcb_address', (YLeaf(YType.str, 'pcb-address'), ['str'])),
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily', '')])),
                            ('local_process_id', (YLeaf(YType.uint32, 'local-process-id'), ['int'])),
                            ('local_port', (YLeaf(YType.uint16, 'local-port'), ['int'])),
                            ('foreign_port', (YLeaf(YType.uint16, 'foreign-port'), ['int'])),
                            ('receive_queue', (YLeaf(YType.uint32, 'receive-queue'), ['int'])),
                            ('send_queue', (YLeaf(YType.uint32, 'send-queue'), ['int'])),
                            ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                        ])
                        self.pcb_address = None
                        self.af_name = None
                        self.local_process_id = None
                        self.local_port = None
                        self.foreign_port = None
                        self.receive_queue = None
                        self.send_queue = None
                        self.vrf_id = None

                        self.local_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"

                        self.foreign_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress()
                        self.foreign_address.parent = self
                        self._children_name_map["foreign_address"] = "foreign-address"
                        self._segment_path = lambda: "pcb-detail" + "[pcb-address='" + str(self.pcb_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(UdpConnection.Nodes.Node.PcbDetails.PcbDetail, ['pcb_address', 'af_name', 'local_process_id', 'local_port', 'foreign_port', 'receive_queue', 'send_queue', 'vrf_id'], name, value)


                    class LocalAddress(Entity):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2018-03-04'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "pcb-detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "local-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                    class ForeignAddress(Entity):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2018-03-04'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress, self).__init__()

                            self.yang_name = "foreign-address"
                            self.yang_parent_name = "pcb-detail"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "foreign-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


            class PcbBriefs(Entity):
                """
                Brief information for list of UDP connections.
                
                .. attribute:: pcb_brief
                
                	Brief information about a UDP connection
                	**type**\: list of  		 :py:class:`PcbBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2018-03-04'

                def __init__(self):
                    super(UdpConnection.Nodes.Node.PcbBriefs, self).__init__()

                    self.yang_name = "pcb-briefs"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("pcb-brief", ("pcb_brief", UdpConnection.Nodes.Node.PcbBriefs.PcbBrief))])
                    self._leafs = OrderedDict()

                    self.pcb_brief = YList(self)
                    self._segment_path = lambda: "pcb-briefs"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(UdpConnection.Nodes.Node.PcbBriefs, [], name, value)


                class PcbBrief(Entity):
                    """
                    Brief information about a UDP connection
                    
                    .. attribute:: pcb_address  (key)
                    
                    	Protocol Control Block address
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress>`
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\:  :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                    
                    .. attribute:: local_port
                    
                    	Local port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: receive_queue
                    
                    	Receive queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_queue
                    
                    	Send queue count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_id
                    
                    	VRF ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2018-03-04'

                    def __init__(self):
                        super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief, self).__init__()

                        self.yang_name = "pcb-brief"
                        self.yang_parent_name = "pcb-briefs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pcb_address']
                        self._child_classes = OrderedDict([("local-address", ("local_address", UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress)), ("foreign-address", ("foreign_address", UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress))])
                        self._leafs = OrderedDict([
                            ('pcb_address', (YLeaf(YType.str, 'pcb-address'), ['str'])),
                            ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily', '')])),
                            ('local_port', (YLeaf(YType.uint16, 'local-port'), ['int'])),
                            ('foreign_port', (YLeaf(YType.uint16, 'foreign-port'), ['int'])),
                            ('receive_queue', (YLeaf(YType.uint32, 'receive-queue'), ['int'])),
                            ('send_queue', (YLeaf(YType.uint32, 'send-queue'), ['int'])),
                            ('vrf_id', (YLeaf(YType.uint32, 'vrf-id'), ['int'])),
                        ])
                        self.pcb_address = None
                        self.af_name = None
                        self.local_port = None
                        self.foreign_port = None
                        self.receive_queue = None
                        self.send_queue = None
                        self.vrf_id = None

                        self.local_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"

                        self.foreign_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress()
                        self.foreign_address.parent = self
                        self._children_name_map["foreign_address"] = "foreign-address"
                        self._segment_path = lambda: "pcb-brief" + "[pcb-address='" + str(self.pcb_address) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief, ['pcb_address', 'af_name', 'local_port', 'foreign_port', 'receive_queue', 'send_queue', 'vrf_id'], name, value)


                    class LocalAddress(Entity):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2018-03-04'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "pcb-brief"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "local-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                    class ForeignAddress(Entity):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`UdpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2018-03-04'

                        def __init__(self):
                            super(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress, self).__init__()

                            self.yang_name = "foreign-address"
                            self.yang_parent_name = "pcb-brief"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', (YLeaf(YType.enumeration, 'af-name'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper', 'UdpAddressFamily', '')])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "foreign-address"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)

    def clone_ptr(self):
        self._top_entity = UdpConnection()
        return self._top_entity

