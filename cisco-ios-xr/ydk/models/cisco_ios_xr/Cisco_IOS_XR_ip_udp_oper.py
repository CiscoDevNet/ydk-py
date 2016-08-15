""" Cisco_IOS_XR_ip_udp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-udp package operational data.

This module contains definitions
for the following management objects\:
  udp\: IP UDP Operational Data
  udp\-connection\: udp connection

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
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

    .. data:: UNSPECIFIED = 0

    	Unspecified

    .. data:: LOCAL = 1

    	Local to host (pipes, portals)

    .. data:: INET = 2

    	Internetwork: UDP, TCP, etc.

    .. data:: IMPLINK = 3

    	arpanet imp addresses

    .. data:: PUP = 4

    	Pup protocols: e.g. BSP

    .. data:: CHAOS = 5

    	mit CHAOS protocols

    .. data:: NS = 6

    	XEROX NS protocols

    .. data:: ISO = 7

    	ISO protocols

    .. data:: ECMA = 8

    	European computer manufacturers

    .. data:: DATA_KIT = 9

    	Datakit protocols

    .. data:: CCITT = 10

    	CCITT protocols, X.25 etc

    .. data:: SNA = 11

    	IBM SNA

    .. data:: DE_CNET = 12

    	DECnet

    .. data:: DLI = 13

    	DEC Direct data link interface

    .. data:: LAT = 14

    	LAT

    .. data:: HYLINK = 15

    	NSC Hyperchannel

    .. data:: APPLETALK = 16

    	Apple Talk

    .. data:: ROUTE = 17

    	Internal Routing Protocol

    .. data:: LINK = 18

    	Link layer interface

    .. data:: PSEUDO_XTP = 19

    	eXpress Transfer Protocol (no AF)

    .. data:: COIP = 20

    	Connection-oriented IP, aka ST II

    .. data:: CNT = 21

    	Computer Network Technology

    .. data:: PSEUDO_RTIP = 22

    	Help Identify RTIP packets

    .. data:: IPX = 23

    	Novell Internet Protocol

    .. data:: SIP = 24

    	Simple Internet Protocol

    .. data:: PSEUDO_PIP = 25

    	Help Identify PIP packets

    .. data:: INET6 = 26

    	IP version 6

    .. data:: SNAP = 27

    	802.2 SNAP sockets

    .. data:: CLNL = 28

    	SAP_CLNS + nlpid encaps

    .. data:: CHDLC = 29

    	cisco HDLC on serial

    .. data:: PPP = 30

    	PPP sockets

    .. data:: HOST_CAS = 31

    	Host-based CAS signaling

    .. data:: DSP = 32

    	DSP messaging

    .. data:: SAP = 33

    	SAP Sockets

    .. data:: ATM = 34

    	ATM Sockets

    .. data:: FR = 35

    	Frame Relay sockets

    .. data:: MSO = 36

    	Voice Media Stream Sockets

    .. data:: DCHAN = 37

    	ISDN D Channel Sockets

    .. data:: CAS = 38

    	Trunk Framer media IF Sockets

    .. data:: NAT = 39

    	Network Address Translation Sockets

    .. data:: ETHER = 40

    	Generic Ethernet Sockets

    .. data:: SRP = 41

    	Spatial Reuse Protocol Sockets

    """

    UNSPECIFIED = 0

    LOCAL = 1

    INET = 2

    IMPLINK = 3

    PUP = 4

    CHAOS = 5

    NS = 6

    ISO = 7

    ECMA = 8

    DATA_KIT = 9

    CCITT = 10

    SNA = 11

    DE_CNET = 12

    DLI = 13

    LAT = 14

    HYLINK = 15

    APPLETALK = 16

    ROUTE = 17

    LINK = 18

    PSEUDO_XTP = 19

    COIP = 20

    CNT = 21

    PSEUDO_RTIP = 22

    IPX = 23

    SIP = 24

    PSEUDO_PIP = 25

    INET6 = 26

    SNAP = 27

    CLNL = 28

    CHDLC = 29

    PPP = 30

    HOST_CAS = 31

    DSP = 32

    SAP = 33

    ATM = 34

    FR = 35

    MSO = 36

    DCHAN = 37

    CAS = 38

    NAT = 39

    ETHER = 40

    SRP = 41


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['AddrFamilyEnum']


class LptsPcbQueryEnum(Enum):
    """
    LptsPcbQueryEnum

    Lpts pcb query

    .. data:: ALL = 0

    	No filter

    .. data:: STATIC_POLICY = 1

    	Static policy filter

    .. data:: INTERFACE = 2

    	Interface filter

    .. data:: PACKET = 3

    	Packet type filter

    """

    ALL = 0

    STATIC_POLICY = 1

    INTERFACE = 2

    PACKET = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['LptsPcbQueryEnum']


class MessageTypeIcmpEnum(Enum):
    """
    MessageTypeIcmpEnum

    LPTS ICMP message types

    .. data:: ECHO_REPLY = 0

    	ICMP Packet type: Echo reply

    .. data:: DESTINATION_UNREACHABLE = 3

    	ICMP Packet type: Destination unreachable

    .. data:: SOURCE_QUENCH = 4

    	ICMP Packet type: Source quench

    .. data:: REDIRECT = 5

    	ICMP Packet type: Redirect

    .. data:: ALTERNATE_HOST_ADDRESS = 6

    	ICMP Packet type: Alternate host address

    .. data:: ECHO = 8

    	ICMP Packet type: Echo

    .. data:: ROUTER_ADVERTISEMENT = 9

    	ICMP Packet type: Router advertisement

    .. data:: ROUTER_SELECTION = 10

    	ICMP Packet type: Router selection

    .. data:: TIME_EXCEEDED = 11

    	ICMP Packet type: Time exceeded

    .. data:: PARAMETER_PROBLEM = 12

    	ICMP Packet type: Parameter problem

    .. data:: TIME_STAMP = 13

    	ICMP Packet type: Time stamp

    .. data:: TIME_STAMP_REPLY = 14

    	ICMP Packet type: Time stamp reply

    .. data:: INFORMATION_REQUEST = 15

    	ICMP Packet type: Information request

    .. data:: INFORMATION_REPLY = 16

    	ICMP Packet type: Information reply

    .. data:: ADDRESS_MASK_REQUEST = 17

    	ICMP Packet type: Address mask request

    .. data:: ADDRESS_MASK_REPLY = 18

    	ICMP Packet type: Address mask reply

    .. data:: TRACE_ROUTE = 30

    	ICMP Packet type: Trace route

    .. data:: DATAGRAM_CONVERSION_ERROR = 31

    	ICMP Packet type: Datagram Conversion error

    .. data:: MOBILE_HOST_REDIRECT = 32

    	ICMP Packet type: Mobile host redirect

    .. data:: WHERE_ARE_YOU = 33

    	ICMP Packet type: IPv6 where-are-you

    .. data:: IAM_HERE = 34

    	ICMP Packet type: IPv6 i-am-here

    .. data:: MOBILE_REGISTRATION_REQUEST = 35

    	ICMP Packet type: Mobile registration request

    .. data:: MOBILE_REGISTRATION_REPLY = 36

    	ICMP Packet type: Mobile registration reply

    .. data:: DOMAIN_NAME_REQUEST = 37

    	ICMP Packet type: Domain name request

    """

    ECHO_REPLY = 0

    DESTINATION_UNREACHABLE = 3

    SOURCE_QUENCH = 4

    REDIRECT = 5

    ALTERNATE_HOST_ADDRESS = 6

    ECHO = 8

    ROUTER_ADVERTISEMENT = 9

    ROUTER_SELECTION = 10

    TIME_EXCEEDED = 11

    PARAMETER_PROBLEM = 12

    TIME_STAMP = 13

    TIME_STAMP_REPLY = 14

    INFORMATION_REQUEST = 15

    INFORMATION_REPLY = 16

    ADDRESS_MASK_REQUEST = 17

    ADDRESS_MASK_REPLY = 18

    TRACE_ROUTE = 30

    DATAGRAM_CONVERSION_ERROR = 31

    MOBILE_HOST_REDIRECT = 32

    WHERE_ARE_YOU = 33

    IAM_HERE = 34

    MOBILE_REGISTRATION_REQUEST = 35

    MOBILE_REGISTRATION_REPLY = 36

    DOMAIN_NAME_REQUEST = 37


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpEnum']


class MessageTypeIcmpEnum(Enum):
    """
    MessageTypeIcmpEnum

    LPTS ICMP message types

    .. data:: ECHO_REPLY = 0

    	ICMP Packet type: Echo reply

    .. data:: DESTINATION_UNREACHABLE = 3

    	ICMP Packet type: Destination unreachable

    .. data:: SOURCE_QUENCH = 4

    	ICMP Packet type: Source quench

    .. data:: REDIRECT = 5

    	ICMP Packet type: Redirect

    .. data:: ALTERNATE_HOST_ADDRESS = 6

    	ICMP Packet type: Alternate host address

    .. data:: ECHO = 8

    	ICMP Packet type: Echo

    .. data:: ROUTER_ADVERTISEMENT = 9

    	ICMP Packet type: Router advertisement

    .. data:: ROUTER_SELECTION = 10

    	ICMP Packet type: Router selection

    .. data:: TIME_EXCEEDED = 11

    	ICMP Packet type: Time exceeded

    .. data:: PARAMETER_PROBLEM = 12

    	ICMP Packet type: Parameter problem

    .. data:: TIME_STAMP = 13

    	ICMP Packet type: Time stamp

    .. data:: TIME_STAMP_REPLY = 14

    	ICMP Packet type: Time stamp reply

    .. data:: INFORMATION_REQUEST = 15

    	ICMP Packet type: Information request

    .. data:: INFORMATION_REPLY = 16

    	ICMP Packet type: Information reply

    .. data:: ADDRESS_MASK_REQUEST = 17

    	ICMP Packet type: Address mask request

    .. data:: ADDRESS_MASK_REPLY = 18

    	ICMP Packet type: Address mask reply

    .. data:: TRACE_ROUTE = 30

    	ICMP Packet type: Trace route

    .. data:: DATAGRAM_CONVERSION_ERROR = 31

    	ICMP Packet type: Datagram Conversion error

    .. data:: MOBILE_HOST_REDIRECT = 32

    	ICMP Packet type: Mobile host redirect

    .. data:: WHERE_ARE_YOU = 33

    	ICMP Packet type: IPv6 where-are-you

    .. data:: IAM_HERE = 34

    	ICMP Packet type: IPv6 i-am-here

    .. data:: MOBILE_REGISTRATION_REQUEST = 35

    	ICMP Packet type: Mobile registration request

    .. data:: MOBILE_REGISTRATION_REPLY = 36

    	ICMP Packet type: Mobile registration reply

    .. data:: DOMAIN_NAME_REQUEST = 37

    	ICMP Packet type: Domain name request

    """

    ECHO_REPLY = 0

    DESTINATION_UNREACHABLE = 3

    SOURCE_QUENCH = 4

    REDIRECT = 5

    ALTERNATE_HOST_ADDRESS = 6

    ECHO = 8

    ROUTER_ADVERTISEMENT = 9

    ROUTER_SELECTION = 10

    TIME_EXCEEDED = 11

    PARAMETER_PROBLEM = 12

    TIME_STAMP = 13

    TIME_STAMP_REPLY = 14

    INFORMATION_REQUEST = 15

    INFORMATION_REPLY = 16

    ADDRESS_MASK_REQUEST = 17

    ADDRESS_MASK_REPLY = 18

    TRACE_ROUTE = 30

    DATAGRAM_CONVERSION_ERROR = 31

    MOBILE_HOST_REDIRECT = 32

    WHERE_ARE_YOU = 33

    IAM_HERE = 34

    MOBILE_REGISTRATION_REQUEST = 35

    MOBILE_REGISTRATION_REPLY = 36

    DOMAIN_NAME_REQUEST = 37


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpEnum']


class MessageTypeIcmpv6Enum(Enum):
    """
    MessageTypeIcmpv6Enum

    LPTS ICMPv6 message types

    .. data:: DESTINATION_UNREACHABLE = 1

    	ICMPv6 Packet type: Destination unreachable

    .. data:: PACKET_TOO_BIG = 2

    	ICMPv6 Packet type: packet too big

    .. data:: TIME_EXCEEDED = 3

    	ICMPv6 Packet type: Time exceeded

    .. data:: PARAMETER_PROBLEM = 4

    	ICMPv6 Packet type: Parameter problem

    .. data:: ECHO_REQUEST = 128

    	ICMPv6 Packet type: Echo request

    .. data:: ECHO_REPLY = 129

    	ICMPv6 Packet type: Echo reply

    .. data:: MULTICAST_LISTENER_QUERY = 130

    	ICMPv6 Packet type: Multicast listener query

    .. data:: MULTICAST_LISTENER_REPORT = 131

    	ICMPv6 Packet type: Multicast listener report

    .. data:: MULTICAST_LISTENER_DONE = 132

    	ICMPv6 Packet type: Multicast listener done

    .. data:: ROUTER_SOLICITATION = 133

    	ICMPv6 Packet type: Router solicitation

    .. data:: ROUTER_ADVERTISEMENT = 134

    	ICMPv6 Packet type: Router advertisement

    .. data:: NEIGHBOR_SOLICITATION = 135

    	ICMPv6 Packet type: Neighbor solicitation

    .. data:: NEIGHBOR_ADVERTISEMENT = 136

    	ICMPv6 Packet type: Neighbor advertisement

    .. data:: REDIRECT_MESSAGE = 137

    	ICMPv6 Packet type: Redirect message

    .. data:: ROUTER_RENUMBERING = 138

    	ICMPv6 Packet type: Router renumbering

    .. data:: NODE_INFORMATION_QUERY = 139

    	ICMPv6 Packet type: Node information query

    .. data:: NODE_INFORMATION_REPLY = 140

    	ICMPv6 Packet type: Node information reply

    .. data:: INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION = 141

    	ICMPv6 Packet type: Inverse neighbor discovery

    	solicitation message

    .. data:: INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT = 142

    	ICMPv6 Packet type: Inverse neighbor discovery

    	advertisement message

    .. data:: V2_MULTICAST_LISTENER_REPORT = 143

    	ICMPv6 Packet type: Version 2 multicast

    	listener report

    .. data:: HOME_AGENT_ADDRESS_DISCOVERY_REQUEST = 144

    	ICMPv6 Packet type: Home agent address

    	discovery request message

    .. data:: HOME_AGENT_ADDRESS_DISCOVERY_REPLY = 145

    	ICMPv6 Packet type: Home agent address

    	discovery reply message

    .. data:: MOBILE_PREFIX_SOLICITATION = 146

    	ICMPv6 Packet type: Mobile prefix solicitation

    .. data:: MOBILE_PREFIX_ADVERTISEMENT = 147

    	ICMPv6 Packet type: Mobile prefix advertisement

    .. data:: CERTIFICATION_PATH_SOLICITATION_MESSAGE = 148

    	ICMPv6 Packet type: Certification path

    	solicitation message

    .. data:: CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE = 149

    	ICMPv6 Packet type: Certification path

    	advertisement message

    .. data:: EXPERIMENTAL_MOBILITY_PROTOCOLS = 150

    	ICMPv6 Packet type: ICMP messages utilized by

    	experimental mobility  protocols such as

    	seamoby

    .. data:: MULTICAST_ROUTER_ADVERTISEMENT = 151

    	ICMPv6 Packet type: Multicast router

    	advertisement

    .. data:: MULTICAST_ROUTER_SOLICITATION = 152

    	ICMPv6 Packet type: Multicast router

    	solicitation

    .. data:: MULTICAST_ROUTER_TERMINATION = 153

    	ICMPv6 Packet type: Multicast router

    	termination

    .. data:: FMIPV6_MESSAGES = 154

    	ICMPv6 Packet type: FMIPv6 messages

    """

    DESTINATION_UNREACHABLE = 1

    PACKET_TOO_BIG = 2

    TIME_EXCEEDED = 3

    PARAMETER_PROBLEM = 4

    ECHO_REQUEST = 128

    ECHO_REPLY = 129

    MULTICAST_LISTENER_QUERY = 130

    MULTICAST_LISTENER_REPORT = 131

    MULTICAST_LISTENER_DONE = 132

    ROUTER_SOLICITATION = 133

    ROUTER_ADVERTISEMENT = 134

    NEIGHBOR_SOLICITATION = 135

    NEIGHBOR_ADVERTISEMENT = 136

    REDIRECT_MESSAGE = 137

    ROUTER_RENUMBERING = 138

    NODE_INFORMATION_QUERY = 139

    NODE_INFORMATION_REPLY = 140

    INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION = 141

    INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT = 142

    V2_MULTICAST_LISTENER_REPORT = 143

    HOME_AGENT_ADDRESS_DISCOVERY_REQUEST = 144

    HOME_AGENT_ADDRESS_DISCOVERY_REPLY = 145

    MOBILE_PREFIX_SOLICITATION = 146

    MOBILE_PREFIX_ADVERTISEMENT = 147

    CERTIFICATION_PATH_SOLICITATION_MESSAGE = 148

    CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE = 149

    EXPERIMENTAL_MOBILITY_PROTOCOLS = 150

    MULTICAST_ROUTER_ADVERTISEMENT = 151

    MULTICAST_ROUTER_SOLICITATION = 152

    MULTICAST_ROUTER_TERMINATION = 153

    FMIPV6_MESSAGES = 154


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpv6Enum']


class MessageTypeIcmpv6Enum(Enum):
    """
    MessageTypeIcmpv6Enum

    LPTS ICMPv6 message types

    .. data:: DESTINATION_UNREACHABLE = 1

    	ICMPv6 Packet type: Destination unreachable

    .. data:: PACKET_TOO_BIG = 2

    	ICMPv6 Packet type: packet too big

    .. data:: TIME_EXCEEDED = 3

    	ICMPv6 Packet type: Time exceeded

    .. data:: PARAMETER_PROBLEM = 4

    	ICMPv6 Packet type: Parameter problem

    .. data:: ECHO_REQUEST = 128

    	ICMPv6 Packet type: Echo request

    .. data:: ECHO_REPLY = 129

    	ICMPv6 Packet type: Echo reply

    .. data:: MULTICAST_LISTENER_QUERY = 130

    	ICMPv6 Packet type: Multicast listener query

    .. data:: MULTICAST_LISTENER_REPORT = 131

    	ICMPv6 Packet type: Multicast listener report

    .. data:: MULTICAST_LISTENER_DONE = 132

    	ICMPv6 Packet type: Multicast listener done

    .. data:: ROUTER_SOLICITATION = 133

    	ICMPv6 Packet type: Router solicitation

    .. data:: ROUTER_ADVERTISEMENT = 134

    	ICMPv6 Packet type: Router advertisement

    .. data:: NEIGHBOR_SOLICITATION = 135

    	ICMPv6 Packet type: Neighbor solicitation

    .. data:: NEIGHBOR_ADVERTISEMENT = 136

    	ICMPv6 Packet type: Neighbor advertisement

    .. data:: REDIRECT_MESSAGE = 137

    	ICMPv6 Packet type: Redirect message

    .. data:: ROUTER_RENUMBERING = 138

    	ICMPv6 Packet type: Router renumbering

    .. data:: NODE_INFORMATION_QUERY = 139

    	ICMPv6 Packet type: Node information query

    .. data:: NODE_INFORMATION_REPLY = 140

    	ICMPv6 Packet type: Node information reply

    .. data:: INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION = 141

    	ICMPv6 Packet type: Inverse neighbor discovery

    	solicitation message

    .. data:: INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT = 142

    	ICMPv6 Packet type: Inverse neighbor discovery

    	advertisement message

    .. data:: V2_MULTICAST_LISTENER_REPORT = 143

    	ICMPv6 Packet type: Version 2 multicast

    	listener report

    .. data:: HOME_AGENT_ADDRESS_DISCOVERY_REQUEST = 144

    	ICMPv6 Packet type: Home agent address

    	discovery request message

    .. data:: HOME_AGENT_ADDRESS_DISCOVERY_REPLY = 145

    	ICMPv6 Packet type: Home agent address

    	discovery reply message

    .. data:: MOBILE_PREFIX_SOLICITATION = 146

    	ICMPv6 Packet type: Mobile prefix solicitation

    .. data:: MOBILE_PREFIX_ADVERTISEMENT = 147

    	ICMPv6 Packet type: Mobile prefix advertisement

    .. data:: CERTIFICATION_PATH_SOLICITATION_MESSAGE = 148

    	ICMPv6 Packet type: Certification path

    	solicitation message

    .. data:: CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE = 149

    	ICMPv6 Packet type: Certification path

    	advertisement message

    .. data:: EXPERIMENTAL_MOBILITY_PROTOCOLS = 150

    	ICMPv6 Packet type: ICMP messages utilized by

    	experimental mobility  protocols such as

    	seamoby

    .. data:: MULTICAST_ROUTER_ADVERTISEMENT = 151

    	ICMPv6 Packet type: Multicast router

    	advertisement

    .. data:: MULTICAST_ROUTER_SOLICITATION = 152

    	ICMPv6 Packet type: Multicast router

    	solicitation

    .. data:: MULTICAST_ROUTER_TERMINATION = 153

    	ICMPv6 Packet type: Multicast router

    	termination

    .. data:: FMIPV6_MESSAGES = 154

    	ICMPv6 Packet type: FMIPv6 messages

    """

    DESTINATION_UNREACHABLE = 1

    PACKET_TOO_BIG = 2

    TIME_EXCEEDED = 3

    PARAMETER_PROBLEM = 4

    ECHO_REQUEST = 128

    ECHO_REPLY = 129

    MULTICAST_LISTENER_QUERY = 130

    MULTICAST_LISTENER_REPORT = 131

    MULTICAST_LISTENER_DONE = 132

    ROUTER_SOLICITATION = 133

    ROUTER_ADVERTISEMENT = 134

    NEIGHBOR_SOLICITATION = 135

    NEIGHBOR_ADVERTISEMENT = 136

    REDIRECT_MESSAGE = 137

    ROUTER_RENUMBERING = 138

    NODE_INFORMATION_QUERY = 139

    NODE_INFORMATION_REPLY = 140

    INVERSE_NEIGHBOR_DISCOVERY_SOLICITAION = 141

    INVERSE_NEIGHBOR_DISCOVER_ADVERTISEMENT = 142

    V2_MULTICAST_LISTENER_REPORT = 143

    HOME_AGENT_ADDRESS_DISCOVERY_REQUEST = 144

    HOME_AGENT_ADDRESS_DISCOVERY_REPLY = 145

    MOBILE_PREFIX_SOLICITATION = 146

    MOBILE_PREFIX_ADVERTISEMENT = 147

    CERTIFICATION_PATH_SOLICITATION_MESSAGE = 148

    CERTIFICATION_PATH_ADVERTISEMENT_MESSAGE = 149

    EXPERIMENTAL_MOBILITY_PROTOCOLS = 150

    MULTICAST_ROUTER_ADVERTISEMENT = 151

    MULTICAST_ROUTER_SOLICITATION = 152

    MULTICAST_ROUTER_TERMINATION = 153

    FMIPV6_MESSAGES = 154


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIcmpv6Enum']


class MessageTypeIgmpEnum(Enum):
    """
    MessageTypeIgmpEnum

    LPTS IGMP message types

    .. data:: MEMBERSHIP_QUERY = 17

    	IGMP Packet type: Membership query

    .. data:: V1_MEMBERSHIP_REPORT = 18

    	IGMP Packet type: V1 membership report

    .. data:: DVMRP = 19

    	IGMP Packet type: DVMRP

    .. data:: PI_MV1 = 20

    	IGMP Packet type: PIM version 1

    .. data:: CISCO_TRACE_MESSAGES = 21

    	IGMP Packet type: Cisco Trace Messages

    .. data:: V2_MEMBERSHIP_REPORT = 22

    	IGMP Packet type: V2 membership report

    .. data:: V2_LEAVE_GROUP = 23

    	IGMP Packet type: V2 leave group

    .. data:: MULTICAST_TRACEROUTE_RESPONSE = 30

    	IGMP Packet type: Multicast traceroute response

    .. data:: MULTICAST_TRACEROUTE = 31

    	IGMP Packet type: MulticastTraceroute

    .. data:: V3_MEMBERSHIP_REPORT = 34

    	IGMP Packet type: V3 membership report

    .. data:: MULTICAST_ROUTER_ADVERTISEMENT = 48

    	IGMP Packet type: Multicast router

    	advertisement

    .. data:: MULTICAST_ROUTER_SOLICITATION = 49

    	IGMP Packet type: Multicast router solicitation

    .. data:: MULTICAST_ROUTER_TERMINATION = 50

    	IGMP Packet type: Multicast router termination

    """

    MEMBERSHIP_QUERY = 17

    V1_MEMBERSHIP_REPORT = 18

    DVMRP = 19

    PI_MV1 = 20

    CISCO_TRACE_MESSAGES = 21

    V2_MEMBERSHIP_REPORT = 22

    V2_LEAVE_GROUP = 23

    MULTICAST_TRACEROUTE_RESPONSE = 30

    MULTICAST_TRACEROUTE = 31

    V3_MEMBERSHIP_REPORT = 34

    MULTICAST_ROUTER_ADVERTISEMENT = 48

    MULTICAST_ROUTER_SOLICITATION = 49

    MULTICAST_ROUTER_TERMINATION = 50


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIgmpEnum']


class MessageTypeIgmpEnum(Enum):
    """
    MessageTypeIgmpEnum

    LPTS IGMP message types

    .. data:: MEMBERSHIP_QUERY = 17

    	IGMP Packet type: Membership query

    .. data:: V1_MEMBERSHIP_REPORT = 18

    	IGMP Packet type: V1 membership report

    .. data:: DVMRP = 19

    	IGMP Packet type: DVMRP

    .. data:: PI_MV1 = 20

    	IGMP Packet type: PIM version 1

    .. data:: CISCO_TRACE_MESSAGES = 21

    	IGMP Packet type: Cisco Trace Messages

    .. data:: V2_MEMBERSHIP_REPORT = 22

    	IGMP Packet type: V2 membership report

    .. data:: V2_LEAVE_GROUP = 23

    	IGMP Packet type: V2 leave group

    .. data:: MULTICAST_TRACEROUTE_RESPONSE = 30

    	IGMP Packet type: Multicast traceroute response

    .. data:: MULTICAST_TRACEROUTE = 31

    	IGMP Packet type: MulticastTraceroute

    .. data:: V3_MEMBERSHIP_REPORT = 34

    	IGMP Packet type: V3 membership report

    .. data:: MULTICAST_ROUTER_ADVERTISEMENT = 48

    	IGMP Packet type: Multicast router

    	advertisement

    .. data:: MULTICAST_ROUTER_SOLICITATION = 49

    	IGMP Packet type: Multicast router solicitation

    .. data:: MULTICAST_ROUTER_TERMINATION = 50

    	IGMP Packet type: Multicast router termination

    """

    MEMBERSHIP_QUERY = 17

    V1_MEMBERSHIP_REPORT = 18

    DVMRP = 19

    PI_MV1 = 20

    CISCO_TRACE_MESSAGES = 21

    V2_MEMBERSHIP_REPORT = 22

    V2_LEAVE_GROUP = 23

    MULTICAST_TRACEROUTE_RESPONSE = 30

    MULTICAST_TRACEROUTE = 31

    V3_MEMBERSHIP_REPORT = 34

    MULTICAST_ROUTER_ADVERTISEMENT = 48

    MULTICAST_ROUTER_SOLICITATION = 49

    MULTICAST_ROUTER_TERMINATION = 50


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['MessageTypeIgmpEnum']


class PacketEnum(Enum):
    """
    PacketEnum

    Packet type

    .. data:: ICMP = 0

    	ICMP packet type

    .. data:: ICM_PV6 = 1

    	ICMPv6 packet type

    .. data:: IGMP = 2

    	IGMP packet type

    .. data:: UNKNOWN = 3

    	Packet type unknown

    """

    ICMP = 0

    ICM_PV6 = 1

    IGMP = 2

    UNKNOWN = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['PacketEnum']


class UdpAddressFamilyEnum(Enum):
    """
    UdpAddressFamilyEnum

    Address Family Type

    .. data:: IPV4 = 2

    	IPv4

    .. data:: IPV6 = 26

    	IPv6

    """

    IPV4 = 2

    IPV6 = 26


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['UdpAddressFamilyEnum']



class Udp(object):
    """
    IP UDP Operational Data
    
    .. attribute:: nodes
    
    	Node\-specific UDP operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Udp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific UDP operational data
        
        .. attribute:: node
        
        	UDP operational data for a particular node
        	**type**\: list of  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2015-11-09'

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
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2015-11-09'

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
                	**type**\:  :py:class:`Ipv4Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv4Traffic>`
                
                .. attribute:: ipv6_traffic
                
                	UDP Traffic statistics for IPv6
                	**type**\:  :py:class:`Ipv6Traffic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.Udp.Nodes.Node.Statistics.Ipv6Traffic>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

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
                    _revision = '2015-11-09'

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
                        if not self.is_config():
                            return False
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
                    _revision = '2015-11-09'

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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            if not self.is_config():
                return False
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
        if not self.is_config():
            return False
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
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes>`
    
    

    """

    _prefix = 'ip-udp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = UdpConnection.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        List of UDP connections nodes
        
        .. attribute:: node
        
        	Information about a particular node
        	**type**\: list of  :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node>`
        
        

        """

        _prefix = 'ip-udp-oper'
        _revision = '2015-11-09'

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
            	**type**\:  :py:class:`Lpts <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts>`
            
            .. attribute:: pcb_briefs
            
            	Brief information for list of UDP connections
            	**type**\:  :py:class:`PcbBriefs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs>`
            
            .. attribute:: pcb_details
            
            	Detail information for list of UDP connections 
            	**type**\:  :py:class:`PcbDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails>`
            
            .. attribute:: statistics
            
            	Statistics of UDP connections
            	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-udp-oper'
            _revision = '2015-11-09'

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
                	**type**\:  :py:class:`Clients <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients>`
                
                .. attribute:: pcb_statistics
                
                	Table listing the UDP connections for which statistics are provided
                	**type**\:  :py:class:`PcbStatistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics>`
                
                .. attribute:: summary
                
                	Summary statistics across all UDP connections
                	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Summary>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

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
                    	**type**\: list of  :py:class:`Client <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.Clients.Client>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

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
                        
                        	**range:** 0..21
                        
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
                        _revision = '2015-11-09'

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
                            if not self.is_config():
                                return False
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
                        if not self.is_config():
                            return False
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
                    _revision = '2015-11-09'

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
                        if not self.is_config():
                            return False
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
                    	**type**\: list of  :py:class:`PcbStatistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

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
                        	**type**\:  :py:class:`Receive <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive>`
                        
                        .. attribute:: send
                        
                        	UDP send statistics
                        	**type**\:  :py:class:`Send <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send>`
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.pcb_address = None
                            self.is_paw_socket = None
                            self.receive = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Receive()
                            self.receive.parent = self
                            self.send = UdpConnection.Nodes.Node.Statistics.PcbStatistics.PcbStatistic.Send()
                            self.send.parent = self


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
                            	**type**\:  long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_xipc_pulses
                            
                            	XIPC pulses received from application
                            	**type**\:  long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_net_io_packets
                            
                            	Packets sent to network (NetIO)
                            	**type**\:  long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: sent_network_packets
                            
                            	Packets sent to network (v4/v6 IO)
                            	**type**\:  long
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2015-11-09'

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
                                if not self.is_config():
                                    return False
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
                            	**type**\:  long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: queued_application_socket_packets
                            
                            	Packets queued to application on socket
                            	**type**\:  long
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: received_network_packets
                            
                            	Packets received from network
                            	**type**\:  long
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2015-11-09'

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
                                if not self.is_config():
                                    return False
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
                            if not self.is_config():
                                return False
                            if self.pcb_address is not None:
                                return True

                            if self.is_paw_socket is not None:
                                return True

                            if self.receive is not None and self.receive._has_data():
                                return True

                            if self.send is not None and self.send._has_data():
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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                	**type**\:  :py:class:`Queries <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.queries = UdpConnection.Nodes.Node.Lpts.Queries()
                    self.queries.parent = self


                class Queries(object):
                    """
                    List of query options
                    
                    .. attribute:: query
                    
                    	Query option
                    	**type**\: list of  :py:class:`Query <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query>`
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

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
                        	**type**\:  :py:class:`LptsPcbQueryEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.LptsPcbQueryEnum>`
                        
                        .. attribute:: pcbs
                        
                        	List of PCBs
                        	**type**\:  :py:class:`Pcbs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs>`
                        
                        

                        """

                        _prefix = 'ip-udp-oper'
                        _revision = '2015-11-09'

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
                            	**type**\: list of  :py:class:`Pcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb>`
                            
                            

                            """

                            _prefix = 'ip-udp-oper'
                            _revision = '2015-11-09'

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
                                	**type**\:  :py:class:`Common <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common>`
                                
                                .. attribute:: foreign_address
                                
                                	Remote IP address
                                	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.ForeignAddress>`
                                
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
                                	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.LocalAddress>`
                                
                                .. attribute:: local_port
                                
                                	Local port
                                	**type**\:  int
                                
                                	**range:** 0..65535
                                
                                

                                """

                                _prefix = 'ip-udp-oper'
                                _revision = '2015-11-09'

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
                                    	**type**\:  :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                    
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
                                    _revision = '2015-11-09'

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
                                        if not self.is_config():
                                            return False
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
                                    	**type**\:  :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                    
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
                                    _revision = '2015-11-09'

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
                                        if not self.is_config():
                                            return False
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
                                    	**type**\:  :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                    
                                    .. attribute:: lpts_pcb
                                    
                                    	LPTS PCB information
                                    	**type**\:  :py:class:`LptsPcb <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb>`
                                    
                                    

                                    """

                                    _prefix = 'ip-udp-oper'
                                    _revision = '2015-11-09'

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
                                        	**type**\:  :py:class:`AcceptMask <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.AcceptMask>`
                                        
                                        .. attribute:: filter
                                        
                                        	Interface Filters
                                        	**type**\: list of  :py:class:`Filter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter>`
                                        
                                        .. attribute:: flow_types_info
                                        
                                        	flow information
                                        	**type**\:  int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: lpts_flags
                                        
                                        	LPTS flags
                                        	**type**\:  :py:class:`LptsFlags <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.LptsFlags>`
                                        
                                        .. attribute:: options
                                        
                                        	Receive options
                                        	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Options>`
                                        
                                        .. attribute:: ttl
                                        
                                        	Minimum TTL
                                        	**type**\:  int
                                        
                                        	**range:** 0..255
                                        
                                        

                                        """

                                        _prefix = 'ip-udp-oper'
                                        _revision = '2015-11-09'

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
                                            _revision = '2015-11-09'

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
                                                if not self.is_config():
                                                    return False
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
                                            _revision = '2015-11-09'

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
                                                if not self.is_config():
                                                    return False
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
                                            _revision = '2015-11-09'

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
                                                if not self.is_config():
                                                    return False
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
                                            
                                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                            
                                            .. attribute:: local_address
                                            
                                            	Local address
                                            	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.LocalAddress>`
                                            
                                            .. attribute:: local_length
                                            
                                            	Local address length
                                            	**type**\:  int
                                            
                                            	**range:** 0..65535
                                            
                                            .. attribute:: packet_type
                                            
                                            	Protocol\-specific packet type
                                            	**type**\:  :py:class:`PacketType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.PacketType>`
                                            
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
                                            	**type**\:  :py:class:`RemoteAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.Lpts.Queries.Query.Pcbs.Pcb.Common.LptsPcb.Filter.RemoteAddress>`
                                            
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
                                            _revision = '2015-11-09'

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
                                                	**type**\:  :py:class:`MessageTypeIcmpv6Enum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmpv6Enum>`
                                                
                                                .. attribute:: icmp_message_type
                                                
                                                	ICMP message type
                                                	**type**\:  :py:class:`MessageTypeIcmpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIcmpEnum>`
                                                
                                                .. attribute:: igmp_message_type
                                                
                                                	IGMP message type
                                                	**type**\:  :py:class:`MessageTypeIgmpEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.MessageTypeIgmpEnum>`
                                                
                                                .. attribute:: message_id
                                                
                                                	Message type in number
                                                	**type**\:  int
                                                
                                                	**range:** 0..4294967295
                                                
                                                .. attribute:: type
                                                
                                                	Type
                                                	**type**\:  :py:class:`PacketEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.PacketEnum>`
                                                
                                                

                                                """

                                                _prefix = 'ip-udp-oper'
                                                _revision = '2015-11-09'

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
                                                    if not self.is_config():
                                                        return False
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
                                                	**type**\:  :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                                
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
                                                _revision = '2015-11-09'

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
                                                    if not self.is_config():
                                                        return False
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
                                                	**type**\:  :py:class:`AddrFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.AddrFamilyEnum>`
                                                
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
                                                _revision = '2015-11-09'

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
                                                    if not self.is_config():
                                                        return False
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
                                                if not self.is_config():
                                                    return False
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
                                            if not self.is_config():
                                                return False
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
                                        if not self.is_config():
                                            return False
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
                                    if not self.is_config():
                                        return False
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
                                if not self.is_config():
                                    return False
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
                            if not self.is_config():
                                return False
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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                	**type**\: list of  :py:class:`PcbDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

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
                    	**type**\:  :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.ForeignAddress>`
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbDetails.PcbDetail.LocalAddress>`
                    
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
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

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


                    class LocalAddress(object):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                        _revision = '2015-11-09'

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
                            if not self.is_config():
                                return False
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
                        	**type**\:  :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                        _revision = '2015-11-09'

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
                            if not self.is_config():
                                return False
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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                	**type**\: list of  :py:class:`PcbBrief <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief>`
                
                

                """

                _prefix = 'ip-udp-oper'
                _revision = '2015-11-09'

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
                    	**type**\:  :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\:  :py:class:`ForeignAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.ForeignAddress>`
                    
                    .. attribute:: foreign_port
                    
                    	Foreign port
                    	**type**\:  int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\:  :py:class:`LocalAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpConnection.Nodes.Node.PcbBriefs.PcbBrief.LocalAddress>`
                    
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
                    
                    

                    """

                    _prefix = 'ip-udp-oper'
                    _revision = '2015-11-09'

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


                    class LocalAddress(object):
                        """
                        Local address
                        
                        .. attribute:: af_name
                        
                        	AFName
                        	**type**\:  :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                        _revision = '2015-11-09'

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
                            if not self.is_config():
                                return False
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
                        	**type**\:  :py:class:`UdpAddressFamilyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_udp_oper.UdpAddressFamilyEnum>`
                        
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
                        _revision = '2015-11-09'

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
                            if not self.is_config():
                                return False
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
                        if not self.is_config():
                            return False
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
                    if not self.is_config():
                        return False
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
                if not self.is_config():
                    return False
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
            if not self.is_config():
                return False
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
        if not self.is_config():
            return False
        if self.nodes is not None and self.nodes._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ip_udp_oper as meta
        return meta._meta_table['UdpConnection']['meta_info']


