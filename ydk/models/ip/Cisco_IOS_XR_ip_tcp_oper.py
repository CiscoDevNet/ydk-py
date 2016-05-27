""" Cisco_IOS_XR_ip_tcp_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ip\-tcp package operational data.

This module contains definitions
for the following management objects\:
  tcp\-connection\: TCP connection operational data
  tcp\: tcp
  tcp\-nsr\: tcp nsr

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class AddrFamilyEnum(Enum):
    """
    AddrFamilyEnum

    Address Family Types

    .. data:: INTERNETWORK = 2

    	Internetwork: UDP, TCP, etc.

    .. data:: IP_VERSION6 = 26

    	IP version 6

    """

    INTERNETWORK = 2

    IP_VERSION6 = 26


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['AddrFamilyEnum']


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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['MessageTypeIgmpEnum']


class NsrDownReasonEnum(Enum):
    """
    NsrDownReasonEnum

    NSR\-Down Reasons

    .. data:: NONE = 0

    	None, i.e. NSR was never up

    .. data:: INIT_SYNC_ABORTED = 1

    	Initial sync was aborted

    .. data:: CLIENT_DISABLED = 2

    	Disabled by Active APP

    .. data:: CLIENT_DISCONNECT = 3

    	Standby APP disconnected

    .. data:: TCP_DISCONNECT = 4

    	Standby TCP disconnected

    .. data:: FAILOVER = 5

    	RP/DRP Failover occurred

    .. data:: NSR_CLEAR = 6

    	Clear nsr command

    .. data:: INTERNAL_ERROR = 7

    	Internal error occurred

    .. data:: RETRANSMIT_THRESHOLD_EXCEED = 8

    	Retransmission threshold exceededprobably

    	becauseS-TCP was not healthy

    .. data:: INIT_SYNC_FAILURE_THRESH_EXCEEDED = 9

    	Init-sync repeat failures have exceeded

    	threshold

    .. data:: AUDIT_TIMEOUT = 10

    	Audit operation timed out

    .. data:: AUDIT_FAILED = 11

    	Audit operation failed

    .. data:: STANDBY_SSCB_DELETED = 12

    	Standby SSCB deleted

    .. data:: STANDBY_SESSION_CLOSE = 13

    	Session was closed on standby

    .. data:: STANDBY_RXPATH_FROZEN = 14

    	RX-Path was frozen on standby

    .. data:: PARTNER_DELETED = 15

    	Partner was deleted from set

    """

    NONE = 0

    INIT_SYNC_ABORTED = 1

    CLIENT_DISABLED = 2

    CLIENT_DISCONNECT = 3

    TCP_DISCONNECT = 4

    FAILOVER = 5

    NSR_CLEAR = 6

    INTERNAL_ERROR = 7

    RETRANSMIT_THRESHOLD_EXCEED = 8

    INIT_SYNC_FAILURE_THRESH_EXCEEDED = 9

    AUDIT_TIMEOUT = 10

    AUDIT_FAILED = 11

    STANDBY_SSCB_DELETED = 12

    STANDBY_SESSION_CLOSE = 13

    STANDBY_RXPATH_FROZEN = 14

    PARTNER_DELETED = 15


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['NsrDownReasonEnum']


class NsrStatusEnum(Enum):
    """
    NsrStatusEnum

    NSR Stream Status

    .. data:: DOWN = 0

    	NSR Stream Down

    .. data:: UP = 1

    	NSR Stream Up

    .. data:: NA = 2

    	NSR Stream Not applicable

    """

    DOWN = 0

    UP = 1

    NA = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['NsrStatusEnum']


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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['PacketEnum']


class PakPrioEnum(Enum):
    """
    PakPrioEnum

    Packet Priority Types

    .. data:: UNSPECIFIED_PACKET = 0

    	Unspecified

    .. data:: NORMAL_PACKET = 1

    	Normal: all traffic routed via this router,

    	Telnet/FTP traffic generated from within this

    	router

    .. data:: MEDIUM_PACKET = 2

    	Medium: Packets with low drop probability e.g.

    	Routing updates & requests

    .. data:: HIGH_PACKET = 3

    	High: Packets with very low drop probability

    	and normal delivery e.g. L3 Keepalives like

    	OSPF/ISIS Hellos

    .. data:: CRUCIAL_PACKET = 4

    	Crucial: Packets with very low drop probability

    	and expedited delivery e.g L2 keepalives, HDLC

    	Keepalives

    """

    UNSPECIFIED_PACKET = 0

    NORMAL_PACKET = 1

    MEDIUM_PACKET = 2

    HIGH_PACKET = 3

    CRUCIAL_PACKET = 4


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['PakPrioEnum']


class ShowEnum(Enum):
    """
    ShowEnum

    Show

    .. data:: ALL = 0

    	To dispay all

    .. data:: STATIC_POLICY = 1

    	To display static policy

    .. data:: INTERFACE_FILTER = 2

    	To display interface filter

    .. data:: PACKET_FILTER = 3

    	To display packet type filter

    """

    ALL = 0

    STATIC_POLICY = 1

    INTERFACE_FILTER = 2

    PACKET_FILTER = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['ShowEnum']


class TcpConnStateEnum(Enum):
    """
    TcpConnStateEnum

    TCP Connection State

    .. data:: CLOSED = 0

    	Closed

    .. data:: LISTEN = 1

    	Listen

    .. data:: SYN_SENT = 2

    	Syn sent

    .. data:: SYN_RECEIVED = 3

    	Syn received

    .. data:: ESTABLISHED = 4

    	Established

    .. data:: CLOSE_WAIT = 5

    	Close wait

    .. data:: FIN_WAIT1 = 6

    	FIN Wait1

    .. data:: CLOSING = 7

    	Closing

    .. data:: LAST_ACK = 8

    	Last ack

    .. data:: FIN_WAIT2 = 9

    	FIN Wait2

    .. data:: TIME_WAIT = 10

    	Time wait

    """

    CLOSED = 0

    LISTEN = 1

    SYN_SENT = 2

    SYN_RECEIVED = 3

    ESTABLISHED = 4

    CLOSE_WAIT = 5

    FIN_WAIT1 = 6

    CLOSING = 7

    LAST_ACK = 8

    FIN_WAIT2 = 9

    TIME_WAIT = 10


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['TcpConnStateEnum']


class TcpTimerEnum(Enum):
    """
    TcpTimerEnum

    TCP Timer Type

    .. data:: RETRANSMISSION_TIMER = 0

    	Retransmission timer

    .. data:: WINDOW_PROBE_TIMER = 1

    	Send Window Probe timer

    .. data:: TIMEWAIT_STATE_TIMER = 2

    	TIMEWAIT state timer

    .. data:: ACK_HOLD_TIMER = 3

    	ACK Hold timer

    .. data:: KEEP_ALIVE_TIMER = 4

    	Keep Alive timer

    .. data:: PMTU_AGER_TIMER = 5

    	PMTU Ager Timer

    .. data:: RETRANSMISSION_GIVEUP_TIMER = 6

    	Retransmission Giveup timer

    .. data:: THROTTLE_TIMER = 7

    	Throttle (for PAW/xipc) timer

    """

    RETRANSMISSION_TIMER = 0

    WINDOW_PROBE_TIMER = 1

    TIMEWAIT_STATE_TIMER = 2

    ACK_HOLD_TIMER = 3

    KEEP_ALIVE_TIMER = 4

    PMTU_AGER_TIMER = 5

    RETRANSMISSION_GIVEUP_TIMER = 6

    THROTTLE_TIMER = 7


    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['TcpTimerEnum']



class TcpConnection(object):
    """
    TCP connection operational data
    
    .. attribute:: nodes
    
    	Table of information about all nodes present on the system
    	**type**\: :py:class:`Nodes <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes>`
    
    

    """

    _prefix = 'ip-tcp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = TcpConnection.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of information about all nodes present on
        the system
        
        .. attribute:: node
        
        	Information about a single node
        	**type**\: list of :py:class:`Node <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node>`
        
        

        """

        _prefix = 'ip-tcp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Information about a single node
            
            .. attribute:: id  <key>
            
            	Describing a location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistics of all TCP connections
            	**type**\: :py:class:`Statistics <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics>`
            
            .. attribute:: extended_information
            
            	Extended Filter related Information
            	**type**\: :py:class:`ExtendedInformation <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation>`
            
            .. attribute:: detail_informations
            
            	Table listing TCP connections for which detailed information is provided
            	**type**\: :py:class:`DetailInformations <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations>`
            
            .. attribute:: brief_informations
            
            	Table listing connections for which brief information is provided.Note that not all connections are listed in the brief table
            	**type**\: :py:class:`BriefInformations <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.BriefInformations>`
            
            

            """

            _prefix = 'ip-tcp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.id = None
                self.statistics = TcpConnection.Nodes.Node.Statistics()
                self.statistics.parent = self
                self.extended_information = TcpConnection.Nodes.Node.ExtendedInformation()
                self.extended_information.parent = self
                self.detail_informations = TcpConnection.Nodes.Node.DetailInformations()
                self.detail_informations.parent = self
                self.brief_informations = TcpConnection.Nodes.Node.BriefInformations()
                self.brief_informations.parent = self


            class Statistics(object):
                """
                Statistics of all TCP connections
                
                .. attribute:: clients
                
                	Table listing clients
                	**type**\: :py:class:`Clients <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Clients>`
                
                .. attribute:: pcbs
                
                	Table listing the TCP connections for which statistics are provided
                	**type**\: :py:class:`Pcbs <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs>`
                
                .. attribute:: summary
                
                	Summary statistics across all TCP connections
                	**type**\: :py:class:`Summary <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Summary>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.clients = TcpConnection.Nodes.Node.Statistics.Clients()
                    self.clients.parent = self
                    self.pcbs = TcpConnection.Nodes.Node.Statistics.Pcbs()
                    self.pcbs.parent = self
                    self.summary = TcpConnection.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self


                class Clients(object):
                    """
                    Table listing clients
                    
                    .. attribute:: client
                    
                    	Describing Client ID
                    	**type**\: list of :py:class:`Client <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Clients.Client>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
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
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: client_jid
                        
                        	Job ID of the transport client
                        	**type**\: int
                        
                        	**range:** \-2147483648..2147483647
                        
                        .. attribute:: client_name
                        
                        	Transport client name
                        	**type**\: str
                        
                        	**range:** 0..21
                        
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
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.client_id is None:
                                raise YPYDataValidationError('Key property client_id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:client[Cisco-IOS-XR-ip-tcp-oper:client-id = ' + str(self.client_id) + ']'

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
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Clients.Client']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:clients'

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
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Clients']['meta_info']


                class Pcbs(object):
                    """
                    Table listing the TCP connections for which
                    statistics are provided
                    
                    .. attribute:: pcb
                    
                    	Protocol Control Block ID
                    	**type**\: list of :py:class:`Pcb <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pcb = YList()
                        self.pcb.parent = self
                        self.pcb.name = 'pcb'


                    class Pcb(object):
                        """
                        Protocol Control Block ID
                        
                        .. attribute:: id  <key>
                        
                        	Displaying statistics associated with a particular PCB
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: read_io_counts
                        
                        	Read  I/O counts
                        	**type**\: :py:class:`ReadIoCounts <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts>`
                        
                        .. attribute:: write_io_counts
                        
                        	Write I/O counts
                        	**type**\: :py:class:`WriteIoCounts <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts>`
                        
                        .. attribute:: async_session_stats
                        
                        	Statistics of Async TCP Sessions
                        	**type**\: :py:class:`AsyncSessionStats <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.read_io_counts = TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts()
                            self.read_io_counts.parent = self
                            self.write_io_counts = TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts()
                            self.write_io_counts.parent = self
                            self.async_session_stats = TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats()
                            self.async_session_stats.parent = self
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


                        class ReadIoCounts(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.io_count = None
                                self.arm_count = None
                                self.unarm_count = None
                                self.autoarm_count = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:read-io-counts'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.io_count is not None:
                                    return True

                                if self.arm_count is not None:
                                    return True

                                if self.unarm_count is not None:
                                    return True

                                if self.autoarm_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.ReadIoCounts']['meta_info']


                        class WriteIoCounts(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.io_count = None
                                self.arm_count = None
                                self.unarm_count = None
                                self.autoarm_count = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:write-io-counts'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.io_count is not None:
                                    return True

                                if self.arm_count is not None:
                                    return True

                                if self.unarm_count is not None:
                                    return True

                                if self.autoarm_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.WriteIoCounts']['meta_info']


                        class AsyncSessionStats(object):
                            """
                            Statistics of Async TCP Sessions
                            
                            .. attribute:: async_session
                            
                            	Flag of async session
                            	**type**\: bool
                            
                            .. attribute:: data_write_success_num
                            
                            	Number of successful data write to XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_read_success_num
                            
                            	Number of successful data read from XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_write_error_num
                            
                            	Number of failed data write to XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_read_error_num
                            
                            	Number of failed data read from XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_write_success_num
                            
                            	Number of successful control write to XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_read_success_num
                            
                            	Number of successful control read to XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_write_error_num
                            
                            	Number of failed control write to XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: control_read_error_num
                            
                            	Number of failed control read from XIPC
                            	**type**\: list of int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: data_write_byte
                            
                            	Number of bytes data has been written
                            	**type**\: list of int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: data_read_byte
                            
                            	Number of bytes data has been read
                            	**type**\: list of int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'ip-tcp-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.async_session = None
                                self.data_write_success_num = YLeafList()
                                self.data_write_success_num.parent = self
                                self.data_write_success_num.name = 'data_write_success_num'
                                self.data_read_success_num = YLeafList()
                                self.data_read_success_num.parent = self
                                self.data_read_success_num.name = 'data_read_success_num'
                                self.data_write_error_num = YLeafList()
                                self.data_write_error_num.parent = self
                                self.data_write_error_num.name = 'data_write_error_num'
                                self.data_read_error_num = YLeafList()
                                self.data_read_error_num.parent = self
                                self.data_read_error_num.name = 'data_read_error_num'
                                self.control_write_success_num = YLeafList()
                                self.control_write_success_num.parent = self
                                self.control_write_success_num.name = 'control_write_success_num'
                                self.control_read_success_num = YLeafList()
                                self.control_read_success_num.parent = self
                                self.control_read_success_num.name = 'control_read_success_num'
                                self.control_write_error_num = YLeafList()
                                self.control_write_error_num.parent = self
                                self.control_write_error_num.name = 'control_write_error_num'
                                self.control_read_error_num = YLeafList()
                                self.control_read_error_num.parent = self
                                self.control_read_error_num.name = 'control_read_error_num'
                                self.data_write_byte = YLeafList()
                                self.data_write_byte.parent = self
                                self.data_write_byte.name = 'data_write_byte'
                                self.data_read_byte = YLeafList()
                                self.data_read_byte.parent = self
                                self.data_read_byte.name = 'data_read_byte'

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:async-session-stats'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.async_session is not None:
                                    return True

                                if self.data_write_success_num is not None:
                                    for child in self.data_write_success_num:
                                        if child is not None:
                                            return True

                                if self.data_read_success_num is not None:
                                    for child in self.data_read_success_num:
                                        if child is not None:
                                            return True

                                if self.data_write_error_num is not None:
                                    for child in self.data_write_error_num:
                                        if child is not None:
                                            return True

                                if self.data_read_error_num is not None:
                                    for child in self.data_read_error_num:
                                        if child is not None:
                                            return True

                                if self.control_write_success_num is not None:
                                    for child in self.control_write_success_num:
                                        if child is not None:
                                            return True

                                if self.control_read_success_num is not None:
                                    for child in self.control_read_success_num:
                                        if child is not None:
                                            return True

                                if self.control_write_error_num is not None:
                                    for child in self.control_write_error_num:
                                        if child is not None:
                                            return True

                                if self.control_read_error_num is not None:
                                    for child in self.control_read_error_num:
                                        if child is not None:
                                            return True

                                if self.data_write_byte is not None:
                                    for child in self.data_write_byte:
                                        if child is not None:
                                            return True

                                if self.data_read_byte is not None:
                                    for child in self.data_read_byte:
                                        if child is not None:
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb.AsyncSessionStats']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:pcb[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.read_io_counts is not None and self.read_io_counts._has_data():
                                return True

                            if self.write_io_counts is not None and self.write_io_counts._has_data():
                                return True

                            if self.async_session_stats is not None and self.async_session_stats._has_data():
                                return True

                            if self.pcb is not None:
                                return True

                            if self.vrf_id is not None:
                                return True

                            if self.packets_sent is not None:
                                return True

                            if self.xipc_pulse_received is not None:
                                return True

                            if self.segment_instruction_received is not None:
                                return True

                            if self.send_packets_queued is not None:
                                return True

                            if self.send_packets_queued_net_io is not None:
                                return True

                            if self.send_queue_failed is not None:
                                return True

                            if self.send_queue_net_io_failed is not None:
                                return True

                            if self.packets_received is not None:
                                return True

                            if self.receive_queue_failed is not None:
                                return True

                            if self.received_packets_queued is not None:
                                return True

                            if self.send_window_shrink_ignored is not None:
                                return True

                            if self.is_paw_socket is not None:
                                return True

                            if self.read_io_time is not None:
                                return True

                            if self.write_io_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs.Pcb']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:pcbs'

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
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Pcbs']['meta_info']


                class Summary(object):
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
                    
                    .. attribute:: packets_retransmitted
                    
                    	Data packets retransmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: bytes_retransmitted
                    
                    	Data bytes retransmitted
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
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
                    
                    	Received packets dropped     due to ACL DENY on SYN pkts
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
                    
                    .. attribute:: duplicate_packets_received
                    
                    	Duplicate packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: duplicate_bytes_received
                    
                    	Duplicate bytes received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: partial_duplicate_ack_received
                    
                    	Packets with partial dup data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: partial_duplicate_bytes_received
                    
                    	Bytes with partial dup data
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_of_order_packets_received
                    
                    	Out\-of\-order packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: out_of_order_bytes_received
                    
                    	Out\-of\-order bytes received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: after_window_packets_received
                    
                    	After\-window packets received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: after_window_bytes_received
                    
                    	After\-window bytes received
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
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
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
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

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.syn_cache_count is not None:
                            return True

                        if self.num_open_sockets is not None:
                            return True

                        if self.total_pakets_sent is not None:
                            return True

                        if self.send_packets_dropped is not None:
                            return True

                        if self.send_auth_packets_dropped is not None:
                            return True

                        if self.data_pakets_sent is not None:
                            return True

                        if self.data_bytes_sent is not None:
                            return True

                        if self.packets_retransmitted is not None:
                            return True

                        if self.bytes_retransmitted is not None:
                            return True

                        if self.ack_only_packets_sent is not None:
                            return True

                        if self.delay_ack_packets_sent is not None:
                            return True

                        if self.urgent_only_packets_sent is not None:
                            return True

                        if self.window_probe_packets_sent is not None:
                            return True

                        if self.window_update_packets_sent is not None:
                            return True

                        if self.control_packets_sent is not None:
                            return True

                        if self.rst_packets_sent is not None:
                            return True

                        if self.total_packets_received is not None:
                            return True

                        if self.received_packets_dropped is not None:
                            return True

                        if self.synacl_match_pkts_dropped is not None:
                            return True

                        if self.received_packets_dropped_stale_c_hdr is not None:
                            return True

                        if self.received_auth_packets_dropped is not None:
                            return True

                        if self.ack_packets_received is not None:
                            return True

                        if self.ackbytes_received is not None:
                            return True

                        if self.duplicated_ack_packets_received is not None:
                            return True

                        if self.ack_packets_for_unsent_received is not None:
                            return True

                        if self.data_packets_received_in_sequence is not None:
                            return True

                        if self.data_bytes_received_in_sequence is not None:
                            return True

                        if self.duplicate_packets_received is not None:
                            return True

                        if self.duplicate_bytes_received is not None:
                            return True

                        if self.partial_duplicate_ack_received is not None:
                            return True

                        if self.partial_duplicate_bytes_received is not None:
                            return True

                        if self.out_of_order_packets_received is not None:
                            return True

                        if self.out_of_order_bytes_received is not None:
                            return True

                        if self.after_window_packets_received is not None:
                            return True

                        if self.after_window_bytes_received is not None:
                            return True

                        if self.window_probe_packets_received is not None:
                            return True

                        if self.window_update_packets_received is not None:
                            return True

                        if self.packets_received_after_close_packet is not None:
                            return True

                        if self.bad_checksum_packets_received is not None:
                            return True

                        if self.too_short_packets_received is not None:
                            return True

                        if self.malformed_packets_received is not None:
                            return True

                        if self.no_port_packets_received is not None:
                            return True

                        if self.connections_requested is not None:
                            return True

                        if self.connections_accepted is not None:
                            return True

                        if self.connections_established is not None:
                            return True

                        if self.connections_forcibly_closed is not None:
                            return True

                        if self.connections_closed is not None:
                            return True

                        if self.connections_dropped is not None:
                            return True

                        if self.embryonic_connection_dropped is not None:
                            return True

                        if self.connections_failed is not None:
                            return True

                        if self.established_connections_reset is not None:
                            return True

                        if self.retransmit_timeouts is not None:
                            return True

                        if self.retransmit_dropped is not None:
                            return True

                        if self.keep_alive_timeouts is not None:
                            return True

                        if self.keep_alive_dropped is not None:
                            return True

                        if self.keep_alive_probes is not None:
                            return True

                        if self.paws_dropped is not None:
                            return True

                        if self.persist_dropped is not None:
                            return True

                        if self.try_lock_dropped is not None:
                            return True

                        if self.connection_rate_limited is not None:
                            return True

                        if self.syn_cache_added is not None:
                            return True

                        if self.syn_cache_completed is not None:
                            return True

                        if self.syn_cache_timed_out is not None:
                            return True

                        if self.syn_cache_overflow is not None:
                            return True

                        if self.syn_cache_reset is not None:
                            return True

                        if self.syn_cache_unreach is not None:
                            return True

                        if self.syn_cache_bucket_oflow is not None:
                            return True

                        if self.syn_cache_aborted is not None:
                            return True

                        if self.syn_cache_duplicate_sy_ns is not None:
                            return True

                        if self.syn_cache_dropped is not None:
                            return True

                        if self.pulse_errors is not None:
                            return True

                        if self.socket_layer_packets is not None:
                            return True

                        if self.reassembly_packets is not None:
                            return True

                        if self.recovered_packets is not None:
                            return True

                        if self.packet_failures is not None:
                            return True

                        if self.mss_up is not None:
                            return True

                        if self.mss_down is not None:
                            return True

                        if self.truncated_write_iov is not None:
                            return True

                        if self.no_throttle is not None:
                            return True

                        if self.low_water_mark_throttle is not None:
                            return True

                        if self.high_water_mark_throttle is not None:
                            return True

                        if self.stalled_timer_tickle_count is not None:
                            return True

                        if self.stalled_timer_tickle_time is not None:
                            return True

                        if self.iq_sock_writes is not None:
                            return True

                        if self.iq_sock_retries is not None:
                            return True

                        if self.iq_sock_aborts is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpConnection.Nodes.Node.Statistics.Summary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.clients is not None and self.clients._has_data():
                        return True

                    if self.pcbs is not None and self.pcbs._has_data():
                        return True

                    if self.summary is not None and self.summary._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpConnection.Nodes.Node.Statistics']['meta_info']


            class ExtendedInformation(object):
                """
                Extended Filter related Information
                
                .. attribute:: display_types
                
                	Table listing display types
                	**type**\: :py:class:`DisplayTypes <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.display_types = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes()
                    self.display_types.parent = self


                class DisplayTypes(object):
                    """
                    Table listing display types
                    
                    .. attribute:: display_type
                    
                    	Describing particular display type
                    	**type**\: list of :py:class:`DisplayType <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.display_type = YList()
                        self.display_type.parent = self
                        self.display_type.name = 'display_type'


                    class DisplayType(object):
                        """
                        Describing particular display type
                        
                        .. attribute:: disp_type  <key>
                        
                        	Specifying display type
                        	**type**\: :py:class:`ShowEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.ShowEnum>`
                        
                        .. attribute:: connection_id
                        
                        	Describing connection ID
                        	**type**\: list of :py:class:`ConnectionId <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.disp_type = None
                            self.connection_id = YList()
                            self.connection_id.parent = self
                            self.connection_id.name = 'connection_id'


                        class ConnectionId(object):
                            """
                            Describing connection ID
                            
                            .. attribute:: pcb_id  <key>
                            
                            	Displaying inforamtion based on selected display type associatedwith a particular PCB
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: local_address
                            
                            	Local IP address
                            	**type**\: :py:class:`LocalAddress <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress>`
                            
                            .. attribute:: foreign_address
                            
                            	Remote IP address
                            	**type**\: :py:class:`ForeignAddress <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress>`
                            
                            .. attribute:: common
                            
                            	Common PCB information
                            	**type**\: :py:class:`Common <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common>`
                            
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.pcb_id = None
                                self.local_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress()
                                self.local_address.parent = self
                                self.foreign_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress()
                                self.foreign_address.parent = self
                                self.common = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common()
                                self.common.parent = self
                                self.l4_protocol = None
                                self.local_port = None
                                self.foreign_port = None


                            class LocalAddress(object):
                                """
                                Local IP address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                                
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.af_name = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:local-address'

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
                                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                    return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.LocalAddress']['meta_info']


                            class ForeignAddress(object):
                                """
                                Remote IP address
                                
                                .. attribute:: af_name
                                
                                	AFName
                                	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                                
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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.af_name = None
                                    self.ipv4_address = None
                                    self.ipv6_address = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:foreign-address'

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
                                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                    return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.ForeignAddress']['meta_info']


                            class Common(object):
                                """
                                Common PCB information
                                
                                .. attribute:: lpts_pcb
                                
                                	LPTS PCB information
                                	**type**\: :py:class:`LptsPcb <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb>`
                                
                                .. attribute:: af_name
                                
                                	Address Family
                                	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                                
                                

                                """

                                _prefix = 'ip-tcp-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    self.parent = None
                                    self.lpts_pcb = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb()
                                    self.lpts_pcb.parent = self
                                    self.af_name = None


                                class LptsPcb(object):
                                    """
                                    LPTS PCB information
                                    
                                    .. attribute:: options
                                    
                                    	Receive options
                                    	**type**\: :py:class:`Options <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options>`
                                    
                                    .. attribute:: lpts_flags
                                    
                                    	LPTS flags
                                    	**type**\: :py:class:`LptsFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags>`
                                    
                                    .. attribute:: accept_mask
                                    
                                    	AcceptMask
                                    	**type**\: :py:class:`AcceptMask <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask>`
                                    
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
                                    	**type**\: list of :py:class:`Filter <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter>`
                                    
                                    

                                    """

                                    _prefix = 'ip-tcp-oper'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        self.parent = None
                                        self.options = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options()
                                        self.options.parent = self
                                        self.lpts_flags = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags()
                                        self.lpts_flags.parent = self
                                        self.accept_mask = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask()
                                        self.accept_mask.parent = self
                                        self.ttl = None
                                        self.flow_types_info = None
                                        self.filter = YList()
                                        self.filter.parent = self
                                        self.filter.name = 'filter'


                                    class Options(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.is_receive_filter = None
                                            self.is_ip_sla = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:options'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_receive_filter is not None:
                                                return True

                                            if self.is_ip_sla is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                            return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Options']['meta_info']


                                    class LptsFlags(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.is_pcb_bound = None
                                            self.is_local_address_ignore = None
                                            self.is_ignore_vrf_filter = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:lpts-flags'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_pcb_bound is not None:
                                                return True

                                            if self.is_local_address_ignore is not None:
                                                return True

                                            if self.is_ignore_vrf_filter is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                            return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.LptsFlags']['meta_info']


                                    class AcceptMask(object):
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.is_interface = None
                                            self.is_packet_type = None
                                            self.is_remote_address = None
                                            self.is_remote_port = None
                                            self.is_local_address = None
                                            self.is_local_port = None

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:accept-mask'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.is_interface is not None:
                                                return True

                                            if self.is_packet_type is not None:
                                                return True

                                            if self.is_remote_address is not None:
                                                return True

                                            if self.is_remote_port is not None:
                                                return True

                                            if self.is_local_address is not None:
                                                return True

                                            if self.is_local_port is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                            return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.AcceptMask']['meta_info']


                                    class Filter(object):
                                        """
                                        Interface Filters
                                        
                                        .. attribute:: packet_type
                                        
                                        	Protocol\-specific packet type
                                        	**type**\: :py:class:`PacketType <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType>`
                                        
                                        .. attribute:: remote_address
                                        
                                        	Remote address
                                        	**type**\: :py:class:`RemoteAddress <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress>`
                                        
                                        .. attribute:: local_address
                                        
                                        	Local address
                                        	**type**\: :py:class:`LocalAddress <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress>`
                                        
                                        .. attribute:: interface_name
                                        
                                        	Interface name
                                        	**type**\: str
                                        
                                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                        
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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            self.parent = None
                                            self.packet_type = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType()
                                            self.packet_type.parent = self
                                            self.remote_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress()
                                            self.remote_address.parent = self
                                            self.local_address = TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress()
                                            self.local_address.parent = self
                                            self.interface_name = None
                                            self.remote_length = None
                                            self.local_length = None
                                            self.receive_remote_port = None
                                            self.receive_local_port = None
                                            self.priority = None
                                            self.ttl = None
                                            self.flow_types_info = None


                                        class PacketType(object):
                                            """
                                            Protocol\-specific packet type
                                            
                                            .. attribute:: type
                                            
                                            	Type
                                            	**type**\: :py:class:`PacketEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.PacketEnum>`
                                            
                                            .. attribute:: icmp_message_type
                                            
                                            	ICMP message type
                                            	**type**\: :py:class:`MessageTypeIcmpEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.MessageTypeIcmpEnum>`
                                            
                                            .. attribute:: icm_pv6_message_type
                                            
                                            	ICMPv6 message type
                                            	**type**\: :py:class:`MessageTypeIcmpv6Enum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.MessageTypeIcmpv6Enum>`
                                            
                                            .. attribute:: igmp_message_type
                                            
                                            	IGMP message type
                                            	**type**\: :py:class:`MessageTypeIgmpEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.MessageTypeIgmpEnum>`
                                            
                                            .. attribute:: message_id
                                            
                                            	Message type in number
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'ip-tcp-oper'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.type = None
                                                self.icmp_message_type = None
                                                self.icm_pv6_message_type = None
                                                self.igmp_message_type = None
                                                self.message_id = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:packet-type'

                                            def is_config(self):
                                                ''' Returns True if this instance represents config data else returns False '''
                                                return False

                                            def _has_data(self):
                                                if not self.is_config():
                                                    return False
                                                if self.type is not None:
                                                    return True

                                                if self.icmp_message_type is not None:
                                                    return True

                                                if self.icm_pv6_message_type is not None:
                                                    return True

                                                if self.igmp_message_type is not None:
                                                    return True

                                                if self.message_id is not None:
                                                    return True

                                                return False

                                            @staticmethod
                                            def _meta_info():
                                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                                return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.PacketType']['meta_info']


                                        class RemoteAddress(object):
                                            """
                                            Remote address
                                            
                                            .. attribute:: af_name
                                            
                                            	AFName
                                            	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                                            
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.af_name = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:remote-address'

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
                                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                                return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.RemoteAddress']['meta_info']


                                        class LocalAddress(object):
                                            """
                                            Local address
                                            
                                            .. attribute:: af_name
                                            
                                            	AFName
                                            	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                                            
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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                self.parent = None
                                                self.af_name = None
                                                self.ipv4_address = None
                                                self.ipv6_address = None

                                            @property
                                            def _common_path(self):
                                                if self.parent is None:
                                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:local-address'

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
                                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                                return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter.LocalAddress']['meta_info']

                                        @property
                                        def _common_path(self):
                                            if self.parent is None:
                                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:filter'

                                        def is_config(self):
                                            ''' Returns True if this instance represents config data else returns False '''
                                            return False

                                        def _has_data(self):
                                            if not self.is_config():
                                                return False
                                            if self.packet_type is not None and self.packet_type._has_data():
                                                return True

                                            if self.remote_address is not None and self.remote_address._has_data():
                                                return True

                                            if self.local_address is not None and self.local_address._has_data():
                                                return True

                                            if self.interface_name is not None:
                                                return True

                                            if self.remote_length is not None:
                                                return True

                                            if self.local_length is not None:
                                                return True

                                            if self.receive_remote_port is not None:
                                                return True

                                            if self.receive_local_port is not None:
                                                return True

                                            if self.priority is not None:
                                                return True

                                            if self.ttl is not None:
                                                return True

                                            if self.flow_types_info is not None:
                                                return True

                                            return False

                                        @staticmethod
                                        def _meta_info():
                                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                            return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb.Filter']['meta_info']

                                    @property
                                    def _common_path(self):
                                        if self.parent is None:
                                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:lpts-pcb'

                                    def is_config(self):
                                        ''' Returns True if this instance represents config data else returns False '''
                                        return False

                                    def _has_data(self):
                                        if not self.is_config():
                                            return False
                                        if self.options is not None and self.options._has_data():
                                            return True

                                        if self.lpts_flags is not None and self.lpts_flags._has_data():
                                            return True

                                        if self.accept_mask is not None and self.accept_mask._has_data():
                                            return True

                                        if self.ttl is not None:
                                            return True

                                        if self.flow_types_info is not None:
                                            return True

                                        if self.filter is not None:
                                            for child_ref in self.filter:
                                                if child_ref._has_data():
                                                    return True

                                        return False

                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                        return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common.LptsPcb']['meta_info']

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:common'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return False

                                def _has_data(self):
                                    if not self.is_config():
                                        return False
                                    if self.lpts_pcb is not None and self.lpts_pcb._has_data():
                                        return True

                                    if self.af_name is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                    return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId.Common']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')
                                if self.pcb_id is None:
                                    raise YPYDataValidationError('Key property pcb_id is None')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:connection-id[Cisco-IOS-XR-ip-tcp-oper:pcb-id = ' + str(self.pcb_id) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.pcb_id is not None:
                                    return True

                                if self.local_address is not None and self.local_address._has_data():
                                    return True

                                if self.foreign_address is not None and self.foreign_address._has_data():
                                    return True

                                if self.common is not None and self.common._has_data():
                                    return True

                                if self.l4_protocol is not None:
                                    return True

                                if self.local_port is not None:
                                    return True

                                if self.foreign_port is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType.ConnectionId']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.disp_type is None:
                                raise YPYDataValidationError('Key property disp_type is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:display-type[Cisco-IOS-XR-ip-tcp-oper:disp-type = ' + str(self.disp_type) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.disp_type is not None:
                                return True

                            if self.connection_id is not None:
                                for child_ref in self.connection_id:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes.DisplayType']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:display-types'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.display_type is not None:
                            for child_ref in self.display_type:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation.DisplayTypes']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:extended-information'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.display_types is not None and self.display_types._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpConnection.Nodes.Node.ExtendedInformation']['meta_info']


            class DetailInformations(object):
                """
                Table listing TCP connections for which
                detailed information is provided
                
                .. attribute:: detail_information
                
                	Protocol Control Block ID
                	**type**\: list of :py:class:`DetailInformation <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.detail_information = YList()
                    self.detail_information.parent = self
                    self.detail_information.name = 'detail_information'


                class DetailInformation(object):
                    """
                    Protocol Control Block ID
                    
                    .. attribute:: pcb_id  <key>
                    
                    	Detail information about TCP connection, put null for all
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: socket_option_flags
                    
                    	Socket option flags
                    	**type**\: :py:class:`SocketOptionFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags>`
                    
                    .. attribute:: socket_state_flags
                    
                    	Socket state flags
                    	**type**\: :py:class:`SocketStateFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags>`
                    
                    .. attribute:: feature_flags
                    
                    	Connection feature flags
                    	**type**\: :py:class:`FeatureFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags>`
                    
                    .. attribute:: state_flags
                    
                    	Connection state flags
                    	**type**\: :py:class:`StateFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags>`
                    
                    .. attribute:: request_flags
                    
                    	Connection request flags
                    	**type**\: :py:class:`RequestFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags>`
                    
                    .. attribute:: receive_buf_state_flags
                    
                    	Receive buffer state flags
                    	**type**\: :py:class:`ReceiveBufStateFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags>`
                    
                    .. attribute:: send_buf_state_flags
                    
                    	Send buffer state flags
                    	**type**\: :py:class:`SendBufStateFlags <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags>`
                    
                    .. attribute:: address_family
                    
                    	Address Family
                    	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                    
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
                    	**type**\: :py:class:`TcpConnStateEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnStateEnum>`
                    
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
                    	**type**\: :py:class:`PakPrioEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.PakPrioEnum>`
                    
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
                    
                    .. attribute:: max_receive_queue_size
                    
                    	Max receive queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: current_send_queue_size
                    
                    	Current send queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: max_send_queue_size
                    
                    	Max send queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
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
                    
                    .. attribute:: send_congestion_window_size
                    
                    	Send congestion window size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
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
                    
                    .. attribute:: receive_window_size
                    
                    	Receive window size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: mss
                    
                    	Max segment size calculated in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: peer_mss
                    
                    	Max segment size offered by the peer in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
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
                    
                    	**range:** 0..64
                    
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
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: fib_pd_ctx
                    
                    	Cached fib pd context
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: fib_label_output
                    
                    	Cached Label stack
                    	**type**\: list of int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: timer
                    
                    	Timers
                    	**type**\: list of :py:class:`Timer <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer>`
                    
                    .. attribute:: sack_blk
                    
                    	Seq nos. of sack blocks
                    	**type**\: list of :py:class:`SackBlk <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk>`
                    
                    .. attribute:: send_sack_hole
                    
                    	Sorted list of sack holes
                    	**type**\: list of :py:class:`SendSackHole <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pcb_id = None
                        self.socket_option_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags()
                        self.socket_option_flags.parent = self
                        self.socket_state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags()
                        self.socket_state_flags.parent = self
                        self.feature_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags()
                        self.feature_flags.parent = self
                        self.state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags()
                        self.state_flags.parent = self
                        self.request_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags()
                        self.request_flags.parent = self
                        self.receive_buf_state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags()
                        self.receive_buf_state_flags.parent = self
                        self.send_buf_state_flags = TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags()
                        self.send_buf_state_flags.parent = self
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
                        self.send_pdu_count = None
                        self.output_ifhandle = None
                        self.fib_pd_ctx_size = None
                        self.num_labels = None
                        self.local_address = YLeafList()
                        self.local_address.parent = self
                        self.local_address.name = 'local_address'
                        self.foreign_address = YLeafList()
                        self.foreign_address.parent = self
                        self.foreign_address.name = 'foreign_address'
                        self.fib_pd_ctx = YLeafList()
                        self.fib_pd_ctx.parent = self
                        self.fib_pd_ctx.name = 'fib_pd_ctx'
                        self.fib_label_output = YLeafList()
                        self.fib_label_output.parent = self
                        self.fib_label_output.name = 'fib_label_output'
                        self.timer = YList()
                        self.timer.parent = self
                        self.timer.name = 'timer'
                        self.sack_blk = YList()
                        self.sack_blk.parent = self
                        self.sack_blk.name = 'sack_blk'
                        self.send_sack_hole = YList()
                        self.send_sack_hole.parent = self
                        self.send_sack_hole.name = 'send_sack_hole'


                    class SocketOptionFlags(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:socket-option-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.debug is not None:
                                return True

                            if self.accept_connection is not None:
                                return True

                            if self.reuse_address is not None:
                                return True

                            if self.keep_alive is not None:
                                return True

                            if self.dont_route is not None:
                                return True

                            if self.broadcast is not None:
                                return True

                            if self.use_loopback is not None:
                                return True

                            if self.linger is not None:
                                return True

                            if self.out_of_band_inline is not None:
                                return True

                            if self.reuse_port is not None:
                                return True

                            if self.nonblocking_io is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketOptionFlags']['meta_info']


                    class SocketStateFlags(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:socket-state-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.no_file_descriptor_reference is not None:
                                return True

                            if self.is_connected is not None:
                                return True

                            if self.is_connecting is not None:
                                return True

                            if self.is_disconnecting is not None:
                                return True

                            if self.cant_send_more is not None:
                                return True

                            if self.cant_receive_more is not None:
                                return True

                            if self.received_at_mark is not None:
                                return True

                            if self.privileged is not None:
                                return True

                            if self.block_close is not None:
                                return True

                            if self.async_io_notify is not None:
                                return True

                            if self.is_confirming is not None:
                                return True

                            if self.is_solock is not None:
                                return True

                            if self.is_detached is not None:
                                return True

                            if self.block_receive is not None:
                                return True

                            if self.block_send is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SocketStateFlags']['meta_info']


                    class FeatureFlags(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.selective_ack = None
                            self.md5 = None
                            self.timestamps = None
                            self.window_scaling = None
                            self.nagle = None
                            self.giveup_timer = None
                            self.connection_keep_alive_timer = None
                            self.path_mtu_discovery = None
                            self.mss_cisco = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:feature-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.selective_ack is not None:
                                return True

                            if self.md5 is not None:
                                return True

                            if self.timestamps is not None:
                                return True

                            if self.window_scaling is not None:
                                return True

                            if self.nagle is not None:
                                return True

                            if self.giveup_timer is not None:
                                return True

                            if self.connection_keep_alive_timer is not None:
                                return True

                            if self.path_mtu_discovery is not None:
                                return True

                            if self.mss_cisco is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.FeatureFlags']['meta_info']


                    class StateFlags(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.nagle_wait = None
                            self.ack_needed = None
                            self.fin_sent = None
                            self.probing = None
                            self.need_push = None
                            self.pushed = None
                            self.in_syn_cache = None
                            self.path_mtu_ager = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:state-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.nagle_wait is not None:
                                return True

                            if self.ack_needed is not None:
                                return True

                            if self.fin_sent is not None:
                                return True

                            if self.probing is not None:
                                return True

                            if self.need_push is not None:
                                return True

                            if self.pushed is not None:
                                return True

                            if self.in_syn_cache is not None:
                                return True

                            if self.path_mtu_ager is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.StateFlags']['meta_info']


                    class RequestFlags(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.selective_ack = None
                            self.md5 = None
                            self.timestamps = None
                            self.window_scaling = None
                            self.nagle = None
                            self.giveup_timer = None
                            self.connection_keep_alive_timer = None
                            self.path_mtu_discovery = None
                            self.mss_cisco = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:request-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.selective_ack is not None:
                                return True

                            if self.md5 is not None:
                                return True

                            if self.timestamps is not None:
                                return True

                            if self.window_scaling is not None:
                                return True

                            if self.nagle is not None:
                                return True

                            if self.giveup_timer is not None:
                                return True

                            if self.connection_keep_alive_timer is not None:
                                return True

                            if self.path_mtu_discovery is not None:
                                return True

                            if self.mss_cisco is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.RequestFlags']['meta_info']


                    class ReceiveBufStateFlags(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:receive-buf-state-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.locked is not None:
                                return True

                            if self.waiting_for_lock is not None:
                                return True

                            if self.waiting_for_data is not None:
                                return True

                            if self.input_select is not None:
                                return True

                            if self.async_io is not None:
                                return True

                            if self.not_interruptible is not None:
                                return True

                            if self.io_timer_set is not None:
                                return True

                            if self.delayed_wakeup is not None:
                                return True

                            if self.wakeup is not None:
                                return True

                            if self.connect_wakeup is not None:
                                return True

                            if self.output_select is not None:
                                return True

                            if self.out_of_band_select is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.ReceiveBufStateFlags']['meta_info']


                    class SendBufStateFlags(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:send-buf-state-flags'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.locked is not None:
                                return True

                            if self.waiting_for_lock is not None:
                                return True

                            if self.waiting_for_data is not None:
                                return True

                            if self.input_select is not None:
                                return True

                            if self.async_io is not None:
                                return True

                            if self.not_interruptible is not None:
                                return True

                            if self.io_timer_set is not None:
                                return True

                            if self.delayed_wakeup is not None:
                                return True

                            if self.wakeup is not None:
                                return True

                            if self.connect_wakeup is not None:
                                return True

                            if self.output_select is not None:
                                return True

                            if self.out_of_band_select is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendBufStateFlags']['meta_info']


                    class Timer(object):
                        """
                        Timers
                        
                        .. attribute:: timer_type
                        
                        	Timer Type
                        	**type**\: :py:class:`TcpTimerEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpTimerEnum>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.timer_type = None
                            self.timer_activations = None
                            self.timer_expirations = None
                            self.timer_next_activation = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:timer'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.timer_type is not None:
                                return True

                            if self.timer_activations is not None:
                                return True

                            if self.timer_expirations is not None:
                                return True

                            if self.timer_next_activation is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.Timer']['meta_info']


                    class SackBlk(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.start = None
                            self.end = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:sack-blk'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.start is not None:
                                return True

                            if self.end is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SackBlk']['meta_info']


                    class SendSackHole(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.start = None
                            self.end = None
                            self.duplicated_ack = None
                            self.retransmitted = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:send-sack-hole'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.start is not None:
                                return True

                            if self.end is not None:
                                return True

                            if self.duplicated_ack is not None:
                                return True

                            if self.retransmitted is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation.SendSackHole']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.pcb_id is None:
                            raise YPYDataValidationError('Key property pcb_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-information[Cisco-IOS-XR-ip-tcp-oper:pcb-id = ' + str(self.pcb_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.pcb_id is not None:
                            return True

                        if self.socket_option_flags is not None and self.socket_option_flags._has_data():
                            return True

                        if self.socket_state_flags is not None and self.socket_state_flags._has_data():
                            return True

                        if self.feature_flags is not None and self.feature_flags._has_data():
                            return True

                        if self.state_flags is not None and self.state_flags._has_data():
                            return True

                        if self.request_flags is not None and self.request_flags._has_data():
                            return True

                        if self.receive_buf_state_flags is not None and self.receive_buf_state_flags._has_data():
                            return True

                        if self.send_buf_state_flags is not None and self.send_buf_state_flags._has_data():
                            return True

                        if self.address_family is not None:
                            return True

                        if self.pcb is not None:
                            return True

                        if self.so is not None:
                            return True

                        if self.tcpcb is not None:
                            return True

                        if self.vrf_id is not None:
                            return True

                        if self.connection_state is not None:
                            return True

                        if self.established_time is not None:
                            return True

                        if self.local_pid is not None:
                            return True

                        if self.local_port is not None:
                            return True

                        if self.foreign_port is not None:
                            return True

                        if self.packet_priority is not None:
                            return True

                        if self.packet_tos is not None:
                            return True

                        if self.packet_ttl is not None:
                            return True

                        if self.hash_index is not None:
                            return True

                        if self.current_receive_queue_size is not None:
                            return True

                        if self.max_receive_queue_size is not None:
                            return True

                        if self.current_send_queue_size is not None:
                            return True

                        if self.max_send_queue_size is not None:
                            return True

                        if self.current_receive_queue_packet_size is not None:
                            return True

                        if self.max_receive_queue_packet_size is not None:
                            return True

                        if self.save_queue_size is not None:
                            return True

                        if self.send_initial_sequence_num is not None:
                            return True

                        if self.send_unack_sequence_num is not None:
                            return True

                        if self.send_next_sequence_num is not None:
                            return True

                        if self.send_max_sequence_num is not None:
                            return True

                        if self.send_window_size is not None:
                            return True

                        if self.send_congestion_window_size is not None:
                            return True

                        if self.receive_initial_sequence_num is not None:
                            return True

                        if self.receive_next_sequence_num is not None:
                            return True

                        if self.receive_adv_window_size is not None:
                            return True

                        if self.receive_window_size is not None:
                            return True

                        if self.mss is not None:
                            return True

                        if self.peer_mss is not None:
                            return True

                        if self.srtt is not None:
                            return True

                        if self.rtto is not None:
                            return True

                        if self.krtt is not None:
                            return True

                        if self.srtv is not None:
                            return True

                        if self.min_rtt is not None:
                            return True

                        if self.max_rtt is not None:
                            return True

                        if self.retries is not None:
                            return True

                        if self.ack_hold_time is not None:
                            return True

                        if self.giveup_time is not None:
                            return True

                        if self.keep_alive_time is not None:
                            return True

                        if self.syn_wait_time is not None:
                            return True

                        if self.rxsy_naclname is not None:
                            return True

                        if self.soft_error is not None:
                            return True

                        if self.sock_error is not None:
                            return True

                        if self.is_retrans_forever is not None:
                            return True

                        if self.min_mss is not None:
                            return True

                        if self.max_mss is not None:
                            return True

                        if self.connect_retries is not None:
                            return True

                        if self.connect_retry_interval is not None:
                            return True

                        if self.receive_window_scale is not None:
                            return True

                        if self.send_window_scale is not None:
                            return True

                        if self.request_receive_window_scale is not None:
                            return True

                        if self.rqst_send_wnd_scale is not None:
                            return True

                        if self.time_stamp_recent is not None:
                            return True

                        if self.time_stamp_recent_age is not None:
                            return True

                        if self.last_ack_sent is not None:
                            return True

                        if self.sendbuf_lowwat is not None:
                            return True

                        if self.recvbuf_lowwat is not None:
                            return True

                        if self.sendbuf_hiwat is not None:
                            return True

                        if self.recvbuf_hiwat is not None:
                            return True

                        if self.sendbuf_notify_thresh is not None:
                            return True

                        if self.send_pdu_count is not None:
                            return True

                        if self.output_ifhandle is not None:
                            return True

                        if self.fib_pd_ctx_size is not None:
                            return True

                        if self.num_labels is not None:
                            return True

                        if self.local_address is not None:
                            for child in self.local_address:
                                if child is not None:
                                    return True

                        if self.foreign_address is not None:
                            for child in self.foreign_address:
                                if child is not None:
                                    return True

                        if self.fib_pd_ctx is not None:
                            for child in self.fib_pd_ctx:
                                if child is not None:
                                    return True

                        if self.fib_label_output is not None:
                            for child in self.fib_label_output:
                                if child is not None:
                                    return True

                        if self.timer is not None:
                            for child_ref in self.timer:
                                if child_ref._has_data():
                                    return True

                        if self.sack_blk is not None:
                            for child_ref in self.sack_blk:
                                if child_ref._has_data():
                                    return True

                        if self.send_sack_hole is not None:
                            for child_ref in self.send_sack_hole:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations.DetailInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-informations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.detail_information is not None:
                        for child_ref in self.detail_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpConnection.Nodes.Node.DetailInformations']['meta_info']


            class BriefInformations(object):
                """
                Table listing connections for which brief
                information is provided.Note that not all
                connections are listed in the brief table.
                
                .. attribute:: brief_information
                
                	Brief information about a TCP connection
                	**type**\: list of :py:class:`BriefInformation <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnection.Nodes.Node.BriefInformations.BriefInformation>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.brief_information = YList()
                    self.brief_information.parent = self
                    self.brief_information.name = 'brief_information'


                class BriefInformation(object):
                    """
                    Brief information about a TCP connection
                    
                    .. attribute:: pcb_id  <key>
                    
                    	Protocol Control Block ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: address_family
                    
                    	Address family
                    	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                    
                    .. attribute:: pcb
                    
                    	PCB Address
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: connection_state
                    
                    	Connection state
                    	**type**\: :py:class:`TcpConnStateEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpConnStateEnum>`
                    
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
                    
                    .. attribute:: current_send_queue_size
                    
                    	Current send queue size in bytes
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: vrf_id
                    
                    	VRF ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_address
                    
                    	Local address
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: foreign_address
                    
                    	Foreign address
                    	**type**\: list of str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.pcb_id = None
                        self.address_family = None
                        self.pcb = None
                        self.connection_state = None
                        self.local_pid = None
                        self.local_port = None
                        self.foreign_port = None
                        self.current_receive_queue_size = None
                        self.current_send_queue_size = None
                        self.vrf_id = None
                        self.local_address = YLeafList()
                        self.local_address.parent = self
                        self.local_address.name = 'local_address'
                        self.foreign_address = YLeafList()
                        self.foreign_address.parent = self
                        self.foreign_address.name = 'foreign_address'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')
                        if self.pcb_id is None:
                            raise YPYDataValidationError('Key property pcb_id is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-information[Cisco-IOS-XR-ip-tcp-oper:pcb-id = ' + str(self.pcb_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.pcb_id is not None:
                            return True

                        if self.address_family is not None:
                            return True

                        if self.pcb is not None:
                            return True

                        if self.connection_state is not None:
                            return True

                        if self.local_pid is not None:
                            return True

                        if self.local_port is not None:
                            return True

                        if self.foreign_port is not None:
                            return True

                        if self.current_receive_queue_size is not None:
                            return True

                        if self.current_send_queue_size is not None:
                            return True

                        if self.vrf_id is not None:
                            return True

                        if self.local_address is not None:
                            for child in self.local_address:
                                if child is not None:
                                    return True

                        if self.foreign_address is not None:
                            for child in self.foreign_address:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpConnection.Nodes.Node.BriefInformations.BriefInformation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-informations'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.brief_information is not None:
                        for child_ref in self.brief_information:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpConnection.Nodes.Node.BriefInformations']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYDataValidationError('Key property id is None')

                return '/Cisco-IOS-XR-ip-tcp-oper:tcp-connection/Cisco-IOS-XR-ip-tcp-oper:nodes/Cisco-IOS-XR-ip-tcp-oper:node[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.id is not None:
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                if self.extended_information is not None and self.extended_information._has_data():
                    return True

                if self.detail_informations is not None and self.detail_informations._has_data():
                    return True

                if self.brief_informations is not None and self.brief_informations._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                return meta._meta_table['TcpConnection.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-oper:tcp-connection/Cisco-IOS-XR-ip-tcp-oper:nodes'

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
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
            return meta._meta_table['TcpConnection.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-tcp-oper:tcp-connection'

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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['TcpConnection']['meta_info']


class Tcp(object):
    """
    tcp
    
    .. attribute:: nodes
    
    	Node\-specific TCP operational data
    	**type**\: :py:class:`Nodes <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes>`
    
    

    """

    _prefix = 'ip-tcp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = Tcp.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Node\-specific TCP operational data
        
        .. attribute:: node
        
        	TCP operational data for a particular node
        	**type**\: list of :py:class:`Node <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node>`
        
        

        """

        _prefix = 'ip-tcp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            TCP operational data for a particular node
            
            .. attribute:: node_name  <key>
            
            	Node name
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: statistics
            
            	Statistical TCP operational data for a node
            	**type**\: :py:class:`Statistics <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-tcp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.node_name = None
                self.statistics = Tcp.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Statistics(object):
                """
                Statistical TCP operational data for a node
                
                .. attribute:: ipv4_traffic
                
                	TCP Traffic statistics for IPv4
                	**type**\: :py:class:`Ipv4Traffic <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node.Statistics.Ipv4Traffic>`
                
                .. attribute:: ipv6_traffic
                
                	TCP Traffic statistics for IPv6
                	**type**\: :py:class:`Ipv6Traffic <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.Tcp.Nodes.Node.Statistics.Ipv6Traffic>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.ipv4_traffic = Tcp.Nodes.Node.Statistics.Ipv4Traffic()
                    self.ipv4_traffic.parent = self
                    self.ipv6_traffic = Tcp.Nodes.Node.Statistics.Ipv6Traffic()
                    self.ipv6_traffic.parent = self


                class Ipv4Traffic(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.tcp_input_packets = None
                        self.tcp_checksum_error_packets = None
                        self.tcp_dropped_packets = None
                        self.tcp_output_packets = None
                        self.tcp_retransmitted_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:ipv4-traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tcp_input_packets is not None:
                            return True

                        if self.tcp_checksum_error_packets is not None:
                            return True

                        if self.tcp_dropped_packets is not None:
                            return True

                        if self.tcp_output_packets is not None:
                            return True

                        if self.tcp_retransmitted_packets is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['Tcp.Nodes.Node.Statistics.Ipv4Traffic']['meta_info']


                class Ipv6Traffic(object):
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.tcp_input_packets = None
                        self.tcp_checksum_error_packets = None
                        self.tcp_dropped_packets = None
                        self.tcp_output_packets = None
                        self.tcp_retransmitted_packets = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:ipv6-traffic'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.tcp_input_packets is not None:
                            return True

                        if self.tcp_checksum_error_packets is not None:
                            return True

                        if self.tcp_dropped_packets is not None:
                            return True

                        if self.tcp_output_packets is not None:
                            return True

                        if self.tcp_retransmitted_packets is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['Tcp.Nodes.Node.Statistics.Ipv6Traffic']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistics'

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
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['Tcp.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.node_name is None:
                    raise YPYDataValidationError('Key property node_name is None')

                return '/Cisco-IOS-XR-ip-tcp-oper:tcp/Cisco-IOS-XR-ip-tcp-oper:nodes/Cisco-IOS-XR-ip-tcp-oper:node[Cisco-IOS-XR-ip-tcp-oper:node-name = ' + str(self.node_name) + ']'

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
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                return meta._meta_table['Tcp.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-oper:tcp/Cisco-IOS-XR-ip-tcp-oper:nodes'

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
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
            return meta._meta_table['Tcp.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-tcp-oper:tcp'

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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['Tcp']['meta_info']


class TcpNsr(object):
    """
    tcp nsr
    
    .. attribute:: nodes
    
    	Table of information about all nodes present on the system
    	**type**\: :py:class:`Nodes <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes>`
    
    

    """

    _prefix = 'ip-tcp-oper'
    _revision = '2015-11-09'

    def __init__(self):
        self.nodes = TcpNsr.Nodes()
        self.nodes.parent = self


    class Nodes(object):
        """
        Table of information about all nodes present on
        the system
        
        .. attribute:: node
        
        	Information about a single node
        	**type**\: list of :py:class:`Node <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node>`
        
        

        """

        _prefix = 'ip-tcp-oper'
        _revision = '2015-11-09'

        def __init__(self):
            self.parent = None
            self.node = YList()
            self.node.parent = self
            self.node.name = 'node'


        class Node(object):
            """
            Information about a single node
            
            .. attribute:: id  <key>
            
            	Describing a location
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: session
            
            	Information about TCP NSR Sessions
            	**type**\: :py:class:`Session <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session>`
            
            .. attribute:: client
            
            	Information about TCP NSR Client
            	**type**\: :py:class:`Client <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client>`
            
            .. attribute:: session_set
            
            	Information about TCP NSR Session Sets
            	**type**\: :py:class:`SessionSet <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet>`
            
            .. attribute:: statistics
            
            	Statis Information about TCP NSR connections
            	**type**\: :py:class:`Statistics <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics>`
            
            

            """

            _prefix = 'ip-tcp-oper'
            _revision = '2015-11-09'

            def __init__(self):
                self.parent = None
                self.id = None
                self.session = TcpNsr.Nodes.Node.Session()
                self.session.parent = self
                self.client = TcpNsr.Nodes.Node.Client()
                self.client.parent = self
                self.session_set = TcpNsr.Nodes.Node.SessionSet()
                self.session_set.parent = self
                self.statistics = TcpNsr.Nodes.Node.Statistics()
                self.statistics.parent = self


            class Session(object):
                """
                Information about TCP NSR Sessions
                
                .. attribute:: brief_sessions
                
                	Information about TCP NSR Sessions
                	**type**\: :py:class:`BriefSessions <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.BriefSessions>`
                
                .. attribute:: detail_sessions
                
                	Table about TCP NSR Sessions details
                	**type**\: :py:class:`DetailSessions <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.brief_sessions = TcpNsr.Nodes.Node.Session.BriefSessions()
                    self.brief_sessions.parent = self
                    self.detail_sessions = TcpNsr.Nodes.Node.Session.DetailSessions()
                    self.detail_sessions.parent = self


                class BriefSessions(object):
                    """
                    Information about TCP NSR Sessions
                    
                    .. attribute:: brief_session
                    
                    	Brief information about NSR Sessions
                    	**type**\: list of :py:class:`BriefSession <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.brief_session = YList()
                        self.brief_session.parent = self
                        self.brief_session.name = 'brief_session'


                    class BriefSession(object):
                        """
                        Brief information about NSR Sessions
                        
                        .. attribute:: id  <key>
                        
                        	ID of NSR Sesison
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: address_family
                        
                        	Address family
                        	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                        
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
                        	**type**\: :py:class:`NsrStatusEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.NsrStatusEnum>`
                        
                        .. attribute:: is_ds_operational_up
                        
                        	Is Downstream NSR operational?
                        	**type**\: :py:class:`NsrStatusEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.NsrStatusEnum>`
                        
                        .. attribute:: is_only_receive_path_replication
                        
                        	Is replication limited to receive\-path only
                        	**type**\: bool
                        
                        .. attribute:: local_address
                        
                        	Local address
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: foreign_address
                        
                        	Foreign address
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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
                            self.local_address = YLeafList()
                            self.local_address.parent = self
                            self.local_address.name = 'local_address'
                            self.foreign_address = YLeafList()
                            self.foreign_address.parent = self
                            self.foreign_address.name = 'foreign_address'

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-session[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.address_family is not None:
                                return True

                            if self.pcb is not None:
                                return True

                            if self.sscb is not None:
                                return True

                            if self.local_port is not None:
                                return True

                            if self.foreign_port is not None:
                                return True

                            if self.vrf_id is not None:
                                return True

                            if self.is_admin_configured_up is not None:
                                return True

                            if self.is_us_operational_up is not None:
                                return True

                            if self.is_ds_operational_up is not None:
                                return True

                            if self.is_only_receive_path_replication is not None:
                                return True

                            if self.local_address is not None:
                                for child in self.local_address:
                                    if child is not None:
                                        return True

                            if self.foreign_address is not None:
                                for child in self.foreign_address:
                                    if child is not None:
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Session.BriefSessions.BriefSession']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.brief_session is not None:
                            for child_ref in self.brief_session:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Session.BriefSessions']['meta_info']


                class DetailSessions(object):
                    """
                    Table about TCP NSR Sessions details
                    
                    .. attribute:: detail_session
                    
                    	showing detailed information of NSR Sessions
                    	**type**\: list of :py:class:`DetailSession <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.detail_session = YList()
                        self.detail_session.parent = self
                        self.detail_session.name = 'detail_session'


                    class DetailSession(object):
                        """
                        showing detailed information of NSR Sessions
                        
                        .. attribute:: id  <key>
                        
                        	ID of NSR Sesison
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: set_information
                        
                        	Sesson\-set information
                        	**type**\: :py:class:`SetInformation <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation>`
                        
                        .. attribute:: address_family
                        
                        	Address family
                        	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                        
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
                        	**type**\: :py:class:`NsrStatusEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.NsrStatusEnum>`
                        
                        .. attribute:: is_ds_operational_up
                        
                        	Is Downstream NSR operational?
                        	**type**\: :py:class:`NsrStatusEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.NsrStatusEnum>`
                        
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
                        	**type**\: :py:class:`NsrDownReasonEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.NsrDownReasonEnum>`
                        
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
                        
                        .. attribute:: init_sync_end_time
                        
                        	Time at which the initial sync operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
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
                        
                        .. attribute:: init_sync_end_time_up_stream
                        
                        	Time at which the initial sync operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fist_standby_sequence_number_up_stream
                        
                        	FSSN for the upstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nsr_down_reason_up_stream
                        
                        	The reason NSR is not up towards the upstream partner
                        	**type**\: :py:class:`NsrDownReasonEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.NsrDownReasonEnum>`
                        
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
                        
                        .. attribute:: init_sync_end_time_down_stream
                        
                        	Time at which the initial sync operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: fist_standby_sequence_number_down_stream
                        
                        	FSSN for the upstream partner
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nsr_down_reason_down_stream
                        
                        	The reason NSR is not up towards the upstream partner
                        	**type**\: :py:class:`NsrDownReasonEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.NsrDownReasonEnum>`
                        
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
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: foreign_address
                        
                        	Foreign address
                        	**type**\: list of str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: packet_hold_queue
                        
                        	Sequence Number and datalength of each node in hold\_pakqueue
                        	**type**\: list of :py:class:`PacketHoldQueue <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue>`
                        
                        .. attribute:: internal_ack_hold_queue
                        
                        	Sequence Number and datalength of each node in hold\_iackqueue
                        	**type**\: list of :py:class:`InternalAckHoldQueue <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.set_information = TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation()
                            self.set_information.parent = self
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
                            self.local_address = YLeafList()
                            self.local_address.parent = self
                            self.local_address.name = 'local_address'
                            self.foreign_address = YLeafList()
                            self.foreign_address.parent = self
                            self.foreign_address.name = 'foreign_address'
                            self.packet_hold_queue = YList()
                            self.packet_hold_queue.parent = self
                            self.packet_hold_queue.name = 'packet_hold_queue'
                            self.internal_ack_hold_queue = YList()
                            self.internal_ack_hold_queue.parent = self
                            self.internal_ack_hold_queue.name = 'internal_ack_hold_queue'


                        class SetInformation(object):
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
                            	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                            
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
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

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:set-information'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.sscb is not None:
                                    return True

                                if self.pid is not None:
                                    return True

                                if self.client_name is not None:
                                    return True

                                if self.client_instance is not None:
                                    return True

                                if self.set_id is not None:
                                    return True

                                if self.sso_role is not None:
                                    return True

                                if self.mode is not None:
                                    return True

                                if self.address_family is not None:
                                    return True

                                if self.well_known_port is not None:
                                    return True

                                if self.local_node is not None:
                                    return True

                                if self.local_instance is not None:
                                    return True

                                if self.protect_node is not None:
                                    return True

                                if self.protect_instance is not None:
                                    return True

                                if self.number_of_sessions is not None:
                                    return True

                                if self.number_of_synced_sessions_up_stream is not None:
                                    return True

                                if self.number_of_synced_sessions_down_stream is not None:
                                    return True

                                if self.is_init_sync_in_progress is not None:
                                    return True

                                if self.is_sscb_init_sync_ready is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.SetInformation']['meta_info']


                        class PacketHoldQueue(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sequence_number = None
                                self.data_length = None
                                self.acknoledgement_number = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:packet-hold-queue'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.sequence_number is not None:
                                    return True

                                if self.data_length is not None:
                                    return True

                                if self.acknoledgement_number is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.PacketHoldQueue']['meta_info']


                        class InternalAckHoldQueue(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.sequence_number = None
                                self.data_length = None
                                self.acknoledgement_number = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:internal-ack-hold-queue'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.sequence_number is not None:
                                    return True

                                if self.data_length is not None:
                                    return True

                                if self.acknoledgement_number is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession.InternalAckHoldQueue']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-session[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.set_information is not None and self.set_information._has_data():
                                return True

                            if self.address_family is not None:
                                return True

                            if self.pcb is not None:
                                return True

                            if self.sscb is not None:
                                return True

                            if self.local_port is not None:
                                return True

                            if self.foreign_port is not None:
                                return True

                            if self.vrf_id is not None:
                                return True

                            if self.is_admin_configured_up is not None:
                                return True

                            if self.is_us_operational_up is not None:
                                return True

                            if self.is_ds_operational_up is not None:
                                return True

                            if self.is_only_receive_path_replication is not None:
                                return True

                            if self.cookie is not None:
                                return True

                            if self.is_session_replicated is not None:
                                return True

                            if self.is_session_synced is not None:
                                return True

                            if self.fist_standby_sequence_number is not None:
                                return True

                            if self.fssn_offset is not None:
                                return True

                            if self.nsr_down_reason is not None:
                                return True

                            if self.nsr_down_time is not None:
                                return True

                            if self.sequence_number_of_init_sync is not None:
                                return True

                            if self.is_init_sync_in_progress is not None:
                                return True

                            if self.is_init_sync_second_phase is not None:
                                return True

                            if self.init_sync_error is not None:
                                return True

                            if self.is_init_sync_error_local is not None:
                                return True

                            if self.init_sync_start_time is not None:
                                return True

                            if self.init_sync_end_time is not None:
                                return True

                            if self.init_sync_flags is not None:
                                return True

                            if self.sequence_number_of_init_sync_up_stream is not None:
                                return True

                            if self.peer_endp_hdl_up_stream is not None:
                                return True

                            if self.init_sync_start_time_up_stream is not None:
                                return True

                            if self.init_sync_end_time_up_stream is not None:
                                return True

                            if self.fist_standby_sequence_number_up_stream is not None:
                                return True

                            if self.nsr_down_reason_up_stream is not None:
                                return True

                            if self.nsr_down_time_up_stream is not None:
                                return True

                            if self.sequence_number_of_init_sync_down_stream is not None:
                                return True

                            if self.peer_endp_hdl_down_stream is not None:
                                return True

                            if self.init_sync_start_time_down_stream is not None:
                                return True

                            if self.init_sync_end_time_down_stream is not None:
                                return True

                            if self.fist_standby_sequence_number_down_stream is not None:
                                return True

                            if self.nsr_down_reason_down_stream is not None:
                                return True

                            if self.nsr_down_time_down_stream is not None:
                                return True

                            if self.max_number_of_held_packet is not None:
                                return True

                            if self.max_number_of_held_packet_reach_time is not None:
                                return True

                            if self.max_number_of_held_internal_ack is not None:
                                return True

                            if self.max_number_of_held_internal_ack_reach_time is not None:
                                return True

                            if self.local_address is not None:
                                for child in self.local_address:
                                    if child is not None:
                                        return True

                            if self.foreign_address is not None:
                                for child in self.foreign_address:
                                    if child is not None:
                                        return True

                            if self.packet_hold_queue is not None:
                                for child_ref in self.packet_hold_queue:
                                    if child_ref._has_data():
                                        return True

                            if self.internal_ack_hold_queue is not None:
                                for child_ref in self.internal_ack_hold_queue:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Session.DetailSessions.DetailSession']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.detail_session is not None:
                            for child_ref in self.detail_session:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Session.DetailSessions']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:session'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.brief_sessions is not None and self.brief_sessions._has_data():
                        return True

                    if self.detail_sessions is not None and self.detail_sessions._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpNsr.Nodes.Node.Session']['meta_info']


            class Client(object):
                """
                Information about TCP NSR Client
                
                .. attribute:: detail_clients
                
                	Table about TCP NSR Client details
                	**type**\: :py:class:`DetailClients <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.DetailClients>`
                
                .. attribute:: brief_clients
                
                	Information about TCP NSR Client
                	**type**\: :py:class:`BriefClients <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.BriefClients>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.detail_clients = TcpNsr.Nodes.Node.Client.DetailClients()
                    self.detail_clients.parent = self
                    self.brief_clients = TcpNsr.Nodes.Node.Client.BriefClients()
                    self.brief_clients.parent = self


                class DetailClients(object):
                    """
                    Table about TCP NSR Client details
                    
                    .. attribute:: detail_client
                    
                    	showing detailed information of NSR Clients
                    	**type**\: list of :py:class:`DetailClient <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.DetailClients.DetailClient>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.detail_client = YList()
                        self.detail_client.parent = self
                        self.detail_client.name = 'detail_client'


                    class DetailClient(object):
                        """
                        showing detailed information of NSR Clients
                        
                        .. attribute:: id  <key>
                        
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
                        
                        .. attribute:: is_notification_registered
                        
                        	Registered with TCP for notifications?
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-client[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.ccb is not None:
                                return True

                            if self.pid is not None:
                                return True

                            if self.process_name is not None:
                                return True

                            if self.job_id is not None:
                                return True

                            if self.instance is not None:
                                return True

                            if self.numberof_sets is not None:
                                return True

                            if self.number_of_sessions is not None:
                                return True

                            if self.number_of_up_sessions is not None:
                                return True

                            if self.connected_at is not None:
                                return True

                            if self.is_notification_registered is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Client.DetailClients.DetailClient']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-clients'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.detail_client is not None:
                            for child_ref in self.detail_client:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Client.DetailClients']['meta_info']


                class BriefClients(object):
                    """
                    Information about TCP NSR Client
                    
                    .. attribute:: brief_client
                    
                    	Brief information about NSR Client
                    	**type**\: list of :py:class:`BriefClient <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Client.BriefClients.BriefClient>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.brief_client = YList()
                        self.brief_client.parent = self
                        self.brief_client.name = 'brief_client'


                    class BriefClient(object):
                        """
                        Brief information about NSR Client
                        
                        .. attribute:: id  <key>
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.ccb = None
                            self.pid = None
                            self.process_name = None
                            self.job_id = None
                            self.instance = None
                            self.numberof_sets = None
                            self.number_of_sessions = None
                            self.number_of_up_sessions = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-client[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.ccb is not None:
                                return True

                            if self.pid is not None:
                                return True

                            if self.process_name is not None:
                                return True

                            if self.job_id is not None:
                                return True

                            if self.instance is not None:
                                return True

                            if self.numberof_sets is not None:
                                return True

                            if self.number_of_sessions is not None:
                                return True

                            if self.number_of_up_sessions is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Client.BriefClients.BriefClient']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-clients'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.brief_client is not None:
                            for child_ref in self.brief_client:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Client.BriefClients']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:client'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.detail_clients is not None and self.detail_clients._has_data():
                        return True

                    if self.brief_clients is not None and self.brief_clients._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpNsr.Nodes.Node.Client']['meta_info']


            class SessionSet(object):
                """
                Information about TCP NSR Session Sets
                
                .. attribute:: detail_sets
                
                	Table about TCP NSR Session Sets details
                	**type**\: :py:class:`DetailSets <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.DetailSets>`
                
                .. attribute:: brief_sets
                
                	Information about TCP NSR Session Sets
                	**type**\: :py:class:`BriefSets <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.BriefSets>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.detail_sets = TcpNsr.Nodes.Node.SessionSet.DetailSets()
                    self.detail_sets.parent = self
                    self.brief_sets = TcpNsr.Nodes.Node.SessionSet.BriefSets()
                    self.brief_sets.parent = self


                class DetailSets(object):
                    """
                    Table about TCP NSR Session Sets details
                    
                    .. attribute:: detail_set
                    
                    	showing detailed information of NSR Session Sets
                    	**type**\: list of :py:class:`DetailSet <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.detail_set = YList()
                        self.detail_set.parent = self
                        self.detail_set.name = 'detail_set'


                    class DetailSet(object):
                        """
                        showing detailed information of NSR Session
                        Sets
                        
                        .. attribute:: id  <key>
                        
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
                        	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                        
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
                        
                        .. attribute:: init_sync_end_time
                        
                        	Time at which the last initial sync operation was ended (in seconds since 1st Jan 1970 00\:00 \:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: is_sscb_init_sync_ready
                        
                        	Is the SSCB ready for another initial sync?
                        	**type**\: bool
                        
                        .. attribute:: init_sync_ready_start_time
                        
                        	Time at which the session was ready for initial sync last (in seconds since 1st Jan 1970 00\:00 \:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: init_sync_ready_end_time
                        
                        	Time at which the session set last went not\-ready for initial sync (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: nsr_reset_time
                        
                        	Time at which NSR was last reset on the session set (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
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
                        
                        .. attribute:: audit_end_time
                        
                        	Time at which the last audit operation was ended (in seconds since 1st Jan 1970 00\:00\:00)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-set[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.sscb is not None:
                                return True

                            if self.pid is not None:
                                return True

                            if self.set_id is not None:
                                return True

                            if self.sso_role is not None:
                                return True

                            if self.mode is not None:
                                return True

                            if self.address_family is not None:
                                return True

                            if self.well_known_port is not None:
                                return True

                            if self.local_node is not None:
                                return True

                            if self.local_instance is not None:
                                return True

                            if self.protect_node is not None:
                                return True

                            if self.protect_instance is not None:
                                return True

                            if self.number_of_sessions is not None:
                                return True

                            if self.number_of_synced_sessions_up_stream is not None:
                                return True

                            if self.number_of_synced_sessions_down_stream is not None:
                                return True

                            if self.is_init_sync_in_progress is not None:
                                return True

                            if self.is_init_sync_second_phase is not None:
                                return True

                            if self.sequence_number_of_init_sync is not None:
                                return True

                            if self.init_sync_timer is not None:
                                return True

                            if self.total_number_of_init_sync_sessions is not None:
                                return True

                            if self.number_of_init_synced_sessions is not None:
                                return True

                            if self.number_of_sessions_init_sync_failed is not None:
                                return True

                            if self.init_sync_error is not None:
                                return True

                            if self.is_init_sync_error_local is not None:
                                return True

                            if self.init_sync_start_time is not None:
                                return True

                            if self.init_sync_end_time is not None:
                                return True

                            if self.is_sscb_init_sync_ready is not None:
                                return True

                            if self.init_sync_ready_start_time is not None:
                                return True

                            if self.init_sync_ready_end_time is not None:
                                return True

                            if self.nsr_reset_time is not None:
                                return True

                            if self.is_audit_in_progress is not None:
                                return True

                            if self.audit_seq_number is not None:
                                return True

                            if self.audit_start_time is not None:
                                return True

                            if self.audit_end_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.SessionSet.DetailSets.DetailSet']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:detail-sets'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.detail_set is not None:
                            for child_ref in self.detail_set:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.SessionSet.DetailSets']['meta_info']


                class BriefSets(object):
                    """
                    Information about TCP NSR Session Sets
                    
                    .. attribute:: brief_set
                    
                    	Brief information about NSR Session Sets
                    	**type**\: list of :py:class:`BriefSet <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.brief_set = YList()
                        self.brief_set.parent = self
                        self.brief_set.name = 'brief_set'


                    class BriefSet(object):
                        """
                        Brief information about NSR Session Sets
                        
                        .. attribute:: id  <key>
                        
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
                        	**type**\: :py:class:`AddrFamilyEnum <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.AddrFamilyEnum>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-set[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.sscb is not None:
                                return True

                            if self.pid is not None:
                                return True

                            if self.client_name is not None:
                                return True

                            if self.client_instance is not None:
                                return True

                            if self.set_id is not None:
                                return True

                            if self.sso_role is not None:
                                return True

                            if self.mode is not None:
                                return True

                            if self.address_family is not None:
                                return True

                            if self.well_known_port is not None:
                                return True

                            if self.local_node is not None:
                                return True

                            if self.local_instance is not None:
                                return True

                            if self.protect_node is not None:
                                return True

                            if self.protect_instance is not None:
                                return True

                            if self.number_of_sessions is not None:
                                return True

                            if self.number_of_synced_sessions_up_stream is not None:
                                return True

                            if self.number_of_synced_sessions_down_stream is not None:
                                return True

                            if self.is_init_sync_in_progress is not None:
                                return True

                            if self.is_sscb_init_sync_ready is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.SessionSet.BriefSets.BriefSet']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:brief-sets'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.brief_set is not None:
                            for child_ref in self.brief_set:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.SessionSet.BriefSets']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:session-set'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.detail_sets is not None and self.detail_sets._has_data():
                        return True

                    if self.brief_sets is not None and self.brief_sets._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpNsr.Nodes.Node.SessionSet']['meta_info']


            class Statistics(object):
                """
                Statis Information about TCP NSR connections
                
                .. attribute:: summary
                
                	Summary statistics across all NSR connections
                	**type**\: :py:class:`Summary <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary>`
                
                .. attribute:: statistic_clients
                
                	Table listing NSR connections for which statistic information is provided
                	**type**\: :py:class:`StatisticClients <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticClients>`
                
                .. attribute:: statistic_sets
                
                	Table listing NSR connections for which statistic information is provided
                	**type**\: :py:class:`StatisticSets <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSets>`
                
                .. attribute:: statistic_sessions
                
                	Table listing NSR connections for which statistic information is provided
                	**type**\: :py:class:`StatisticSessions <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSessions>`
                
                

                """

                _prefix = 'ip-tcp-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    self.parent = None
                    self.summary = TcpNsr.Nodes.Node.Statistics.Summary()
                    self.summary.parent = self
                    self.statistic_clients = TcpNsr.Nodes.Node.Statistics.StatisticClients()
                    self.statistic_clients.parent = self
                    self.statistic_sets = TcpNsr.Nodes.Node.Statistics.StatisticSets()
                    self.statistic_sets.parent = self
                    self.statistic_sessions = TcpNsr.Nodes.Node.Statistics.StatisticSessions()
                    self.statistic_sessions.parent = self


                class Summary(object):
                    """
                    Summary statistics across all NSR connections
                    
                    .. attribute:: snd_counters
                    
                    	Aggregate Send path counters
                    	**type**\: :py:class:`SndCounters <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.SndCounters>`
                    
                    .. attribute:: audit_counters
                    
                    	Aggregate Audit counters
                    	**type**\: :py:class:`AuditCounters <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters>`
                    
                    .. attribute:: last_cleared_time
                    
                    	Time of last clear (in seconds since 1st Jan 1970 00\:00\:00)
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
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
                    	**type**\: list of :py:class:`NotificationStatistic <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.snd_counters = TcpNsr.Nodes.Node.Statistics.Summary.SndCounters()
                        self.snd_counters.parent = self
                        self.audit_counters = TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters()
                        self.audit_counters.parent = self
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
                        self.notification_statistic = YList()
                        self.notification_statistic.parent = self
                        self.notification_statistic.name = 'notification_statistic'


                    class SndCounters(object):
                        """
                        Aggregate Send path counters
                        
                        .. attribute:: common
                        
                        	Common send path counters
                        	**type**\: :py:class:`Common <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common>`
                        
                        .. attribute:: aggr_only
                        
                        	Aggregate only send path counters
                        	**type**\: :py:class:`AggrOnly <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.common = TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common()
                            self.common.parent = self
                            self.aggr_only = TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly()
                            self.aggr_only.parent = self


                        class Common(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
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

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:common'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.data_xfer_send is not None:
                                    return True

                                if self.data_xfer_send_total is not None:
                                    return True

                                if self.data_xfer_send_drop is not None:
                                    return True

                                if self.data_xfer_send_iov_alloc is not None:
                                    return True

                                if self.data_xfer_rcv is not None:
                                    return True

                                if self.data_xfer_rcv_success is not None:
                                    return True

                                if self.data_xfer_rcv_fail_buffer_trim is not None:
                                    return True

                                if self.data_xfer_rcv_fail_snd_una_out_of_sync is not None:
                                    return True

                                if self.seg_instr_send is not None:
                                    return True

                                if self.seg_instr_send_units is not None:
                                    return True

                                if self.seg_instr_send_drop is not None:
                                    return True

                                if self.seg_instr_rcv is not None:
                                    return True

                                if self.seg_instr_rcv_success is not None:
                                    return True

                                if self.seg_instr_rcv_fail_buffer_trim is not None:
                                    return True

                                if self.seg_instr_rcv_fail_tcp_process is not None:
                                    return True

                                if self.nack_send is not None:
                                    return True

                                if self.nack_send_drop is not None:
                                    return True

                                if self.nack_rcv is not None:
                                    return True

                                if self.nack_rcv_success is not None:
                                    return True

                                if self.nack_rcv_fail_data_send is not None:
                                    return True

                                if self.cleanup_send is not None:
                                    return True

                                if self.cleanup_send_drop is not None:
                                    return True

                                if self.cleanup_rcv is not None:
                                    return True

                                if self.cleanup_rcv_success is not None:
                                    return True

                                if self.cleanup_rcv_fail_buffer_trim is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.Common']['meta_info']


                        class AggrOnly(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.data_xfer_rcv_drop_no_pcb = None
                                self.data_xfer_rcv_drop_no_scb_dp = None
                                self.seg_instr_rcv_drop_no_pcb = None
                                self.seg_instr_rcv_drop_no_scb_dp = None
                                self.nack_rcv_drop_no_pcb = None
                                self.nack_rcv_drop_no_scb_dp = None
                                self.cleanup_rcv_drop_no_pcb = None
                                self.cleanup_rcv_drop_no_scb_dp = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:aggr-only'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.data_xfer_rcv_drop_no_pcb is not None:
                                    return True

                                if self.data_xfer_rcv_drop_no_scb_dp is not None:
                                    return True

                                if self.seg_instr_rcv_drop_no_pcb is not None:
                                    return True

                                if self.seg_instr_rcv_drop_no_scb_dp is not None:
                                    return True

                                if self.nack_rcv_drop_no_pcb is not None:
                                    return True

                                if self.nack_rcv_drop_no_scb_dp is not None:
                                    return True

                                if self.cleanup_rcv_drop_no_pcb is not None:
                                    return True

                                if self.cleanup_rcv_drop_no_scb_dp is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters.AggrOnly']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:snd-counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.common is not None and self.common._has_data():
                                return True

                            if self.aggr_only is not None and self.aggr_only._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary.SndCounters']['meta_info']


                    class AuditCounters(object):
                        """
                        Aggregate Audit counters
                        
                        .. attribute:: common
                        
                        	Common audit counters
                        	**type**\: :py:class:`Common <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common>`
                        
                        .. attribute:: aggr_only
                        
                        	Aggregate only audit counters
                        	**type**\: :py:class:`AggrOnly <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.common = TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common()
                            self.common.parent = self
                            self.aggr_only = TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly()
                            self.aggr_only.parent = self


                        class Common(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
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

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:common'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mark_session_set_send is not None:
                                    return True

                                if self.mark_session_set_send_drop is not None:
                                    return True

                                if self.mark_session_set_rcv is not None:
                                    return True

                                if self.mark_session_set_rcv_drop is not None:
                                    return True

                                if self.session_send is not None:
                                    return True

                                if self.session_send_drop is not None:
                                    return True

                                if self.session_rcv is not None:
                                    return True

                                if self.session_rcv_drop is not None:
                                    return True

                                if self.sweep_session_set_send is not None:
                                    return True

                                if self.sweep_session_set_send_drop is not None:
                                    return True

                                if self.sweep_session_set_rcv is not None:
                                    return True

                                if self.sweep_session_set_rcv_drop is not None:
                                    return True

                                if self.session_set_response_send is not None:
                                    return True

                                if self.session_set_response_send_drop is not None:
                                    return True

                                if self.session_set_response_rcv is not None:
                                    return True

                                if self.session_set_response_rcv_drop is not None:
                                    return True

                                if self.mark_session_set_ack_send is not None:
                                    return True

                                if self.mark_session_set_ack_send_drop is not None:
                                    return True

                                if self.mark_session_set_ack_rcv is not None:
                                    return True

                                if self.mark_session_set_ack_rcv_drop is not None:
                                    return True

                                if self.mark_session_set_nack_send is not None:
                                    return True

                                if self.mark_session_set_nack_send_drop is not None:
                                    return True

                                if self.mark_session_set_nack_rcv is not None:
                                    return True

                                if self.mark_session_set_nack_rcv_drop is not None:
                                    return True

                                if self.abort is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.Common']['meta_info']


                        class AggrOnly(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.mark_session_set_rcv_drop_aggr = None
                                self.session_rcv_drop_aggr = None
                                self.sweep_session_set_rcv_drop_aggr = None
                                self.session_set_response_rcv_drop_aggr = None
                                self.mark_session_set_ack_rcv_drop_aggr = None
                                self.mark_session_set_nack_rcv_drop_aggr = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:aggr-only'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.mark_session_set_rcv_drop_aggr is not None:
                                    return True

                                if self.session_rcv_drop_aggr is not None:
                                    return True

                                if self.sweep_session_set_rcv_drop_aggr is not None:
                                    return True

                                if self.session_set_response_rcv_drop_aggr is not None:
                                    return True

                                if self.mark_session_set_ack_rcv_drop_aggr is not None:
                                    return True

                                if self.mark_session_set_nack_rcv_drop_aggr is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters.AggrOnly']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:audit-counters'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.common is not None and self.common._has_data():
                                return True

                            if self.aggr_only is not None and self.aggr_only._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary.AuditCounters']['meta_info']


                    class NotificationStatistic(object):
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.queued_count = None
                            self.failed_count = None
                            self.delivered_count = None
                            self.dropped_count = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:notification-statistic'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.queued_count is not None:
                                return True

                            if self.failed_count is not None:
                                return True

                            if self.delivered_count is not None:
                                return True

                            if self.dropped_count is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary.NotificationStatistic']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:summary'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.snd_counters is not None and self.snd_counters._has_data():
                            return True

                        if self.audit_counters is not None and self.audit_counters._has_data():
                            return True

                        if self.last_cleared_time is not None:
                            return True

                        if self.number_of_connected_clients is not None:
                            return True

                        if self.number_of_disconnected_clients is not None:
                            return True

                        if self.number_of_current_clients is not None:
                            return True

                        if self.number_of_created_session_sets is not None:
                            return True

                        if self.number_of_destroyed_session_sets is not None:
                            return True

                        if self.number_of_current_session_sets is not None:
                            return True

                        if self.number_of_added_sessions is not None:
                            return True

                        if self.number_of_deleted_sessions is not None:
                            return True

                        if self.number_of_current_sessions is not None:
                            return True

                        if self.number_of_partner_node is not None:
                            return True

                        if self.number_of_attempted_init_sync is not None:
                            return True

                        if self.number_of_succeeded_init_sync is not None:
                            return True

                        if self.number_of_failed_init_sync is not None:
                            return True

                        if self.number_of_held_packets is not None:
                            return True

                        if self.number_of_held_but_dropped_packets is not None:
                            return True

                        if self.number_of_held_internal_acks is not None:
                            return True

                        if self.number_of_held_but_dropped_internal_acks is not None:
                            return True

                        if self.number_of_sent_internal_acks is not None:
                            return True

                        if self.number_of_received_internal_acks is not None:
                            return True

                        if self.number_of_qad_receive_messages_drops is not None:
                            return True

                        if self.number_of_qad_receive_messages_unknowns is not None:
                            return True

                        if self.number_of_qad_receive_messages_accepts is not None:
                            return True

                        if self.number_of_qad_stale_receive_messages_drops is not None:
                            return True

                        if self.number_of_qad_transfer_message_sent is not None:
                            return True

                        if self.number_of_qad_transfer_message_drops is not None:
                            return True

                        if self.number_of_internal_ack_drops_no_pcb is not None:
                            return True

                        if self.number_of_internal_ack_drops_no_scbdp is not None:
                            return True

                        if self.internal_ack_drops_not_replicated is not None:
                            return True

                        if self.internal_ack_drops_initsync_first_phase is not None:
                            return True

                        if self.internal_ack_drops_stale is not None:
                            return True

                        if self.internal_ack_drops_immediate_match is not None:
                            return True

                        if self.held_packet_drops is not None:
                            return True

                        if self.notification_statistic is not None:
                            for child_ref in self.notification_statistic:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Statistics.Summary']['meta_info']


                class StatisticClients(object):
                    """
                    Table listing NSR connections for which
                    statistic information is provided
                    
                    .. attribute:: statistic_client
                    
                    	showing statistic information of NSR Clients
                    	**type**\: list of :py:class:`StatisticClient <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.statistic_client = YList()
                        self.statistic_client.parent = self
                        self.statistic_client.name = 'statistic_client'


                    class StatisticClient(object):
                        """
                        showing statistic information of NSR Clients
                        
                        .. attribute:: id  <key>
                        
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
                        
                        .. attribute:: notification_statistic
                        
                        	Various types of notification stats
                        	**type**\: list of :py:class:`NotificationStatistic <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic>`
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
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
                            self.notification_statistic = YList()
                            self.notification_statistic.parent = self
                            self.notification_statistic.name = 'notification_statistic'


                        class NotificationStatistic(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
                                self.queued_count = None
                                self.failed_count = None
                                self.delivered_count = None
                                self.dropped_count = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:notification-statistic'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.queued_count is not None:
                                    return True

                                if self.failed_count is not None:
                                    return True

                                if self.delivered_count is not None:
                                    return True

                                if self.dropped_count is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient.NotificationStatistic']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistic-client[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.ccb is not None:
                                return True

                            if self.pid is not None:
                                return True

                            if self.process_name is not None:
                                return True

                            if self.job_id is not None:
                                return True

                            if self.instance is not None:
                                return True

                            if self.connected_at is not None:
                                return True

                            if self.number_of_created_sscb is not None:
                                return True

                            if self.number_of_deleted_sscb is not None:
                                return True

                            if self.last_cleared_time is not None:
                                return True

                            if self.notification_statistic is not None:
                                for child_ref in self.notification_statistic:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients.StatisticClient']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistic-clients'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.statistic_client is not None:
                            for child_ref in self.statistic_client:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticClients']['meta_info']


                class StatisticSets(object):
                    """
                    Table listing NSR connections for which
                    statistic information is provided
                    
                    .. attribute:: statistic_set
                    
                    	showing statistic information of NSR Session Set
                    	**type**\: list of :py:class:`StatisticSet <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.statistic_set = YList()
                        self.statistic_set.parent = self
                        self.statistic_set.name = 'statistic_set'


                    class StatisticSet(object):
                        """
                        showing statistic information of NSR Session
                        Set
                        
                        .. attribute:: id  <key>
                        
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
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.sscb = None
                            self.set_id = None
                            self.number_of_attempted_init_sync = None
                            self.number_of_succeeded_init_sync = None
                            self.number_of_failed_init_sync = None
                            self.number_of_failover = None
                            self.number_of_nsr_resets = None
                            self.last_cleared_time = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistic-set[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.sscb is not None:
                                return True

                            if self.set_id is not None:
                                return True

                            if self.number_of_attempted_init_sync is not None:
                                return True

                            if self.number_of_succeeded_init_sync is not None:
                                return True

                            if self.number_of_failed_init_sync is not None:
                                return True

                            if self.number_of_failover is not None:
                                return True

                            if self.number_of_nsr_resets is not None:
                                return True

                            if self.last_cleared_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSets.StatisticSet']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistic-sets'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.statistic_set is not None:
                            for child_ref in self.statistic_set:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSets']['meta_info']


                class StatisticSessions(object):
                    """
                    Table listing NSR connections for which
                    statistic information is provided
                    
                    .. attribute:: statistic_session
                    
                    	showing statistic information of TCP connections
                    	**type**\: list of :py:class:`StatisticSession <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession>`
                    
                    

                    """

                    _prefix = 'ip-tcp-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        self.parent = None
                        self.statistic_session = YList()
                        self.statistic_session.parent = self
                        self.statistic_session.name = 'statistic_session'


                    class StatisticSession(object):
                        """
                        showing statistic information of TCP
                        connections
                        
                        .. attribute:: id  <key>
                        
                        	ID of TCP connection
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{1,8}
                        
                        .. attribute:: snd_counters
                        
                        	Send path counters for the PCB
                        	**type**\: :py:class:`SndCounters <ydk.models.ip.Cisco_IOS_XR_ip_tcp_oper.TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters>`
                        
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
                        
                        

                        """

                        _prefix = 'ip-tcp-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            self.parent = None
                            self.id = None
                            self.snd_counters = TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters()
                            self.snd_counters.parent = self
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


                        class SndCounters(object):
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
                            _revision = '2015-11-09'

                            def __init__(self):
                                self.parent = None
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

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYDataValidationError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:snd-counters'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.data_xfer_send is not None:
                                    return True

                                if self.data_xfer_send_total is not None:
                                    return True

                                if self.data_xfer_send_drop is not None:
                                    return True

                                if self.data_xfer_send_iov_alloc is not None:
                                    return True

                                if self.data_xfer_rcv is not None:
                                    return True

                                if self.data_xfer_rcv_success is not None:
                                    return True

                                if self.data_xfer_rcv_fail_buffer_trim is not None:
                                    return True

                                if self.data_xfer_rcv_fail_snd_una_out_of_sync is not None:
                                    return True

                                if self.seg_instr_send is not None:
                                    return True

                                if self.seg_instr_send_units is not None:
                                    return True

                                if self.seg_instr_send_drop is not None:
                                    return True

                                if self.seg_instr_rcv is not None:
                                    return True

                                if self.seg_instr_rcv_success is not None:
                                    return True

                                if self.seg_instr_rcv_fail_buffer_trim is not None:
                                    return True

                                if self.seg_instr_rcv_fail_tcp_process is not None:
                                    return True

                                if self.nack_send is not None:
                                    return True

                                if self.nack_send_drop is not None:
                                    return True

                                if self.nack_rcv is not None:
                                    return True

                                if self.nack_rcv_success is not None:
                                    return True

                                if self.nack_rcv_fail_data_send is not None:
                                    return True

                                if self.cleanup_send is not None:
                                    return True

                                if self.cleanup_send_drop is not None:
                                    return True

                                if self.cleanup_rcv is not None:
                                    return True

                                if self.cleanup_rcv_success is not None:
                                    return True

                                if self.cleanup_rcv_fail_buffer_trim is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                                return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession.SndCounters']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYDataValidationError('parent is not set . Cannot derive path.')
                            if self.id is None:
                                raise YPYDataValidationError('Key property id is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistic-session[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.id is not None:
                                return True

                            if self.snd_counters is not None and self.snd_counters._has_data():
                                return True

                            if self.pcb is not None:
                                return True

                            if self.number_of_times_nsr_up is not None:
                                return True

                            if self.number_of_timers_nsr_down is not None:
                                return True

                            if self.number_of_times_nsr_disabled is not None:
                                return True

                            if self.number_of_times_nsr_fail_over is not None:
                                return True

                            if self.internal_ack_drops_not_replicated is not None:
                                return True

                            if self.internal_ack_drops_initsync_first_phase is not None:
                                return True

                            if self.internal_ack_drops_stale is not None:
                                return True

                            if self.internal_ack_drops_immediate_match is not None:
                                return True

                            if self.last_cleared_time is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                            return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions.StatisticSession']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYDataValidationError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistic-sessions'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.statistic_session is not None:
                            for child_ref in self.statistic_session:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                        return meta._meta_table['TcpNsr.Nodes.Node.Statistics.StatisticSessions']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYDataValidationError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-ip-tcp-oper:statistics'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.summary is not None and self.summary._has_data():
                        return True

                    if self.statistic_clients is not None and self.statistic_clients._has_data():
                        return True

                    if self.statistic_sets is not None and self.statistic_sets._has_data():
                        return True

                    if self.statistic_sessions is not None and self.statistic_sessions._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                    return meta._meta_table['TcpNsr.Nodes.Node.Statistics']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYDataValidationError('Key property id is None')

                return '/Cisco-IOS-XR-ip-tcp-oper:tcp-nsr/Cisco-IOS-XR-ip-tcp-oper:nodes/Cisco-IOS-XR-ip-tcp-oper:node[Cisco-IOS-XR-ip-tcp-oper:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.id is not None:
                    return True

                if self.session is not None and self.session._has_data():
                    return True

                if self.client is not None and self.client._has_data():
                    return True

                if self.session_set is not None and self.session_set._has_data():
                    return True

                if self.statistics is not None and self.statistics._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
                return meta._meta_table['TcpNsr.Nodes.Node']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-ip-tcp-oper:tcp-nsr/Cisco-IOS-XR-ip-tcp-oper:nodes'

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
            from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
            return meta._meta_table['TcpNsr.Nodes']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-ip-tcp-oper:tcp-nsr'

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
        from ydk.models.ip._meta import _Cisco_IOS_XR_ip_tcp_oper as meta
        return meta._meta_table['TcpNsr']['meta_info']


