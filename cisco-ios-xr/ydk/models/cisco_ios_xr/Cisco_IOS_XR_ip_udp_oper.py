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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AddrFamilyEnum(Enum):
    """
    AddrFamilyEnum

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

    unspecified = 0

    local = 1

    inet = 2

    implink = 3

    pup = 4

    chaos = 5

    ns = 6

    iso = 7

    ecma = 8

    data_kit = 9

    ccitt = 10

    sna = 11

    de_cnet = 12

    dli = 13

    lat = 14

    hylink = 15

    appletalk = 16

    route = 17

    link = 18

    pseudo_xtp = 19

    coip = 20

    cnt = 21

    pseudo_rtip = 22

    ipx = 23

    sip = 24

    pseudo_pip = 25

    inet6 = 26

    snap = 27

    clnl = 28

    chdlc = 29

    ppp = 30

    host_cas = 31

    dsp = 32

    sap = 33

    atm = 34

    fr = 35

    mso = 36

    dchan = 37

    cas = 38

    nat = 39

    ether = 40

    srp = 41


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['AddrFamilyEnum']


class LptsPcbQueryEnum(Enum):
    """
    LptsPcbQueryEnum

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

    all = 0

    static_policy = 1

    interface = 2

    packet = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['LptsPcbQueryEnum']


class MessageTypeIcmpEnum(Enum):
    """
    MessageTypeIcmpEnum

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

    echo_reply = 0

    destination_unreachable = 3

    source_quench = 4

    redirect = 5

    alternate_host_address = 6

    echo = 8

    router_advertisement = 9

    router_selection = 10

    time_exceeded = 11

    parameter_problem = 12

    time_stamp = 13

    time_stamp_reply = 14

    information_request = 15

    information_reply = 16

    address_mask_request = 17

    address_mask_reply = 18

    trace_route = 30

    datagram_conversion_error = 31

    mobile_host_redirect = 32

    where_are_you = 33

    iam_here = 34

    mobile_registration_request = 35

    mobile_registration_reply = 36

    domain_name_request = 37


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpEnum']


class MessageTypeIcmpEnum(Enum):
    """
    MessageTypeIcmpEnum

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

    echo_reply = 0

    destination_unreachable = 3

    source_quench = 4

    redirect = 5

    alternate_host_address = 6

    echo = 8

    router_advertisement = 9

    router_selection = 10

    time_exceeded = 11

    parameter_problem = 12

    time_stamp = 13

    time_stamp_reply = 14

    information_request = 15

    information_reply = 16

    address_mask_request = 17

    address_mask_reply = 18

    trace_route = 30

    datagram_conversion_error = 31

    mobile_host_redirect = 32

    where_are_you = 33

    iam_here = 34

    mobile_registration_request = 35

    mobile_registration_reply = 36

    domain_name_request = 37


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpEnum']


class MessageTypeIcmpv6Enum(Enum):
    """
    MessageTypeIcmpv6Enum

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

    destination_unreachable = 1

    packet_too_big = 2

    time_exceeded = 3

    parameter_problem = 4

    echo_request = 128

    echo_reply = 129

    multicast_listener_query = 130

    multicast_listener_report = 131

    multicast_listener_done = 132

    router_solicitation = 133

    router_advertisement = 134

    neighbor_solicitation = 135

    neighbor_advertisement = 136

    redirect_message = 137

    router_renumbering = 138

    node_information_query = 139

    node_information_reply = 140

    inverse_neighbor_discovery_solicitaion = 141

    inverse_neighbor_discover_advertisement = 142

    v2_multicast_listener_report = 143

    home_agent_address_discovery_request = 144

    home_agent_address_discovery_reply = 145

    mobile_prefix_solicitation = 146

    mobile_prefix_advertisement = 147

    certification_path_solicitation_message = 148

    certification_path_advertisement_message = 149

    experimental_mobility_protocols = 150

    multicast_router_advertisement = 151

    multicast_router_solicitation = 152

    multicast_router_termination = 153

    fmipv6_messages = 154


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpv6Enum']


class MessageTypeIcmpv6Enum(Enum):
    """
    MessageTypeIcmpv6Enum

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

    destination_unreachable = 1

    packet_too_big = 2

    time_exceeded = 3

    parameter_problem = 4

    echo_request = 128

    echo_reply = 129

    multicast_listener_query = 130

    multicast_listener_report = 131

    multicast_listener_done = 132

    router_solicitation = 133

    router_advertisement = 134

    neighbor_solicitation = 135

    neighbor_advertisement = 136

    redirect_message = 137

    router_renumbering = 138

    node_information_query = 139

    node_information_reply = 140

    inverse_neighbor_discovery_solicitaion = 141

    inverse_neighbor_discover_advertisement = 142

    v2_multicast_listener_report = 143

    home_agent_address_discovery_request = 144

    home_agent_address_discovery_reply = 145

    mobile_prefix_solicitation = 146

    mobile_prefix_advertisement = 147

    certification_path_solicitation_message = 148

    certification_path_advertisement_message = 149

    experimental_mobility_protocols = 150

    multicast_router_advertisement = 151

    multicast_router_solicitation = 152

    multicast_router_termination = 153

    fmipv6_messages = 154


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpv6Enum']


class MessageTypeIgmpEnum(Enum):
    """
    MessageTypeIgmpEnum

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

    membership_query = 17

    v1_membership_report = 18

    dvmrp = 19

    pi_mv1 = 20

    cisco_trace_messages = 21

    v2_membership_report = 22

    v2_leave_group = 23

    multicast_traceroute_response = 30

    multicast_traceroute = 31

    v3_membership_report = 34

    multicast_router_advertisement = 48

    multicast_router_solicitation = 49

    multicast_router_termination = 50


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIgmpEnum']


class MessageTypeIgmpEnum(Enum):
    """
    MessageTypeIgmpEnum

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

    membership_query = 17

    v1_membership_report = 18

    dvmrp = 19

    pi_mv1 = 20

    cisco_trace_messages = 21

    v2_membership_report = 22

    v2_leave_group = 23

    multicast_traceroute_response = 30

    multicast_traceroute = 31

    v3_membership_report = 34

    multicast_router_advertisement = 48

    multicast_router_solicitation = 49

    multicast_router_termination = 50


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIgmpEnum']


class PacketEnum(Enum):
    """
    PacketEnum

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

    icmp = 0

    icm_pv6 = 1

    igmp = 2

    unknown = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['PacketEnum']


class UdpAddressFamilyEnum(Enum):
    """
    UdpAddressFamilyEnum

    Address Family Type

    .. data:: ipv4 = 2

    	IPv4

    .. data:: ipv6 = 10

    	IPv6

    """

    ipv4 = 2

    ipv6 = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['UdpAddressFamilyEnum']



class Udp(object):
    """
    IP UDP Operational Data
    
    .. attribute:: nodes
    
    	Node\-specific UDP operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2016-02-26'

    def __init__(self):
        self.nodes = Udp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific UDP operational data
        
        .. attribute:: node
        
        	UDP operational data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2016-02-26'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_name = None
                self.statistics = Udp.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Statistics(object):
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
                    self.parent = None
                    self.ipv4_traffic = Udp.Nodes.Node.Statistics.Ipv4Traffic()
                    self.ipv4_traffic.parent = self
                    self.ipv6_traffic = Udp.Nodes.Node.Statistics.Ipv6Traffic()
                    self.ipv6_traffic.parent = self


                class Ipv4Traffic(object):
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
                        self.parent = None
                        self.udp_bad_length_packets = None
                        self.udp_checksum_error_packets = None
                        self.udp_dropped_packets = None
                        self.udp_input_packets = None
                        self.udp_no_port_packets = None
                        self.udp_output_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:ipv4-traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.udp_bad_length_packets is not None:
                            return True

                        if self.udp_checksum_error_packets is not None:
                            return True

                        if self.udp_dropped_packets is not None:
                            return True

                        if self.udp_input_packets is not None:
                            return True

                        if self.udp_no_port_packets is not None:
                            return True

                        if self.udp_output_packets is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['Udp.Nodes.Node.Statistics.Ipv4Traffic']['meta_info']


                class Ipv6Traffic(object):
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
                        self.parent = None
                        self.udp_bad_length_packets = None
                        self.udp_checksum_error_packets = None
                        self.udp_dropped_packets = None
                        self.udp_input_packets = None
                        self.udp_no_port_packets = None
                        self.udp_output_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:ipv6-traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.udp_bad_length_packets is not None:
                            return True

                        if self.udp_checksum_error_packets is not None:
                            return True

                        if self.udp_dropped_packets is not None:
                            return True

                        if self.udp_input_packets is not None:
                            return True

                        if self.udp_no_port_packets is not None:
                            return True

                        if self.udp_output_packets is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['Udp.Nodes.Node.Statistics.Ipv6Traffic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ipv4_traffic is not None and self.ipv4_traffic._has_data():
                        return True

                    if self.ipv6_traffic is not None and self.ipv6_traffic._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['Udp.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-udp-oper:udp/Cisco-IOS-XR-ip-udp-oper:nodes/Cisco-IOS-XR-ip-udp-oper:node[Cisco-IOS-XR-ip-udp-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                return meta._meta_table['Udp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-udp-oper:udp/Cisco-IOS-XR-ip-udp-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
            return meta._meta_table['Udp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-udp-oper:udp'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['Udp']['meta_info']


class UdpConnection(object):
    """
    udp connection
    
    .. attribute:: nodes
    
    	List of UDP connections nodes
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2016-02-26'

    def __init__(self):
        self.nodes = UdpConnection.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of UDP connections nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2016-02-26'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
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
                self.parent = None
                self.node_name = None
                self.lpts = UdpConnection.Nodes.Node.Lpts()
                self.lpts.parent = self
                self.pcb_briefs = UdpConnection.Nodes.Node.PcbBriefs()
                self.pcb_briefs.parent = self
                self.pcb_details = UdpConnection.Nodes.Node.PcbDetails()
                self.pcb_details.parent = self
                self.statistics = UdpConnection.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Statistics(object):
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
                    self.parent = None
                    self.clients = UdpConnection.Nodes.Node.Statistics.Clients()
                    self.clients.parent = self
                    self.pcb_statistics = UdpConnection.Nodes.Node.Statistics.PcbStatistics()
                    self.pcb_statistics.parent = self
                    self.summary = UdpConnection.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self


                class Clients(object):
                    """
                    Table listing clients
                    
                    .. attribute:: client
                    
                    	Describing Client ID
                    	**type**\: list of    :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients.Client>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        self.parent = None
                        self.client = YList()
                        self.client.parent = self
                        self.client.name = 'client'


                    class Client(object):
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
                            self.parent = None
                            self.client_id = None
                            self.client_jid = None
                            self.client_name = None
                            self.ipv4_received_packets = None
                            self.ipv4_sent_packets = None
                            self.ipv6_received_packets = None
                            self.ipv6_sent_packets = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.client_id is None:
                                raise YPYModelError('Key property client_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:client[Cisco-IOS-XR-ip-udp-oper:client-id = ' + str(self.client_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.client_id is not None:
                                return True

                            if self.client_jid is not None:
                                return True

                            if self.client_name is not None:
                                return True

                            if self.ipv4_received_packets is not None:
                                return True

                            if self.ipv4_sent_packets is not None:
                                return True

                            if self.ipv6_received_packets is not None:
                                return True

                            if self.ipv6_sent_packets is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.Statistics.Clients.Client']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:clients'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.client is not None:
                            for child_ref in self.client:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Statistics.Clients']['meta_info']


                class Summary(object):
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
                        self.parent = None
                        self.cloned_packets = None
                        self.failed_clone_packets = None
                        self.forward_broadcast_packets = None
                        self.received_bad_checksum_packets = None
                        self.received_drop_packets = None
                        self.received_no_port_packets = None
                        self.received_too_short_packets = None
                        self.received_total_packets = None
                        self.sent_error_packets = None
                        self.sent_total_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.cloned_packets is not None:
                            return True

                        if self.failed_clone_packets is not None:
                            return True

                        if self.forward_broadcast_packets is not None:
                            return True

                        if self.received_bad_checksum_packets is not None:
                            return True

                        if self.received_drop_packets is not None:
                            return True

                        if self.received_no_port_packets is not None:
                            return True

                        if self.received_too_short_packets is not None:
                            return True

                        if self.received_total_packets is not None:
                            return True

                        if self.sent_error_packets is not None:
                            return True

                        if self.sent_total_packets is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Statistics.Summary']['meta_info']


                class PcbStatistics(object):
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
                        self.parent = None
                        self.pcb_statistic = YList()
                        self.pcb_statistic.parent = self
                        self.pcb_statistic.name = 'pcb_statistic'


                    class PcbStatistic(object):
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
                            self.parent = None
                            self.pcb_address = None
                            self.is_paw_socket = None
                            self.receive = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive()
                            self.receive.parent = self
                            self.send = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send()
                            self.send.parent = self
                            self.vrf_id = None


                        class Send(object):
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
                                self.parent = None
                                self.failed_queued_net_io_packets = None
                                self.failed_queued_network_packets = None
                                self.received_application_bytes = None
                                self.received_xipc_pulses = None
                                self.sent_net_io_packets = None
                                self.sent_network_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:send'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.failed_queued_net_io_packets is not None:
                                    return True

                                if self.failed_queued_network_packets is not None:
                                    return True

                                if self.received_application_bytes is not None:
                                    return True

                                if self.received_xipc_pulses is not None:
                                    return True

                                if self.sent_net_io_packets is not None:
                                    return True

                                if self.sent_network_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send']['meta_info']


                        class Receive(object):
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
                                self.parent = None
                                self.failed_queued_application_packets = None
                                self.failed_queued_application_socket_packets = None
                                self.queued_application_packets = None
                                self.queued_application_socket_packets = None
                                self.received_network_packets = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:receive'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.failed_queued_application_packets is not None:
                                    return True

                                if self.failed_queued_application_socket_packets is not None:
                                    return True

                                if self.queued_application_packets is not None:
                                    return True

                                if self.queued_application_socket_packets is not None:
                                    return True

                                if self.received_network_packets is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.pcb_address is None:
                                raise YPYModelError('Key property pcb_address is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-statistic[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.pcb_address is not None:
                                return True

                            if self.is_paw_socket is not None:
                                return True

                            if self.receive is not None and self.receive._has_data():
                                return True

                            if self.send is not None and self.send._has_data():
                                return True

                            if self.vrf_id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-statistics'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pcb_statistic is not None:
                            for child_ref in self.pcb_statistic:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Statistics.PcbStatistics']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.clients is not None and self.clients._has_data():
                        return True

                    if self.pcb_statistics is not None and self.pcb_statistics._has_data():
                        return True

                    if self.summary is not None and self.summary._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.Statistics']['meta_info']


            class Lpts(object):
                """
                LPTS statistical data
                
                .. attribute:: queries
                
                	List of query options
                	**type**\:   :py:class:`Queries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2016-02-26'

                def __init__(self):
                    self.parent = None
                    self.queries = UdpConnection.Nodes.Node.Lpts.Queries()
                    self.queries.parent = self


                class Queries(object):
                    """
                    List of query options
                    
                    .. attribute:: query
                    
                    	Query option
                    	**type**\: list of    :py:class:`Query <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2016-02-26'

                    def __init__(self):
                        self.parent = None
                        self.query = YList()
                        self.query.parent = self
                        self.query.name = 'query'


                    class Query(object):
                        """
                        Query option
                        
                        .. attribute:: query_name  <key>
                        
                        	Query option
                        	**type**\:   :py:class:`LptsPcbQueryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.LptsPcbQueryEnum>`
                        
                        .. attribute:: pcbs
                        
                        	List of PCBs
                        	**type**\:   :py:class:`Pcbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs>`
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2016-02-26'

                        def __init__(self):
                            self.parent = None
                            self.query_name = None
                            self.pcbs = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs()
                            self.pcbs.parent = self


                        class Pcbs(object):
                            """
                            List of PCBs
                            
                            .. attribute:: pcb
                            
                            	A PCB information
                            	**type**\: list of    :py:class:`Pcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb>`
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2016-02-26'

                            def __init__(self):
                                self.parent = None
                                self.pcb = YList()
                                self.pcb.parent = self
                                self.pcb.name = 'pcb'


                            class Pcb(object):
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
                                    self.parent = None
                                    self.pcb_address = None
                                    self.common = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common()
                                    self.common.parent = self
                                    self.foreign_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress()
                                    self.foreign_address.parent = self
                                    self.foreign_port = None
                                    self.l4_protocol = None
                                    self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress()
                                    self.local_address.parent = self
                                    self.local_port = None


                                class LocalAddress(object):
                                    """
                                    Local IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                    
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
                                        self.parent = None
                                        self.af_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.af_name is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress']['meta_info']


                                class ForeignAddress(object):
                                    """
                                    Remote IP address
                                    
                                    .. attribute:: af_name
                                    
                                    	AFName
                                    	**type**\:   :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                    
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
                                        self.parent = None
                                        self.af_name = None
                                        self.ipv4_address = None
                                        self.ipv6_address = None

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:foreign-address'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.af_name is not None:
                                            return True

                                        if self.ipv4_address is not None:
                                            return True

                                        if self.ipv6_address is not None:
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress']['meta_info']


                                class Common(object):
                                    """
                                    Common PCB information
                                    
                                    .. attribute:: af_name
                                    
                                    	Address Family
                                    	**type**\:   :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                    
                                    .. attribute:: lpts_pcb
                                    
                                    	LPTS PCB information
                                    	**type**\:   :py:class:`LptsPcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb>`
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2016-02-26'

                                    def __init__(self):
                                        self.parent = None
                                        self.af_name = None
                                        self.lpts_pcb = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb()
                                        self.lpts_pcb.parent = self


                                    class LptsPcb(object):
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
                                            self.parent = None
                                            self.accept_mask = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask()
                                            self.accept_mask.parent = self
                                            self.filter = YList()
                                            self.filter.parent = self
                                            self.filter.name = 'filter'
                                            self.flow_types_info = None
                                            self.lpts_flags = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags()
                                            self.lpts_flags.parent = self
                                            self.options = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options()
                                            self.options.parent = self
                                            self.ttl = None


                                        class Options(object):
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
                                                self.parent = None
                                                self.is_ip_sla = None
                                                self.is_receive_filter = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:options'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.is_ip_sla is not None:
                                                    return True

                                                if self.is_receive_filter is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options']['meta_info']


                                        class LptsFlags(object):
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
                                                self.parent = None
                                                self.is_ignore_vrf_filter = None
                                                self.is_local_address_ignore = None
                                                self.is_pcb_bound = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:lpts-flags'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.is_ignore_vrf_filter is not None:
                                                    return True

                                                if self.is_local_address_ignore is not None:
                                                    return True

                                                if self.is_pcb_bound is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags']['meta_info']


                                        class AcceptMask(object):
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
                                                self.parent = None
                                                self.is_interface = None
                                                self.is_local_address = None
                                                self.is_local_port = None
                                                self.is_packet_type = None
                                                self.is_remote_address = None
                                                self.is_remote_port = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:accept-mask'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.is_interface is not None:
                                                    return True

                                                if self.is_local_address is not None:
                                                    return True

                                                if self.is_local_port is not None:
                                                    return True

                                                if self.is_packet_type is not None:
                                                    return True

                                                if self.is_remote_address is not None:
                                                    return True

                                                if self.is_remote_port is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask']['meta_info']


                                        class Filter(object):
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
                                                self.parent = None
                                                self.flow_types_info = None
                                                self.interface_name = None
                                                self.local_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress()
                                                self.local_address.parent = self
                                                self.local_length = None
                                                self.packet_type = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType()
                                                self.packet_type.parent = self
                                                self.priority = None
                                                self.receive_local_port = None
                                                self.receive_remote_port = None
                                                self.remote_address = UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress()
                                                self.remote_address.parent = self
                                                self.remote_length = None
                                                self.ttl = None


                                            class PacketType(object):
                                                """
                                                Protocol\-specific packet type
                                                
                                                .. attribute:: icm_pv6_message_type
                                                
                                                	ICMPv6 message type
                                                	**type**\:   :py:class:`MessageTypeIcmpv6Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmpv6Enum>`
                                                
                                                .. attribute:: icmp_message_type
                                                
                                                	ICMP message type
                                                	**type**\:   :py:class:`MessageTypeIcmpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmpEnum>`
                                                
                                                .. attribute:: igmp_message_type
                                                
                                                	IGMP message type
                                                	**type**\:   :py:class:`MessageTypeIgmpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIgmpEnum>`
                                                
                                                .. attribute:: message_id
                                                
                                                	Message type in number
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: type
                                                
                                                	Type
                                                	**type**\:   :py:class:`PacketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.PacketEnum>`
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2016-02-26'

                                                def __init__(self):
                                                    self.parent = None
                                                    self.icm_pv6_message_type = None
                                                    self.icmp_message_type = None
                                                    self.igmp_message_type = None
                                                    self.message_id = None
                                                    self.type = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:packet-type'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.icm_pv6_message_type is not None:
                                                        return True

                                                    if self.icmp_message_type is not None:
                                                        return True

                                                    if self.igmp_message_type is not None:
                                                        return True

                                                    if self.message_id is not None:
                                                        return True

                                                    if self.type is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType']['meta_info']


                                            class RemoteAddress(object):
                                                """
                                                Remote address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\:   :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                                
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
                                                    self.parent = None
                                                    self.af_name = None
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:remote-address'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.af_name is not None:
                                                        return True

                                                    if self.ipv4_address is not None:
                                                        return True

                                                    if self.ipv6_address is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress']['meta_info']


                                            class LocalAddress(object):
                                                """
                                                Local address
                                                
                                                .. attribute:: af_name
                                                
                                                	AFName
                                                	**type**\:   :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                                
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
                                                    self.parent = None
                                                    self.af_name = None
                                                    self.ipv4_address = None
                                                    self.ipv6_address = None

                                                @property
                                                def _common_path(self):
                                                    if self.parent is None:
                                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                                                def is_config(self):
                                                    ''' Returns True if this instance represents config data else returns False '''
                                                    return False

                                                def _has_data(self):
                                                    if self.af_name is not None:
                                                        return True

                                                    if self.ipv4_address is not None:
                                                        return True

                                                    if self.ipv6_address is not None:
                                                        return True

                                                    return False

                                                @staticmethod
                                                def _meta_info():
                                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress']['meta_info']

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:filter'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if self.flow_types_info is not None:
                                                    return True

                                                if self.interface_name is not None:
                                                    return True

                                                if self.local_address is not None and self.local_address._has_data():
                                                    return True

                                                if self.local_length is not None:
                                                    return True

                                                if self.packet_type is not None and self.packet_type._has_data():
                                                    return True

                                                if self.priority is not None:
                                                    return True

                                                if self.receive_local_port is not None:
                                                    return True

                                                if self.receive_remote_port is not None:
                                                    return True

                                                if self.remote_address is not None and self.remote_address._has_data():
                                                    return True

                                                if self.remote_length is not None:
                                                    return True

                                                if self.ttl is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYModelError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:lpts-pcb'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if self.accept_mask is not None and self.accept_mask._has_data():
                                                return True

                                            if self.filter is not None:
                                                for child_ref in self.filter:
                                                    if child_ref._has_data():
                                                        return True

                                            if self.flow_types_info is not None:
                                                return True

                                            if self.lpts_flags is not None and self.lpts_flags._has_data():
                                                return True

                                            if self.options is not None and self.options._has_data():
                                                return True

                                            if self.ttl is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                            return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYModelError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:common'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if self.af_name is not None:
                                            return True

                                        if self.lpts_pcb is not None and self.lpts_pcb._has_data():
                                            return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.pcb_address is None:
                                        raise YPYModelError('Key property pcb_address is None')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if self.pcb_address is not None:
                                        return True

                                    if self.common is not None and self.common._has_data():
                                        return True

                                    if self.foreign_address is not None and self.foreign_address._has_data():
                                        return True

                                    if self.foreign_port is not None:
                                        return True

                                    if self.l4_protocol is not None:
                                        return True

                                    if self.local_address is not None and self.local_address._has_data():
                                        return True

                                    if self.local_port is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcbs'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.pcb is not None:
                                    for child_ref in self.pcb:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                                return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.query_name is None:
                                raise YPYModelError('Key property query_name is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:query[Cisco-IOS-XR-ip-udp-oper:query-name = ' + str(self.query_name) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.query_name is not None:
                                return True

                            if self.pcbs is not None and self.pcbs._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries.Query']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:queries'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.query is not None:
                            for child_ref in self.query:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.Lpts.Queries']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:lpts'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.queries is not None and self.queries._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.Lpts']['meta_info']


            class PcbDetails(object):
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
                    self.parent = None
                    self.pcb_detail = YList()
                    self.pcb_detail.parent = self
                    self.pcb_detail.name = 'pcb_detail'


                class PcbDetail(object):
                    """
                    Detail information about a UDP connection
                    
                    .. attribute:: pcb_address  <key>
                    
                    	Protocol Control Block address
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\:   :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                    
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
                        self.parent = None
                        self.pcb_address = None
                        self.af_name = None
                        self.foreign_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress()
                        self.foreign_address.parent = self
                        self.foreign_port = None
                        self.local_address = UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress()
                        self.local_address.parent = self
                        self.local_port = None
                        self.local_process_id = None
                        self.receive_queue = None
                        self.send_queue = None
                        self.vrf_id = None


                    class LocalAddress(object):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress']['meta_info']


                    class ForeignAddress(object):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:foreign-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.pcb_address is None:
                            raise YPYModelError('Key property pcb_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-detail[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pcb_address is not None:
                            return True

                        if self.af_name is not None:
                            return True

                        if self.foreign_address is not None and self.foreign_address._has_data():
                            return True

                        if self.foreign_port is not None:
                            return True

                        if self.local_address is not None and self.local_address._has_data():
                            return True

                        if self.local_port is not None:
                            return True

                        if self.local_process_id is not None:
                            return True

                        if self.receive_queue is not None:
                            return True

                        if self.send_queue is not None:
                            return True

                        if self.vrf_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails.PcbDetail']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-details'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.pcb_detail is not None:
                        for child_ref in self.pcb_detail:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.PcbDetails']['meta_info']


            class PcbBriefs(object):
                """
                Brief information for list of UDP connections.
                
                .. attribute:: pcb_brief
                
                	Brief information about a UDP connection
                	**type**\: list of    :py:class:`PcbBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2016-02-26'

                def __init__(self):
                    self.parent = None
                    self.pcb_brief = YList()
                    self.pcb_brief.parent = self
                    self.pcb_brief.name = 'pcb_brief'


                class PcbBrief(object):
                    """
                    Brief information about a UDP connection
                    
                    .. attribute:: pcb_address  <key>
                    
                    	Protocol Control Block address
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    .. attribute:: af_name
                    
                    	Address family
                    	**type**\:   :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                    
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
                        self.parent = None
                        self.pcb_address = None
                        self.af_name = None
                        self.foreign_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress()
                        self.foreign_address.parent = self
                        self.foreign_port = None
                        self.local_address = UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress()
                        self.local_address.parent = self
                        self.local_port = None
                        self.receive_queue = None
                        self.send_queue = None
                        self.vrf_id = None


                    class LocalAddress(object):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:local-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress']['meta_info']


                    class ForeignAddress(object):
                        """
                        Foreign address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:   :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                            self.parent = None
                            self.af_name = None
                            self.ipv4_address = None
                            self.ipv6_address = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:foreign-address'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.af_name is not None:
                                return True

                            if self.ipv4_address is not None:
                                return True

                            if self.ipv6_address is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                            return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.pcb_address is None:
                            raise YPYModelError('Key property pcb_address is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-brief[Cisco-IOS-XR-ip-udp-oper:pcb-address = ' + str(self.pcb_address) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.pcb_address is not None:
                            return True

                        if self.af_name is not None:
                            return True

                        if self.foreign_address is not None and self.foreign_address._has_data():
                            return True

                        if self.foreign_port is not None:
                            return True

                        if self.local_address is not None and self.local_address._has_data():
                            return True

                        if self.local_port is not None:
                            return True

                        if self.receive_queue is not None:
                            return True

                        if self.send_queue is not None:
                            return True

                        if self.vrf_id is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                        return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs.PcbBrief']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-udp-oper:pcb-briefs'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.pcb_brief is not None:
                        for child_ref in self.pcb_brief:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                    return meta._meta_table['UdpConnection.Nodes.Node.PcbBriefs']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYModelError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-udp-oper:udp-connection/Cisco-IOS-XR-ip-udp-oper:nodes/Cisco-IOS-XR-ip-udp-oper:node[Cisco-IOS-XR-ip-udp-oper:node-name = ' + str(self.node_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.node_name is not None:
                    return True

                if self.lpts is not None and self.lpts._has_data():
                    return True

                if self.pcb_briefs is not None and self.pcb_briefs._has_data():
                    return True

                if self.pcb_details is not None and self.pcb_details._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
                return meta._meta_table['UdpConnection.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-udp-oper:udp-connection/Cisco-IOS-XR-ip-udp-oper:nodes'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.node is not None:
                for child_ref in self.node:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
            return meta._meta_table['UdpConnection.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-udp-oper:udp-connection'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['UdpConnection']['meta_info']


