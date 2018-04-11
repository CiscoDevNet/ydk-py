""" Cisco_IOS_XR_ip_tcp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-tcp package operational data.

This module contains definitions
for the following management objects\:
  tcp\-connection\: TCP connection operational data
  tcp\: tcp
  tcp\-nsr\: tcp nsr

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
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

    .. data:: internetwork = 2

    	Internetwork: UDP, TCP, etc.

    .. data:: ip_version6 = 10

    	IP version 6

    """

    internetwork = Enum.YLeaf(2, "internetwork")

    ip_version6 = Enum.YLeaf(10, "ip-version6")


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


class NsrDownReason(Enum):
    """
    NsrDownReason (Enum Class)

    NSR\-Down Reasons

    .. data:: none = 0

    	None, i.e. NSR was never up

    .. data:: init_sync_aborted = 1

    	Initial sync was aborted

    .. data:: client_disabled = 2

    	Disabled by Active APP

    .. data:: client_disconnect = 3

    	Standby APP disconnected

    .. data:: tcp_disconnect = 4

    	Standby TCP disconnected

    .. data:: failover = 5

    	RP/DRP Failover occurred

    .. data:: nsr_clear = 6

    	Clear nsr command

    .. data:: internal_error = 7

    	Internal error occurred

    .. data:: retransmit_threshold_exceed = 8

    	Retransmission threshold exceededprobably

    	becauseS-TCP was not healthy

    .. data:: init_sync_failure_thresh_exceeded = 9

    	Init-sync repeat failures have exceeded

    	threshold

    .. data:: audit_timeout = 10

    	Audit operation timed out

    .. data:: audit_failed = 11

    	Audit operation failed

    .. data:: standby_sscb_deleted = 12

    	Standby SSCB deleted

    .. data:: standby_session_close = 13

    	Session was closed on standby

    .. data:: standby_rxpath_frozen = 14

    	RX-Path was frozen on standby

    .. data:: partner_deleted = 15

    	Partner was deleted from set

    """

    none = Enum.YLeaf(0, "none")

    init_sync_aborted = Enum.YLeaf(1, "init-sync-aborted")

    client_disabled = Enum.YLeaf(2, "client-disabled")

    client_disconnect = Enum.YLeaf(3, "client-disconnect")

    tcp_disconnect = Enum.YLeaf(4, "tcp-disconnect")

    failover = Enum.YLeaf(5, "failover")

    nsr_clear = Enum.YLeaf(6, "nsr-clear")

    internal_error = Enum.YLeaf(7, "internal-error")

    retransmit_threshold_exceed = Enum.YLeaf(8, "retransmit-threshold-exceed")

    init_sync_failure_thresh_exceeded = Enum.YLeaf(9, "init-sync-failure-thresh-exceeded")

    audit_timeout = Enum.YLeaf(10, "audit-timeout")

    audit_failed = Enum.YLeaf(11, "audit-failed")

    standby_sscb_deleted = Enum.YLeaf(12, "standby-sscb-deleted")

    standby_session_close = Enum.YLeaf(13, "standby-session-close")

    standby_rxpath_frozen = Enum.YLeaf(14, "standby-rxpath-frozen")

    partner_deleted = Enum.YLeaf(15, "partner-deleted")


class NsrStatus(Enum):
    """
    NsrStatus (Enum Class)

    NSR Stream Status

    .. data:: down = 0

    	NSR Stream Down

    .. data:: up = 1

    	NSR Stream Up

    .. data:: na = 2

    	NSR Stream Not applicable

    """

    down = Enum.YLeaf(0, "down")

    up = Enum.YLeaf(1, "up")

    na = Enum.YLeaf(2, "na")


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


class PakPrio(Enum):
    """
    PakPrio (Enum Class)

    Packet Priority Types

    .. data:: unspecified_packet = 0

    	Unspecified

    .. data:: normal_packet = 1

    	Normal: all traffic routed via this router,

    	Telnet/FTP traffic generated from within this

    	router

    .. data:: medium_packet = 2

    	Medium: Packets with low drop probability e.g.

    	Routing updates & requests

    .. data:: high_packet = 3

    	High: Packets with very low drop probability

    	and normal delivery e.g. L3 Keepalives like

    	OSPF/ISIS Hellos

    .. data:: crucial_packet = 4

    	Crucial: Packets with very low drop probability

    	and expedited delivery e.g L2 keepalives, HDLC

    	Keepalives

    """

    unspecified_packet = Enum.YLeaf(0, "unspecified-packet")

    normal_packet = Enum.YLeaf(1, "normal-packet")

    medium_packet = Enum.YLeaf(2, "medium-packet")

    high_packet = Enum.YLeaf(3, "high-packet")

    crucial_packet = Enum.YLeaf(4, "crucial-packet")


class Show(Enum):
    """
    Show (Enum Class)

    Show

    .. data:: all = 0

    	To dispay all

    .. data:: static_policy = 1

    	To display static policy

    .. data:: interface_filter = 2

    	To display interface filter

    .. data:: packet_filter = 3

    	To display packet type filter

    """

    all = Enum.YLeaf(0, "all")

    static_policy = Enum.YLeaf(1, "static-policy")

    interface_filter = Enum.YLeaf(2, "interface-filter")

    packet_filter = Enum.YLeaf(3, "packet-filter")


class TcpAddressFamily(Enum):
    """
    TcpAddressFamily (Enum Class)

    Address Family Type

    .. data:: ipv4 = 2

    	IPv4

    .. data:: ipv6 = 10

    	IPv6

    """

    ipv4 = Enum.YLeaf(2, "ipv4")

    ipv6 = Enum.YLeaf(10, "ipv6")


class TcpConnState(Enum):
    """
    TcpConnState (Enum Class)

    TCP Connection State

    .. data:: closed = 0

    	Closed

    .. data:: listen = 1

    	Listen

    .. data:: syn_sent = 2

    	Syn sent

    .. data:: syn_received = 3

    	Syn received

    .. data:: established = 4

    	Established

    .. data:: close_wait = 5

    	Close wait

    .. data:: fin_wait1 = 6

    	FIN Wait1

    .. data:: closing = 7

    	Closing

    .. data:: last_ack = 8

    	Last ack

    .. data:: fin_wait2 = 9

    	FIN Wait2

    .. data:: time_wait = 10

    	Time wait

    """

    closed = Enum.YLeaf(0, "closed")

    listen = Enum.YLeaf(1, "listen")

    syn_sent = Enum.YLeaf(2, "syn-sent")

    syn_received = Enum.YLeaf(3, "syn-received")

    established = Enum.YLeaf(4, "established")

    close_wait = Enum.YLeaf(5, "close-wait")

    fin_wait1 = Enum.YLeaf(6, "fin-wait1")

    closing = Enum.YLeaf(7, "closing")

    last_ack = Enum.YLeaf(8, "last-ack")

    fin_wait2 = Enum.YLeaf(9, "fin-wait2")

    time_wait = Enum.YLeaf(10, "time-wait")


class TcpTimer(Enum):
    """
    TcpTimer (Enum Class)

    TCP Timer Type

    .. data:: retransmission_timer = 0

    	Retransmission timer

    .. data:: window_probe_timer = 1

    	Send Window Probe timer

    .. data:: timewait_state_timer = 2

    	TIMEWAIT state timer

    .. data:: ack_hold_timer = 3

    	ACK Hold timer

    .. data:: keep_alive_timer = 4

    	Keep Alive timer

    .. data:: pmtu_ager_timer = 5

    	PMTU Ager Timer

    .. data:: retransmission_giveup_timer = 6

    	Retransmission Giveup timer

    .. data:: throttle_timer = 7

    	Throttle (for PAW/xipc) timer

    """

    retransmission_timer = Enum.YLeaf(0, "retransmission-timer")

    window_probe_timer = Enum.YLeaf(1, "window-probe-timer")

    timewait_state_timer = Enum.YLeaf(2, "timewait-state-timer")

    ack_hold_timer = Enum.YLeaf(3, "ack-hold-timer")

    keep_alive_timer = Enum.YLeaf(4, "keep-alive-timer")

    pmtu_ager_timer = Enum.YLeaf(5, "pmtu-ager-timer")

    retransmission_giveup_timer = Enum.YLeaf(6, "retransmission-giveup-timer")

    throttle_timer = Enum.YLeaf(7, "throttle-timer")



class TcpConnection(Entity):
    """
    TCP connection operational data
    
    .. attribute:: nodes
    
    	Table of information about all nodes present on the system
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes>`
    
    

    """

    _prefix = 'ip-tcp-oper'
    _revision = '2018-02-14'

    def __init__(self):
        super(TcpConnection, self).__init__()
        self._top_entity = None

        self.yang_name = "tcp-connection"
        self.yang_parent_name = "Cisco-IOS-XR-ip-tcp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", TcpConnection.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = TcpConnection.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp-connection"


    class Nodes(Entity):
        """
        Table of information about all nodes present on
        the system
        
        .. attribute:: node
        
        	Information about a single node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node>`
        
        

        """

        _prefix = 'ip-tcp-oper'
        _revision = '2018-02-14'

        def __init__(self):
            super(TcpConnection.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "tcp-connection"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", TcpConnection.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp-connection/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TcpConnection.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a single node
            
            .. attribute:: id  (key)
            
            	Describing a location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistics of all TCP connections
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics>`
            
            .. attribute:: extended_information
            
            	Extended Filter related Information
            	**type**\:  :py:class:`ExtendedInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation>`
            
            .. attribute:: detail_informations
            
            	Table listing TCP connections for which detailed information is provided
            	**type**\:  :py:class:`DetailInformations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations>`
            
            .. attribute:: brief_informations
            
            	Table listing connections for which brief information is provided.Note that not all connections are listed in the brief table
            	**type**\:  :py:class:`BriefInformations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.BriefInformations>`
            
            

            """

            _prefix = 'ip-tcp-oper'
            _revision = '2018-02-14'

            def __init__(self):
                super(TcpConnection.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_container_classes = OrderedDict([("statistics", ("statistics", TcpConnection.Nodes.Node.Statistics)), ("extended-information", ("extended_information", TcpConnection.Nodes.Node.ExtendedInformation)), ("detail-informations", ("detail_informations", TcpConnection.Nodes.Node.DetailInformations)), ("brief-informations", ("brief_informations", TcpConnection.Nodes.Node.BriefInformations))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id', YLeaf(YType.str, 'id')),
                ])
                self.id = None

                self.statistics = TcpConnection.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")

                self.extended_information = TcpConnection.Nodes.Node.ExtendedInformation()
                self.extended_information.parent = self
                self._children_name_map["extended_information"] = "extended-information"
                self._children_yang_names.add("extended-information")

                self.detail_informations = TcpConnection.Nodes.Node.DetailInformations()
                self.detail_informations.parent = self
                self._children_name_map["detail_informations"] = "detail-informations"
                self._children_yang_names.add("detail-informations")

                self.brief_informations = TcpConnection.Nodes.Node.BriefInformations()
                self.brief_informations.parent = self
                self._children_name_map["brief_informations"] = "brief-informations"
                self._children_yang_names.add("brief-informations")
                self._segment_path = lambda: "node" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp-connection/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TcpConnection.Nodes.Node, ['id'], name, value)


            class Statistics(Entity):
                """
                Statistics of all TCP connections
                
                .. attribute:: clients
                
                	Table listing clients
                	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Clients>`
                
                .. attribute:: pcbs
                
                	Table listing the TCP connections for which statistics are provided
                	**type**\:  :py:class:`Pcbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs>`
                
                .. attribute:: summary
                
                	Summary statistics across all TCP connections
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Summary>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpConnection.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("clients", ("clients", TcpConnection.Nodes.Node.Statistics.Clients)), ("pcbs", ("pcbs", TcpConnection.Nodes.Node.Statistics.Pcbs)), ("summary", ("summary", TcpConnection.Nodes.Node.Statistics.Summary))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.clients = TcpConnection.Nodes.Node.Statistics.Clients()
                    self.clients.parent = self
                    self._children_name_map["clients"] = "clients"
                    self._children_yang_names.add("clients")

                    self.pcbs = TcpConnection.Nodes.Node.Statistics.Pcbs()
                    self.pcbs.parent = self
                    self._children_name_map["pcbs"] = "pcbs"
                    self._children_yang_names.add("pcbs")

                    self.summary = TcpConnection.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")
                    self._segment_path = lambda: "statistics"


                class Clients(Entity):
                    """
                    Table listing clients
                    
                    .. attribute:: client
                    
                    	Describing Client ID
                    	**type**\: list of  		 :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Clients.Client>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpConnection.Nodes.Node.Statistics.Clients, self).__init__()

                        self.yang_name = "clients"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("client", ("client", TcpConnection.Nodes.Node.Statistics.Clients.Client))])
                        self._leafs = OrderedDict()

                        self.client = YList(self)
                        self._segment_path = lambda: "clients"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Clients, [], name, value)


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

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.Statistics.Clients.Client, self).__init__()

                            self.yang_name = "client"
                            self.yang_parent_name = "clients"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['client_id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('client_id', YLeaf(YType.uint32, 'client-id')),
                                ('client_jid', YLeaf(YType.int32, 'client-jid')),
                                ('client_name', YLeaf(YType.str, 'client-name')),
                                ('ipv4_received_packets', YLeaf(YType.uint32, 'ipv4-received-packets')),
                                ('ipv4_sent_packets', YLeaf(YType.uint32, 'ipv4-sent-packets')),
                                ('ipv6_received_packets', YLeaf(YType.uint32, 'ipv6-received-packets')),
                                ('ipv6_sent_packets', YLeaf(YType.uint32, 'ipv6-sent-packets')),
                            ])
                            self.client_id = None
                            self.client_jid = None
                            self.client_name = None
                            self.ipv4_received_packets = None
                            self.ipv4_sent_packets = None
                            self.ipv6_received_packets = None
                            self.ipv6_sent_packets = None
                            self._segment_path = lambda: "client" + "[client-id='" + str(self.client_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Clients.Client, ['client_id', 'client_jid', 'client_name', 'ipv4_received_packets', 'ipv4_sent_packets', 'ipv6_received_packets', 'ipv6_sent_packets'], name, value)


                class Pcbs(Entity):
                    """
                    Table listing the TCP connections for which
                    statistics are provided
                    
                    .. attribute:: pcb
                    
                    	Protocol Control Block ID
                    	**type**\: list of  		 :py:class:`Pcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpConnection.Nodes.Node.Statistics.Pcbs, self).__init__()

                        self.yang_name = "pcbs"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("pcb", ("pcb", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb))])
                        self._leafs = OrderedDict()

                        self.pcb = YList(self)
                        self._segment_path = lambda: "pcbs"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs, [], name, value)


                    class Pcb(Entity):
                        """
                        Protocol Control Block ID
                        
                        .. attribute:: id  (key)
                        
                        	Displaying statistics associated with a particular PCB
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: read_io_counts
                        
                        	Read  I/O counts
                        	**type**\:  :py:class:`ReadIoCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts>`
                        
                        .. attribute:: write_io_counts
                        
                        	Write I/O counts
                        	**type**\:  :py:class:`WriteIoCounts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts>`
                        
                        .. attribute:: async_session_stats
                        
                        	Statistics of Async TCP Sessions
                        	**type**\:  :py:class:`AsyncSessionStats <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats>`
                        
                        .. attribute:: pcb
                        
                        	PCB Address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: vrf_id
                        
                        	VRF Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_sent
                        
                        	Packets received from application
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: xipc_pulse_received
                        
                        	XIPC pulses received from application
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: segment_instruction_received
                        
                        	Segment Instruction received from partner node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: send_packets_queued
                        
                        	Packets queued to v4/v6 IO
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: send_packets_queued_net_io
                        
                        	Packets queued to NetIO
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: send_queue_failed
                        
                        	Packets failed to be queued to v4/v6 IO
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: send_queue_net_io_failed
                        
                        	Packets failed to be queued to NetIO
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: packets_received
                        
                        	Packets received from network
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: receive_queue_failed
                        
                        	Received packets failed to be queued to application
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: received_packets_queued
                        
                        	Received packets queued to application
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: send_window_shrink_ignored
                        
                        	No. of times send window shrinkage by peer was ignored
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_paw_socket
                        
                        	PAW or non\-PAW socket?
                        	**type**\: bool
                        
                        .. attribute:: read_io_time
                        
                        	Time at which receive buffer was last read from
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: write_io_time
                        
                        	Time at which send buffer was last written to
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb, self).__init__()

                            self.yang_name = "pcb"
                            self.yang_parent_name = "pcbs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([("read-io-counts", ("read_io_counts", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts)), ("write-io-counts", ("write_io_counts", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts)), ("async-session-stats", ("async_session_stats", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('pcb', YLeaf(YType.uint64, 'pcb')),
                                ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                                ('packets_sent', YLeaf(YType.uint64, 'packets-sent')),
                                ('xipc_pulse_received', YLeaf(YType.uint64, 'xipc-pulse-received')),
                                ('segment_instruction_received', YLeaf(YType.uint32, 'segment-instruction-received')),
                                ('send_packets_queued', YLeaf(YType.uint64, 'send-packets-queued')),
                                ('send_packets_queued_net_io', YLeaf(YType.uint64, 'send-packets-queued-net-io')),
                                ('send_queue_failed', YLeaf(YType.uint32, 'send-queue-failed')),
                                ('send_queue_net_io_failed', YLeaf(YType.uint32, 'send-queue-net-io-failed')),
                                ('packets_received', YLeaf(YType.uint64, 'packets-received')),
                                ('receive_queue_failed', YLeaf(YType.uint32, 'receive-queue-failed')),
                                ('received_packets_queued', YLeaf(YType.uint64, 'received-packets-queued')),
                                ('send_window_shrink_ignored', YLeaf(YType.uint32, 'send-window-shrink-ignored')),
                                ('is_paw_socket', YLeaf(YType.boolean, 'is-paw-socket')),
                                ('read_io_time', YLeaf(YType.uint32, 'read-io-time')),
                                ('write_io_time', YLeaf(YType.uint32, 'write-io-time')),
                            ])
                            self.id = None
                            self.pcb = None
                            self.vrf_id = None
                            self.packets_sent = None
                            self.xipc_pulse_received = None
                            self.segment_instruction_received = None
                            self.send_packets_queued = None
                            self.send_packets_queued_net_io = None
                            self.send_queue_failed = None
                            self.send_queue_net_io_failed = None
                            self.packets_received = None
                            self.receive_queue_failed = None
                            self.received_packets_queued = None
                            self.send_window_shrink_ignored = None
                            self.is_paw_socket = None
                            self.read_io_time = None
                            self.write_io_time = None

                            self.read_io_counts = TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts()
                            self.read_io_counts.parent = self
                            self._children_name_map["read_io_counts"] = "read-io-counts"
                            self._children_yang_names.add("read-io-counts")

                            self.write_io_counts = TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts()
                            self.write_io_counts.parent = self
                            self._children_name_map["write_io_counts"] = "write-io-counts"
                            self._children_yang_names.add("write-io-counts")

                            self.async_session_stats = TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats()
                            self.async_session_stats.parent = self
                            self._children_name_map["async_session_stats"] = "async-session-stats"
                            self._children_yang_names.add("async-session-stats")
                            self._segment_path = lambda: "pcb" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb, ['id', 'pcb', 'vrf_id', 'packets_sent', 'xipc_pulse_received', 'segment_instruction_received', 'send_packets_queued', 'send_packets_queued_net_io', 'send_queue_failed', 'send_queue_net_io_failed', 'packets_received', 'receive_queue_failed', 'received_packets_queued', 'send_window_shrink_ignored', 'is_paw_socket', 'read_io_time', 'write_io_time'], name, value)


                        class ReadIoCounts(Entity):
                            """
                            Read  I/O counts
                            
                            .. attribute:: io_count
                            
                            	Number of I/O operations done by application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: arm_count
                            
                            	How many times socket was armed by application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unarm_count
                            
                            	How many times socket was unarmed by application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: autoarm_count
                            
                            	How many times socket was auto\-armed by TCP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts, self).__init__()

                                self.yang_name = "read-io-counts"
                                self.yang_parent_name = "pcb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('io_count', YLeaf(YType.uint32, 'io-count')),
                                    ('arm_count', YLeaf(YType.uint32, 'arm-count')),
                                    ('unarm_count', YLeaf(YType.uint32, 'unarm-count')),
                                    ('autoarm_count', YLeaf(YType.uint32, 'autoarm-count')),
                                ])
                                self.io_count = None
                                self.arm_count = None
                                self.unarm_count = None
                                self.autoarm_count = None
                                self._segment_path = lambda: "read-io-counts"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts, ['io_count', 'arm_count', 'unarm_count', 'autoarm_count'], name, value)


                        class WriteIoCounts(Entity):
                            """
                            Write I/O counts
                            
                            .. attribute:: io_count
                            
                            	Number of I/O operations done by application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: arm_count
                            
                            	How many times socket was armed by application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: unarm_count
                            
                            	How many times socket was unarmed by application
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: autoarm_count
                            
                            	How many times socket was auto\-armed by TCP
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts, self).__init__()

                                self.yang_name = "write-io-counts"
                                self.yang_parent_name = "pcb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('io_count', YLeaf(YType.uint32, 'io-count')),
                                    ('arm_count', YLeaf(YType.uint32, 'arm-count')),
                                    ('unarm_count', YLeaf(YType.uint32, 'unarm-count')),
                                    ('autoarm_count', YLeaf(YType.uint32, 'autoarm-count')),
                                ])
                                self.io_count = None
                                self.arm_count = None
                                self.unarm_count = None
                                self.autoarm_count = None
                                self._segment_path = lambda: "write-io-counts"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts, ['io_count', 'arm_count', 'unarm_count', 'autoarm_count'], name, value)


                        class AsyncSessionStats(Entity):
                            """
                            Statistics of Async TCP Sessions
                            
                            .. attribute:: async_session
                            
                            	Flag of async session
                            	**type**\: bool
                            
                            .. attribute:: data_write_success_num
                            
                            	Number of successful data write to XIPC
                            	**type**\: list of  		 :py:class:`DataWriteSuccessNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteSuccessNum>`
                            
                            .. attribute:: data_read_success_num
                            
                            	Number of successful data read from XIPC
                            	**type**\: list of  		 :py:class:`DataReadSuccessNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadSuccessNum>`
                            
                            .. attribute:: data_write_error_num
                            
                            	Number of failed data write to XIPC
                            	**type**\: list of  		 :py:class:`DataWriteErrorNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteErrorNum>`
                            
                            .. attribute:: data_read_error_num
                            
                            	Number of failed data read from XIPC
                            	**type**\: list of  		 :py:class:`DataReadErrorNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadErrorNum>`
                            
                            .. attribute:: control_write_success_num
                            
                            	Number of successful control write to XIPC
                            	**type**\: list of  		 :py:class:`ControlWriteSuccessNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteSuccessNum>`
                            
                            .. attribute:: control_read_success_num
                            
                            	Number of successful control read to XIPC
                            	**type**\: list of  		 :py:class:`ControlReadSuccessNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadSuccessNum>`
                            
                            .. attribute:: control_write_error_num
                            
                            	Number of failed control write to XIPC
                            	**type**\: list of  		 :py:class:`ControlWriteErrorNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteErrorNum>`
                            
                            .. attribute:: control_read_error_num
                            
                            	Number of failed control read from XIPC
                            	**type**\: list of  		 :py:class:`ControlReadErrorNum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadErrorNum>`
                            
                            .. attribute:: data_write_byte
                            
                            	Number of bytes data has been written
                            	**type**\: list of  		 :py:class:`DataWriteByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteByte>`
                            
                            .. attribute:: data_read_byte
                            
                            	Number of bytes data has been read
                            	**type**\: list of  		 :py:class:`DataReadByte <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadByte>`
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats, self).__init__()

                                self.yang_name = "async-session-stats"
                                self.yang_parent_name = "pcb"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("data-write-success-num", ("data_write_success_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteSuccessNum)), ("data-read-success-num", ("data_read_success_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadSuccessNum)), ("data-write-error-num", ("data_write_error_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteErrorNum)), ("data-read-error-num", ("data_read_error_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadErrorNum)), ("control-write-success-num", ("control_write_success_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteSuccessNum)), ("control-read-success-num", ("control_read_success_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadSuccessNum)), ("control-write-error-num", ("control_write_error_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteErrorNum)), ("control-read-error-num", ("control_read_error_num", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadErrorNum)), ("data-write-byte", ("data_write_byte", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteByte)), ("data-read-byte", ("data_read_byte", TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadByte))])
                                self._leafs = OrderedDict([
                                    ('async_session', YLeaf(YType.boolean, 'async-session')),
                                ])
                                self.async_session = None

                                self.data_write_success_num = YList(self)
                                self.data_read_success_num = YList(self)
                                self.data_write_error_num = YList(self)
                                self.data_read_error_num = YList(self)
                                self.control_write_success_num = YList(self)
                                self.control_read_success_num = YList(self)
                                self.control_write_error_num = YList(self)
                                self.control_read_error_num = YList(self)
                                self.data_write_byte = YList(self)
                                self.data_read_byte = YList(self)
                                self._segment_path = lambda: "async-session-stats"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats, ['async_session'], name, value)


                            class DataWriteSuccessNum(Entity):
                                """
                                Number of successful data write to XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteSuccessNum, self).__init__()

                                    self.yang_name = "data-write-success-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "data-write-success-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteSuccessNum, ['entry'], name, value)


                            class DataReadSuccessNum(Entity):
                                """
                                Number of successful data read from XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadSuccessNum, self).__init__()

                                    self.yang_name = "data-read-success-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "data-read-success-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadSuccessNum, ['entry'], name, value)


                            class DataWriteErrorNum(Entity):
                                """
                                Number of failed data write to XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteErrorNum, self).__init__()

                                    self.yang_name = "data-write-error-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "data-write-error-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteErrorNum, ['entry'], name, value)


                            class DataReadErrorNum(Entity):
                                """
                                Number of failed data read from XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadErrorNum, self).__init__()

                                    self.yang_name = "data-read-error-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "data-read-error-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadErrorNum, ['entry'], name, value)


                            class ControlWriteSuccessNum(Entity):
                                """
                                Number of successful control write to XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteSuccessNum, self).__init__()

                                    self.yang_name = "control-write-success-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "control-write-success-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteSuccessNum, ['entry'], name, value)


                            class ControlReadSuccessNum(Entity):
                                """
                                Number of successful control read to XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadSuccessNum, self).__init__()

                                    self.yang_name = "control-read-success-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "control-read-success-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadSuccessNum, ['entry'], name, value)


                            class ControlWriteErrorNum(Entity):
                                """
                                Number of failed control write to XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteErrorNum, self).__init__()

                                    self.yang_name = "control-write-error-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "control-write-error-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlWriteErrorNum, ['entry'], name, value)


                            class ControlReadErrorNum(Entity):
                                """
                                Number of failed control read from XIPC
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadErrorNum, self).__init__()

                                    self.yang_name = "control-read-error-num"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint32, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "control-read-error-num"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.ControlReadErrorNum, ['entry'], name, value)


                            class DataWriteByte(Entity):
                                """
                                Number of bytes data has been written
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteByte, self).__init__()

                                    self.yang_name = "data-write-byte"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint64, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "data-write-byte"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataWriteByte, ['entry'], name, value)


                            class DataReadByte(Entity):
                                """
                                Number of bytes data has been read
                                
                                .. attribute:: entry
                                
                                	
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: byte
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadByte, self).__init__()

                                    self.yang_name = "data-read-byte"
                                    self.yang_parent_name = "async-session-stats"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('entry', YLeaf(YType.uint64, 'entry')),
                                    ])
                                    self.entry = None
                                    self._segment_path = lambda: "data-read-byte"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats.DataReadByte, ['entry'], name, value)


                class Summary(Entity):
                    """
                    Summary statistics across all TCP connections
                    
                    .. attribute:: syn_cache_count
                    
                    	Current number of SYN cache entries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_open_sockets
                    
                    	Number of Open sockets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_pakets_sent
                    
                    	Total packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_packets_dropped
                    
                    	Total transmit packets dropped due to general failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_auth_packets_dropped
                    
                    	Total transmit packets dropped due to authentication failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_pakets_sent
                    
                    	Data packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_bytes_sent
                    
                    	Data bytes sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: packets_retransmitted
                    
                    	Data packets retransmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_retransmitted
                    
                    	Data bytes retransmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: ack_only_packets_sent
                    
                    	Ack only packets sent (incl. delay)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: delay_ack_packets_sent
                    
                    	Delay ack packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: urgent_only_packets_sent
                    
                    	Urgent only packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: window_probe_packets_sent
                    
                    	Window probe packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: window_update_packets_sent
                    
                    	Window update packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: control_packets_sent
                    
                    	Control (SYN\|FIN\|RST) packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rst_packets_sent
                    
                    	RST packets sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_packets_received
                    
                    	Total packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_packets_dropped
                    
                    	Received packets dropped due to general failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: synacl_match_pkts_dropped
                    
                    	Received packets dropped due to ACL DENY on SYN pkts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_packets_dropped_stale_c_hdr
                    
                    	Received packets dropped due to stale cached header
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: received_auth_packets_dropped
                    
                    	Received packets dropped due to authentication failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ack_packets_received
                    
                    	Ack packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ackbytes_received
                    
                    	Bytes acked by ack packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: duplicated_ack_packets_received
                    
                    	Duplicate ack packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ack_packets_for_unsent_received
                    
                    	Ack packets for unsent data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_packets_received_in_sequence
                    
                    	Data packets received in sequence
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: data_bytes_received_in_sequence
                    
                    	Data bytes received in sequence
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: duplicate_packets_received
                    
                    	Duplicate packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_bytes_received
                    
                    	Duplicate bytes received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: partial_duplicate_ack_received
                    
                    	Packets with partial dup data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: partial_duplicate_bytes_received
                    
                    	Bytes with partial dup data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: out_of_order_packets_received
                    
                    	Out\-of\-order packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_of_order_bytes_received
                    
                    	Out\-of\-order bytes received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: after_window_packets_received
                    
                    	After\-window packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: after_window_bytes_received
                    
                    	After\-window bytes received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: window_probe_packets_received
                    
                    	Window probe packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: window_update_packets_received
                    
                    	Window update packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packets_received_after_close_packet
                    
                    	Packets received after close
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bad_checksum_packets_received
                    
                    	Packets received with bad checksum
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: too_short_packets_received
                    
                    	Packets received with too short size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: malformed_packets_received
                    
                    	Packets received with malformed header
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_port_packets_received
                    
                    	Packets rcceived with no wild listener
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connections_requested
                    
                    	Connection requests sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connections_accepted
                    
                    	Connection requests accepted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connections_established
                    
                    	Connections established
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connections_forcibly_closed
                    
                    	Connections forcibly closed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connections_closed
                    
                    	connections closed (incl. drops)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connections_dropped
                    
                    	connections dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: embryonic_connection_dropped
                    
                    	Embryonic connections dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connections_failed
                    
                    	Connections failed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: established_connections_reset
                    
                    	Established connections reset
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: retransmit_timeouts
                    
                    	Retransmit timeouts (incl. data packets)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: retransmit_dropped
                    
                    	Connection drops during retransmit timeouts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_timeouts
                    
                    	Keepalive timeouts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_dropped
                    
                    	Connection drops due to keepalive timeouts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_probes
                    
                    	Keepalive probes sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: paws_dropped
                    
                    	Segments dropped due to PAWS
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: persist_dropped
                    
                    	Segments dropped due to window probe
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: try_lock_dropped
                    
                    	Segments dropped due to trylock fail
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_rate_limited
                    
                    	Connections rate\-limited
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_added
                    
                    	SYN Cache entries added
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_completed
                    
                    	SYN Cache connections completed
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_timed_out
                    
                    	SYN Cache entries timed out
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_overflow
                    
                    	SYN Cache entries dropped due to overflow
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_reset
                    
                    	SYN Cache entries dropped due to RST
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_unreach
                    
                    	SYN Cache entries dropped due to ICMP unreach
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_bucket_oflow
                    
                    	SYN Cache entries dropped due to bucket overflow
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_aborted
                    
                    	SYN Cache entries aborted (no mem)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_duplicate_sy_ns
                    
                    	SYN Cache duplicate SYNs received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_cache_dropped
                    
                    	SYN Cache entries dropped (no route/mem)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: pulse_errors
                    
                    	Punt (down to ip) failures
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_layer_packets
                    
                    	Packets owned by the socket layer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: reassembly_packets
                    
                    	Packets owned by TCP reassembly
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: recovered_packets
                    
                    	Packets freed after starvation
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_failures
                    
                    	Packet allocation errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mss_up
                    
                    	Number of times MSS was increased
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mss_down
                    
                    	Number of times MSS was decreased
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: truncated_write_iov
                    
                    	Segments truncated due to insufficient Write I/O vectors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: no_throttle
                    
                    	Number of times throttle mode was off
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: low_water_mark_throttle
                    
                    	Number of times low water mark throttle was on
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: high_water_mark_throttle
                    
                    	Number of times high water mark throttle was on
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stalled_timer_tickle_count
                    
                    	Number of times a stalled tcp timer was tickled
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: stalled_timer_tickle_time
                    
                    	Last timestamp when a stalled tcp timer was tickled
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iq_sock_writes
                    
                    	Number of write attempts from socket\-lib into an IQ
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iq_sock_retries
                    
                    	Number of retried write attempts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iq_sock_aborts
                    
                    	Number of aborted socket\-lib writes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iq_ingress_drops
                    
                    	Number of total ingress dropped packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: total_i_qs
                    
                    	Number of TCP internal queues in use
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: iqs_total_ingpacket
                    
                    	Total Number of Ingress packets on TCP iqs
                    	**type**\: list of  		 :py:class:`IqsTotalIngpacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalIngpacket>`
                    
                    .. attribute:: iqs_total_egpacket
                    
                    	Total Number of Egress packets on TCP iqs
                    	**type**\: list of  		 :py:class:`IqsTotalEgpacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalEgpacket>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpConnection.Nodes.Node.Statistics.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("iqs-total-ingpacket", ("iqs_total_ingpacket", TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalIngpacket)), ("iqs-total-egpacket", ("iqs_total_egpacket", TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalEgpacket))])
                        self._leafs = OrderedDict([
                            ('syn_cache_count', YLeaf(YType.uint32, 'syn-cache-count')),
                            ('num_open_sockets', YLeaf(YType.uint32, 'num-open-sockets')),
                            ('total_pakets_sent', YLeaf(YType.uint32, 'total-pakets-sent')),
                            ('send_packets_dropped', YLeaf(YType.uint32, 'send-packets-dropped')),
                            ('send_auth_packets_dropped', YLeaf(YType.uint32, 'send-auth-packets-dropped')),
                            ('data_pakets_sent', YLeaf(YType.uint32, 'data-pakets-sent')),
                            ('data_bytes_sent', YLeaf(YType.uint32, 'data-bytes-sent')),
                            ('packets_retransmitted', YLeaf(YType.uint32, 'packets-retransmitted')),
                            ('bytes_retransmitted', YLeaf(YType.uint32, 'bytes-retransmitted')),
                            ('ack_only_packets_sent', YLeaf(YType.uint32, 'ack-only-packets-sent')),
                            ('delay_ack_packets_sent', YLeaf(YType.uint32, 'delay-ack-packets-sent')),
                            ('urgent_only_packets_sent', YLeaf(YType.uint32, 'urgent-only-packets-sent')),
                            ('window_probe_packets_sent', YLeaf(YType.uint32, 'window-probe-packets-sent')),
                            ('window_update_packets_sent', YLeaf(YType.uint32, 'window-update-packets-sent')),
                            ('control_packets_sent', YLeaf(YType.uint32, 'control-packets-sent')),
                            ('rst_packets_sent', YLeaf(YType.uint32, 'rst-packets-sent')),
                            ('total_packets_received', YLeaf(YType.uint32, 'total-packets-received')),
                            ('received_packets_dropped', YLeaf(YType.uint32, 'received-packets-dropped')),
                            ('synacl_match_pkts_dropped', YLeaf(YType.uint32, 'synacl-match-pkts-dropped')),
                            ('received_packets_dropped_stale_c_hdr', YLeaf(YType.uint32, 'received-packets-dropped-stale-c-hdr')),
                            ('received_auth_packets_dropped', YLeaf(YType.uint32, 'received-auth-packets-dropped')),
                            ('ack_packets_received', YLeaf(YType.uint32, 'ack-packets-received')),
                            ('ackbytes_received', YLeaf(YType.uint32, 'ackbytes-received')),
                            ('duplicated_ack_packets_received', YLeaf(YType.uint32, 'duplicated-ack-packets-received')),
                            ('ack_packets_for_unsent_received', YLeaf(YType.uint32, 'ack-packets-for-unsent-received')),
                            ('data_packets_received_in_sequence', YLeaf(YType.uint32, 'data-packets-received-in-sequence')),
                            ('data_bytes_received_in_sequence', YLeaf(YType.uint32, 'data-bytes-received-in-sequence')),
                            ('duplicate_packets_received', YLeaf(YType.uint32, 'duplicate-packets-received')),
                            ('duplicate_bytes_received', YLeaf(YType.uint32, 'duplicate-bytes-received')),
                            ('partial_duplicate_ack_received', YLeaf(YType.uint32, 'partial-duplicate-ack-received')),
                            ('partial_duplicate_bytes_received', YLeaf(YType.uint32, 'partial-duplicate-bytes-received')),
                            ('out_of_order_packets_received', YLeaf(YType.uint32, 'out-of-order-packets-received')),
                            ('out_of_order_bytes_received', YLeaf(YType.uint32, 'out-of-order-bytes-received')),
                            ('after_window_packets_received', YLeaf(YType.uint32, 'after-window-packets-received')),
                            ('after_window_bytes_received', YLeaf(YType.uint32, 'after-window-bytes-received')),
                            ('window_probe_packets_received', YLeaf(YType.uint32, 'window-probe-packets-received')),
                            ('window_update_packets_received', YLeaf(YType.uint32, 'window-update-packets-received')),
                            ('packets_received_after_close_packet', YLeaf(YType.uint32, 'packets-received-after-close-packet')),
                            ('bad_checksum_packets_received', YLeaf(YType.uint32, 'bad-checksum-packets-received')),
                            ('too_short_packets_received', YLeaf(YType.uint32, 'too-short-packets-received')),
                            ('malformed_packets_received', YLeaf(YType.uint32, 'malformed-packets-received')),
                            ('no_port_packets_received', YLeaf(YType.uint32, 'no-port-packets-received')),
                            ('connections_requested', YLeaf(YType.uint32, 'connections-requested')),
                            ('connections_accepted', YLeaf(YType.uint32, 'connections-accepted')),
                            ('connections_established', YLeaf(YType.uint32, 'connections-established')),
                            ('connections_forcibly_closed', YLeaf(YType.uint32, 'connections-forcibly-closed')),
                            ('connections_closed', YLeaf(YType.uint32, 'connections-closed')),
                            ('connections_dropped', YLeaf(YType.uint32, 'connections-dropped')),
                            ('embryonic_connection_dropped', YLeaf(YType.uint32, 'embryonic-connection-dropped')),
                            ('connections_failed', YLeaf(YType.uint32, 'connections-failed')),
                            ('established_connections_reset', YLeaf(YType.uint32, 'established-connections-reset')),
                            ('retransmit_timeouts', YLeaf(YType.uint32, 'retransmit-timeouts')),
                            ('retransmit_dropped', YLeaf(YType.uint32, 'retransmit-dropped')),
                            ('keep_alive_timeouts', YLeaf(YType.uint32, 'keep-alive-timeouts')),
                            ('keep_alive_dropped', YLeaf(YType.uint32, 'keep-alive-dropped')),
                            ('keep_alive_probes', YLeaf(YType.uint32, 'keep-alive-probes')),
                            ('paws_dropped', YLeaf(YType.uint32, 'paws-dropped')),
                            ('persist_dropped', YLeaf(YType.uint32, 'persist-dropped')),
                            ('try_lock_dropped', YLeaf(YType.uint32, 'try-lock-dropped')),
                            ('connection_rate_limited', YLeaf(YType.uint32, 'connection-rate-limited')),
                            ('syn_cache_added', YLeaf(YType.uint32, 'syn-cache-added')),
                            ('syn_cache_completed', YLeaf(YType.uint32, 'syn-cache-completed')),
                            ('syn_cache_timed_out', YLeaf(YType.uint32, 'syn-cache-timed-out')),
                            ('syn_cache_overflow', YLeaf(YType.uint32, 'syn-cache-overflow')),
                            ('syn_cache_reset', YLeaf(YType.uint32, 'syn-cache-reset')),
                            ('syn_cache_unreach', YLeaf(YType.uint32, 'syn-cache-unreach')),
                            ('syn_cache_bucket_oflow', YLeaf(YType.uint32, 'syn-cache-bucket-oflow')),
                            ('syn_cache_aborted', YLeaf(YType.uint32, 'syn-cache-aborted')),
                            ('syn_cache_duplicate_sy_ns', YLeaf(YType.uint32, 'syn-cache-duplicate-sy-ns')),
                            ('syn_cache_dropped', YLeaf(YType.uint32, 'syn-cache-dropped')),
                            ('pulse_errors', YLeaf(YType.uint32, 'pulse-errors')),
                            ('socket_layer_packets', YLeaf(YType.uint32, 'socket-layer-packets')),
                            ('reassembly_packets', YLeaf(YType.uint32, 'reassembly-packets')),
                            ('recovered_packets', YLeaf(YType.uint32, 'recovered-packets')),
                            ('packet_failures', YLeaf(YType.uint32, 'packet-failures')),
                            ('mss_up', YLeaf(YType.uint32, 'mss-up')),
                            ('mss_down', YLeaf(YType.uint32, 'mss-down')),
                            ('truncated_write_iov', YLeaf(YType.uint32, 'truncated-write-iov')),
                            ('no_throttle', YLeaf(YType.uint32, 'no-throttle')),
                            ('low_water_mark_throttle', YLeaf(YType.uint32, 'low-water-mark-throttle')),
                            ('high_water_mark_throttle', YLeaf(YType.uint32, 'high-water-mark-throttle')),
                            ('stalled_timer_tickle_count', YLeaf(YType.uint32, 'stalled-timer-tickle-count')),
                            ('stalled_timer_tickle_time', YLeaf(YType.uint32, 'stalled-timer-tickle-time')),
                            ('iq_sock_writes', YLeaf(YType.uint32, 'iq-sock-writes')),
                            ('iq_sock_retries', YLeaf(YType.uint32, 'iq-sock-retries')),
                            ('iq_sock_aborts', YLeaf(YType.uint32, 'iq-sock-aborts')),
                            ('iq_ingress_drops', YLeaf(YType.uint32, 'iq-ingress-drops')),
                            ('total_i_qs', YLeaf(YType.uint32, 'total-i-qs')),
                        ])
                        self.syn_cache_count = None
                        self.num_open_sockets = None
                        self.total_pakets_sent = None
                        self.send_packets_dropped = None
                        self.send_auth_packets_dropped = None
                        self.data_pakets_sent = None
                        self.data_bytes_sent = None
                        self.packets_retransmitted = None
                        self.bytes_retransmitted = None
                        self.ack_only_packets_sent = None
                        self.delay_ack_packets_sent = None
                        self.urgent_only_packets_sent = None
                        self.window_probe_packets_sent = None
                        self.window_update_packets_sent = None
                        self.control_packets_sent = None
                        self.rst_packets_sent = None
                        self.total_packets_received = None
                        self.received_packets_dropped = None
                        self.synacl_match_pkts_dropped = None
                        self.received_packets_dropped_stale_c_hdr = None
                        self.received_auth_packets_dropped = None
                        self.ack_packets_received = None
                        self.ackbytes_received = None
                        self.duplicated_ack_packets_received = None
                        self.ack_packets_for_unsent_received = None
                        self.data_packets_received_in_sequence = None
                        self.data_bytes_received_in_sequence = None
                        self.duplicate_packets_received = None
                        self.duplicate_bytes_received = None
                        self.partial_duplicate_ack_received = None
                        self.partial_duplicate_bytes_received = None
                        self.out_of_order_packets_received = None
                        self.out_of_order_bytes_received = None
                        self.after_window_packets_received = None
                        self.after_window_bytes_received = None
                        self.window_probe_packets_received = None
                        self.window_update_packets_received = None
                        self.packets_received_after_close_packet = None
                        self.bad_checksum_packets_received = None
                        self.too_short_packets_received = None
                        self.malformed_packets_received = None
                        self.no_port_packets_received = None
                        self.connections_requested = None
                        self.connections_accepted = None
                        self.connections_established = None
                        self.connections_forcibly_closed = None
                        self.connections_closed = None
                        self.connections_dropped = None
                        self.embryonic_connection_dropped = None
                        self.connections_failed = None
                        self.established_connections_reset = None
                        self.retransmit_timeouts = None
                        self.retransmit_dropped = None
                        self.keep_alive_timeouts = None
                        self.keep_alive_dropped = None
                        self.keep_alive_probes = None
                        self.paws_dropped = None
                        self.persist_dropped = None
                        self.try_lock_dropped = None
                        self.connection_rate_limited = None
                        self.syn_cache_added = None
                        self.syn_cache_completed = None
                        self.syn_cache_timed_out = None
                        self.syn_cache_overflow = None
                        self.syn_cache_reset = None
                        self.syn_cache_unreach = None
                        self.syn_cache_bucket_oflow = None
                        self.syn_cache_aborted = None
                        self.syn_cache_duplicate_sy_ns = None
                        self.syn_cache_dropped = None
                        self.pulse_errors = None
                        self.socket_layer_packets = None
                        self.reassembly_packets = None
                        self.recovered_packets = None
                        self.packet_failures = None
                        self.mss_up = None
                        self.mss_down = None
                        self.truncated_write_iov = None
                        self.no_throttle = None
                        self.low_water_mark_throttle = None
                        self.high_water_mark_throttle = None
                        self.stalled_timer_tickle_count = None
                        self.stalled_timer_tickle_time = None
                        self.iq_sock_writes = None
                        self.iq_sock_retries = None
                        self.iq_sock_aborts = None
                        self.iq_ingress_drops = None
                        self.total_i_qs = None

                        self.iqs_total_ingpacket = YList(self)
                        self.iqs_total_egpacket = YList(self)
                        self._segment_path = lambda: "summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Summary, ['syn_cache_count', 'num_open_sockets', 'total_pakets_sent', 'send_packets_dropped', 'send_auth_packets_dropped', 'data_pakets_sent', 'data_bytes_sent', 'packets_retransmitted', 'bytes_retransmitted', 'ack_only_packets_sent', 'delay_ack_packets_sent', 'urgent_only_packets_sent', 'window_probe_packets_sent', 'window_update_packets_sent', 'control_packets_sent', 'rst_packets_sent', 'total_packets_received', 'received_packets_dropped', 'synacl_match_pkts_dropped', 'received_packets_dropped_stale_c_hdr', 'received_auth_packets_dropped', 'ack_packets_received', 'ackbytes_received', 'duplicated_ack_packets_received', 'ack_packets_for_unsent_received', 'data_packets_received_in_sequence', 'data_bytes_received_in_sequence', 'duplicate_packets_received', 'duplicate_bytes_received', 'partial_duplicate_ack_received', 'partial_duplicate_bytes_received', 'out_of_order_packets_received', 'out_of_order_bytes_received', 'after_window_packets_received', 'after_window_bytes_received', 'window_probe_packets_received', 'window_update_packets_received', 'packets_received_after_close_packet', 'bad_checksum_packets_received', 'too_short_packets_received', 'malformed_packets_received', 'no_port_packets_received', 'connections_requested', 'connections_accepted', 'connections_established', 'connections_forcibly_closed', 'connections_closed', 'connections_dropped', 'embryonic_connection_dropped', 'connections_failed', 'established_connections_reset', 'retransmit_timeouts', 'retransmit_dropped', 'keep_alive_timeouts', 'keep_alive_dropped', 'keep_alive_probes', 'paws_dropped', 'persist_dropped', 'try_lock_dropped', 'connection_rate_limited', 'syn_cache_added', 'syn_cache_completed', 'syn_cache_timed_out', 'syn_cache_overflow', 'syn_cache_reset', 'syn_cache_unreach', 'syn_cache_bucket_oflow', 'syn_cache_aborted', 'syn_cache_duplicate_sy_ns', 'syn_cache_dropped', 'pulse_errors', 'socket_layer_packets', 'reassembly_packets', 'recovered_packets', 'packet_failures', 'mss_up', 'mss_down', 'truncated_write_iov', 'no_throttle', 'low_water_mark_throttle', 'high_water_mark_throttle', 'stalled_timer_tickle_count', 'stalled_timer_tickle_time', 'iq_sock_writes', 'iq_sock_retries', 'iq_sock_aborts', 'iq_ingress_drops', 'total_i_qs'], name, value)


                    class IqsTotalIngpacket(Entity):
                        """
                        Total Number of Ingress packets on TCP iqs
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalIngpacket, self).__init__()

                            self.yang_name = "iqs-total-ingpacket"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "iqs-total-ingpacket"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalIngpacket, ['entry'], name, value)


                    class IqsTotalEgpacket(Entity):
                        """
                        Total Number of Egress packets on TCP iqs
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalEgpacket, self).__init__()

                            self.yang_name = "iqs-total-egpacket"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "iqs-total-egpacket"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.Statistics.Summary.IqsTotalEgpacket, ['entry'], name, value)


            class ExtendedInformation(Entity):
                """
                Extended Filter related Information
                
                .. attribute:: display_types
                
                	Table listing display types
                	**type**\:  :py:class:`DisplayTypes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpConnection.Nodes.Node.ExtendedInformation, self).__init__()

                    self.yang_name = "extended-information"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("display-types", ("display_types", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.display_types = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes()
                    self.display_types.parent = self
                    self._children_name_map["display_types"] = "display-types"
                    self._children_yang_names.add("display-types")
                    self._segment_path = lambda: "extended-information"


                class DisplayTypes(Entity):
                    """
                    Table listing display types
                    
                    .. attribute:: display_type
                    
                    	Describing particular display type
                    	**type**\: list of  		 :py:class:`DisplayType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes, self).__init__()

                        self.yang_name = "display-types"
                        self.yang_parent_name = "extended-information"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("display-type", ("display_type", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType))])
                        self._leafs = OrderedDict()

                        self.display_type = YList(self)
                        self._segment_path = lambda: "display-types"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes, [], name, value)


                    class DisplayType(Entity):
                        """
                        Describing particular display type
                        
                        .. attribute:: disp_type  (key)
                        
                        	Specifying display type
                        	**type**\:  :py:class:`Show <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.Show>`
                        
                        .. attribute:: connection_id
                        
                        	Describing connection ID
                        	**type**\: list of  		 :py:class:`ConnectionId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType, self).__init__()

                            self.yang_name = "display-type"
                            self.yang_parent_name = "display-types"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['disp_type']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("connection-id", ("connection_id", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId))])
                            self._leafs = OrderedDict([
                                ('disp_type', YLeaf(YType.enumeration, 'disp-type')),
                            ])
                            self.disp_type = None

                            self.connection_id = YList(self)
                            self._segment_path = lambda: "display-type" + "[disp-type='" + str(self.disp_type) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType, ['disp_type'], name, value)


                        class ConnectionId(Entity):
                            """
                            Describing connection ID
                            
                            .. attribute:: pcb_id  (key)
                            
                            	Displaying inforamtion based on selected display type associatedwith a particular PCB
                            	**type**\: str
                            
                            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                            
                            .. attribute:: local_address
                            
                            	Local IP address
                            	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress>`
                            
                            .. attribute:: foreign_address
                            
                            	Remote IP address
                            	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress>`
                            
                            .. attribute:: common
                            
                            	Common PCB information
                            	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common>`
                            
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

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId, self).__init__()

                                self.yang_name = "connection-id"
                                self.yang_parent_name = "display-type"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['pcb_id']
                                self._child_container_classes = OrderedDict([("local-address", ("local_address", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress)), ("foreign-address", ("foreign_address", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress)), ("common", ("common", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('pcb_id', YLeaf(YType.str, 'pcb-id')),
                                    ('l4_protocol', YLeaf(YType.uint32, 'l4-protocol')),
                                    ('local_port', YLeaf(YType.uint16, 'local-port')),
                                    ('foreign_port', YLeaf(YType.uint16, 'foreign-port')),
                                ])
                                self.pcb_id = None
                                self.l4_protocol = None
                                self.local_port = None
                                self.foreign_port = None

                                self.local_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress()
                                self.local_address.parent = self
                                self._children_name_map["local_address"] = "local-address"
                                self._children_yang_names.add("local-address")

                                self.foreign_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress()
                                self.foreign_address.parent = self
                                self._children_name_map["foreign_address"] = "foreign-address"
                                self._children_yang_names.add("foreign-address")

                                self.common = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common()
                                self.common.parent = self
                                self._children_name_map["common"] = "common"
                                self._children_yang_names.add("common")
                                self._segment_path = lambda: "connection-id" + "[pcb-id='" + str(self.pcb_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId, ['pcb_id', 'l4_protocol', 'local_port', 'foreign_port'], name, value)


                            class LocalAddress(Entity):
                                """
                                Local IP address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress, self).__init__()

                                    self.yang_name = "local-address"
                                    self.yang_parent_name = "connection-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                                    ])
                                    self.af_name = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "local-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                            class ForeignAddress(Entity):
                                """
                                Remote IP address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress, self).__init__()

                                    self.yang_name = "foreign-address"
                                    self.yang_parent_name = "connection-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                        ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                        ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                                    ])
                                    self.af_name = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None
                                    self._segment_path = lambda: "foreign-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                            class Common(Entity):
                                """
                                Common PCB information
                                
                                .. attribute:: lpts_pcb
                                
                                	LPTS PCB information
                                	**type**\:  :py:class:`LptsPcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb>`
                                
                                .. attribute:: af_name
                                
                                	Address Family
                                	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2018-02-14'

                                def __init__(self):
                                    super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common, self).__init__()

                                    self.yang_name = "common"
                                    self.yang_parent_name = "connection-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([("lpts-pcb", ("lpts_pcb", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb))])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                    ])
                                    self.af_name = None

                                    self.lpts_pcb = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb()
                                    self.lpts_pcb.parent = self
                                    self._children_name_map["lpts_pcb"] = "lpts-pcb"
                                    self._children_yang_names.add("lpts-pcb")
                                    self._segment_path = lambda: "common"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common, ['af_name'], name, value)


                                class LptsPcb(Entity):
                                    """
                                    LPTS PCB information
                                    
                                    .. attribute:: options
                                    
                                    	Receive options
                                    	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options>`
                                    
                                    .. attribute:: lpts_flags
                                    
                                    	LPTS flags
                                    	**type**\:  :py:class:`LptsFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags>`
                                    
                                    .. attribute:: accept_mask
                                    
                                    	AcceptMask
                                    	**type**\:  :py:class:`AcceptMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask>`
                                    
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
                                    	**type**\: list of  		 :py:class:`Filter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter>`
                                    
                                    

                                    """

                                    _prefix = 'ip-tcp-oper'
                                    _revision = '2018-02-14'

                                    def __init__(self):
                                        super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb, self).__init__()

                                        self.yang_name = "lpts-pcb"
                                        self.yang_parent_name = "common"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_container_classes = OrderedDict([("options", ("options", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options)), ("lpts-flags", ("lpts_flags", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags)), ("accept-mask", ("accept_mask", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask))])
                                        self._child_list_classes = OrderedDict([("filter", ("filter", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter))])
                                        self._leafs = OrderedDict([
                                            ('ttl', YLeaf(YType.uint8, 'ttl')),
                                            ('flow_types_info', YLeaf(YType.uint32, 'flow-types-info')),
                                        ])
                                        self.ttl = None
                                        self.flow_types_info = None

                                        self.options = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options()
                                        self.options.parent = self
                                        self._children_name_map["options"] = "options"
                                        self._children_yang_names.add("options")

                                        self.lpts_flags = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags()
                                        self.lpts_flags.parent = self
                                        self._children_name_map["lpts_flags"] = "lpts-flags"
                                        self._children_yang_names.add("lpts-flags")

                                        self.accept_mask = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask()
                                        self.accept_mask.parent = self
                                        self._children_name_map["accept_mask"] = "accept-mask"
                                        self._children_yang_names.add("accept-mask")

                                        self.filter = YList(self)
                                        self._segment_path = lambda: "lpts-pcb"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb, ['ttl', 'flow_types_info'], name, value)


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

                                        _prefix = 'ip-tcp-oper'
                                        _revision = '2018-02-14'

                                        def __init__(self):
                                            super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options, self).__init__()

                                            self.yang_name = "options"
                                            self.yang_parent_name = "lpts-pcb"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('is_receive_filter', YLeaf(YType.boolean, 'is-receive-filter')),
                                                ('is_ip_sla', YLeaf(YType.boolean, 'is-ip-sla')),
                                            ])
                                            self.is_receive_filter = None
                                            self.is_ip_sla = None
                                            self._segment_path = lambda: "options"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options, ['is_receive_filter', 'is_ip_sla'], name, value)


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

                                        _prefix = 'ip-tcp-oper'
                                        _revision = '2018-02-14'

                                        def __init__(self):
                                            super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags, self).__init__()

                                            self.yang_name = "lpts-flags"
                                            self.yang_parent_name = "lpts-pcb"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('is_pcb_bound', YLeaf(YType.boolean, 'is-pcb-bound')),
                                                ('is_local_address_ignore', YLeaf(YType.boolean, 'is-local-address-ignore')),
                                                ('is_ignore_vrf_filter', YLeaf(YType.boolean, 'is-ignore-vrf-filter')),
                                            ])
                                            self.is_pcb_bound = None
                                            self.is_local_address_ignore = None
                                            self.is_ignore_vrf_filter = None
                                            self._segment_path = lambda: "lpts-flags"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags, ['is_pcb_bound', 'is_local_address_ignore', 'is_ignore_vrf_filter'], name, value)


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

                                        _prefix = 'ip-tcp-oper'
                                        _revision = '2018-02-14'

                                        def __init__(self):
                                            super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask, self).__init__()

                                            self.yang_name = "accept-mask"
                                            self.yang_parent_name = "lpts-pcb"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('is_interface', YLeaf(YType.boolean, 'is-interface')),
                                                ('is_packet_type', YLeaf(YType.boolean, 'is-packet-type')),
                                                ('is_remote_address', YLeaf(YType.boolean, 'is-remote-address')),
                                                ('is_remote_port', YLeaf(YType.boolean, 'is-remote-port')),
                                                ('is_local_address', YLeaf(YType.boolean, 'is-local-address')),
                                                ('is_local_port', YLeaf(YType.boolean, 'is-local-port')),
                                            ])
                                            self.is_interface = None
                                            self.is_packet_type = None
                                            self.is_remote_address = None
                                            self.is_remote_port = None
                                            self.is_local_address = None
                                            self.is_local_port = None
                                            self._segment_path = lambda: "accept-mask"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask, ['is_interface', 'is_packet_type', 'is_remote_address', 'is_remote_port', 'is_local_address', 'is_local_port'], name, value)


                                    class Filter(Entity):
                                        """
                                        Interface Filters
                                        
                                        .. attribute:: packet_type
                                        
                                        	Protocol\-specific packet type
                                        	**type**\:  :py:class:`PacketType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType>`
                                        
                                        .. attribute:: remote_address
                                        
                                        	Remote address
                                        	**type**\:  :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress>`
                                        
                                        .. attribute:: local_address
                                        
                                        	Local address
                                        	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress>`
                                        
                                        .. attribute:: interface_name
                                        
                                        	Interface name
                                        	**type**\: str
                                        
                                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                                        
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

                                        _prefix = 'ip-tcp-oper'
                                        _revision = '2018-02-14'

                                        def __init__(self):
                                            super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter, self).__init__()

                                            self.yang_name = "filter"
                                            self.yang_parent_name = "lpts-pcb"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([("packet-type", ("packet_type", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType)), ("remote-address", ("remote_address", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress)), ("local-address", ("local_address", TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress))])
                                            self._child_list_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('interface_name', YLeaf(YType.str, 'interface-name')),
                                                ('remote_length', YLeaf(YType.uint16, 'remote-length')),
                                                ('local_length', YLeaf(YType.uint16, 'local-length')),
                                                ('receive_remote_port', YLeaf(YType.uint16, 'receive-remote-port')),
                                                ('receive_local_port', YLeaf(YType.uint16, 'receive-local-port')),
                                                ('priority', YLeaf(YType.uint8, 'priority')),
                                                ('ttl', YLeaf(YType.uint8, 'ttl')),
                                                ('flow_types_info', YLeaf(YType.uint32, 'flow-types-info')),
                                            ])
                                            self.interface_name = None
                                            self.remote_length = None
                                            self.local_length = None
                                            self.receive_remote_port = None
                                            self.receive_local_port = None
                                            self.priority = None
                                            self.ttl = None
                                            self.flow_types_info = None

                                            self.packet_type = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType()
                                            self.packet_type.parent = self
                                            self._children_name_map["packet_type"] = "packet-type"
                                            self._children_yang_names.add("packet-type")

                                            self.remote_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress()
                                            self.remote_address.parent = self
                                            self._children_name_map["remote_address"] = "remote-address"
                                            self._children_yang_names.add("remote-address")

                                            self.local_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress()
                                            self.local_address.parent = self
                                            self._children_name_map["local_address"] = "local-address"
                                            self._children_yang_names.add("local-address")
                                            self._segment_path = lambda: "filter"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter, ['interface_name', 'remote_length', 'local_length', 'receive_remote_port', 'receive_local_port', 'priority', 'ttl', 'flow_types_info'], name, value)


                                        class PacketType(Entity):
                                            """
                                            Protocol\-specific packet type
                                            
                                            .. attribute:: type
                                            
                                            	Type
                                            	**type**\:  :py:class:`Packet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.Packet>`
                                            
                                            .. attribute:: icmp_message_type
                                            
                                            	ICMP message type
                                            	**type**\:  :py:class:`MessageTypeIcmp_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.MessageTypeIcmp_>`
                                            
                                            .. attribute:: icm_pv6_message_type
                                            
                                            	ICMPv6 message type
                                            	**type**\:  :py:class:`MessageTypeIcmpv6_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.MessageTypeIcmpv6_>`
                                            
                                            .. attribute:: igmp_message_type
                                            
                                            	IGMP message type
                                            	**type**\:  :py:class:`MessageTypeIgmp_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.MessageTypeIgmp_>`
                                            
                                            .. attribute:: message_id
                                            
                                            	Message type in number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ip-tcp-oper'
                                            _revision = '2018-02-14'

                                            def __init__(self):
                                                super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType, self).__init__()

                                                self.yang_name = "packet-type"
                                                self.yang_parent_name = "filter"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('type', YLeaf(YType.enumeration, 'type')),
                                                    ('icmp_message_type', YLeaf(YType.enumeration, 'icmp-message-type')),
                                                    ('icm_pv6_message_type', YLeaf(YType.enumeration, 'icm-pv6-message-type')),
                                                    ('igmp_message_type', YLeaf(YType.enumeration, 'igmp-message-type')),
                                                    ('message_id', YLeaf(YType.uint32, 'message-id')),
                                                ])
                                                self.type = None
                                                self.icmp_message_type = None
                                                self.icm_pv6_message_type = None
                                                self.igmp_message_type = None
                                                self.message_id = None
                                                self._segment_path = lambda: "packet-type"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType, ['type', 'icmp_message_type', 'icm_pv6_message_type', 'igmp_message_type', 'message_id'], name, value)


                                        class RemoteAddress(Entity):
                                            """
                                            Remote address
                                            
                                            .. attribute:: af_name
                                            
                                            	AFName
                                            	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ip-tcp-oper'
                                            _revision = '2018-02-14'

                                            def __init__(self):
                                                super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress, self).__init__()

                                                self.yang_name = "remote-address"
                                                self.yang_parent_name = "filter"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                                    ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                                                ])
                                                self.af_name = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "remote-address"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                                        class LocalAddress(Entity):
                                            """
                                            Local address
                                            
                                            .. attribute:: af_name
                                            
                                            	AFName
                                            	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                                            
                                            .. attribute:: ipv4_address
                                            
                                            	IPv4 address
                                            	**type**\: str
                                            
                                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                            
                                            .. attribute:: ipv6_address
                                            
                                            	IPv6 address
                                            	**type**\: str
                                            
                                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                            
                                            

                                            """

                                            _prefix = 'ip-tcp-oper'
                                            _revision = '2018-02-14'

                                            def __init__(self):
                                                super(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress, self).__init__()

                                                self.yang_name = "local-address"
                                                self.yang_parent_name = "filter"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_container_classes = OrderedDict([])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                                    ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                                    ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                                                ])
                                                self.af_name = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None
                                                self._segment_path = lambda: "local-address"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


            class DetailInformations(Entity):
                """
                Table listing TCP connections for which
                detailed information is provided
                
                .. attribute:: detail_information
                
                	Protocol Control Block ID
                	**type**\: list of  		 :py:class:`DetailInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpConnection.Nodes.Node.DetailInformations, self).__init__()

                    self.yang_name = "detail-informations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("detail-information", ("detail_information", TcpConnection.Nodes.Node.DetailInformations.DetailInformation))])
                    self._leafs = OrderedDict()

                    self.detail_information = YList(self)
                    self._segment_path = lambda: "detail-informations"

                def __setattr__(self, name, value):
                    self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations, [], name, value)


                class DetailInformation(Entity):
                    """
                    Protocol Control Block ID
                    
                    .. attribute:: pcb_id  (key)
                    
                    	Detail information about TCP connection, put null for all
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress>`
                    
                    .. attribute:: socket_option_flags
                    
                    	Socket option flags
                    	**type**\:  :py:class:`SocketOptionFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags>`
                    
                    .. attribute:: socket_state_flags
                    
                    	Socket state flags
                    	**type**\:  :py:class:`SocketStateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags>`
                    
                    .. attribute:: feature_flags
                    
                    	Connection feature flags
                    	**type**\:  :py:class:`FeatureFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags>`
                    
                    .. attribute:: state_flags
                    
                    	Connection state flags
                    	**type**\:  :py:class:`StateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags>`
                    
                    .. attribute:: request_flags
                    
                    	Connection request flags
                    	**type**\:  :py:class:`RequestFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags>`
                    
                    .. attribute:: receive_buf_state_flags
                    
                    	Receive buffer state flags
                    	**type**\:  :py:class:`ReceiveBufStateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags>`
                    
                    .. attribute:: send_buf_state_flags
                    
                    	Send buffer state flags
                    	**type**\:  :py:class:`SendBufStateFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags>`
                    
                    .. attribute:: address_family
                    
                    	Address Family
                    	**type**\:  :py:class:`TcpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpAddressFamily>`
                    
                    .. attribute:: pcb
                    
                    	PCB Address
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: so
                    
                    	Socket Address
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: tcpcb
                    
                    	TCPCB Address
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: vrf_id
                    
                    	VRF Id
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connection_state
                    
                    	Connection state
                    	**type**\:  :py:class:`TcpConnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnState>`
                    
                    .. attribute:: established_time
                    
                    	Time at which connection is established
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_pid
                    
                    	Id of the local process
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
                    
                    .. attribute:: packet_priority
                    
                    	Priority given to packets on this socket
                    	**type**\:  :py:class:`PakPrio <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.PakPrio>`
                    
                    .. attribute:: packet_tos
                    
                    	Type of Service value to be applied to transmistted packets
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: packet_ttl
                    
                    	TTL to be applied to transmited packets
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: hash_index
                    
                    	Index of the Hash Bucket
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_receive_queue_size
                    
                    	Current receive queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: max_receive_queue_size
                    
                    	Max receive queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: current_send_queue_size
                    
                    	Current send queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: max_send_queue_size
                    
                    	Max send queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: current_receive_queue_packet_size
                    
                    	Current receive queue size in packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_receive_queue_packet_size
                    
                    	Max receive queue size in packets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: save_queue_size
                    
                    	Save queue (out\-of seq data) size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: send_initial_sequence_num
                    
                    	Initial send sequence number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_unack_sequence_num
                    
                    	Sequence number of unacked data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_next_sequence_num
                    
                    	Sequence number of next data to be sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_max_sequence_num
                    
                    	Highest sequence number sent
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_window_size
                    
                    	Send window size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: send_congestion_window_size
                    
                    	Send congestion window size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: receive_initial_sequence_num
                    
                    	Initial receive sequence number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_next_sequence_num
                    
                    	Next sequence number expected
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: receive_adv_window_size
                    
                    	Receive advertised window size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: receive_window_size
                    
                    	Receive window size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: mss
                    
                    	Max segment size calculated in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: peer_mss
                    
                    	Max segment size offered by the peer in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: srtt
                    
                    	Smoothed round trip time \* 8 (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rtto
                    
                    	Round trip timeout (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: krtt
                    
                    	Round trip time (karn algorithm) (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: srtv
                    
                    	Smoothed round trip time variance \* 4 (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: min_rtt
                    
                    	Min RTT (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_rtt
                    
                    	Max RTT (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: retries
                    
                    	Number of retries
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ack_hold_time
                    
                    	ACK hold time (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: giveup_time
                    
                    	Giveup time (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keep_alive_time
                    
                    	Keepalive time (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: syn_wait_time
                    
                    	SYN wait time (msec)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rxsy_naclname
                    
                    	RX Syn acl name
                    	**type**\: str
                    
                    	**length:** 0..64
                    
                    .. attribute:: soft_error
                    
                    	Error code from ICMP Notify
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: sock_error
                    
                    	Socket error code
                    	**type**\: int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: is_retrans_forever
                    
                    	Retransimit forever?
                    	**type**\: bool
                    
                    .. attribute:: min_mss
                    
                    	Lowest MSS ever used
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_mss
                    
                    	Highest MSS ever used
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: connect_retries
                    
                    	Number of times connect will be retried?
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: connect_retry_interval
                    
                    	Connect retry interval in seconds
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    	**units**\: second
                    
                    .. attribute:: receive_window_scale
                    
                    	Window scaling for receive window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_window_scale
                    
                    	Window scaling for send window
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: request_receive_window_scale
                    
                    	Requested receive window scale
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: rqst_send_wnd_scale
                    
                    	Requested send window scale
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_stamp_recent
                    
                    	Timestamp from remote host
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: time_stamp_recent_age
                    
                    	Timestamp when last updated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: last_ack_sent
                    
                    	ACK number of a sent segment
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sendbuf_lowwat
                    
                    	Send buffer's low water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: recvbuf_lowwat
                    
                    	Receive buffer's low water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sendbuf_hiwat
                    
                    	Send buffer's high water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: recvbuf_hiwat
                    
                    	Receive buffer's high water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: sendbuf_notify_thresh
                    
                    	Send buffer's notify threshold
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: recvbuf_datasize
                    
                    	Receive buffer's data size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: queue_length
                    
                    	Incoming connection queue size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: queue_zero_length
                    
                    	Incoming half\-connection queue size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: queue_limit
                    
                    	Incoming connection queue limit
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_error
                    
                    	Socket error status
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: auto_rearm
                    
                    	Socket auto rearm state
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: send_pdu_count
                    
                    	# of PDU's in Send Buffer
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: output_ifhandle
                    
                    	Cached Outgoing interface  handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: fib_pd_ctx_size
                    
                    	Cached fib pd context size
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: num_labels
                    
                    	Number of labels returned by fib lookup
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_app_instance
                    
                    	Instance number of the local process
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: fib_pd_ctx
                    
                    	Cached fib pd context
                    	**type**\: list of  		 :py:class:`FibPdCtx <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibPdCtx>`
                    
                    .. attribute:: fib_label_output
                    
                    	Cached Label stack
                    	**type**\: list of  		 :py:class:`FibLabelOutput <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibLabelOutput>`
                    
                    .. attribute:: timer
                    
                    	Timers
                    	**type**\: list of  		 :py:class:`Timer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer>`
                    
                    .. attribute:: sack_blk
                    
                    	Seq nos. of sack blocks
                    	**type**\: list of  		 :py:class:`SackBlk <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk>`
                    
                    .. attribute:: send_sack_hole
                    
                    	Sorted list of sack holes
                    	**type**\: list of  		 :py:class:`SendSackHole <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation, self).__init__()

                        self.yang_name = "detail-information"
                        self.yang_parent_name = "detail-informations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pcb_id']
                        self._child_container_classes = OrderedDict([("local-address", ("local_address", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress)), ("foreign-address", ("foreign_address", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress)), ("socket-option-flags", ("socket_option_flags", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags)), ("socket-state-flags", ("socket_state_flags", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags)), ("feature-flags", ("feature_flags", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags)), ("state-flags", ("state_flags", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags)), ("request-flags", ("request_flags", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags)), ("receive-buf-state-flags", ("receive_buf_state_flags", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags)), ("send-buf-state-flags", ("send_buf_state_flags", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags))])
                        self._child_list_classes = OrderedDict([("fib-pd-ctx", ("fib_pd_ctx", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibPdCtx)), ("fib-label-output", ("fib_label_output", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibLabelOutput)), ("timer", ("timer", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer)), ("sack-blk", ("sack_blk", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk)), ("send-sack-hole", ("send_sack_hole", TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole))])
                        self._leafs = OrderedDict([
                            ('pcb_id', YLeaf(YType.str, 'pcb-id')),
                            ('address_family', YLeaf(YType.enumeration, 'address-family')),
                            ('pcb', YLeaf(YType.uint64, 'pcb')),
                            ('so', YLeaf(YType.uint64, 'so')),
                            ('tcpcb', YLeaf(YType.uint64, 'tcpcb')),
                            ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                            ('connection_state', YLeaf(YType.enumeration, 'connection-state')),
                            ('established_time', YLeaf(YType.uint32, 'established-time')),
                            ('local_pid', YLeaf(YType.uint32, 'local-pid')),
                            ('local_port', YLeaf(YType.uint16, 'local-port')),
                            ('foreign_port', YLeaf(YType.uint16, 'foreign-port')),
                            ('packet_priority', YLeaf(YType.enumeration, 'packet-priority')),
                            ('packet_tos', YLeaf(YType.uint16, 'packet-tos')),
                            ('packet_ttl', YLeaf(YType.uint16, 'packet-ttl')),
                            ('hash_index', YLeaf(YType.uint32, 'hash-index')),
                            ('current_receive_queue_size', YLeaf(YType.uint32, 'current-receive-queue-size')),
                            ('max_receive_queue_size', YLeaf(YType.uint32, 'max-receive-queue-size')),
                            ('current_send_queue_size', YLeaf(YType.uint32, 'current-send-queue-size')),
                            ('max_send_queue_size', YLeaf(YType.uint32, 'max-send-queue-size')),
                            ('current_receive_queue_packet_size', YLeaf(YType.uint32, 'current-receive-queue-packet-size')),
                            ('max_receive_queue_packet_size', YLeaf(YType.uint32, 'max-receive-queue-packet-size')),
                            ('save_queue_size', YLeaf(YType.uint32, 'save-queue-size')),
                            ('send_initial_sequence_num', YLeaf(YType.uint32, 'send-initial-sequence-num')),
                            ('send_unack_sequence_num', YLeaf(YType.uint32, 'send-unack-sequence-num')),
                            ('send_next_sequence_num', YLeaf(YType.uint32, 'send-next-sequence-num')),
                            ('send_max_sequence_num', YLeaf(YType.uint32, 'send-max-sequence-num')),
                            ('send_window_size', YLeaf(YType.uint32, 'send-window-size')),
                            ('send_congestion_window_size', YLeaf(YType.uint32, 'send-congestion-window-size')),
                            ('receive_initial_sequence_num', YLeaf(YType.uint32, 'receive-initial-sequence-num')),
                            ('receive_next_sequence_num', YLeaf(YType.uint32, 'receive-next-sequence-num')),
                            ('receive_adv_window_size', YLeaf(YType.uint32, 'receive-adv-window-size')),
                            ('receive_window_size', YLeaf(YType.uint32, 'receive-window-size')),
                            ('mss', YLeaf(YType.uint32, 'mss')),
                            ('peer_mss', YLeaf(YType.uint32, 'peer-mss')),
                            ('srtt', YLeaf(YType.uint32, 'srtt')),
                            ('rtto', YLeaf(YType.uint32, 'rtto')),
                            ('krtt', YLeaf(YType.uint32, 'krtt')),
                            ('srtv', YLeaf(YType.uint32, 'srtv')),
                            ('min_rtt', YLeaf(YType.uint32, 'min-rtt')),
                            ('max_rtt', YLeaf(YType.uint32, 'max-rtt')),
                            ('retries', YLeaf(YType.uint32, 'retries')),
                            ('ack_hold_time', YLeaf(YType.uint32, 'ack-hold-time')),
                            ('giveup_time', YLeaf(YType.uint32, 'giveup-time')),
                            ('keep_alive_time', YLeaf(YType.uint32, 'keep-alive-time')),
                            ('syn_wait_time', YLeaf(YType.uint32, 'syn-wait-time')),
                            ('rxsy_naclname', YLeaf(YType.str, 'rxsy-naclname')),
                            ('soft_error', YLeaf(YType.int32, 'soft-error')),
                            ('sock_error', YLeaf(YType.int32, 'sock-error')),
                            ('is_retrans_forever', YLeaf(YType.boolean, 'is-retrans-forever')),
                            ('min_mss', YLeaf(YType.uint32, 'min-mss')),
                            ('max_mss', YLeaf(YType.uint32, 'max-mss')),
                            ('connect_retries', YLeaf(YType.uint16, 'connect-retries')),
                            ('connect_retry_interval', YLeaf(YType.uint16, 'connect-retry-interval')),
                            ('receive_window_scale', YLeaf(YType.uint32, 'receive-window-scale')),
                            ('send_window_scale', YLeaf(YType.uint32, 'send-window-scale')),
                            ('request_receive_window_scale', YLeaf(YType.uint32, 'request-receive-window-scale')),
                            ('rqst_send_wnd_scale', YLeaf(YType.uint32, 'rqst-send-wnd-scale')),
                            ('time_stamp_recent', YLeaf(YType.uint32, 'time-stamp-recent')),
                            ('time_stamp_recent_age', YLeaf(YType.uint32, 'time-stamp-recent-age')),
                            ('last_ack_sent', YLeaf(YType.uint32, 'last-ack-sent')),
                            ('sendbuf_lowwat', YLeaf(YType.uint32, 'sendbuf-lowwat')),
                            ('recvbuf_lowwat', YLeaf(YType.uint32, 'recvbuf-lowwat')),
                            ('sendbuf_hiwat', YLeaf(YType.uint32, 'sendbuf-hiwat')),
                            ('recvbuf_hiwat', YLeaf(YType.uint32, 'recvbuf-hiwat')),
                            ('sendbuf_notify_thresh', YLeaf(YType.uint32, 'sendbuf-notify-thresh')),
                            ('recvbuf_datasize', YLeaf(YType.uint32, 'recvbuf-datasize')),
                            ('queue_length', YLeaf(YType.uint32, 'queue-length')),
                            ('queue_zero_length', YLeaf(YType.uint32, 'queue-zero-length')),
                            ('queue_limit', YLeaf(YType.uint32, 'queue-limit')),
                            ('socket_error', YLeaf(YType.uint32, 'socket-error')),
                            ('auto_rearm', YLeaf(YType.uint32, 'auto-rearm')),
                            ('send_pdu_count', YLeaf(YType.uint32, 'send-pdu-count')),
                            ('output_ifhandle', YLeaf(YType.uint32, 'output-ifhandle')),
                            ('fib_pd_ctx_size', YLeaf(YType.uint32, 'fib-pd-ctx-size')),
                            ('num_labels', YLeaf(YType.uint32, 'num-labels')),
                            ('local_app_instance', YLeaf(YType.uint32, 'local-app-instance')),
                        ])
                        self.pcb_id = None
                        self.address_family = None
                        self.pcb = None
                        self.so = None
                        self.tcpcb = None
                        self.vrf_id = None
                        self.connection_state = None
                        self.established_time = None
                        self.local_pid = None
                        self.local_port = None
                        self.foreign_port = None
                        self.packet_priority = None
                        self.packet_tos = None
                        self.packet_ttl = None
                        self.hash_index = None
                        self.current_receive_queue_size = None
                        self.max_receive_queue_size = None
                        self.current_send_queue_size = None
                        self.max_send_queue_size = None
                        self.current_receive_queue_packet_size = None
                        self.max_receive_queue_packet_size = None
                        self.save_queue_size = None
                        self.send_initial_sequence_num = None
                        self.send_unack_sequence_num = None
                        self.send_next_sequence_num = None
                        self.send_max_sequence_num = None
                        self.send_window_size = None
                        self.send_congestion_window_size = None
                        self.receive_initial_sequence_num = None
                        self.receive_next_sequence_num = None
                        self.receive_adv_window_size = None
                        self.receive_window_size = None
                        self.mss = None
                        self.peer_mss = None
                        self.srtt = None
                        self.rtto = None
                        self.krtt = None
                        self.srtv = None
                        self.min_rtt = None
                        self.max_rtt = None
                        self.retries = None
                        self.ack_hold_time = None
                        self.giveup_time = None
                        self.keep_alive_time = None
                        self.syn_wait_time = None
                        self.rxsy_naclname = None
                        self.soft_error = None
                        self.sock_error = None
                        self.is_retrans_forever = None
                        self.min_mss = None
                        self.max_mss = None
                        self.connect_retries = None
                        self.connect_retry_interval = None
                        self.receive_window_scale = None
                        self.send_window_scale = None
                        self.request_receive_window_scale = None
                        self.rqst_send_wnd_scale = None
                        self.time_stamp_recent = None
                        self.time_stamp_recent_age = None
                        self.last_ack_sent = None
                        self.sendbuf_lowwat = None
                        self.recvbuf_lowwat = None
                        self.sendbuf_hiwat = None
                        self.recvbuf_hiwat = None
                        self.sendbuf_notify_thresh = None
                        self.recvbuf_datasize = None
                        self.queue_length = None
                        self.queue_zero_length = None
                        self.queue_limit = None
                        self.socket_error = None
                        self.auto_rearm = None
                        self.send_pdu_count = None
                        self.output_ifhandle = None
                        self.fib_pd_ctx_size = None
                        self.num_labels = None
                        self.local_app_instance = None

                        self.local_address = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                        self.foreign_address = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress()
                        self.foreign_address.parent = self
                        self._children_name_map["foreign_address"] = "foreign-address"
                        self._children_yang_names.add("foreign-address")

                        self.socket_option_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags()
                        self.socket_option_flags.parent = self
                        self._children_name_map["socket_option_flags"] = "socket-option-flags"
                        self._children_yang_names.add("socket-option-flags")

                        self.socket_state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags()
                        self.socket_state_flags.parent = self
                        self._children_name_map["socket_state_flags"] = "socket-state-flags"
                        self._children_yang_names.add("socket-state-flags")

                        self.feature_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags()
                        self.feature_flags.parent = self
                        self._children_name_map["feature_flags"] = "feature-flags"
                        self._children_yang_names.add("feature-flags")

                        self.state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags()
                        self.state_flags.parent = self
                        self._children_name_map["state_flags"] = "state-flags"
                        self._children_yang_names.add("state-flags")

                        self.request_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags()
                        self.request_flags.parent = self
                        self._children_name_map["request_flags"] = "request-flags"
                        self._children_yang_names.add("request-flags")

                        self.receive_buf_state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags()
                        self.receive_buf_state_flags.parent = self
                        self._children_name_map["receive_buf_state_flags"] = "receive-buf-state-flags"
                        self._children_yang_names.add("receive-buf-state-flags")

                        self.send_buf_state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags()
                        self.send_buf_state_flags.parent = self
                        self._children_name_map["send_buf_state_flags"] = "send-buf-state-flags"
                        self._children_yang_names.add("send-buf-state-flags")

                        self.fib_pd_ctx = YList(self)
                        self.fib_label_output = YList(self)
                        self.timer = YList(self)
                        self.sack_blk = YList(self)
                        self.send_sack_hole = YList(self)
                        self._segment_path = lambda: "detail-information" + "[pcb-id='" + str(self.pcb_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation, ['pcb_id', 'address_family', 'pcb', 'so', 'tcpcb', 'vrf_id', 'connection_state', 'established_time', 'local_pid', 'local_port', 'foreign_port', 'packet_priority', 'packet_tos', 'packet_ttl', 'hash_index', 'current_receive_queue_size', 'max_receive_queue_size', 'current_send_queue_size', 'max_send_queue_size', 'current_receive_queue_packet_size', 'max_receive_queue_packet_size', 'save_queue_size', 'send_initial_sequence_num', 'send_unack_sequence_num', 'send_next_sequence_num', 'send_max_sequence_num', 'send_window_size', 'send_congestion_window_size', 'receive_initial_sequence_num', 'receive_next_sequence_num', 'receive_adv_window_size', 'receive_window_size', 'mss', 'peer_mss', 'srtt', 'rtto', 'krtt', 'srtv', 'min_rtt', 'max_rtt', 'retries', 'ack_hold_time', 'giveup_time', 'keep_alive_time', 'syn_wait_time', 'rxsy_naclname', 'soft_error', 'sock_error', 'is_retrans_forever', 'min_mss', 'max_mss', 'connect_retries', 'connect_retry_interval', 'receive_window_scale', 'send_window_scale', 'request_receive_window_scale', 'rqst_send_wnd_scale', 'time_stamp_recent', 'time_stamp_recent_age', 'last_ack_sent', 'sendbuf_lowwat', 'recvbuf_lowwat', 'sendbuf_hiwat', 'recvbuf_hiwat', 'sendbuf_notify_thresh', 'recvbuf_datasize', 'queue_length', 'queue_zero_length', 'queue_limit', 'socket_error', 'auto_rearm', 'send_pdu_count', 'output_ifhandle', 'fib_pd_ctx_size', 'num_labels', 'local_app_instance'], name, value)


                    class LocalAddress(Entity):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`TcpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "local-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                    class ForeignAddress(Entity):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`TcpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress, self).__init__()

                            self.yang_name = "foreign-address"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "foreign-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ForeignAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                    class SocketOptionFlags(Entity):
                        """
                        Socket option flags
                        
                        .. attribute:: debug
                        
                        	Turn on debugging info recording
                        	**type**\: bool
                        
                        .. attribute:: accept_connection
                        
                        	Socket has had listen()
                        	**type**\: bool
                        
                        .. attribute:: reuse_address
                        
                        	Allow local address reuse
                        	**type**\: bool
                        
                        .. attribute:: keep_alive
                        
                        	Keep connections alive
                        	**type**\: bool
                        
                        .. attribute:: dont_route
                        
                        	Just use interface addresses
                        	**type**\: bool
                        
                        .. attribute:: broadcast
                        
                        	Permit sending of broadcast msgs
                        	**type**\: bool
                        
                        .. attribute:: use_loopback
                        
                        	Bypass hardware when possible
                        	**type**\: bool
                        
                        .. attribute:: linger
                        
                        	Linger on close if data present
                        	**type**\: bool
                        
                        .. attribute:: out_of_band_inline
                        
                        	Leave received Out\-of\-band data inline
                        	**type**\: bool
                        
                        .. attribute:: reuse_port
                        
                        	Allow local address & port reuse
                        	**type**\: bool
                        
                        .. attribute:: nonblocking_io
                        
                        	Nonblocking socket I/O operation
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags, self).__init__()

                            self.yang_name = "socket-option-flags"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('debug', YLeaf(YType.boolean, 'debug')),
                                ('accept_connection', YLeaf(YType.boolean, 'accept-connection')),
                                ('reuse_address', YLeaf(YType.boolean, 'reuse-address')),
                                ('keep_alive', YLeaf(YType.boolean, 'keep-alive')),
                                ('dont_route', YLeaf(YType.boolean, 'dont-route')),
                                ('broadcast', YLeaf(YType.boolean, 'broadcast')),
                                ('use_loopback', YLeaf(YType.boolean, 'use-loopback')),
                                ('linger', YLeaf(YType.boolean, 'linger')),
                                ('out_of_band_inline', YLeaf(YType.boolean, 'out-of-band-inline')),
                                ('reuse_port', YLeaf(YType.boolean, 'reuse-port')),
                                ('nonblocking_io', YLeaf(YType.boolean, 'nonblocking-io')),
                            ])
                            self.debug = None
                            self.accept_connection = None
                            self.reuse_address = None
                            self.keep_alive = None
                            self.dont_route = None
                            self.broadcast = None
                            self.use_loopback = None
                            self.linger = None
                            self.out_of_band_inline = None
                            self.reuse_port = None
                            self.nonblocking_io = None
                            self._segment_path = lambda: "socket-option-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags, ['debug', 'accept_connection', 'reuse_address', 'keep_alive', 'dont_route', 'broadcast', 'use_loopback', 'linger', 'out_of_band_inline', 'reuse_port', 'nonblocking_io'], name, value)


                    class SocketStateFlags(Entity):
                        """
                        Socket state flags
                        
                        .. attribute:: no_file_descriptor_reference
                        
                        	No file descriptor ref
                        	**type**\: bool
                        
                        .. attribute:: is_connected
                        
                        	Socket is connected to peer
                        	**type**\: bool
                        
                        .. attribute:: is_connecting
                        
                        	Connecting in progress
                        	**type**\: bool
                        
                        .. attribute:: is_disconnecting
                        
                        	Disconnecting in progress
                        	**type**\: bool
                        
                        .. attribute:: cant_send_more
                        
                        	Can't send more data to peer
                        	**type**\: bool
                        
                        .. attribute:: cant_receive_more
                        
                        	Can't recv more data from peer
                        	**type**\: bool
                        
                        .. attribute:: received_at_mark
                        
                        	At mark on input
                        	**type**\: bool
                        
                        .. attribute:: privileged
                        
                        	Privileged for broadcast, raw..
                        	**type**\: bool
                        
                        .. attribute:: block_close
                        
                        	Close is blocked (i.e. socket is a replicated socket on a standby node
                        	**type**\: bool
                        
                        .. attribute:: async_io_notify
                        
                        	Async i/o notify
                        	**type**\: bool
                        
                        .. attribute:: is_confirming
                        
                        	Deciding to accept connection req
                        	**type**\: bool
                        
                        .. attribute:: is_solock
                        
                        	Mutex acquired by solock()
                        	**type**\: bool
                        
                        .. attribute:: is_detached
                        
                        	PCB and socket are detached
                        	**type**\: bool
                        
                        .. attribute:: block_receive
                        
                        	Socket is blocked for receive \- while going through SSO initial sync
                        	**type**\: bool
                        
                        .. attribute:: block_send
                        
                        	Socket is blocked for send (if it is a replicated socket on a standby node)
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags, self).__init__()

                            self.yang_name = "socket-state-flags"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('no_file_descriptor_reference', YLeaf(YType.boolean, 'no-file-descriptor-reference')),
                                ('is_connected', YLeaf(YType.boolean, 'is-connected')),
                                ('is_connecting', YLeaf(YType.boolean, 'is-connecting')),
                                ('is_disconnecting', YLeaf(YType.boolean, 'is-disconnecting')),
                                ('cant_send_more', YLeaf(YType.boolean, 'cant-send-more')),
                                ('cant_receive_more', YLeaf(YType.boolean, 'cant-receive-more')),
                                ('received_at_mark', YLeaf(YType.boolean, 'received-at-mark')),
                                ('privileged', YLeaf(YType.boolean, 'privileged')),
                                ('block_close', YLeaf(YType.boolean, 'block-close')),
                                ('async_io_notify', YLeaf(YType.boolean, 'async-io-notify')),
                                ('is_confirming', YLeaf(YType.boolean, 'is-confirming')),
                                ('is_solock', YLeaf(YType.boolean, 'is-solock')),
                                ('is_detached', YLeaf(YType.boolean, 'is-detached')),
                                ('block_receive', YLeaf(YType.boolean, 'block-receive')),
                                ('block_send', YLeaf(YType.boolean, 'block-send')),
                            ])
                            self.no_file_descriptor_reference = None
                            self.is_connected = None
                            self.is_connecting = None
                            self.is_disconnecting = None
                            self.cant_send_more = None
                            self.cant_receive_more = None
                            self.received_at_mark = None
                            self.privileged = None
                            self.block_close = None
                            self.async_io_notify = None
                            self.is_confirming = None
                            self.is_solock = None
                            self.is_detached = None
                            self.block_receive = None
                            self.block_send = None
                            self._segment_path = lambda: "socket-state-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags, ['no_file_descriptor_reference', 'is_connected', 'is_connecting', 'is_disconnecting', 'cant_send_more', 'cant_receive_more', 'received_at_mark', 'privileged', 'block_close', 'async_io_notify', 'is_confirming', 'is_solock', 'is_detached', 'block_receive', 'block_send'], name, value)


                    class FeatureFlags(Entity):
                        """
                        Connection feature flags
                        
                        .. attribute:: selective_ack
                        
                        	Selective ack on?
                        	**type**\: bool
                        
                        .. attribute:: md5
                        
                        	MD5 option on?
                        	**type**\: bool
                        
                        .. attribute:: timestamps
                        
                        	Timestamps on?
                        	**type**\: bool
                        
                        .. attribute:: window_scaling
                        
                        	Window\-scaling on?
                        	**type**\: bool
                        
                        .. attribute:: nagle
                        
                        	Nagle algorithm on?
                        	**type**\: bool
                        
                        .. attribute:: giveup_timer
                        
                        	Giveup timer is on?
                        	**type**\: bool
                        
                        .. attribute:: connection_keep_alive_timer
                        
                        	Keepalive timer is on?
                        	**type**\: bool
                        
                        .. attribute:: path_mtu_discovery
                        
                        	Path MTU Discovery feature is on?
                        	**type**\: bool
                        
                        .. attribute:: mss_cisco
                        
                        	tcp mss feature is on?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags, self).__init__()

                            self.yang_name = "feature-flags"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selective_ack', YLeaf(YType.boolean, 'selective-ack')),
                                ('md5', YLeaf(YType.boolean, 'md5')),
                                ('timestamps', YLeaf(YType.boolean, 'timestamps')),
                                ('window_scaling', YLeaf(YType.boolean, 'window-scaling')),
                                ('nagle', YLeaf(YType.boolean, 'nagle')),
                                ('giveup_timer', YLeaf(YType.boolean, 'giveup-timer')),
                                ('connection_keep_alive_timer', YLeaf(YType.boolean, 'connection-keep-alive-timer')),
                                ('path_mtu_discovery', YLeaf(YType.boolean, 'path-mtu-discovery')),
                                ('mss_cisco', YLeaf(YType.boolean, 'mss-cisco')),
                            ])
                            self.selective_ack = None
                            self.md5 = None
                            self.timestamps = None
                            self.window_scaling = None
                            self.nagle = None
                            self.giveup_timer = None
                            self.connection_keep_alive_timer = None
                            self.path_mtu_discovery = None
                            self.mss_cisco = None
                            self._segment_path = lambda: "feature-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags, ['selective_ack', 'md5', 'timestamps', 'window_scaling', 'nagle', 'giveup_timer', 'connection_keep_alive_timer', 'path_mtu_discovery', 'mss_cisco'], name, value)


                    class StateFlags(Entity):
                        """
                        Connection state flags
                        
                        .. attribute:: nagle_wait
                        
                        	Nagle has delayed output
                        	**type**\: bool
                        
                        .. attribute:: ack_needed
                        
                        	Send an ACK
                        	**type**\: bool
                        
                        .. attribute:: fin_sent
                        
                        	FIN has been sent
                        	**type**\: bool
                        
                        .. attribute:: probing
                        
                        	Probing a closed window
                        	**type**\: bool
                        
                        .. attribute:: need_push
                        
                        	Need to push data out
                        	**type**\: bool
                        
                        .. attribute:: pushed
                        
                        	A segment is pushed due to MSG\_PUSH
                        	**type**\: bool
                        
                        .. attribute:: in_syn_cache
                        
                        	Connection is in SYN cache
                        	**type**\: bool
                        
                        .. attribute:: path_mtu_ager
                        
                        	Path MTU aging timer is running
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags, self).__init__()

                            self.yang_name = "state-flags"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('nagle_wait', YLeaf(YType.boolean, 'nagle-wait')),
                                ('ack_needed', YLeaf(YType.boolean, 'ack-needed')),
                                ('fin_sent', YLeaf(YType.boolean, 'fin-sent')),
                                ('probing', YLeaf(YType.boolean, 'probing')),
                                ('need_push', YLeaf(YType.boolean, 'need-push')),
                                ('pushed', YLeaf(YType.boolean, 'pushed')),
                                ('in_syn_cache', YLeaf(YType.boolean, 'in-syn-cache')),
                                ('path_mtu_ager', YLeaf(YType.boolean, 'path-mtu-ager')),
                            ])
                            self.nagle_wait = None
                            self.ack_needed = None
                            self.fin_sent = None
                            self.probing = None
                            self.need_push = None
                            self.pushed = None
                            self.in_syn_cache = None
                            self.path_mtu_ager = None
                            self._segment_path = lambda: "state-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags, ['nagle_wait', 'ack_needed', 'fin_sent', 'probing', 'need_push', 'pushed', 'in_syn_cache', 'path_mtu_ager'], name, value)


                    class RequestFlags(Entity):
                        """
                        Connection request flags
                        
                        .. attribute:: selective_ack
                        
                        	Selective ack on?
                        	**type**\: bool
                        
                        .. attribute:: md5
                        
                        	MD5 option on?
                        	**type**\: bool
                        
                        .. attribute:: timestamps
                        
                        	Timestamps on?
                        	**type**\: bool
                        
                        .. attribute:: window_scaling
                        
                        	Window\-scaling on?
                        	**type**\: bool
                        
                        .. attribute:: nagle
                        
                        	Nagle algorithm on?
                        	**type**\: bool
                        
                        .. attribute:: giveup_timer
                        
                        	Giveup timer is on?
                        	**type**\: bool
                        
                        .. attribute:: connection_keep_alive_timer
                        
                        	Keepalive timer is on?
                        	**type**\: bool
                        
                        .. attribute:: path_mtu_discovery
                        
                        	Path MTU Discovery feature is on?
                        	**type**\: bool
                        
                        .. attribute:: mss_cisco
                        
                        	tcp mss feature is on?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags, self).__init__()

                            self.yang_name = "request-flags"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('selective_ack', YLeaf(YType.boolean, 'selective-ack')),
                                ('md5', YLeaf(YType.boolean, 'md5')),
                                ('timestamps', YLeaf(YType.boolean, 'timestamps')),
                                ('window_scaling', YLeaf(YType.boolean, 'window-scaling')),
                                ('nagle', YLeaf(YType.boolean, 'nagle')),
                                ('giveup_timer', YLeaf(YType.boolean, 'giveup-timer')),
                                ('connection_keep_alive_timer', YLeaf(YType.boolean, 'connection-keep-alive-timer')),
                                ('path_mtu_discovery', YLeaf(YType.boolean, 'path-mtu-discovery')),
                                ('mss_cisco', YLeaf(YType.boolean, 'mss-cisco')),
                            ])
                            self.selective_ack = None
                            self.md5 = None
                            self.timestamps = None
                            self.window_scaling = None
                            self.nagle = None
                            self.giveup_timer = None
                            self.connection_keep_alive_timer = None
                            self.path_mtu_discovery = None
                            self.mss_cisco = None
                            self._segment_path = lambda: "request-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags, ['selective_ack', 'md5', 'timestamps', 'window_scaling', 'nagle', 'giveup_timer', 'connection_keep_alive_timer', 'path_mtu_discovery', 'mss_cisco'], name, value)


                    class ReceiveBufStateFlags(Entity):
                        """
                        Receive buffer state flags
                        
                        .. attribute:: locked
                        
                        	Lock on data queue (so\_rcv only)
                        	**type**\: bool
                        
                        .. attribute:: waiting_for_lock
                        
                        	Someone is waiting to lock
                        	**type**\: bool
                        
                        .. attribute:: waiting_for_data
                        
                        	Someone is waiting for data/space
                        	**type**\: bool
                        
                        .. attribute:: input_select
                        
                        	Buffer is selected for INPUT
                        	**type**\: bool
                        
                        .. attribute:: async_io
                        
                        	Async I/O
                        	**type**\: bool
                        
                        .. attribute:: not_interruptible
                        
                        	Not interruptible
                        	**type**\: bool
                        
                        .. attribute:: io_timer_set
                        
                        	Read/write timer set
                        	**type**\: bool
                        
                        .. attribute:: delayed_wakeup
                        
                        	Want delayed wakeups
                        	**type**\: bool
                        
                        .. attribute:: wakeup
                        
                        	Read/write wakeup pending
                        	**type**\: bool
                        
                        .. attribute:: connect_wakeup
                        
                        	Connect wakeup pending
                        	**type**\: bool
                        
                        .. attribute:: output_select
                        
                        	Buffer is selected for OUTPUT
                        	**type**\: bool
                        
                        .. attribute:: out_of_band_select
                        
                        	Buffer is selected for OBAND
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags, self).__init__()

                            self.yang_name = "receive-buf-state-flags"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('locked', YLeaf(YType.boolean, 'locked')),
                                ('waiting_for_lock', YLeaf(YType.boolean, 'waiting-for-lock')),
                                ('waiting_for_data', YLeaf(YType.boolean, 'waiting-for-data')),
                                ('input_select', YLeaf(YType.boolean, 'input-select')),
                                ('async_io', YLeaf(YType.boolean, 'async-io')),
                                ('not_interruptible', YLeaf(YType.boolean, 'not-interruptible')),
                                ('io_timer_set', YLeaf(YType.boolean, 'io-timer-set')),
                                ('delayed_wakeup', YLeaf(YType.boolean, 'delayed-wakeup')),
                                ('wakeup', YLeaf(YType.boolean, 'wakeup')),
                                ('connect_wakeup', YLeaf(YType.boolean, 'connect-wakeup')),
                                ('output_select', YLeaf(YType.boolean, 'output-select')),
                                ('out_of_band_select', YLeaf(YType.boolean, 'out-of-band-select')),
                            ])
                            self.locked = None
                            self.waiting_for_lock = None
                            self.waiting_for_data = None
                            self.input_select = None
                            self.async_io = None
                            self.not_interruptible = None
                            self.io_timer_set = None
                            self.delayed_wakeup = None
                            self.wakeup = None
                            self.connect_wakeup = None
                            self.output_select = None
                            self.out_of_band_select = None
                            self._segment_path = lambda: "receive-buf-state-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags, ['locked', 'waiting_for_lock', 'waiting_for_data', 'input_select', 'async_io', 'not_interruptible', 'io_timer_set', 'delayed_wakeup', 'wakeup', 'connect_wakeup', 'output_select', 'out_of_band_select'], name, value)


                    class SendBufStateFlags(Entity):
                        """
                        Send buffer state flags
                        
                        .. attribute:: locked
                        
                        	Lock on data queue (so\_rcv only)
                        	**type**\: bool
                        
                        .. attribute:: waiting_for_lock
                        
                        	Someone is waiting to lock
                        	**type**\: bool
                        
                        .. attribute:: waiting_for_data
                        
                        	Someone is waiting for data/space
                        	**type**\: bool
                        
                        .. attribute:: input_select
                        
                        	Buffer is selected for INPUT
                        	**type**\: bool
                        
                        .. attribute:: async_io
                        
                        	Async I/O
                        	**type**\: bool
                        
                        .. attribute:: not_interruptible
                        
                        	Not interruptible
                        	**type**\: bool
                        
                        .. attribute:: io_timer_set
                        
                        	Read/write timer set
                        	**type**\: bool
                        
                        .. attribute:: delayed_wakeup
                        
                        	Want delayed wakeups
                        	**type**\: bool
                        
                        .. attribute:: wakeup
                        
                        	Read/write wakeup pending
                        	**type**\: bool
                        
                        .. attribute:: connect_wakeup
                        
                        	Connect wakeup pending
                        	**type**\: bool
                        
                        .. attribute:: output_select
                        
                        	Buffer is selected for OUTPUT
                        	**type**\: bool
                        
                        .. attribute:: out_of_band_select
                        
                        	Buffer is selected for OBAND
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags, self).__init__()

                            self.yang_name = "send-buf-state-flags"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('locked', YLeaf(YType.boolean, 'locked')),
                                ('waiting_for_lock', YLeaf(YType.boolean, 'waiting-for-lock')),
                                ('waiting_for_data', YLeaf(YType.boolean, 'waiting-for-data')),
                                ('input_select', YLeaf(YType.boolean, 'input-select')),
                                ('async_io', YLeaf(YType.boolean, 'async-io')),
                                ('not_interruptible', YLeaf(YType.boolean, 'not-interruptible')),
                                ('io_timer_set', YLeaf(YType.boolean, 'io-timer-set')),
                                ('delayed_wakeup', YLeaf(YType.boolean, 'delayed-wakeup')),
                                ('wakeup', YLeaf(YType.boolean, 'wakeup')),
                                ('connect_wakeup', YLeaf(YType.boolean, 'connect-wakeup')),
                                ('output_select', YLeaf(YType.boolean, 'output-select')),
                                ('out_of_band_select', YLeaf(YType.boolean, 'out-of-band-select')),
                            ])
                            self.locked = None
                            self.waiting_for_lock = None
                            self.waiting_for_data = None
                            self.input_select = None
                            self.async_io = None
                            self.not_interruptible = None
                            self.io_timer_set = None
                            self.delayed_wakeup = None
                            self.wakeup = None
                            self.connect_wakeup = None
                            self.output_select = None
                            self.out_of_band_select = None
                            self._segment_path = lambda: "send-buf-state-flags"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags, ['locked', 'waiting_for_lock', 'waiting_for_data', 'input_select', 'async_io', 'not_interruptible', 'io_timer_set', 'delayed_wakeup', 'wakeup', 'connect_wakeup', 'output_select', 'out_of_band_select'], name, value)


                    class FibPdCtx(Entity):
                        """
                        Cached fib pd context
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibPdCtx, self).__init__()

                            self.yang_name = "fib-pd-ctx"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "fib-pd-ctx"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibPdCtx, ['entry'], name, value)


                    class FibLabelOutput(Entity):
                        """
                        Cached Label stack
                        
                        .. attribute:: entry
                        
                        	
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibLabelOutput, self).__init__()

                            self.yang_name = "fib-label-output"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('entry', YLeaf(YType.uint32, 'entry')),
                            ])
                            self.entry = None
                            self._segment_path = lambda: "fib-label-output"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FibLabelOutput, ['entry'], name, value)


                    class Timer(Entity):
                        """
                        Timers
                        
                        .. attribute:: timer_type
                        
                        	Timer Type
                        	**type**\:  :py:class:`TcpTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpTimer>`
                        
                        .. attribute:: timer_activations
                        
                        	Count of timer activations
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timer_expirations
                        
                        	Count of timer expirations
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: timer_next_activation
                        
                        	Timer next activation (msec)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer, self).__init__()

                            self.yang_name = "timer"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('timer_type', YLeaf(YType.enumeration, 'timer-type')),
                                ('timer_activations', YLeaf(YType.uint32, 'timer-activations')),
                                ('timer_expirations', YLeaf(YType.uint32, 'timer-expirations')),
                                ('timer_next_activation', YLeaf(YType.uint32, 'timer-next-activation')),
                            ])
                            self.timer_type = None
                            self.timer_activations = None
                            self.timer_expirations = None
                            self.timer_next_activation = None
                            self._segment_path = lambda: "timer"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer, ['timer_type', 'timer_activations', 'timer_expirations', 'timer_next_activation'], name, value)


                    class SackBlk(Entity):
                        """
                        Seq nos. of sack blocks
                        
                        .. attribute:: start
                        
                        	Start seq no. of sack block
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end
                        
                        	End   seq no. of sack block
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk, self).__init__()

                            self.yang_name = "sack-blk"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', YLeaf(YType.uint32, 'start')),
                                ('end', YLeaf(YType.uint32, 'end')),
                            ])
                            self.start = None
                            self.end = None
                            self._segment_path = lambda: "sack-blk"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk, ['start', 'end'], name, value)


                    class SendSackHole(Entity):
                        """
                        Sorted list of sack holes
                        
                        .. attribute:: start
                        
                        	Start seq no. of hole
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: end
                        
                        	End   seq no. of hole
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: duplicated_ack
                        
                        	Number of dup (s)acks for this hole
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: retransmitted
                        
                        	Next seq. no in hole to be retransmitted
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole, self).__init__()

                            self.yang_name = "send-sack-hole"
                            self.yang_parent_name = "detail-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('start', YLeaf(YType.uint32, 'start')),
                                ('end', YLeaf(YType.uint32, 'end')),
                                ('duplicated_ack', YLeaf(YType.uint32, 'duplicated-ack')),
                                ('retransmitted', YLeaf(YType.uint32, 'retransmitted')),
                            ])
                            self.start = None
                            self.end = None
                            self.duplicated_ack = None
                            self.retransmitted = None
                            self._segment_path = lambda: "send-sack-hole"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole, ['start', 'end', 'duplicated_ack', 'retransmitted'], name, value)


            class BriefInformations(Entity):
                """
                Table listing connections for which brief
                information is provided.Note that not all
                connections are listed in the brief table.
                
                .. attribute:: brief_information
                
                	Brief information about a TCP connection
                	**type**\: list of  		 :py:class:`BriefInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.BriefInformations.BriefInformation>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpConnection.Nodes.Node.BriefInformations, self).__init__()

                    self.yang_name = "brief-informations"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("brief-information", ("brief_information", TcpConnection.Nodes.Node.BriefInformations.BriefInformation))])
                    self._leafs = OrderedDict()

                    self.brief_information = YList(self)
                    self._segment_path = lambda: "brief-informations"

                def __setattr__(self, name, value):
                    self._perform_setattr(TcpConnection.Nodes.Node.BriefInformations, [], name, value)


                class BriefInformation(Entity):
                    """
                    Brief information about a TCP connection
                    
                    .. attribute:: pcb_id  (key)
                    
                    	Protocol Control Block ID
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress>`
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\:  :py:class:`TcpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpAddressFamily>`
                    
                    .. attribute:: pcb
                    
                    	PCB Address
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: connection_state
                    
                    	Connection state
                    	**type**\:  :py:class:`TcpConnState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpConnState>`
                    
                    .. attribute:: local_pid
                    
                    	Id of the local process
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
                    
                    .. attribute:: current_receive_queue_size
                    
                    	Current receive queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: current_send_queue_size
                    
                    	Current send queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: byte
                    
                    .. attribute:: vrf_id
                    
                    	VRF ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpConnection.Nodes.Node.BriefInformations.BriefInformation, self).__init__()

                        self.yang_name = "brief-information"
                        self.yang_parent_name = "brief-informations"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['pcb_id']
                        self._child_container_classes = OrderedDict([("local-address", ("local_address", TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress)), ("foreign-address", ("foreign_address", TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('pcb_id', YLeaf(YType.str, 'pcb-id')),
                            ('af_name', YLeaf(YType.enumeration, 'af-name')),
                            ('pcb', YLeaf(YType.uint64, 'pcb')),
                            ('connection_state', YLeaf(YType.enumeration, 'connection-state')),
                            ('local_pid', YLeaf(YType.uint32, 'local-pid')),
                            ('local_port', YLeaf(YType.uint16, 'local-port')),
                            ('foreign_port', YLeaf(YType.uint16, 'foreign-port')),
                            ('current_receive_queue_size', YLeaf(YType.uint32, 'current-receive-queue-size')),
                            ('current_send_queue_size', YLeaf(YType.uint32, 'current-send-queue-size')),
                            ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                        ])
                        self.pcb_id = None
                        self.af_name = None
                        self.pcb = None
                        self.connection_state = None
                        self.local_pid = None
                        self.local_port = None
                        self.foreign_port = None
                        self.current_receive_queue_size = None
                        self.current_send_queue_size = None
                        self.vrf_id = None

                        self.local_address = TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress()
                        self.local_address.parent = self
                        self._children_name_map["local_address"] = "local-address"
                        self._children_yang_names.add("local-address")

                        self.foreign_address = TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress()
                        self.foreign_address.parent = self
                        self._children_name_map["foreign_address"] = "foreign-address"
                        self._children_yang_names.add("foreign-address")
                        self._segment_path = lambda: "brief-information" + "[pcb-id='" + str(self.pcb_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpConnection.Nodes.Node.BriefInformations.BriefInformation, ['pcb_id', 'af_name', 'pcb', 'connection_state', 'local_pid', 'local_port', 'foreign_port', 'current_receive_queue_size', 'current_send_queue_size', 'vrf_id'], name, value)


                    class LocalAddress(Entity):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`TcpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress, self).__init__()

                            self.yang_name = "local-address"
                            self.yang_parent_name = "brief-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "local-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.BriefInformations.BriefInformation.LocalAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)


                    class ForeignAddress(Entity):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`TcpAddressFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpAddressFamily>`
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress, self).__init__()

                            self.yang_name = "foreign-address"
                            self.yang_parent_name = "brief-information"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('af_name', YLeaf(YType.enumeration, 'af-name')),
                                ('ipv4_address', YLeaf(YType.str, 'ipv4-address')),
                                ('ipv6_address', YLeaf(YType.str, 'ipv6-address')),
                            ])
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "foreign-address"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpConnection.Nodes.Node.BriefInformations.BriefInformation.ForeignAddress, ['af_name', 'ipv4_address', 'ipv6_address'], name, value)

    def clone_ptr(self):
        self._top_entity = TcpConnection()
        return self._top_entity

class Tcp(Entity):
    """
    tcp
    
    .. attribute:: nodes
    
    	Node\-specific TCP operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes>`
    
    

    """

    _prefix = 'ip-tcp-oper'
    _revision = '2018-02-14'

    def __init__(self):
        super(Tcp, self).__init__()
        self._top_entity = None

        self.yang_name = "tcp"
        self.yang_parent_name = "Cisco-IOS-XR-ip-tcp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", Tcp.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = Tcp.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp"


    class Nodes(Entity):
        """
        Node\-specific TCP operational data
        
        .. attribute:: node
        
        	TCP operational data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-tcp-oper'
        _revision = '2018-02-14'

        def __init__(self):
            super(Tcp.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "tcp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", Tcp.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Tcp.Nodes, [], name, value)


        class Node(Entity):
            """
            TCP operational data for a particular node
            
            .. attribute:: node_name  (key)
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistical TCP operational data for a node
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-tcp-oper'
            _revision = '2018-02-14'

            def __init__(self):
                super(Tcp.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node_name']
                self._child_container_classes = OrderedDict([("statistics", ("statistics", Tcp.Nodes.Node.Statistics))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('node_name', YLeaf(YType.str, 'node-name')),
                ])
                self.node_name = None

                self.statistics = Tcp.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")
                self._segment_path = lambda: "node" + "[node-name='" + str(self.node_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Tcp.Nodes.Node, ['node_name'], name, value)


            class Statistics(Entity):
                """
                Statistical TCP operational data for a node
                
                .. attribute:: ipv4_traffic
                
                	TCP Traffic statistics for IPv4
                	**type**\:  :py:class:`Ipv4Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node.Statistics.Ipv4Traffic>`
                
                .. attribute:: ipv6_traffic
                
                	TCP Traffic statistics for IPv6
                	**type**\:  :py:class:`Ipv6Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node.Statistics.Ipv6Traffic>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(Tcp.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("ipv4-traffic", ("ipv4_traffic", Tcp.Nodes.Node.Statistics.Ipv4Traffic)), ("ipv6-traffic", ("ipv6_traffic", Tcp.Nodes.Node.Statistics.Ipv6Traffic))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.ipv4_traffic = Tcp.Nodes.Node.Statistics.Ipv4Traffic()
                    self.ipv4_traffic.parent = self
                    self._children_name_map["ipv4_traffic"] = "ipv4-traffic"
                    self._children_yang_names.add("ipv4-traffic")

                    self.ipv6_traffic = Tcp.Nodes.Node.Statistics.Ipv6Traffic()
                    self.ipv6_traffic.parent = self
                    self._children_name_map["ipv6_traffic"] = "ipv6-traffic"
                    self._children_yang_names.add("ipv6-traffic")
                    self._segment_path = lambda: "statistics"


                class Ipv4Traffic(Entity):
                    """
                    TCP Traffic statistics for IPv4
                    
                    .. attribute:: tcp_input_packets
                    
                    	TCP packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_checksum_error_packets
                    
                    	TCP packets with checksum errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_dropped_packets
                    
                    	TCP packets dropped (no port)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_output_packets
                    
                    	TCP packets transmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_retransmitted_packets
                    
                    	TCP packets retransmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(Tcp.Nodes.Node.Statistics.Ipv4Traffic, self).__init__()

                        self.yang_name = "ipv4-traffic"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tcp_input_packets', YLeaf(YType.uint32, 'tcp-input-packets')),
                            ('tcp_checksum_error_packets', YLeaf(YType.uint32, 'tcp-checksum-error-packets')),
                            ('tcp_dropped_packets', YLeaf(YType.uint32, 'tcp-dropped-packets')),
                            ('tcp_output_packets', YLeaf(YType.uint32, 'tcp-output-packets')),
                            ('tcp_retransmitted_packets', YLeaf(YType.uint32, 'tcp-retransmitted-packets')),
                        ])
                        self.tcp_input_packets = None
                        self.tcp_checksum_error_packets = None
                        self.tcp_dropped_packets = None
                        self.tcp_output_packets = None
                        self.tcp_retransmitted_packets = None
                        self._segment_path = lambda: "ipv4-traffic"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tcp.Nodes.Node.Statistics.Ipv4Traffic, ['tcp_input_packets', 'tcp_checksum_error_packets', 'tcp_dropped_packets', 'tcp_output_packets', 'tcp_retransmitted_packets'], name, value)


                class Ipv6Traffic(Entity):
                    """
                    TCP Traffic statistics for IPv6
                    
                    .. attribute:: tcp_input_packets
                    
                    	TCP packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_checksum_error_packets
                    
                    	TCP packets with checksum errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_dropped_packets
                    
                    	TCP packets dropped (no port)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_output_packets
                    
                    	TCP packets transmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: tcp_retransmitted_packets
                    
                    	TCP packets retransmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(Tcp.Nodes.Node.Statistics.Ipv6Traffic, self).__init__()

                        self.yang_name = "ipv6-traffic"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('tcp_input_packets', YLeaf(YType.uint32, 'tcp-input-packets')),
                            ('tcp_checksum_error_packets', YLeaf(YType.uint32, 'tcp-checksum-error-packets')),
                            ('tcp_dropped_packets', YLeaf(YType.uint32, 'tcp-dropped-packets')),
                            ('tcp_output_packets', YLeaf(YType.uint32, 'tcp-output-packets')),
                            ('tcp_retransmitted_packets', YLeaf(YType.uint32, 'tcp-retransmitted-packets')),
                        ])
                        self.tcp_input_packets = None
                        self.tcp_checksum_error_packets = None
                        self.tcp_dropped_packets = None
                        self.tcp_output_packets = None
                        self.tcp_retransmitted_packets = None
                        self._segment_path = lambda: "ipv6-traffic"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Tcp.Nodes.Node.Statistics.Ipv6Traffic, ['tcp_input_packets', 'tcp_checksum_error_packets', 'tcp_dropped_packets', 'tcp_output_packets', 'tcp_retransmitted_packets'], name, value)

    def clone_ptr(self):
        self._top_entity = Tcp()
        return self._top_entity

class TcpNsr(Entity):
    """
    tcp nsr
    
    .. attribute:: nodes
    
    	Table of information about all nodes present on the system
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes>`
    
    

    """

    _prefix = 'ip-tcp-oper'
    _revision = '2018-02-14'

    def __init__(self):
        super(TcpNsr, self).__init__()
        self._top_entity = None

        self.yang_name = "tcp-nsr"
        self.yang_parent_name = "Cisco-IOS-XR-ip-tcp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("nodes", ("nodes", TcpNsr.Nodes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.nodes = TcpNsr.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp-nsr"


    class Nodes(Entity):
        """
        Table of information about all nodes present on
        the system
        
        .. attribute:: node
        
        	Information about a single node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node>`
        
        

        """

        _prefix = 'ip-tcp-oper'
        _revision = '2018-02-14'

        def __init__(self):
            super(TcpNsr.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "tcp-nsr"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("node", ("node", TcpNsr.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp-nsr/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(TcpNsr.Nodes, [], name, value)


        class Node(Entity):
            """
            Information about a single node
            
            .. attribute:: id  (key)
            
            	Describing a location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: session
            
            	Information about TCP NSR Sessions
            	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session>`
            
            .. attribute:: client
            
            	Information about TCP NSR Client
            	**type**\:  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client>`
            
            .. attribute:: session_set
            
            	Information about TCP NSR Session Sets
            	**type**\:  :py:class:`SessionSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet>`
            
            .. attribute:: statistics
            
            	Statis Information about TCP NSR connections
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-tcp-oper'
            _revision = '2018-02-14'

            def __init__(self):
                super(TcpNsr.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_container_classes = OrderedDict([("session", ("session", TcpNsr.Nodes.Node.Session)), ("client", ("client", TcpNsr.Nodes.Node.Client)), ("session-set", ("session_set", TcpNsr.Nodes.Node.SessionSet)), ("statistics", ("statistics", TcpNsr.Nodes.Node.Statistics))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id', YLeaf(YType.str, 'id')),
                ])
                self.id = None

                self.session = TcpNsr.Nodes.Node.Session()
                self.session.parent = self
                self._children_name_map["session"] = "session"
                self._children_yang_names.add("session")

                self.client = TcpNsr.Nodes.Node.Client()
                self.client.parent = self
                self._children_name_map["client"] = "client"
                self._children_yang_names.add("client")

                self.session_set = TcpNsr.Nodes.Node.SessionSet()
                self.session_set.parent = self
                self._children_name_map["session_set"] = "session-set"
                self._children_yang_names.add("session-set")

                self.statistics = TcpNsr.Nodes.Node.Statistics()
                self.statistics.parent = self
                self._children_name_map["statistics"] = "statistics"
                self._children_yang_names.add("statistics")
                self._segment_path = lambda: "node" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ip-tcp-oper:tcp-nsr/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(TcpNsr.Nodes.Node, ['id'], name, value)


            class Session(Entity):
                """
                Information about TCP NSR Sessions
                
                .. attribute:: brief_sessions
                
                	Information about TCP NSR Sessions
                	**type**\:  :py:class:`BriefSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.BriefSessions>`
                
                .. attribute:: detail_sessions
                
                	Table about TCP NSR Sessions details
                	**type**\:  :py:class:`DetailSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpNsr.Nodes.Node.Session, self).__init__()

                    self.yang_name = "session"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("brief-sessions", ("brief_sessions", TcpNsr.Nodes.Node.Session.BriefSessions)), ("detail-sessions", ("detail_sessions", TcpNsr.Nodes.Node.Session.DetailSessions))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.brief_sessions = TcpNsr.Nodes.Node.Session.BriefSessions()
                    self.brief_sessions.parent = self
                    self._children_name_map["brief_sessions"] = "brief-sessions"
                    self._children_yang_names.add("brief-sessions")

                    self.detail_sessions = TcpNsr.Nodes.Node.Session.DetailSessions()
                    self.detail_sessions.parent = self
                    self._children_name_map["detail_sessions"] = "detail-sessions"
                    self._children_yang_names.add("detail-sessions")
                    self._segment_path = lambda: "session"


                class BriefSessions(Entity):
                    """
                    Information about TCP NSR Sessions
                    
                    .. attribute:: brief_session
                    
                    	Brief information about NSR Sessions
                    	**type**\: list of  		 :py:class:`BriefSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Session.BriefSessions, self).__init__()

                        self.yang_name = "brief-sessions"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("brief-session", ("brief_session", TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession))])
                        self._leafs = OrderedDict()

                        self.brief_session = YList(self)
                        self._segment_path = lambda: "brief-sessions"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Session.BriefSessions, [], name, value)


                    class BriefSession(Entity):
                        """
                        Brief information about NSR Sessions
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR Sesison
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: address_family
                        
                        	Address family
                        	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                        
                        .. attribute:: pcb
                        
                        	PCB Address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sscb
                        
                        	SSCB Address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: local_port
                        
                        	Local port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: foreign_port
                        
                        	Foreign port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vrf_id
                        
                        	VRF Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_admin_configured_up
                        
                        	Is NSR administratively configured?
                        	**type**\: bool
                        
                        .. attribute:: is_us_operational_up
                        
                        	Is Upstream NSR operational?
                        	**type**\:  :py:class:`NsrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.NsrStatus>`
                        
                        .. attribute:: is_ds_operational_up
                        
                        	Is Downstream NSR operational?
                        	**type**\:  :py:class:`NsrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.NsrStatus>`
                        
                        .. attribute:: is_only_receive_path_replication
                        
                        	Is replication limited to receive\-path only
                        	**type**\: bool
                        
                        .. attribute:: local_address
                        
                        	Local address
                        	**type**\: list of  		 :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.LocalAddress>`
                        
                        .. attribute:: foreign_address
                        
                        	Foreign address
                        	**type**\: list of  		 :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.ForeignAddress>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession, self).__init__()

                            self.yang_name = "brief-session"
                            self.yang_parent_name = "brief-sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("local-address", ("local_address", TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.LocalAddress)), ("foreign-address", ("foreign_address", TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.ForeignAddress))])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('address_family', YLeaf(YType.enumeration, 'address-family')),
                                ('pcb', YLeaf(YType.uint64, 'pcb')),
                                ('sscb', YLeaf(YType.uint64, 'sscb')),
                                ('local_port', YLeaf(YType.uint16, 'local-port')),
                                ('foreign_port', YLeaf(YType.uint16, 'foreign-port')),
                                ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                                ('is_admin_configured_up', YLeaf(YType.boolean, 'is-admin-configured-up')),
                                ('is_us_operational_up', YLeaf(YType.enumeration, 'is-us-operational-up')),
                                ('is_ds_operational_up', YLeaf(YType.enumeration, 'is-ds-operational-up')),
                                ('is_only_receive_path_replication', YLeaf(YType.boolean, 'is-only-receive-path-replication')),
                            ])
                            self.id = None
                            self.address_family = None
                            self.pcb = None
                            self.sscb = None
                            self.local_port = None
                            self.foreign_port = None
                            self.vrf_id = None
                            self.is_admin_configured_up = None
                            self.is_us_operational_up = None
                            self.is_ds_operational_up = None
                            self.is_only_receive_path_replication = None

                            self.local_address = YList(self)
                            self.foreign_address = YList(self)
                            self._segment_path = lambda: "brief-session" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession, ['id', 'address_family', 'pcb', 'sscb', 'local_port', 'foreign_port', 'vrf_id', 'is_admin_configured_up', 'is_us_operational_up', 'is_ds_operational_up', 'is_only_receive_path_replication'], name, value)


                        class LocalAddress(Entity):
                            """
                            Local address
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.LocalAddress, self).__init__()

                                self.yang_name = "local-address"
                                self.yang_parent_name = "brief-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.str, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "local-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.LocalAddress, ['entry'], name, value)


                        class ForeignAddress(Entity):
                            """
                            Foreign address
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.ForeignAddress, self).__init__()

                                self.yang_name = "foreign-address"
                                self.yang_parent_name = "brief-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.str, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "foreign-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession.ForeignAddress, ['entry'], name, value)


                class DetailSessions(Entity):
                    """
                    Table about TCP NSR Sessions details
                    
                    .. attribute:: detail_session
                    
                    	showing detailed information of NSR Sessions
                    	**type**\: list of  		 :py:class:`DetailSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Session.DetailSessions, self).__init__()

                        self.yang_name = "detail-sessions"
                        self.yang_parent_name = "session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("detail-session", ("detail_session", TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession))])
                        self._leafs = OrderedDict()

                        self.detail_session = YList(self)
                        self._segment_path = lambda: "detail-sessions"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Session.DetailSessions, [], name, value)


                    class DetailSession(Entity):
                        """
                        showing detailed information of NSR Sessions
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR Sesison
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: set_information
                        
                        	Sesson\-set information
                        	**type**\:  :py:class:`SetInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation>`
                        
                        .. attribute:: address_family
                        
                        	Address family
                        	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                        
                        .. attribute:: pcb
                        
                        	PCB Address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: sscb
                        
                        	SSCB Address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: local_port
                        
                        	Local port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: foreign_port
                        
                        	Foreign port
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: vrf_id
                        
                        	VRF Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_admin_configured_up
                        
                        	Is NSR administratively configured?
                        	**type**\: bool
                        
                        .. attribute:: is_us_operational_up
                        
                        	Is Upstream NSR operational?
                        	**type**\:  :py:class:`NsrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.NsrStatus>`
                        
                        .. attribute:: is_ds_operational_up
                        
                        	Is Downstream NSR operational?
                        	**type**\:  :py:class:`NsrStatus <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.NsrStatus>`
                        
                        .. attribute:: is_only_receive_path_replication
                        
                        	Is replication limited to receive\-path only
                        	**type**\: bool
                        
                        .. attribute:: cookie
                        
                        	Cookie provided by active APP
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: is_session_replicated
                        
                        	Has the session been replicated to standby?
                        	**type**\: bool
                        
                        .. attribute:: is_session_synced
                        
                        	Has the session completed initial\-sync?
                        	**type**\: bool
                        
                        .. attribute:: fist_standby_sequence_number
                        
                        	If initial sync is completed, then the FSSN \- First Standby Sequence Number
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fssn_offset
                        
                        	Offset of FSSN in input stream
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nsr_down_reason
                        
                        	If NSR is not up, the reason for it
                        	**type**\:  :py:class:`NsrDownReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.NsrDownReason>`
                        
                        .. attribute:: nsr_down_time
                        
                        	Time at which NSR went down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sequence_number_of_init_sync
                        
                        	ID of the Initial sync operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_init_sync_in_progress
                        
                        	Is initial\-sync currently in progress?
                        	**type**\: bool
                        
                        .. attribute:: is_init_sync_second_phase
                        
                        	Is initial sync in the second phase?
                        	**type**\: bool
                        
                        .. attribute:: init_sync_error
                        
                        	Initial sync failure reason, if any
                        	**type**\: str
                        
                        .. attribute:: is_init_sync_error_local
                        
                        	Initial sync failed due to a local error or remote stack
                        	**type**\: bool
                        
                        .. attribute:: init_sync_start_time
                        
                        	Time at which the initial sync operation was started (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: init_sync_end_time
                        
                        	Time at which the initial sync operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: init_sync_flags
                        
                        	Init Sync flags for the session
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sequence_number_of_init_sync_up_stream
                        
                        	ID of the Initial sync operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_endp_hdl_up_stream
                        
                        	Peer NCD endp handle
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: init_sync_start_time_up_stream
                        
                        	Time at which the initial sync operation was started (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: init_sync_end_time_up_stream
                        
                        	Time at which the initial sync operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: fist_standby_sequence_number_up_stream
                        
                        	FSSN for the upstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nsr_down_reason_up_stream
                        
                        	The reason NSR is not up towards the upstream partner
                        	**type**\:  :py:class:`NsrDownReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.NsrDownReason>`
                        
                        .. attribute:: nsr_down_time_up_stream
                        
                        	Time at which NSR went down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sequence_number_of_init_sync_down_stream
                        
                        	ID of the Initial sync operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: peer_endp_hdl_down_stream
                        
                        	Peer NCD endp handle
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: init_sync_start_time_down_stream
                        
                        	Time at which the initial sync operation was started (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: init_sync_end_time_down_stream
                        
                        	Time at which the initial sync operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: fist_standby_sequence_number_down_stream
                        
                        	FSSN for the upstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nsr_down_reason_down_stream
                        
                        	The reason NSR is not up towards the upstream partner
                        	**type**\:  :py:class:`NsrDownReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.NsrDownReason>`
                        
                        .. attribute:: nsr_down_time_down_stream
                        
                        	Time at which NSR went down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: max_number_of_held_packet
                        
                        	Max number of incoming packets have been held
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: max_number_of_held_packet_reach_time
                        
                        	Max number of held incoming packets reaches at
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: max_number_of_held_internal_ack
                        
                        	Max number of internal acks have been held
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: max_number_of_held_internal_ack_reach_time
                        
                        	Max number of held internal acks reaches at
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: local_address
                        
                        	Local address
                        	**type**\: list of  		 :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.LocalAddress>`
                        
                        .. attribute:: foreign_address
                        
                        	Foreign address
                        	**type**\: list of  		 :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.ForeignAddress>`
                        
                        .. attribute:: packet_hold_queue
                        
                        	Sequence Number and datalength of each node in hold\_pakqueue
                        	**type**\: list of  		 :py:class:`PacketHoldQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue>`
                        
                        .. attribute:: internal_ack_hold_queue
                        
                        	Sequence Number and datalength of each node in hold\_iackqueue
                        	**type**\: list of  		 :py:class:`InternalAckHoldQueue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession, self).__init__()

                            self.yang_name = "detail-session"
                            self.yang_parent_name = "detail-sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([("set-information", ("set_information", TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation))])
                            self._child_list_classes = OrderedDict([("local-address", ("local_address", TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.LocalAddress)), ("foreign-address", ("foreign_address", TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.ForeignAddress)), ("packet-hold-queue", ("packet_hold_queue", TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue)), ("internal-ack-hold-queue", ("internal_ack_hold_queue", TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue))])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('address_family', YLeaf(YType.enumeration, 'address-family')),
                                ('pcb', YLeaf(YType.uint64, 'pcb')),
                                ('sscb', YLeaf(YType.uint64, 'sscb')),
                                ('local_port', YLeaf(YType.uint16, 'local-port')),
                                ('foreign_port', YLeaf(YType.uint16, 'foreign-port')),
                                ('vrf_id', YLeaf(YType.uint32, 'vrf-id')),
                                ('is_admin_configured_up', YLeaf(YType.boolean, 'is-admin-configured-up')),
                                ('is_us_operational_up', YLeaf(YType.enumeration, 'is-us-operational-up')),
                                ('is_ds_operational_up', YLeaf(YType.enumeration, 'is-ds-operational-up')),
                                ('is_only_receive_path_replication', YLeaf(YType.boolean, 'is-only-receive-path-replication')),
                                ('cookie', YLeaf(YType.uint64, 'cookie')),
                                ('is_session_replicated', YLeaf(YType.boolean, 'is-session-replicated')),
                                ('is_session_synced', YLeaf(YType.boolean, 'is-session-synced')),
                                ('fist_standby_sequence_number', YLeaf(YType.uint32, 'fist-standby-sequence-number')),
                                ('fssn_offset', YLeaf(YType.uint32, 'fssn-offset')),
                                ('nsr_down_reason', YLeaf(YType.enumeration, 'nsr-down-reason')),
                                ('nsr_down_time', YLeaf(YType.uint32, 'nsr-down-time')),
                                ('sequence_number_of_init_sync', YLeaf(YType.uint32, 'sequence-number-of-init-sync')),
                                ('is_init_sync_in_progress', YLeaf(YType.boolean, 'is-init-sync-in-progress')),
                                ('is_init_sync_second_phase', YLeaf(YType.boolean, 'is-init-sync-second-phase')),
                                ('init_sync_error', YLeaf(YType.str, 'init-sync-error')),
                                ('is_init_sync_error_local', YLeaf(YType.boolean, 'is-init-sync-error-local')),
                                ('init_sync_start_time', YLeaf(YType.uint32, 'init-sync-start-time')),
                                ('init_sync_end_time', YLeaf(YType.uint32, 'init-sync-end-time')),
                                ('init_sync_flags', YLeaf(YType.uint32, 'init-sync-flags')),
                                ('sequence_number_of_init_sync_up_stream', YLeaf(YType.uint32, 'sequence-number-of-init-sync-up-stream')),
                                ('peer_endp_hdl_up_stream', YLeaf(YType.uint64, 'peer-endp-hdl-up-stream')),
                                ('init_sync_start_time_up_stream', YLeaf(YType.uint32, 'init-sync-start-time-up-stream')),
                                ('init_sync_end_time_up_stream', YLeaf(YType.uint32, 'init-sync-end-time-up-stream')),
                                ('fist_standby_sequence_number_up_stream', YLeaf(YType.uint32, 'fist-standby-sequence-number-up-stream')),
                                ('nsr_down_reason_up_stream', YLeaf(YType.enumeration, 'nsr-down-reason-up-stream')),
                                ('nsr_down_time_up_stream', YLeaf(YType.uint32, 'nsr-down-time-up-stream')),
                                ('sequence_number_of_init_sync_down_stream', YLeaf(YType.uint32, 'sequence-number-of-init-sync-down-stream')),
                                ('peer_endp_hdl_down_stream', YLeaf(YType.uint64, 'peer-endp-hdl-down-stream')),
                                ('init_sync_start_time_down_stream', YLeaf(YType.uint32, 'init-sync-start-time-down-stream')),
                                ('init_sync_end_time_down_stream', YLeaf(YType.uint32, 'init-sync-end-time-down-stream')),
                                ('fist_standby_sequence_number_down_stream', YLeaf(YType.uint32, 'fist-standby-sequence-number-down-stream')),
                                ('nsr_down_reason_down_stream', YLeaf(YType.enumeration, 'nsr-down-reason-down-stream')),
                                ('nsr_down_time_down_stream', YLeaf(YType.uint32, 'nsr-down-time-down-stream')),
                                ('max_number_of_held_packet', YLeaf(YType.int32, 'max-number-of-held-packet')),
                                ('max_number_of_held_packet_reach_time', YLeaf(YType.uint32, 'max-number-of-held-packet-reach-time')),
                                ('max_number_of_held_internal_ack', YLeaf(YType.int32, 'max-number-of-held-internal-ack')),
                                ('max_number_of_held_internal_ack_reach_time', YLeaf(YType.uint32, 'max-number-of-held-internal-ack-reach-time')),
                            ])
                            self.id = None
                            self.address_family = None
                            self.pcb = None
                            self.sscb = None
                            self.local_port = None
                            self.foreign_port = None
                            self.vrf_id = None
                            self.is_admin_configured_up = None
                            self.is_us_operational_up = None
                            self.is_ds_operational_up = None
                            self.is_only_receive_path_replication = None
                            self.cookie = None
                            self.is_session_replicated = None
                            self.is_session_synced = None
                            self.fist_standby_sequence_number = None
                            self.fssn_offset = None
                            self.nsr_down_reason = None
                            self.nsr_down_time = None
                            self.sequence_number_of_init_sync = None
                            self.is_init_sync_in_progress = None
                            self.is_init_sync_second_phase = None
                            self.init_sync_error = None
                            self.is_init_sync_error_local = None
                            self.init_sync_start_time = None
                            self.init_sync_end_time = None
                            self.init_sync_flags = None
                            self.sequence_number_of_init_sync_up_stream = None
                            self.peer_endp_hdl_up_stream = None
                            self.init_sync_start_time_up_stream = None
                            self.init_sync_end_time_up_stream = None
                            self.fist_standby_sequence_number_up_stream = None
                            self.nsr_down_reason_up_stream = None
                            self.nsr_down_time_up_stream = None
                            self.sequence_number_of_init_sync_down_stream = None
                            self.peer_endp_hdl_down_stream = None
                            self.init_sync_start_time_down_stream = None
                            self.init_sync_end_time_down_stream = None
                            self.fist_standby_sequence_number_down_stream = None
                            self.nsr_down_reason_down_stream = None
                            self.nsr_down_time_down_stream = None
                            self.max_number_of_held_packet = None
                            self.max_number_of_held_packet_reach_time = None
                            self.max_number_of_held_internal_ack = None
                            self.max_number_of_held_internal_ack_reach_time = None

                            self.set_information = TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation()
                            self.set_information.parent = self
                            self._children_name_map["set_information"] = "set-information"
                            self._children_yang_names.add("set-information")

                            self.local_address = YList(self)
                            self.foreign_address = YList(self)
                            self.packet_hold_queue = YList(self)
                            self.internal_ack_hold_queue = YList(self)
                            self._segment_path = lambda: "detail-session" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession, ['id', 'address_family', 'pcb', 'sscb', 'local_port', 'foreign_port', 'vrf_id', 'is_admin_configured_up', 'is_us_operational_up', 'is_ds_operational_up', 'is_only_receive_path_replication', 'cookie', 'is_session_replicated', 'is_session_synced', 'fist_standby_sequence_number', 'fssn_offset', 'nsr_down_reason', 'nsr_down_time', 'sequence_number_of_init_sync', 'is_init_sync_in_progress', 'is_init_sync_second_phase', 'init_sync_error', 'is_init_sync_error_local', 'init_sync_start_time', 'init_sync_end_time', 'init_sync_flags', 'sequence_number_of_init_sync_up_stream', 'peer_endp_hdl_up_stream', 'init_sync_start_time_up_stream', 'init_sync_end_time_up_stream', 'fist_standby_sequence_number_up_stream', 'nsr_down_reason_up_stream', 'nsr_down_time_up_stream', 'sequence_number_of_init_sync_down_stream', 'peer_endp_hdl_down_stream', 'init_sync_start_time_down_stream', 'init_sync_end_time_down_stream', 'fist_standby_sequence_number_down_stream', 'nsr_down_reason_down_stream', 'nsr_down_time_down_stream', 'max_number_of_held_packet', 'max_number_of_held_packet_reach_time', 'max_number_of_held_internal_ack', 'max_number_of_held_internal_ack_reach_time'], name, value)


                        class SetInformation(Entity):
                            """
                            Sesson\-set information
                            
                            .. attribute:: sscb
                            
                            	Address of the Session Set Control Block
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: pid
                            
                            	PID of the Client that owns this Session\-set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: client_name
                            
                            	the name of Clinet that owns this Session\-set
                            	**type**\: str
                            
                            .. attribute:: client_instance
                            
                            	Instance of the Client that owns this Session\-set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: set_id
                            
                            	ID of this Session\-set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sso_role
                            
                            	TCP role for this set?
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mode
                            
                            	Session\-set mode
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: address_family
                            
                            	Address Family of the sessions in this set
                            	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                            
                            .. attribute:: well_known_port
                            
                            	Well Known Port of the client
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: local_node
                            
                            	Local node of this set
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: local_instance
                            
                            	Instance of the client application on the local node
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: protect_node
                            
                            	The node protecting this set
                            	**type**\: str
                            
                            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                            
                            .. attribute:: protect_instance
                            
                            	Instance of the client application on the protection node
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: number_of_sessions
                            
                            	Number of Sessions in the set
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: number_of_synced_sessions_up_stream
                            
                            	How many sessions are synced with upstream partner
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: number_of_synced_sessions_down_stream
                            
                            	How many sessions are synced with downstream partner
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: is_init_sync_in_progress
                            
                            	Is an initial sync in progress currently?
                            	**type**\: bool
                            
                            .. attribute:: is_sscb_init_sync_ready
                            
                            	Is the SSCB ready for another initial sync?
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation, self).__init__()

                                self.yang_name = "set-information"
                                self.yang_parent_name = "detail-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sscb', YLeaf(YType.uint64, 'sscb')),
                                    ('pid', YLeaf(YType.uint32, 'pid')),
                                    ('client_name', YLeaf(YType.str, 'client-name')),
                                    ('client_instance', YLeaf(YType.uint32, 'client-instance')),
                                    ('set_id', YLeaf(YType.uint32, 'set-id')),
                                    ('sso_role', YLeaf(YType.uint32, 'sso-role')),
                                    ('mode', YLeaf(YType.uint32, 'mode')),
                                    ('address_family', YLeaf(YType.enumeration, 'address-family')),
                                    ('well_known_port', YLeaf(YType.uint16, 'well-known-port')),
                                    ('local_node', YLeaf(YType.str, 'local-node')),
                                    ('local_instance', YLeaf(YType.uint32, 'local-instance')),
                                    ('protect_node', YLeaf(YType.str, 'protect-node')),
                                    ('protect_instance', YLeaf(YType.uint32, 'protect-instance')),
                                    ('number_of_sessions', YLeaf(YType.uint32, 'number-of-sessions')),
                                    ('number_of_synced_sessions_up_stream', YLeaf(YType.uint32, 'number-of-synced-sessions-up-stream')),
                                    ('number_of_synced_sessions_down_stream', YLeaf(YType.uint32, 'number-of-synced-sessions-down-stream')),
                                    ('is_init_sync_in_progress', YLeaf(YType.boolean, 'is-init-sync-in-progress')),
                                    ('is_sscb_init_sync_ready', YLeaf(YType.boolean, 'is-sscb-init-sync-ready')),
                                ])
                                self.sscb = None
                                self.pid = None
                                self.client_name = None
                                self.client_instance = None
                                self.set_id = None
                                self.sso_role = None
                                self.mode = None
                                self.address_family = None
                                self.well_known_port = None
                                self.local_node = None
                                self.local_instance = None
                                self.protect_node = None
                                self.protect_instance = None
                                self.number_of_sessions = None
                                self.number_of_synced_sessions_up_stream = None
                                self.number_of_synced_sessions_down_stream = None
                                self.is_init_sync_in_progress = None
                                self.is_sscb_init_sync_ready = None
                                self._segment_path = lambda: "set-information"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation, ['sscb', 'pid', 'client_name', 'client_instance', 'set_id', 'sso_role', 'mode', 'address_family', 'well_known_port', 'local_node', 'local_instance', 'protect_node', 'protect_instance', 'number_of_sessions', 'number_of_synced_sessions_up_stream', 'number_of_synced_sessions_down_stream', 'is_init_sync_in_progress', 'is_sscb_init_sync_ready'], name, value)


                        class LocalAddress(Entity):
                            """
                            Local address
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.LocalAddress, self).__init__()

                                self.yang_name = "local-address"
                                self.yang_parent_name = "detail-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.str, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "local-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.LocalAddress, ['entry'], name, value)


                        class ForeignAddress(Entity):
                            """
                            Foreign address
                            
                            .. attribute:: entry
                            
                            	
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.ForeignAddress, self).__init__()

                                self.yang_name = "foreign-address"
                                self.yang_parent_name = "detail-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('entry', YLeaf(YType.str, 'entry')),
                                ])
                                self.entry = None
                                self._segment_path = lambda: "foreign-address"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.ForeignAddress, ['entry'], name, value)


                        class PacketHoldQueue(Entity):
                            """
                            Sequence Number and datalength of each node in
                            hold\_pakqueue
                            
                            .. attribute:: sequence_number
                            
                            	Sequence Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_length
                            
                            	Data Length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknoledgement_number
                            
                            	Ack Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue, self).__init__()

                                self.yang_name = "packet-hold-queue"
                                self.yang_parent_name = "detail-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sequence_number', YLeaf(YType.uint32, 'sequence-number')),
                                    ('data_length', YLeaf(YType.uint32, 'data-length')),
                                    ('acknoledgement_number', YLeaf(YType.uint32, 'acknoledgement-number')),
                                ])
                                self.sequence_number = None
                                self.data_length = None
                                self.acknoledgement_number = None
                                self._segment_path = lambda: "packet-hold-queue"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue, ['sequence_number', 'data_length', 'acknoledgement_number'], name, value)


                        class InternalAckHoldQueue(Entity):
                            """
                            Sequence Number and datalength of each node in
                            hold\_iackqueue
                            
                            .. attribute:: sequence_number
                            
                            	Sequence Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_length
                            
                            	Data Length
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: acknoledgement_number
                            
                            	Ack Number
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue, self).__init__()

                                self.yang_name = "internal-ack-hold-queue"
                                self.yang_parent_name = "detail-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('sequence_number', YLeaf(YType.uint32, 'sequence-number')),
                                    ('data_length', YLeaf(YType.uint32, 'data-length')),
                                    ('acknoledgement_number', YLeaf(YType.uint32, 'acknoledgement-number')),
                                ])
                                self.sequence_number = None
                                self.data_length = None
                                self.acknoledgement_number = None
                                self._segment_path = lambda: "internal-ack-hold-queue"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue, ['sequence_number', 'data_length', 'acknoledgement_number'], name, value)


            class Client(Entity):
                """
                Information about TCP NSR Client
                
                .. attribute:: detail_clients
                
                	Table about TCP NSR Client details
                	**type**\:  :py:class:`DetailClients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.DetailClients>`
                
                .. attribute:: brief_clients
                
                	Information about TCP NSR Client
                	**type**\:  :py:class:`BriefClients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.BriefClients>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpNsr.Nodes.Node.Client, self).__init__()

                    self.yang_name = "client"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("detail-clients", ("detail_clients", TcpNsr.Nodes.Node.Client.DetailClients)), ("brief-clients", ("brief_clients", TcpNsr.Nodes.Node.Client.BriefClients))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.detail_clients = TcpNsr.Nodes.Node.Client.DetailClients()
                    self.detail_clients.parent = self
                    self._children_name_map["detail_clients"] = "detail-clients"
                    self._children_yang_names.add("detail-clients")

                    self.brief_clients = TcpNsr.Nodes.Node.Client.BriefClients()
                    self.brief_clients.parent = self
                    self._children_name_map["brief_clients"] = "brief-clients"
                    self._children_yang_names.add("brief-clients")
                    self._segment_path = lambda: "client"


                class DetailClients(Entity):
                    """
                    Table about TCP NSR Client details
                    
                    .. attribute:: detail_client
                    
                    	showing detailed information of NSR Clients
                    	**type**\: list of  		 :py:class:`DetailClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.DetailClients.DetailClient>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Client.DetailClients, self).__init__()

                        self.yang_name = "detail-clients"
                        self.yang_parent_name = "client"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("detail-client", ("detail_client", TcpNsr.Nodes.Node.Client.DetailClients.DetailClient))])
                        self._leafs = OrderedDict()

                        self.detail_client = YList(self)
                        self._segment_path = lambda: "detail-clients"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Client.DetailClients, [], name, value)


                    class DetailClient(Entity):
                        """
                        showing detailed information of NSR Clients
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR client
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: ccb
                        
                        	Address of the Client Control Block
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pid
                        
                        	PID of the Client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: process_name
                        
                        	Proc name of Clinet
                        	**type**\: str
                        
                        .. attribute:: job_id
                        
                        	JOb ID of Client
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: instance
                        
                        	Instance of the Client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: numberof_sets
                        
                        	Number of Sets owned by this client 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_sessions
                        
                        	Number of sessions owned by this client 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_up_sessions
                        
                        	Number of sessions with NSR up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: connected_at
                        
                        	Time of connect (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: is_notification_registered
                        
                        	Registered with TCP for notifications?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Client.DetailClients.DetailClient, self).__init__()

                            self.yang_name = "detail-client"
                            self.yang_parent_name = "detail-clients"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('ccb', YLeaf(YType.uint64, 'ccb')),
                                ('pid', YLeaf(YType.uint32, 'pid')),
                                ('process_name', YLeaf(YType.str, 'process-name')),
                                ('job_id', YLeaf(YType.int32, 'job-id')),
                                ('instance', YLeaf(YType.uint32, 'instance')),
                                ('numberof_sets', YLeaf(YType.uint32, 'numberof-sets')),
                                ('number_of_sessions', YLeaf(YType.uint32, 'number-of-sessions')),
                                ('number_of_up_sessions', YLeaf(YType.uint32, 'number-of-up-sessions')),
                                ('connected_at', YLeaf(YType.uint32, 'connected-at')),
                                ('is_notification_registered', YLeaf(YType.boolean, 'is-notification-registered')),
                            ])
                            self.id = None
                            self.ccb = None
                            self.pid = None
                            self.process_name = None
                            self.job_id = None
                            self.instance = None
                            self.numberof_sets = None
                            self.number_of_sessions = None
                            self.number_of_up_sessions = None
                            self.connected_at = None
                            self.is_notification_registered = None
                            self._segment_path = lambda: "detail-client" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Client.DetailClients.DetailClient, ['id', 'ccb', 'pid', 'process_name', 'job_id', 'instance', 'numberof_sets', 'number_of_sessions', 'number_of_up_sessions', 'connected_at', 'is_notification_registered'], name, value)


                class BriefClients(Entity):
                    """
                    Information about TCP NSR Client
                    
                    .. attribute:: brief_client
                    
                    	Brief information about NSR Client
                    	**type**\: list of  		 :py:class:`BriefClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.BriefClients.BriefClient>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Client.BriefClients, self).__init__()

                        self.yang_name = "brief-clients"
                        self.yang_parent_name = "client"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("brief-client", ("brief_client", TcpNsr.Nodes.Node.Client.BriefClients.BriefClient))])
                        self._leafs = OrderedDict()

                        self.brief_client = YList(self)
                        self._segment_path = lambda: "brief-clients"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Client.BriefClients, [], name, value)


                    class BriefClient(Entity):
                        """
                        Brief information about NSR Client
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR client
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: ccb
                        
                        	Address of the Client Control Block
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pid
                        
                        	PID of the Client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: process_name
                        
                        	Proc name of Clinet
                        	**type**\: str
                        
                        .. attribute:: job_id
                        
                        	JOb ID of Client
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: instance
                        
                        	Instance of the Client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: numberof_sets
                        
                        	Number of Sets owned by this client 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_sessions
                        
                        	Number of sessions owned by this client 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_up_sessions
                        
                        	Number of sessions with NSR up 
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Client.BriefClients.BriefClient, self).__init__()

                            self.yang_name = "brief-client"
                            self.yang_parent_name = "brief-clients"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('ccb', YLeaf(YType.uint64, 'ccb')),
                                ('pid', YLeaf(YType.uint32, 'pid')),
                                ('process_name', YLeaf(YType.str, 'process-name')),
                                ('job_id', YLeaf(YType.int32, 'job-id')),
                                ('instance', YLeaf(YType.uint32, 'instance')),
                                ('numberof_sets', YLeaf(YType.uint32, 'numberof-sets')),
                                ('number_of_sessions', YLeaf(YType.uint32, 'number-of-sessions')),
                                ('number_of_up_sessions', YLeaf(YType.uint32, 'number-of-up-sessions')),
                            ])
                            self.id = None
                            self.ccb = None
                            self.pid = None
                            self.process_name = None
                            self.job_id = None
                            self.instance = None
                            self.numberof_sets = None
                            self.number_of_sessions = None
                            self.number_of_up_sessions = None
                            self._segment_path = lambda: "brief-client" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Client.BriefClients.BriefClient, ['id', 'ccb', 'pid', 'process_name', 'job_id', 'instance', 'numberof_sets', 'number_of_sessions', 'number_of_up_sessions'], name, value)


            class SessionSet(Entity):
                """
                Information about TCP NSR Session Sets
                
                .. attribute:: detail_sets
                
                	Table about TCP NSR Session Sets details
                	**type**\:  :py:class:`DetailSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.DetailSets>`
                
                .. attribute:: brief_sets
                
                	Information about TCP NSR Session Sets
                	**type**\:  :py:class:`BriefSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.BriefSets>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpNsr.Nodes.Node.SessionSet, self).__init__()

                    self.yang_name = "session-set"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("detail-sets", ("detail_sets", TcpNsr.Nodes.Node.SessionSet.DetailSets)), ("brief-sets", ("brief_sets", TcpNsr.Nodes.Node.SessionSet.BriefSets))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.detail_sets = TcpNsr.Nodes.Node.SessionSet.DetailSets()
                    self.detail_sets.parent = self
                    self._children_name_map["detail_sets"] = "detail-sets"
                    self._children_yang_names.add("detail-sets")

                    self.brief_sets = TcpNsr.Nodes.Node.SessionSet.BriefSets()
                    self.brief_sets.parent = self
                    self._children_name_map["brief_sets"] = "brief-sets"
                    self._children_yang_names.add("brief-sets")
                    self._segment_path = lambda: "session-set"


                class DetailSets(Entity):
                    """
                    Table about TCP NSR Session Sets details
                    
                    .. attribute:: detail_set
                    
                    	showing detailed information of NSR Session Sets
                    	**type**\: list of  		 :py:class:`DetailSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.SessionSet.DetailSets, self).__init__()

                        self.yang_name = "detail-sets"
                        self.yang_parent_name = "session-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("detail-set", ("detail_set", TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet))])
                        self._leafs = OrderedDict()

                        self.detail_set = YList(self)
                        self._segment_path = lambda: "detail-sets"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.SessionSet.DetailSets, [], name, value)


                    class DetailSet(Entity):
                        """
                        showing detailed information of NSR Session
                        Sets
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR Sesison Set
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: sscb
                        
                        	Address of the Session Set Control Block
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pid
                        
                        	PID of the Client that owns this Session\-set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_id
                        
                        	ID of this Session\-set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sso_role
                        
                        	TCP role for this set?
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mode
                        
                        	Session\-set mode
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: address_family
                        
                        	Address Family of the sessions in this set
                        	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                        
                        .. attribute:: well_known_port
                        
                        	Well Known Port of the client
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: local_node
                        
                        	Local node of this set
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: local_instance
                        
                        	Instance of the client application on the local node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protect_node
                        
                        	The node protecting this set
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: protect_instance
                        
                        	Instance of the client application on the protection node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_sessions
                        
                        	Number of Sessions in the set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_synced_sessions_up_stream
                        
                        	How many sessions are synced with upstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_synced_sessions_down_stream
                        
                        	How many sessions are synced with downstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_init_sync_in_progress
                        
                        	Is an initial sync in progress currently?
                        	**type**\: bool
                        
                        .. attribute:: is_init_sync_second_phase
                        
                        	Is initial sync in the second phase?
                        	**type**\: bool
                        
                        .. attribute:: sequence_number_of_init_sync
                        
                        	ID of the current or the last initial sync operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: init_sync_timer
                        
                        	Time left on the initial sync timer
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: total_number_of_init_sync_sessions
                        
                        	Number of sessions being synced as part of the current initial sync operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_init_synced_sessions
                        
                        	Number of sessions that are synced as part of the current initial sync operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_sessions_init_sync_failed
                        
                        	Number of sessions that failed to sync as part of the current initial sync operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: init_sync_error
                        
                        	Initial sync failure reason, if any
                        	**type**\: str
                        
                        .. attribute:: is_init_sync_error_local
                        
                        	Initial sync failed due to a local error or remote stack
                        	**type**\: bool
                        
                        .. attribute:: init_sync_start_time
                        
                        	Time at which last or current initial sync operation was started (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: init_sync_end_time
                        
                        	Time at which the last initial sync operation was ended (in seconds since 1st Jan 1970 00\:00 \:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: is_sscb_init_sync_ready
                        
                        	Is the SSCB ready for another initial sync?
                        	**type**\: bool
                        
                        .. attribute:: init_sync_ready_start_time
                        
                        	Time at which the session was ready for initial sync last (in seconds since 1st Jan 1970 00\:00 \:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: init_sync_ready_end_time
                        
                        	Time at which the session set last went not\-ready for initial sync (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: nsr_reset_time
                        
                        	Time at which NSR was last reset on the session set (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: is_audit_in_progress
                        
                        	Is an audit in progress currently?
                        	**type**\: bool
                        
                        .. attribute:: audit_seq_number
                        
                        	ID of the current or the last audit operation
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: audit_start_time
                        
                        	Time at which last or current audit operation was started (in seconds since 1st Jan 1970 00\:00 \:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: audit_end_time
                        
                        	Time at which the last audit operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet, self).__init__()

                            self.yang_name = "detail-set"
                            self.yang_parent_name = "detail-sets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('sscb', YLeaf(YType.uint64, 'sscb')),
                                ('pid', YLeaf(YType.uint32, 'pid')),
                                ('set_id', YLeaf(YType.uint32, 'set-id')),
                                ('sso_role', YLeaf(YType.uint32, 'sso-role')),
                                ('mode', YLeaf(YType.uint32, 'mode')),
                                ('address_family', YLeaf(YType.enumeration, 'address-family')),
                                ('well_known_port', YLeaf(YType.uint16, 'well-known-port')),
                                ('local_node', YLeaf(YType.str, 'local-node')),
                                ('local_instance', YLeaf(YType.uint32, 'local-instance')),
                                ('protect_node', YLeaf(YType.str, 'protect-node')),
                                ('protect_instance', YLeaf(YType.uint32, 'protect-instance')),
                                ('number_of_sessions', YLeaf(YType.uint32, 'number-of-sessions')),
                                ('number_of_synced_sessions_up_stream', YLeaf(YType.uint32, 'number-of-synced-sessions-up-stream')),
                                ('number_of_synced_sessions_down_stream', YLeaf(YType.uint32, 'number-of-synced-sessions-down-stream')),
                                ('is_init_sync_in_progress', YLeaf(YType.boolean, 'is-init-sync-in-progress')),
                                ('is_init_sync_second_phase', YLeaf(YType.boolean, 'is-init-sync-second-phase')),
                                ('sequence_number_of_init_sync', YLeaf(YType.uint32, 'sequence-number-of-init-sync')),
                                ('init_sync_timer', YLeaf(YType.uint32, 'init-sync-timer')),
                                ('total_number_of_init_sync_sessions', YLeaf(YType.uint32, 'total-number-of-init-sync-sessions')),
                                ('number_of_init_synced_sessions', YLeaf(YType.uint32, 'number-of-init-synced-sessions')),
                                ('number_of_sessions_init_sync_failed', YLeaf(YType.uint32, 'number-of-sessions-init-sync-failed')),
                                ('init_sync_error', YLeaf(YType.str, 'init-sync-error')),
                                ('is_init_sync_error_local', YLeaf(YType.boolean, 'is-init-sync-error-local')),
                                ('init_sync_start_time', YLeaf(YType.uint32, 'init-sync-start-time')),
                                ('init_sync_end_time', YLeaf(YType.uint32, 'init-sync-end-time')),
                                ('is_sscb_init_sync_ready', YLeaf(YType.boolean, 'is-sscb-init-sync-ready')),
                                ('init_sync_ready_start_time', YLeaf(YType.uint32, 'init-sync-ready-start-time')),
                                ('init_sync_ready_end_time', YLeaf(YType.uint32, 'init-sync-ready-end-time')),
                                ('nsr_reset_time', YLeaf(YType.uint32, 'nsr-reset-time')),
                                ('is_audit_in_progress', YLeaf(YType.boolean, 'is-audit-in-progress')),
                                ('audit_seq_number', YLeaf(YType.uint32, 'audit-seq-number')),
                                ('audit_start_time', YLeaf(YType.uint32, 'audit-start-time')),
                                ('audit_end_time', YLeaf(YType.uint32, 'audit-end-time')),
                            ])
                            self.id = None
                            self.sscb = None
                            self.pid = None
                            self.set_id = None
                            self.sso_role = None
                            self.mode = None
                            self.address_family = None
                            self.well_known_port = None
                            self.local_node = None
                            self.local_instance = None
                            self.protect_node = None
                            self.protect_instance = None
                            self.number_of_sessions = None
                            self.number_of_synced_sessions_up_stream = None
                            self.number_of_synced_sessions_down_stream = None
                            self.is_init_sync_in_progress = None
                            self.is_init_sync_second_phase = None
                            self.sequence_number_of_init_sync = None
                            self.init_sync_timer = None
                            self.total_number_of_init_sync_sessions = None
                            self.number_of_init_synced_sessions = None
                            self.number_of_sessions_init_sync_failed = None
                            self.init_sync_error = None
                            self.is_init_sync_error_local = None
                            self.init_sync_start_time = None
                            self.init_sync_end_time = None
                            self.is_sscb_init_sync_ready = None
                            self.init_sync_ready_start_time = None
                            self.init_sync_ready_end_time = None
                            self.nsr_reset_time = None
                            self.is_audit_in_progress = None
                            self.audit_seq_number = None
                            self.audit_start_time = None
                            self.audit_end_time = None
                            self._segment_path = lambda: "detail-set" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet, ['id', 'sscb', 'pid', 'set_id', 'sso_role', 'mode', 'address_family', 'well_known_port', 'local_node', 'local_instance', 'protect_node', 'protect_instance', 'number_of_sessions', 'number_of_synced_sessions_up_stream', 'number_of_synced_sessions_down_stream', 'is_init_sync_in_progress', 'is_init_sync_second_phase', 'sequence_number_of_init_sync', 'init_sync_timer', 'total_number_of_init_sync_sessions', 'number_of_init_synced_sessions', 'number_of_sessions_init_sync_failed', 'init_sync_error', 'is_init_sync_error_local', 'init_sync_start_time', 'init_sync_end_time', 'is_sscb_init_sync_ready', 'init_sync_ready_start_time', 'init_sync_ready_end_time', 'nsr_reset_time', 'is_audit_in_progress', 'audit_seq_number', 'audit_start_time', 'audit_end_time'], name, value)


                class BriefSets(Entity):
                    """
                    Information about TCP NSR Session Sets
                    
                    .. attribute:: brief_set
                    
                    	Brief information about NSR Session Sets
                    	**type**\: list of  		 :py:class:`BriefSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.SessionSet.BriefSets, self).__init__()

                        self.yang_name = "brief-sets"
                        self.yang_parent_name = "session-set"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("brief-set", ("brief_set", TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet))])
                        self._leafs = OrderedDict()

                        self.brief_set = YList(self)
                        self._segment_path = lambda: "brief-sets"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.SessionSet.BriefSets, [], name, value)


                    class BriefSet(Entity):
                        """
                        Brief information about NSR Session Sets
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR Session Set
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: sscb
                        
                        	Address of the Session Set Control Block
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pid
                        
                        	PID of the Client that owns this Session\-set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: client_name
                        
                        	the name of Clinet that owns this Session\-set
                        	**type**\: str
                        
                        .. attribute:: client_instance
                        
                        	Instance of the Client that owns this Session\-set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: set_id
                        
                        	ID of this Session\-set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: sso_role
                        
                        	TCP role for this set?
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: mode
                        
                        	Session\-set mode
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: address_family
                        
                        	Address Family of the sessions in this set
                        	**type**\:  :py:class:`AddrFamily <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.AddrFamily>`
                        
                        .. attribute:: well_known_port
                        
                        	Well Known Port of the client
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: local_node
                        
                        	Local node of this set
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: local_instance
                        
                        	Instance of the client application on the local node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: protect_node
                        
                        	The node protecting this set
                        	**type**\: str
                        
                        	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
                        
                        .. attribute:: protect_instance
                        
                        	Instance of the client application on the protection node
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_sessions
                        
                        	Number of Sessions in the set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_synced_sessions_up_stream
                        
                        	How many sessions are synced with upstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_synced_sessions_down_stream
                        
                        	How many sessions are synced with downstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_init_sync_in_progress
                        
                        	Is an initial sync in progress currently?
                        	**type**\: bool
                        
                        .. attribute:: is_sscb_init_sync_ready
                        
                        	Is the SSCB ready for another initial sync?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet, self).__init__()

                            self.yang_name = "brief-set"
                            self.yang_parent_name = "brief-sets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('sscb', YLeaf(YType.uint64, 'sscb')),
                                ('pid', YLeaf(YType.uint32, 'pid')),
                                ('client_name', YLeaf(YType.str, 'client-name')),
                                ('client_instance', YLeaf(YType.uint32, 'client-instance')),
                                ('set_id', YLeaf(YType.uint32, 'set-id')),
                                ('sso_role', YLeaf(YType.uint32, 'sso-role')),
                                ('mode', YLeaf(YType.uint32, 'mode')),
                                ('address_family', YLeaf(YType.enumeration, 'address-family')),
                                ('well_known_port', YLeaf(YType.uint16, 'well-known-port')),
                                ('local_node', YLeaf(YType.str, 'local-node')),
                                ('local_instance', YLeaf(YType.uint32, 'local-instance')),
                                ('protect_node', YLeaf(YType.str, 'protect-node')),
                                ('protect_instance', YLeaf(YType.uint32, 'protect-instance')),
                                ('number_of_sessions', YLeaf(YType.uint32, 'number-of-sessions')),
                                ('number_of_synced_sessions_up_stream', YLeaf(YType.uint32, 'number-of-synced-sessions-up-stream')),
                                ('number_of_synced_sessions_down_stream', YLeaf(YType.uint32, 'number-of-synced-sessions-down-stream')),
                                ('is_init_sync_in_progress', YLeaf(YType.boolean, 'is-init-sync-in-progress')),
                                ('is_sscb_init_sync_ready', YLeaf(YType.boolean, 'is-sscb-init-sync-ready')),
                            ])
                            self.id = None
                            self.sscb = None
                            self.pid = None
                            self.client_name = None
                            self.client_instance = None
                            self.set_id = None
                            self.sso_role = None
                            self.mode = None
                            self.address_family = None
                            self.well_known_port = None
                            self.local_node = None
                            self.local_instance = None
                            self.protect_node = None
                            self.protect_instance = None
                            self.number_of_sessions = None
                            self.number_of_synced_sessions_up_stream = None
                            self.number_of_synced_sessions_down_stream = None
                            self.is_init_sync_in_progress = None
                            self.is_sscb_init_sync_ready = None
                            self._segment_path = lambda: "brief-set" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet, ['id', 'sscb', 'pid', 'client_name', 'client_instance', 'set_id', 'sso_role', 'mode', 'address_family', 'well_known_port', 'local_node', 'local_instance', 'protect_node', 'protect_instance', 'number_of_sessions', 'number_of_synced_sessions_up_stream', 'number_of_synced_sessions_down_stream', 'is_init_sync_in_progress', 'is_sscb_init_sync_ready'], name, value)


            class Statistics(Entity):
                """
                Statis Information about TCP NSR connections
                
                .. attribute:: summary
                
                	Summary statistics across all NSR connections
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary>`
                
                .. attribute:: statistic_clients
                
                	Table listing NSR connections for which statistic information is provided
                	**type**\:  :py:class:`StatisticClients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticClients>`
                
                .. attribute:: statistic_sets
                
                	Table listing NSR connections for which statistic information is provided
                	**type**\:  :py:class:`StatisticSets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSets>`
                
                .. attribute:: statistic_sessions
                
                	Table listing NSR connections for which statistic information is provided
                	**type**\:  :py:class:`StatisticSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSessions>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2018-02-14'

                def __init__(self):
                    super(TcpNsr.Nodes.Node.Statistics, self).__init__()

                    self.yang_name = "statistics"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("summary", ("summary", TcpNsr.Nodes.Node.Statistics.Summary)), ("statistic-clients", ("statistic_clients", TcpNsr.Nodes.Node.Statistics.StatisticClients)), ("statistic-sets", ("statistic_sets", TcpNsr.Nodes.Node.Statistics.StatisticSets)), ("statistic-sessions", ("statistic_sessions", TcpNsr.Nodes.Node.Statistics.StatisticSessions))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.summary = TcpNsr.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self
                    self._children_name_map["summary"] = "summary"
                    self._children_yang_names.add("summary")

                    self.statistic_clients = TcpNsr.Nodes.Node.Statistics.StatisticClients()
                    self.statistic_clients.parent = self
                    self._children_name_map["statistic_clients"] = "statistic-clients"
                    self._children_yang_names.add("statistic-clients")

                    self.statistic_sets = TcpNsr.Nodes.Node.Statistics.StatisticSets()
                    self.statistic_sets.parent = self
                    self._children_name_map["statistic_sets"] = "statistic-sets"
                    self._children_yang_names.add("statistic-sets")

                    self.statistic_sessions = TcpNsr.Nodes.Node.Statistics.StatisticSessions()
                    self.statistic_sessions.parent = self
                    self._children_name_map["statistic_sessions"] = "statistic-sessions"
                    self._children_yang_names.add("statistic-sessions")
                    self._segment_path = lambda: "statistics"


                class Summary(Entity):
                    """
                    Summary statistics across all NSR connections
                    
                    .. attribute:: snd_counters
                    
                    	Aggregate Send path counters
                    	**type**\:  :py:class:`SndCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.SndCounters>`
                    
                    .. attribute:: audit_counters
                    
                    	Aggregate Audit counters
                    	**type**\:  :py:class:`AuditCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters>`
                    
                    .. attribute:: last_cleared_time
                    
                    	Time of last clear (in seconds since 1st Jan 1970 00\:00\:00)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    .. attribute:: number_of_connected_clients
                    
                    	Number of disconnected clients
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_disconnected_clients
                    
                    	Number of disconnected clients
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_current_clients
                    
                    	Number of current  clients
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_created_session_sets
                    
                    	Number of created session sets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_destroyed_session_sets
                    
                    	Number of destroyed session sets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_current_session_sets
                    
                    	Number of current session sets
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_added_sessions
                    
                    	Number of added sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_deleted_sessions
                    
                    	Number of deleted sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_current_sessions
                    
                    	Number of current sessions
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_partner_node
                    
                    	 Number of Parner Nodes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_attempted_init_sync
                    
                    	no. of initial\-sync attempts
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_succeeded_init_sync
                    
                    	no. of initial\-sync successes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_failed_init_sync
                    
                    	no. of initial\-sync fails
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_held_packets
                    
                    	Number of Packets held by Active TCP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_held_but_dropped_packets
                    
                    	Number of held packets dropped by Active TCP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_held_internal_acks
                    
                    	Number of Internal Acks held by Active TCP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_held_but_dropped_internal_acks
                    
                    	Number of held Internal Acks dropped by Active TCP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_sent_internal_acks
                    
                    	Number of Internal Acks sent to Active TCP by Standby TCP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_received_internal_acks
                    
                    	Number of Internal Acks received by Active TCP
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_qad_receive_messages_drops
                    
                    	Number of dropped messages from partner TCP stack(s)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_qad_receive_messages_unknowns
                    
                    	Number of unknown messages from partner TCP stack(s)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_qad_receive_messages_accepts
                    
                    	Number of messages accepted from partner TCP stack(s)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_qad_stale_receive_messages_drops
                    
                    	Number of dropped messages from partner TCP stack(s) because they were out\-of\-order
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_qad_transfer_message_sent
                    
                    	Number of messages sent to partner TCP stack(s)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_qad_transfer_message_drops
                    
                    	Number of messages failed to be sent to partner TCP stack(s)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_internal_ack_drops_no_pcb
                    
                    	Number of iACKs dropped because there is no PCB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: number_of_internal_ack_drops_no_scbdp
                    
                    	Number of iACKs dropped because there is no datapath SCB
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: internal_ack_drops_not_replicated
                    
                    	Number of iACKs dropped because session is not replicated
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: internal_ack_drops_initsync_first_phase
                    
                    	Number of iACKs dropped because init\-sync is in 1st phase
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: internal_ack_drops_stale
                    
                    	Number of stale iACKs dropped
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: internal_ack_drops_immediate_match
                    
                    	Number of iACKs not held because of an immediate match
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: held_packet_drops
                    
                    	Number of held packets dropped because of errors
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notification_statistic
                    
                    	Various types of notification stats
                    	**type**\: list of  		 :py:class:`NotificationStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Statistics.Summary, self).__init__()

                        self.yang_name = "summary"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("snd-counters", ("snd_counters", TcpNsr.Nodes.Node.Statistics.Summary.SndCounters)), ("audit-counters", ("audit_counters", TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters))])
                        self._child_list_classes = OrderedDict([("notification-statistic", ("notification_statistic", TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic))])
                        self._leafs = OrderedDict([
                            ('last_cleared_time', YLeaf(YType.uint32, 'last-cleared-time')),
                            ('number_of_connected_clients', YLeaf(YType.uint32, 'number-of-connected-clients')),
                            ('number_of_disconnected_clients', YLeaf(YType.uint32, 'number-of-disconnected-clients')),
                            ('number_of_current_clients', YLeaf(YType.uint32, 'number-of-current-clients')),
                            ('number_of_created_session_sets', YLeaf(YType.uint32, 'number-of-created-session-sets')),
                            ('number_of_destroyed_session_sets', YLeaf(YType.uint32, 'number-of-destroyed-session-sets')),
                            ('number_of_current_session_sets', YLeaf(YType.uint32, 'number-of-current-session-sets')),
                            ('number_of_added_sessions', YLeaf(YType.uint32, 'number-of-added-sessions')),
                            ('number_of_deleted_sessions', YLeaf(YType.uint32, 'number-of-deleted-sessions')),
                            ('number_of_current_sessions', YLeaf(YType.uint32, 'number-of-current-sessions')),
                            ('number_of_partner_node', YLeaf(YType.uint32, 'number-of-partner-node')),
                            ('number_of_attempted_init_sync', YLeaf(YType.uint32, 'number-of-attempted-init-sync')),
                            ('number_of_succeeded_init_sync', YLeaf(YType.uint32, 'number-of-succeeded-init-sync')),
                            ('number_of_failed_init_sync', YLeaf(YType.uint32, 'number-of-failed-init-sync')),
                            ('number_of_held_packets', YLeaf(YType.uint32, 'number-of-held-packets')),
                            ('number_of_held_but_dropped_packets', YLeaf(YType.uint32, 'number-of-held-but-dropped-packets')),
                            ('number_of_held_internal_acks', YLeaf(YType.uint32, 'number-of-held-internal-acks')),
                            ('number_of_held_but_dropped_internal_acks', YLeaf(YType.uint32, 'number-of-held-but-dropped-internal-acks')),
                            ('number_of_sent_internal_acks', YLeaf(YType.uint32, 'number-of-sent-internal-acks')),
                            ('number_of_received_internal_acks', YLeaf(YType.uint32, 'number-of-received-internal-acks')),
                            ('number_of_qad_receive_messages_drops', YLeaf(YType.uint32, 'number-of-qad-receive-messages-drops')),
                            ('number_of_qad_receive_messages_unknowns', YLeaf(YType.uint32, 'number-of-qad-receive-messages-unknowns')),
                            ('number_of_qad_receive_messages_accepts', YLeaf(YType.uint32, 'number-of-qad-receive-messages-accepts')),
                            ('number_of_qad_stale_receive_messages_drops', YLeaf(YType.uint32, 'number-of-qad-stale-receive-messages-drops')),
                            ('number_of_qad_transfer_message_sent', YLeaf(YType.uint32, 'number-of-qad-transfer-message-sent')),
                            ('number_of_qad_transfer_message_drops', YLeaf(YType.uint32, 'number-of-qad-transfer-message-drops')),
                            ('number_of_internal_ack_drops_no_pcb', YLeaf(YType.uint32, 'number-of-internal-ack-drops-no-pcb')),
                            ('number_of_internal_ack_drops_no_scbdp', YLeaf(YType.uint32, 'number-of-internal-ack-drops-no-scbdp')),
                            ('internal_ack_drops_not_replicated', YLeaf(YType.uint32, 'internal-ack-drops-not-replicated')),
                            ('internal_ack_drops_initsync_first_phase', YLeaf(YType.uint32, 'internal-ack-drops-initsync-first-phase')),
                            ('internal_ack_drops_stale', YLeaf(YType.uint32, 'internal-ack-drops-stale')),
                            ('internal_ack_drops_immediate_match', YLeaf(YType.uint32, 'internal-ack-drops-immediate-match')),
                            ('held_packet_drops', YLeaf(YType.uint32, 'held-packet-drops')),
                        ])
                        self.last_cleared_time = None
                        self.number_of_connected_clients = None
                        self.number_of_disconnected_clients = None
                        self.number_of_current_clients = None
                        self.number_of_created_session_sets = None
                        self.number_of_destroyed_session_sets = None
                        self.number_of_current_session_sets = None
                        self.number_of_added_sessions = None
                        self.number_of_deleted_sessions = None
                        self.number_of_current_sessions = None
                        self.number_of_partner_node = None
                        self.number_of_attempted_init_sync = None
                        self.number_of_succeeded_init_sync = None
                        self.number_of_failed_init_sync = None
                        self.number_of_held_packets = None
                        self.number_of_held_but_dropped_packets = None
                        self.number_of_held_internal_acks = None
                        self.number_of_held_but_dropped_internal_acks = None
                        self.number_of_sent_internal_acks = None
                        self.number_of_received_internal_acks = None
                        self.number_of_qad_receive_messages_drops = None
                        self.number_of_qad_receive_messages_unknowns = None
                        self.number_of_qad_receive_messages_accepts = None
                        self.number_of_qad_stale_receive_messages_drops = None
                        self.number_of_qad_transfer_message_sent = None
                        self.number_of_qad_transfer_message_drops = None
                        self.number_of_internal_ack_drops_no_pcb = None
                        self.number_of_internal_ack_drops_no_scbdp = None
                        self.internal_ack_drops_not_replicated = None
                        self.internal_ack_drops_initsync_first_phase = None
                        self.internal_ack_drops_stale = None
                        self.internal_ack_drops_immediate_match = None
                        self.held_packet_drops = None

                        self.snd_counters = TcpNsr.Nodes.Node.Statistics.Summary.SndCounters()
                        self.snd_counters.parent = self
                        self._children_name_map["snd_counters"] = "snd-counters"
                        self._children_yang_names.add("snd-counters")

                        self.audit_counters = TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters()
                        self.audit_counters.parent = self
                        self._children_name_map["audit_counters"] = "audit-counters"
                        self._children_yang_names.add("audit-counters")

                        self.notification_statistic = YList(self)
                        self._segment_path = lambda: "summary"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Statistics.Summary, ['last_cleared_time', 'number_of_connected_clients', 'number_of_disconnected_clients', 'number_of_current_clients', 'number_of_created_session_sets', 'number_of_destroyed_session_sets', 'number_of_current_session_sets', 'number_of_added_sessions', 'number_of_deleted_sessions', 'number_of_current_sessions', 'number_of_partner_node', 'number_of_attempted_init_sync', 'number_of_succeeded_init_sync', 'number_of_failed_init_sync', 'number_of_held_packets', 'number_of_held_but_dropped_packets', 'number_of_held_internal_acks', 'number_of_held_but_dropped_internal_acks', 'number_of_sent_internal_acks', 'number_of_received_internal_acks', 'number_of_qad_receive_messages_drops', 'number_of_qad_receive_messages_unknowns', 'number_of_qad_receive_messages_accepts', 'number_of_qad_stale_receive_messages_drops', 'number_of_qad_transfer_message_sent', 'number_of_qad_transfer_message_drops', 'number_of_internal_ack_drops_no_pcb', 'number_of_internal_ack_drops_no_scbdp', 'internal_ack_drops_not_replicated', 'internal_ack_drops_initsync_first_phase', 'internal_ack_drops_stale', 'internal_ack_drops_immediate_match', 'held_packet_drops'], name, value)


                    class SndCounters(Entity):
                        """
                        Aggregate Send path counters
                        
                        .. attribute:: common
                        
                        	Common send path counters
                        	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common>`
                        
                        .. attribute:: aggr_only
                        
                        	Aggregate only send path counters
                        	**type**\:  :py:class:`AggrOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Statistics.Summary.SndCounters, self).__init__()

                            self.yang_name = "snd-counters"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("common", ("common", TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common)), ("aggr-only", ("aggr_only", TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.common = TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common()
                            self.common.parent = self
                            self._children_name_map["common"] = "common"
                            self._children_yang_names.add("common")

                            self.aggr_only = TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly()
                            self.aggr_only.parent = self
                            self._children_name_map["aggr_only"] = "aggr-only"
                            self._children_yang_names.add("aggr-only")
                            self._segment_path = lambda: "snd-counters"


                        class Common(Entity):
                            """
                            Common send path counters
                            
                            .. attribute:: data_xfer_send
                            
                            	Number of successful DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_send_total
                            
                            	Amount of data transferred
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_xfer_send_drop
                            
                            	Number of failed DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_send_iov_alloc
                            
                            	Number of data transfer msgs., that required new IOV's to be allocated
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv
                            
                            	Number of received DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv_success
                            
                            	Number of successfully received DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv_fail_buffer_trim
                            
                            	Number of received DATA transfers that had buffer trim failures
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv_fail_snd_una_out_of_sync
                            
                            	Number of received DATA transfers that had failures because the send path was out of sync
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_send
                            
                            	Number of successful Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_send_units
                            
                            	Number of segement units transferred via the successful Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_send_drop
                            
                            	Number of failed Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv
                            
                            	Number of received Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_success
                            
                            	Number of successfully received Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_fail_buffer_trim
                            
                            	Number of received Segmentation instructions that had buffer trim failures
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_fail_tcp_process
                            
                            	Number of received Segmentation instructions that had failures during TCP processing
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_send
                            
                            	Number of successful NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_send_drop
                            
                            	Number of failed NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv
                            
                            	Number of received NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv_success
                            
                            	Number of successfully received NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv_fail_data_send
                            
                            	Number of received NACK messages that had failures when sending data in response to the NACK
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_send
                            
                            	Number of successful Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_send_drop
                            
                            	Number of failed Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv
                            
                            	Number of received Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv_success
                            
                            	Number of successfully received Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv_fail_buffer_trim
                            
                            	Number of Cleanup messages that had trim failures
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common, self).__init__()

                                self.yang_name = "common"
                                self.yang_parent_name = "snd-counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('data_xfer_send', YLeaf(YType.uint32, 'data-xfer-send')),
                                    ('data_xfer_send_total', YLeaf(YType.uint64, 'data-xfer-send-total')),
                                    ('data_xfer_send_drop', YLeaf(YType.uint32, 'data-xfer-send-drop')),
                                    ('data_xfer_send_iov_alloc', YLeaf(YType.uint32, 'data-xfer-send-iov-alloc')),
                                    ('data_xfer_rcv', YLeaf(YType.uint32, 'data-xfer-rcv')),
                                    ('data_xfer_rcv_success', YLeaf(YType.uint32, 'data-xfer-rcv-success')),
                                    ('data_xfer_rcv_fail_buffer_trim', YLeaf(YType.uint32, 'data-xfer-rcv-fail-buffer-trim')),
                                    ('data_xfer_rcv_fail_snd_una_out_of_sync', YLeaf(YType.uint32, 'data-xfer-rcv-fail-snd-una-out-of-sync')),
                                    ('seg_instr_send', YLeaf(YType.uint32, 'seg-instr-send')),
                                    ('seg_instr_send_units', YLeaf(YType.uint32, 'seg-instr-send-units')),
                                    ('seg_instr_send_drop', YLeaf(YType.uint32, 'seg-instr-send-drop')),
                                    ('seg_instr_rcv', YLeaf(YType.uint32, 'seg-instr-rcv')),
                                    ('seg_instr_rcv_success', YLeaf(YType.uint32, 'seg-instr-rcv-success')),
                                    ('seg_instr_rcv_fail_buffer_trim', YLeaf(YType.uint32, 'seg-instr-rcv-fail-buffer-trim')),
                                    ('seg_instr_rcv_fail_tcp_process', YLeaf(YType.uint32, 'seg-instr-rcv-fail-tcp-process')),
                                    ('nack_send', YLeaf(YType.uint32, 'nack-send')),
                                    ('nack_send_drop', YLeaf(YType.uint32, 'nack-send-drop')),
                                    ('nack_rcv', YLeaf(YType.uint32, 'nack-rcv')),
                                    ('nack_rcv_success', YLeaf(YType.uint32, 'nack-rcv-success')),
                                    ('nack_rcv_fail_data_send', YLeaf(YType.uint32, 'nack-rcv-fail-data-send')),
                                    ('cleanup_send', YLeaf(YType.uint32, 'cleanup-send')),
                                    ('cleanup_send_drop', YLeaf(YType.uint32, 'cleanup-send-drop')),
                                    ('cleanup_rcv', YLeaf(YType.uint32, 'cleanup-rcv')),
                                    ('cleanup_rcv_success', YLeaf(YType.uint32, 'cleanup-rcv-success')),
                                    ('cleanup_rcv_fail_buffer_trim', YLeaf(YType.uint32, 'cleanup-rcv-fail-buffer-trim')),
                                ])
                                self.data_xfer_send = None
                                self.data_xfer_send_total = None
                                self.data_xfer_send_drop = None
                                self.data_xfer_send_iov_alloc = None
                                self.data_xfer_rcv = None
                                self.data_xfer_rcv_success = None
                                self.data_xfer_rcv_fail_buffer_trim = None
                                self.data_xfer_rcv_fail_snd_una_out_of_sync = None
                                self.seg_instr_send = None
                                self.seg_instr_send_units = None
                                self.seg_instr_send_drop = None
                                self.seg_instr_rcv = None
                                self.seg_instr_rcv_success = None
                                self.seg_instr_rcv_fail_buffer_trim = None
                                self.seg_instr_rcv_fail_tcp_process = None
                                self.nack_send = None
                                self.nack_send_drop = None
                                self.nack_rcv = None
                                self.nack_rcv_success = None
                                self.nack_rcv_fail_data_send = None
                                self.cleanup_send = None
                                self.cleanup_send_drop = None
                                self.cleanup_rcv = None
                                self.cleanup_rcv_success = None
                                self.cleanup_rcv_fail_buffer_trim = None
                                self._segment_path = lambda: "common"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common, ['data_xfer_send', 'data_xfer_send_total', 'data_xfer_send_drop', 'data_xfer_send_iov_alloc', 'data_xfer_rcv', 'data_xfer_rcv_success', 'data_xfer_rcv_fail_buffer_trim', 'data_xfer_rcv_fail_snd_una_out_of_sync', 'seg_instr_send', 'seg_instr_send_units', 'seg_instr_send_drop', 'seg_instr_rcv', 'seg_instr_rcv_success', 'seg_instr_rcv_fail_buffer_trim', 'seg_instr_rcv_fail_tcp_process', 'nack_send', 'nack_send_drop', 'nack_rcv', 'nack_rcv_success', 'nack_rcv_fail_data_send', 'cleanup_send', 'cleanup_send_drop', 'cleanup_rcv', 'cleanup_rcv_success', 'cleanup_rcv_fail_buffer_trim'], name, value)


                        class AggrOnly(Entity):
                            """
                            Aggregate only send path counters
                            
                            .. attribute:: data_xfer_rcv_drop_no_pcb
                            
                            	Number of Data transfer messages dropped because PCB wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv_drop_no_scb_dp
                            
                            	Number of Data transfer messages dropped because SCB DP wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_drop_no_pcb
                            
                            	Number of Segmentation instruction messages dropped because PCB wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_drop_no_scb_dp
                            
                            	Number of Segmentation instruction messages dropped because SCB DP wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv_drop_no_pcb
                            
                            	Number of NACK messages dropped because PCB wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv_drop_no_scb_dp
                            
                            	Number of NACK messages dropped because SCB DP wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv_drop_no_pcb
                            
                            	Number of Cleanup messages dropped because PCB wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv_drop_no_scb_dp
                            
                            	Number of Cleanup messages dropped because SCB DP wasn't found
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly, self).__init__()

                                self.yang_name = "aggr-only"
                                self.yang_parent_name = "snd-counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('data_xfer_rcv_drop_no_pcb', YLeaf(YType.uint32, 'data-xfer-rcv-drop-no-pcb')),
                                    ('data_xfer_rcv_drop_no_scb_dp', YLeaf(YType.uint32, 'data-xfer-rcv-drop-no-scb-dp')),
                                    ('seg_instr_rcv_drop_no_pcb', YLeaf(YType.uint32, 'seg-instr-rcv-drop-no-pcb')),
                                    ('seg_instr_rcv_drop_no_scb_dp', YLeaf(YType.uint32, 'seg-instr-rcv-drop-no-scb-dp')),
                                    ('nack_rcv_drop_no_pcb', YLeaf(YType.uint32, 'nack-rcv-drop-no-pcb')),
                                    ('nack_rcv_drop_no_scb_dp', YLeaf(YType.uint32, 'nack-rcv-drop-no-scb-dp')),
                                    ('cleanup_rcv_drop_no_pcb', YLeaf(YType.uint32, 'cleanup-rcv-drop-no-pcb')),
                                    ('cleanup_rcv_drop_no_scb_dp', YLeaf(YType.uint32, 'cleanup-rcv-drop-no-scb-dp')),
                                ])
                                self.data_xfer_rcv_drop_no_pcb = None
                                self.data_xfer_rcv_drop_no_scb_dp = None
                                self.seg_instr_rcv_drop_no_pcb = None
                                self.seg_instr_rcv_drop_no_scb_dp = None
                                self.nack_rcv_drop_no_pcb = None
                                self.nack_rcv_drop_no_scb_dp = None
                                self.cleanup_rcv_drop_no_pcb = None
                                self.cleanup_rcv_drop_no_scb_dp = None
                                self._segment_path = lambda: "aggr-only"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly, ['data_xfer_rcv_drop_no_pcb', 'data_xfer_rcv_drop_no_scb_dp', 'seg_instr_rcv_drop_no_pcb', 'seg_instr_rcv_drop_no_scb_dp', 'nack_rcv_drop_no_pcb', 'nack_rcv_drop_no_scb_dp', 'cleanup_rcv_drop_no_pcb', 'cleanup_rcv_drop_no_scb_dp'], name, value)


                    class AuditCounters(Entity):
                        """
                        Aggregate Audit counters
                        
                        .. attribute:: common
                        
                        	Common audit counters
                        	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common>`
                        
                        .. attribute:: aggr_only
                        
                        	Aggregate only audit counters
                        	**type**\:  :py:class:`AggrOnly <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters, self).__init__()

                            self.yang_name = "audit-counters"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("common", ("common", TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common)), ("aggr-only", ("aggr_only", TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict()

                            self.common = TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common()
                            self.common.parent = self
                            self._children_name_map["common"] = "common"
                            self._children_yang_names.add("common")

                            self.aggr_only = TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly()
                            self.aggr_only.parent = self
                            self._children_name_map["aggr_only"] = "aggr-only"
                            self._children_yang_names.add("aggr-only")
                            self._segment_path = lambda: "audit-counters"


                        class Common(Entity):
                            """
                            Common audit counters
                            
                            .. attribute:: mark_session_set_send
                            
                            	Number of successful session\-set Mark's sent by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_send_drop
                            
                            	Number of failed session\-set Mark's
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_rcv
                            
                            	Number of successful session\-set Mark's received by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_rcv_drop
                            
                            	Number of session\-set Mark's dropped by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_send
                            
                            	Number of successful session audits sent by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_send_drop
                            
                            	Number of session audits that couldn't be sent by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_rcv
                            
                            	Number of session audits received by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_rcv_drop
                            
                            	Number of session audits dropped by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sweep_session_set_send
                            
                            	Number of successful session\-set Sweep's sent by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sweep_session_set_send_drop
                            
                            	Number of failed session\-set Sweep's
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sweep_session_set_rcv
                            
                            	Number of successful session\-set Sweep's received by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sweep_session_set_rcv_drop
                            
                            	Number of session\-set Sweep's dropped by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_set_response_send
                            
                            	Number of successful audit responses sent by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_set_response_send_drop
                            
                            	Number of audit responses that couldn't be sent by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_set_response_rcv
                            
                            	Number of audit responses received by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_set_response_rcv_drop
                            
                            	Number of audit responses dropped by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_ack_send
                            
                            	Number of successful audit mark acks sent by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_ack_send_drop
                            
                            	Number of audit mark acks that couldn't be sent by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_ack_rcv
                            
                            	Number of audit mark acks received by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_ack_rcv_drop
                            
                            	Number of audit mark acks dropped by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_nack_send
                            
                            	Number of successful audit mark nacks sent by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_nack_send_drop
                            
                            	Number of audit mark nacks that couldn't be sent by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_nack_rcv
                            
                            	Number of audit mark nacks received by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_nack_rcv_drop
                            
                            	Number of audit mark nacks dropped by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: abort
                            
                            	Number of times the active aborted an audit session
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common, self).__init__()

                                self.yang_name = "common"
                                self.yang_parent_name = "audit-counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mark_session_set_send', YLeaf(YType.uint32, 'mark-session-set-send')),
                                    ('mark_session_set_send_drop', YLeaf(YType.uint32, 'mark-session-set-send-drop')),
                                    ('mark_session_set_rcv', YLeaf(YType.uint32, 'mark-session-set-rcv')),
                                    ('mark_session_set_rcv_drop', YLeaf(YType.uint32, 'mark-session-set-rcv-drop')),
                                    ('session_send', YLeaf(YType.uint32, 'session-send')),
                                    ('session_send_drop', YLeaf(YType.uint32, 'session-send-drop')),
                                    ('session_rcv', YLeaf(YType.uint32, 'session-rcv')),
                                    ('session_rcv_drop', YLeaf(YType.uint32, 'session-rcv-drop')),
                                    ('sweep_session_set_send', YLeaf(YType.uint32, 'sweep-session-set-send')),
                                    ('sweep_session_set_send_drop', YLeaf(YType.uint32, 'sweep-session-set-send-drop')),
                                    ('sweep_session_set_rcv', YLeaf(YType.uint32, 'sweep-session-set-rcv')),
                                    ('sweep_session_set_rcv_drop', YLeaf(YType.uint32, 'sweep-session-set-rcv-drop')),
                                    ('session_set_response_send', YLeaf(YType.uint32, 'session-set-response-send')),
                                    ('session_set_response_send_drop', YLeaf(YType.uint32, 'session-set-response-send-drop')),
                                    ('session_set_response_rcv', YLeaf(YType.uint32, 'session-set-response-rcv')),
                                    ('session_set_response_rcv_drop', YLeaf(YType.uint32, 'session-set-response-rcv-drop')),
                                    ('mark_session_set_ack_send', YLeaf(YType.uint32, 'mark-session-set-ack-send')),
                                    ('mark_session_set_ack_send_drop', YLeaf(YType.uint32, 'mark-session-set-ack-send-drop')),
                                    ('mark_session_set_ack_rcv', YLeaf(YType.uint32, 'mark-session-set-ack-rcv')),
                                    ('mark_session_set_ack_rcv_drop', YLeaf(YType.uint32, 'mark-session-set-ack-rcv-drop')),
                                    ('mark_session_set_nack_send', YLeaf(YType.uint32, 'mark-session-set-nack-send')),
                                    ('mark_session_set_nack_send_drop', YLeaf(YType.uint32, 'mark-session-set-nack-send-drop')),
                                    ('mark_session_set_nack_rcv', YLeaf(YType.uint32, 'mark-session-set-nack-rcv')),
                                    ('mark_session_set_nack_rcv_drop', YLeaf(YType.uint32, 'mark-session-set-nack-rcv-drop')),
                                    ('abort', YLeaf(YType.uint32, 'abort')),
                                ])
                                self.mark_session_set_send = None
                                self.mark_session_set_send_drop = None
                                self.mark_session_set_rcv = None
                                self.mark_session_set_rcv_drop = None
                                self.session_send = None
                                self.session_send_drop = None
                                self.session_rcv = None
                                self.session_rcv_drop = None
                                self.sweep_session_set_send = None
                                self.sweep_session_set_send_drop = None
                                self.sweep_session_set_rcv = None
                                self.sweep_session_set_rcv_drop = None
                                self.session_set_response_send = None
                                self.session_set_response_send_drop = None
                                self.session_set_response_rcv = None
                                self.session_set_response_rcv_drop = None
                                self.mark_session_set_ack_send = None
                                self.mark_session_set_ack_send_drop = None
                                self.mark_session_set_ack_rcv = None
                                self.mark_session_set_ack_rcv_drop = None
                                self.mark_session_set_nack_send = None
                                self.mark_session_set_nack_send_drop = None
                                self.mark_session_set_nack_rcv = None
                                self.mark_session_set_nack_rcv_drop = None
                                self.abort = None
                                self._segment_path = lambda: "common"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common, ['mark_session_set_send', 'mark_session_set_send_drop', 'mark_session_set_rcv', 'mark_session_set_rcv_drop', 'session_send', 'session_send_drop', 'session_rcv', 'session_rcv_drop', 'sweep_session_set_send', 'sweep_session_set_send_drop', 'sweep_session_set_rcv', 'sweep_session_set_rcv_drop', 'session_set_response_send', 'session_set_response_send_drop', 'session_set_response_rcv', 'session_set_response_rcv_drop', 'mark_session_set_ack_send', 'mark_session_set_ack_send_drop', 'mark_session_set_ack_rcv', 'mark_session_set_ack_rcv_drop', 'mark_session_set_nack_send', 'mark_session_set_nack_send_drop', 'mark_session_set_nack_rcv', 'mark_session_set_nack_rcv_drop', 'abort'], name, value)


                        class AggrOnly(Entity):
                            """
                            Aggregate only audit counters
                            
                            .. attribute:: mark_session_set_rcv_drop_aggr
                            
                            	Number of session\-set Mark messages dropped by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_rcv_drop_aggr
                            
                            	Number of session audit messages dropped by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: sweep_session_set_rcv_drop_aggr
                            
                            	Number of session\-set Sweep messages dropped by standby
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: session_set_response_rcv_drop_aggr
                            
                            	Number of session\-set response messages dropped by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_ack_rcv_drop_aggr
                            
                            	Number of session\-set mark ack messages dropped by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: mark_session_set_nack_rcv_drop_aggr
                            
                            	Number of session\-set mark nack messages dropped by active
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly, self).__init__()

                                self.yang_name = "aggr-only"
                                self.yang_parent_name = "audit-counters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('mark_session_set_rcv_drop_aggr', YLeaf(YType.uint32, 'mark-session-set-rcv-drop-aggr')),
                                    ('session_rcv_drop_aggr', YLeaf(YType.uint32, 'session-rcv-drop-aggr')),
                                    ('sweep_session_set_rcv_drop_aggr', YLeaf(YType.uint32, 'sweep-session-set-rcv-drop-aggr')),
                                    ('session_set_response_rcv_drop_aggr', YLeaf(YType.uint32, 'session-set-response-rcv-drop-aggr')),
                                    ('mark_session_set_ack_rcv_drop_aggr', YLeaf(YType.uint32, 'mark-session-set-ack-rcv-drop-aggr')),
                                    ('mark_session_set_nack_rcv_drop_aggr', YLeaf(YType.uint32, 'mark-session-set-nack-rcv-drop-aggr')),
                                ])
                                self.mark_session_set_rcv_drop_aggr = None
                                self.session_rcv_drop_aggr = None
                                self.sweep_session_set_rcv_drop_aggr = None
                                self.session_set_response_rcv_drop_aggr = None
                                self.mark_session_set_ack_rcv_drop_aggr = None
                                self.mark_session_set_nack_rcv_drop_aggr = None
                                self._segment_path = lambda: "aggr-only"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly, ['mark_session_set_rcv_drop_aggr', 'session_rcv_drop_aggr', 'sweep_session_set_rcv_drop_aggr', 'session_set_response_rcv_drop_aggr', 'mark_session_set_ack_rcv_drop_aggr', 'mark_session_set_nack_rcv_drop_aggr'], name, value)


                    class NotificationStatistic(Entity):
                        """
                        Various types of notification stats
                        
                        .. attribute:: queued_count
                        
                        	how many were queued
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: failed_count
                        
                        	Errors while queuing the notifs
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: delivered_count
                        
                        	How many were picked up by app?
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: dropped_count
                        
                        	How many were dropped because of timeout
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic, self).__init__()

                            self.yang_name = "notification-statistic"
                            self.yang_parent_name = "summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('queued_count', YLeaf(YType.uint32, 'queued-count')),
                                ('failed_count', YLeaf(YType.uint32, 'failed-count')),
                                ('delivered_count', YLeaf(YType.uint32, 'delivered-count')),
                                ('dropped_count', YLeaf(YType.uint32, 'dropped-count')),
                            ])
                            self.queued_count = None
                            self.failed_count = None
                            self.delivered_count = None
                            self.dropped_count = None
                            self._segment_path = lambda: "notification-statistic"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic, ['queued_count', 'failed_count', 'delivered_count', 'dropped_count'], name, value)


                class StatisticClients(Entity):
                    """
                    Table listing NSR connections for which
                    statistic information is provided
                    
                    .. attribute:: statistic_client
                    
                    	showing statistic information of NSR Clients
                    	**type**\: list of  		 :py:class:`StatisticClient <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Statistics.StatisticClients, self).__init__()

                        self.yang_name = "statistic-clients"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("statistic-client", ("statistic_client", TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient))])
                        self._leafs = OrderedDict()

                        self.statistic_client = YList(self)
                        self._segment_path = lambda: "statistic-clients"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticClients, [], name, value)


                    class StatisticClient(Entity):
                        """
                        showing statistic information of NSR Clients
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR Client
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: ccb
                        
                        	Address of the Client Control Block
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: pid
                        
                        	PID of the Client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: process_name
                        
                        	Proc name of Clinet
                        	**type**\: str
                        
                        .. attribute:: job_id
                        
                        	JOb ID of Client
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: instance
                        
                        	Instance of the Client
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: connected_at
                        
                        	Time of connect (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: number_of_created_sscb
                        
                        	Num of created session sets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_deleted_sscb
                        
                        	Num of deleted session sets
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_cleared_time
                        
                        	Time of last clear (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        .. attribute:: notification_statistic
                        
                        	Various types of notification stats
                        	**type**\: list of  		 :py:class:`NotificationStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient, self).__init__()

                            self.yang_name = "statistic-client"
                            self.yang_parent_name = "statistic-clients"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("notification-statistic", ("notification_statistic", TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic))])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('ccb', YLeaf(YType.uint64, 'ccb')),
                                ('pid', YLeaf(YType.uint32, 'pid')),
                                ('process_name', YLeaf(YType.str, 'process-name')),
                                ('job_id', YLeaf(YType.int32, 'job-id')),
                                ('instance', YLeaf(YType.uint32, 'instance')),
                                ('connected_at', YLeaf(YType.uint32, 'connected-at')),
                                ('number_of_created_sscb', YLeaf(YType.uint32, 'number-of-created-sscb')),
                                ('number_of_deleted_sscb', YLeaf(YType.uint32, 'number-of-deleted-sscb')),
                                ('last_cleared_time', YLeaf(YType.uint32, 'last-cleared-time')),
                            ])
                            self.id = None
                            self.ccb = None
                            self.pid = None
                            self.process_name = None
                            self.job_id = None
                            self.instance = None
                            self.connected_at = None
                            self.number_of_created_sscb = None
                            self.number_of_deleted_sscb = None
                            self.last_cleared_time = None

                            self.notification_statistic = YList(self)
                            self._segment_path = lambda: "statistic-client" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient, ['id', 'ccb', 'pid', 'process_name', 'job_id', 'instance', 'connected_at', 'number_of_created_sscb', 'number_of_deleted_sscb', 'last_cleared_time'], name, value)


                        class NotificationStatistic(Entity):
                            """
                            Various types of notification stats
                            
                            .. attribute:: queued_count
                            
                            	how many were queued
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: failed_count
                            
                            	Errors while queuing the notifs
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delivered_count
                            
                            	How many were picked up by app?
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: dropped_count
                            
                            	How many were dropped because of timeout
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic, self).__init__()

                                self.yang_name = "notification-statistic"
                                self.yang_parent_name = "statistic-client"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('queued_count', YLeaf(YType.uint32, 'queued-count')),
                                    ('failed_count', YLeaf(YType.uint32, 'failed-count')),
                                    ('delivered_count', YLeaf(YType.uint32, 'delivered-count')),
                                    ('dropped_count', YLeaf(YType.uint32, 'dropped-count')),
                                ])
                                self.queued_count = None
                                self.failed_count = None
                                self.delivered_count = None
                                self.dropped_count = None
                                self._segment_path = lambda: "notification-statistic"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic, ['queued_count', 'failed_count', 'delivered_count', 'dropped_count'], name, value)


                class StatisticSets(Entity):
                    """
                    Table listing NSR connections for which
                    statistic information is provided
                    
                    .. attribute:: statistic_set
                    
                    	showing statistic information of NSR Session Set
                    	**type**\: list of  		 :py:class:`StatisticSet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Statistics.StatisticSets, self).__init__()

                        self.yang_name = "statistic-sets"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("statistic-set", ("statistic_set", TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet))])
                        self._leafs = OrderedDict()

                        self.statistic_set = YList(self)
                        self._segment_path = lambda: "statistic-sets"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticSets, [], name, value)


                    class StatisticSet(Entity):
                        """
                        showing statistic information of NSR Session
                        Set
                        
                        .. attribute:: id  (key)
                        
                        	ID of NSR Session Set
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: sscb
                        
                        	SSCB Address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: set_id
                        
                        	ID of this Session\-set
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_attempted_init_sync
                        
                        	no. of initial\-sync attempts
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_succeeded_init_sync
                        
                        	no. of initial\-sync successes
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_failed_init_sync
                        
                        	no. of initial\-sync failures
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_failover
                        
                        	Number of Switch\-overs
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_nsr_resets
                        
                        	Number of times NSR was reset for the session
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: last_cleared_time
                        
                        	Time of last clear (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet, self).__init__()

                            self.yang_name = "statistic-set"
                            self.yang_parent_name = "statistic-sets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('sscb', YLeaf(YType.uint64, 'sscb')),
                                ('set_id', YLeaf(YType.uint32, 'set-id')),
                                ('number_of_attempted_init_sync', YLeaf(YType.uint32, 'number-of-attempted-init-sync')),
                                ('number_of_succeeded_init_sync', YLeaf(YType.uint32, 'number-of-succeeded-init-sync')),
                                ('number_of_failed_init_sync', YLeaf(YType.uint32, 'number-of-failed-init-sync')),
                                ('number_of_failover', YLeaf(YType.uint32, 'number-of-failover')),
                                ('number_of_nsr_resets', YLeaf(YType.uint32, 'number-of-nsr-resets')),
                                ('last_cleared_time', YLeaf(YType.uint32, 'last-cleared-time')),
                            ])
                            self.id = None
                            self.sscb = None
                            self.set_id = None
                            self.number_of_attempted_init_sync = None
                            self.number_of_succeeded_init_sync = None
                            self.number_of_failed_init_sync = None
                            self.number_of_failover = None
                            self.number_of_nsr_resets = None
                            self.last_cleared_time = None
                            self._segment_path = lambda: "statistic-set" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet, ['id', 'sscb', 'set_id', 'number_of_attempted_init_sync', 'number_of_succeeded_init_sync', 'number_of_failed_init_sync', 'number_of_failover', 'number_of_nsr_resets', 'last_cleared_time'], name, value)


                class StatisticSessions(Entity):
                    """
                    Table listing NSR connections for which
                    statistic information is provided
                    
                    .. attribute:: statistic_session
                    
                    	showing statistic information of TCP connections
                    	**type**\: list of  		 :py:class:`StatisticSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2018-02-14'

                    def __init__(self):
                        super(TcpNsr.Nodes.Node.Statistics.StatisticSessions, self).__init__()

                        self.yang_name = "statistic-sessions"
                        self.yang_parent_name = "statistics"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("statistic-session", ("statistic_session", TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession))])
                        self._leafs = OrderedDict()

                        self.statistic_session = YList(self)
                        self._segment_path = lambda: "statistic-sessions"

                    def __setattr__(self, name, value):
                        self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticSessions, [], name, value)


                    class StatisticSession(Entity):
                        """
                        showing statistic information of TCP
                        connections
                        
                        .. attribute:: id  (key)
                        
                        	ID of TCP connection
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: snd_counters
                        
                        	Send path counters for the PCB
                        	**type**\:  :py:class:`SndCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters>`
                        
                        .. attribute:: pcb
                        
                        	PCB Address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: number_of_times_nsr_up
                        
                        	no. of times nsr went up
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_timers_nsr_down
                        
                        	no. of times nsr went down
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_times_nsr_disabled
                        
                        	no. of times nsr was disabled
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: number_of_times_nsr_fail_over
                        
                        	no. of times fail\-over occured
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: internal_ack_drops_not_replicated
                        
                        	Number of iACKs dropped because session is not replicated
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: internal_ack_drops_initsync_first_phase
                        
                        	Number of iACKs dropped because 1st phase of init\-sync is in progress
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: internal_ack_drops_stale
                        
                        	Number of stale iACKs dropped
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: internal_ack_drops_immediate_match
                        
                        	Number of iACKs not held because of an immediate match
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: last_cleared_time
                        
                        	Time of last clear (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: second
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2018-02-14'

                        def __init__(self):
                            super(TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession, self).__init__()

                            self.yang_name = "statistic-session"
                            self.yang_parent_name = "statistic-sessions"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['id']
                            self._child_container_classes = OrderedDict([("snd-counters", ("snd_counters", TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.str, 'id')),
                                ('pcb', YLeaf(YType.uint64, 'pcb')),
                                ('number_of_times_nsr_up', YLeaf(YType.uint32, 'number-of-times-nsr-up')),
                                ('number_of_timers_nsr_down', YLeaf(YType.uint32, 'number-of-timers-nsr-down')),
                                ('number_of_times_nsr_disabled', YLeaf(YType.uint32, 'number-of-times-nsr-disabled')),
                                ('number_of_times_nsr_fail_over', YLeaf(YType.uint32, 'number-of-times-nsr-fail-over')),
                                ('internal_ack_drops_not_replicated', YLeaf(YType.uint64, 'internal-ack-drops-not-replicated')),
                                ('internal_ack_drops_initsync_first_phase', YLeaf(YType.uint64, 'internal-ack-drops-initsync-first-phase')),
                                ('internal_ack_drops_stale', YLeaf(YType.uint64, 'internal-ack-drops-stale')),
                                ('internal_ack_drops_immediate_match', YLeaf(YType.uint64, 'internal-ack-drops-immediate-match')),
                                ('last_cleared_time', YLeaf(YType.uint32, 'last-cleared-time')),
                            ])
                            self.id = None
                            self.pcb = None
                            self.number_of_times_nsr_up = None
                            self.number_of_timers_nsr_down = None
                            self.number_of_times_nsr_disabled = None
                            self.number_of_times_nsr_fail_over = None
                            self.internal_ack_drops_not_replicated = None
                            self.internal_ack_drops_initsync_first_phase = None
                            self.internal_ack_drops_stale = None
                            self.internal_ack_drops_immediate_match = None
                            self.last_cleared_time = None

                            self.snd_counters = TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters()
                            self.snd_counters.parent = self
                            self._children_name_map["snd_counters"] = "snd-counters"
                            self._children_yang_names.add("snd-counters")
                            self._segment_path = lambda: "statistic-session" + "[id='" + str(self.id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession, ['id', 'pcb', 'number_of_times_nsr_up', 'number_of_timers_nsr_down', 'number_of_times_nsr_disabled', 'number_of_times_nsr_fail_over', 'internal_ack_drops_not_replicated', 'internal_ack_drops_initsync_first_phase', 'internal_ack_drops_stale', 'internal_ack_drops_immediate_match', 'last_cleared_time'], name, value)


                        class SndCounters(Entity):
                            """
                            Send path counters for the PCB
                            
                            .. attribute:: data_xfer_send
                            
                            	Number of successful DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_send_total
                            
                            	Amount of data transferred
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_xfer_send_drop
                            
                            	Number of failed DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_send_iov_alloc
                            
                            	Number of data transfer msgs., that required new IOV's to be allocated
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv
                            
                            	Number of received DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv_success
                            
                            	Number of successfully received DATA transfers
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv_fail_buffer_trim
                            
                            	Number of received DATA transfers that had buffer trim failures
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_xfer_rcv_fail_snd_una_out_of_sync
                            
                            	Number of received DATA transfers that had failures because the send path was out of sync
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_send
                            
                            	Number of successful Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_send_units
                            
                            	Number of segement units transferred via the successful Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_send_drop
                            
                            	Number of failed Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv
                            
                            	Number of received Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_success
                            
                            	Number of successfully received Segmentation instruction messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_fail_buffer_trim
                            
                            	Number of received Segmentation instructions that had buffer trim failures
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: seg_instr_rcv_fail_tcp_process
                            
                            	Number of received Segmentation instructions that had failures during TCP processing
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_send
                            
                            	Number of successful NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_send_drop
                            
                            	Number of failed NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv
                            
                            	Number of received NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv_success
                            
                            	Number of successfully received NACK messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: nack_rcv_fail_data_send
                            
                            	Number of received NACK messages that had failures when sending data in response to the NACK
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_send
                            
                            	Number of successful Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_send_drop
                            
                            	Number of failed Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv
                            
                            	Number of received Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv_success
                            
                            	Number of successfully received Cleanup messages
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: cleanup_rcv_fail_buffer_trim
                            
                            	Number of Cleanup messages that had trim failures
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2018-02-14'

                            def __init__(self):
                                super(TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters, self).__init__()

                                self.yang_name = "snd-counters"
                                self.yang_parent_name = "statistic-session"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('data_xfer_send', YLeaf(YType.uint32, 'data-xfer-send')),
                                    ('data_xfer_send_total', YLeaf(YType.uint64, 'data-xfer-send-total')),
                                    ('data_xfer_send_drop', YLeaf(YType.uint32, 'data-xfer-send-drop')),
                                    ('data_xfer_send_iov_alloc', YLeaf(YType.uint32, 'data-xfer-send-iov-alloc')),
                                    ('data_xfer_rcv', YLeaf(YType.uint32, 'data-xfer-rcv')),
                                    ('data_xfer_rcv_success', YLeaf(YType.uint32, 'data-xfer-rcv-success')),
                                    ('data_xfer_rcv_fail_buffer_trim', YLeaf(YType.uint32, 'data-xfer-rcv-fail-buffer-trim')),
                                    ('data_xfer_rcv_fail_snd_una_out_of_sync', YLeaf(YType.uint32, 'data-xfer-rcv-fail-snd-una-out-of-sync')),
                                    ('seg_instr_send', YLeaf(YType.uint32, 'seg-instr-send')),
                                    ('seg_instr_send_units', YLeaf(YType.uint32, 'seg-instr-send-units')),
                                    ('seg_instr_send_drop', YLeaf(YType.uint32, 'seg-instr-send-drop')),
                                    ('seg_instr_rcv', YLeaf(YType.uint32, 'seg-instr-rcv')),
                                    ('seg_instr_rcv_success', YLeaf(YType.uint32, 'seg-instr-rcv-success')),
                                    ('seg_instr_rcv_fail_buffer_trim', YLeaf(YType.uint32, 'seg-instr-rcv-fail-buffer-trim')),
                                    ('seg_instr_rcv_fail_tcp_process', YLeaf(YType.uint32, 'seg-instr-rcv-fail-tcp-process')),
                                    ('nack_send', YLeaf(YType.uint32, 'nack-send')),
                                    ('nack_send_drop', YLeaf(YType.uint32, 'nack-send-drop')),
                                    ('nack_rcv', YLeaf(YType.uint32, 'nack-rcv')),
                                    ('nack_rcv_success', YLeaf(YType.uint32, 'nack-rcv-success')),
                                    ('nack_rcv_fail_data_send', YLeaf(YType.uint32, 'nack-rcv-fail-data-send')),
                                    ('cleanup_send', YLeaf(YType.uint32, 'cleanup-send')),
                                    ('cleanup_send_drop', YLeaf(YType.uint32, 'cleanup-send-drop')),
                                    ('cleanup_rcv', YLeaf(YType.uint32, 'cleanup-rcv')),
                                    ('cleanup_rcv_success', YLeaf(YType.uint32, 'cleanup-rcv-success')),
                                    ('cleanup_rcv_fail_buffer_trim', YLeaf(YType.uint32, 'cleanup-rcv-fail-buffer-trim')),
                                ])
                                self.data_xfer_send = None
                                self.data_xfer_send_total = None
                                self.data_xfer_send_drop = None
                                self.data_xfer_send_iov_alloc = None
                                self.data_xfer_rcv = None
                                self.data_xfer_rcv_success = None
                                self.data_xfer_rcv_fail_buffer_trim = None
                                self.data_xfer_rcv_fail_snd_una_out_of_sync = None
                                self.seg_instr_send = None
                                self.seg_instr_send_units = None
                                self.seg_instr_send_drop = None
                                self.seg_instr_rcv = None
                                self.seg_instr_rcv_success = None
                                self.seg_instr_rcv_fail_buffer_trim = None
                                self.seg_instr_rcv_fail_tcp_process = None
                                self.nack_send = None
                                self.nack_send_drop = None
                                self.nack_rcv = None
                                self.nack_rcv_success = None
                                self.nack_rcv_fail_data_send = None
                                self.cleanup_send = None
                                self.cleanup_send_drop = None
                                self.cleanup_rcv = None
                                self.cleanup_rcv_success = None
                                self.cleanup_rcv_fail_buffer_trim = None
                                self._segment_path = lambda: "snd-counters"

                            def __setattr__(self, name, value):
                                self._perform_setattr(TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters, ['data_xfer_send', 'data_xfer_send_total', 'data_xfer_send_drop', 'data_xfer_send_iov_alloc', 'data_xfer_rcv', 'data_xfer_rcv_success', 'data_xfer_rcv_fail_buffer_trim', 'data_xfer_rcv_fail_snd_una_out_of_sync', 'seg_instr_send', 'seg_instr_send_units', 'seg_instr_send_drop', 'seg_instr_rcv', 'seg_instr_rcv_success', 'seg_instr_rcv_fail_buffer_trim', 'seg_instr_rcv_fail_tcp_process', 'nack_send', 'nack_send_drop', 'nack_rcv', 'nack_rcv_success', 'nack_rcv_fail_data_send', 'cleanup_send', 'cleanup_send_drop', 'cleanup_rcv', 'cleanup_rcv_success', 'cleanup_rcv_fail_buffer_trim'], name, value)

    def clone_ptr(self):
        self._top_entity = TcpNsr()
        return self._top_entity

