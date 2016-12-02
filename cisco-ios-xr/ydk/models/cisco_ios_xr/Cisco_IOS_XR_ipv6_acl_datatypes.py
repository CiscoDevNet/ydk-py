""" Cisco_IOS_XR_ipv6_acl_datatypes 

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



class Ipv6AclDscpNumberEnum(Enum):
    """
    Ipv6AclDscpNumberEnum

    Ipv6 acl dscp number

    .. data:: default = 0

    	Default DSCP

    .. data:: af11 = 10

    	Match packets with AF11 DSCP

    .. data:: af12 = 12

    	Match packets with AF12 DSCP

    .. data:: af13 = 14

    	Match packets with AF13 DSCP

    .. data:: af21 = 18

    	Match packets with AF21 DSCP

    .. data:: af22 = 20

    	Match packets with AF22 DSCP

    .. data:: af23 = 22

    	Match packets with AF23 DSCP

    .. data:: af31 = 26

    	Match packets with AF31 DSCP

    .. data:: af32 = 28

    	Match packets with AF32 DSCP

    .. data:: af33 = 30

    	Match packets with AF33 DSCP

    .. data:: af41 = 34

    	Match packets with AF41 DSCP

    .. data:: af42 = 36

    	Match packets with AF42 DSCP

    .. data:: af43 = 38

    	Match packets with AF43 DSCP

    .. data:: cs1 = 8

    	Match packets with CS1 (precedence 1) DSCP

    .. data:: cs2 = 16

    	Match packets with CS2 (precedence 2) DSCP

    .. data:: cs3 = 24

    	Match packets with CS3 (precedence 3) DSCP

    .. data:: cs4 = 32

    	Match packets with CS4 (precedence 4) DSCP

    .. data:: cs5 = 40

    	Match packets with CS5 (precedence 5) DSCP

    .. data:: cs6 = 48

    	Match packets with CS6 (precedence 6) DSCP

    .. data:: cs7 = 56

    	Match packets with CS7 (precedence 7) DSCP

    .. data:: ef = 46

    	Match packets with EF DSCP

    """

    default = 0

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclDscpNumberEnum']


class Ipv6AclGrantEnumEnum(Enum):
    """
    Ipv6AclGrantEnumEnum

    Ipv6 acl grant enum

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    """

    deny = 0

    permit = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclGrantEnumEnum']


class Ipv6AclIcmpTypeCodeEnumEnum(Enum):
    """
    Ipv6AclIcmpTypeCodeEnumEnum

    Ipv6 acl icmp type code enum

    .. data:: no_route_to_destination = 65536

    	No route to destination

    .. data:: administratively_prohibited = 65537

    	Administratively prohibited

    .. data:: beyond_scope_of_source_address = 65538

    	Unreachable beyond scope of address

    .. data:: host_unreachable = 65539

    	Host unreachable

    .. data:: port_unreachable = 65540

    	Port unreachable

    .. data:: unreachable = 131071

    	All unreachables

    .. data:: packet_too_big = 131072

    	packet too big

    .. data:: ttl_exceeded = 196608

    	TTL exceeded

    .. data:: reassembly_timeout = 196609

    	Reassembly timeout

    .. data:: time_exceeded = 262143

    	All time exceeds

    .. data:: erronenous_header_field = 262144

    	Erroneous header field

    .. data:: option_missing = 262145

    	Parameter required but not present

    .. data:: no_room_for_option = 262146

    	Parameter required but no room

    .. data:: parameter_problem = 327679

    	All parameter problems

    .. data:: echo = 8388608

    	Echo ping

    .. data:: echo_reply = 8454144

    	Echo reply

    .. data:: group_membership_query = 8585215

    	Multicast listener query

    .. data:: group_membership_report = 8650751

    	Multicast listener report

    .. data:: group_membership_reduction = 8716287

    	Multicast listener done

    .. data:: router_solicitation = 8716288

    	Router discovery solicitations

    .. data:: router_advertisement = 8781824

    	Router discovery advertisements

    .. data:: neighbor_solicitation = 8847360

    	Neighbor discovery neighbor solicitations

    .. data:: neighbor_advertisement = 8912896

    	Neighbor discovery neighbor advertisements

    .. data:: redirect = 8978432

    	All redirects

    .. data:: rr_command = 9043968

    	Router renumbering command

    .. data:: rr_result = 9043969

    	Router renumbering result

    .. data:: rr_seqnum_reset = 9044223

    	Router renumbering seqnum

    .. data:: router_renumbering = 9109503

    	Router renumbering

    .. data:: query_subject_is_ipv6_address = 9109504

    	Query subject is ipv6 address

    .. data:: query_subject_is_domain_name = 9109505

    	Query subject is domain name

    .. data:: query_subject_is_ipv4_address = 9109506

    	Query subject is ipv4 address

    .. data:: who_are_you_request = 9175039

    	Who are you request

    .. data:: node_information_successful_reply = 9175040

    	Node information successful reply

    .. data:: node_information_request_is_refused = 9175041

    	Node information reply rejected

    .. data:: unknown_query_type = 9175042

    	Unknown query type

    .. data:: who_are_you_reply = 9240575

    	Who are you reply

    """

    no_route_to_destination = 65536

    administratively_prohibited = 65537

    beyond_scope_of_source_address = 65538

    host_unreachable = 65539

    port_unreachable = 65540

    unreachable = 131071

    packet_too_big = 131072

    ttl_exceeded = 196608

    reassembly_timeout = 196609

    time_exceeded = 262143

    erronenous_header_field = 262144

    option_missing = 262145

    no_room_for_option = 262146

    parameter_problem = 327679

    echo = 8388608

    echo_reply = 8454144

    group_membership_query = 8585215

    group_membership_report = 8650751

    group_membership_reduction = 8716287

    router_solicitation = 8716288

    router_advertisement = 8781824

    neighbor_solicitation = 8847360

    neighbor_advertisement = 8912896

    redirect = 8978432

    rr_command = 9043968

    rr_result = 9043969

    rr_seqnum_reset = 9044223

    router_renumbering = 9109503

    query_subject_is_ipv6_address = 9109504

    query_subject_is_domain_name = 9109505

    query_subject_is_ipv4_address = 9109506

    who_are_you_request = 9175039

    node_information_successful_reply = 9175040

    node_information_request_is_refused = 9175041

    unknown_query_type = 9175042

    who_are_you_reply = 9240575


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclIcmpTypeCodeEnumEnum']


class Ipv6AclLoggingEnumEnum(Enum):
    """
    Ipv6AclLoggingEnumEnum

    Ipv6 acl logging enum

    .. data:: log = 1

    	Log matches against this entry

    .. data:: log_input = 2

    	Log matches against this entry, including input

    	interface

    """

    log = 1

    log_input = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclLoggingEnumEnum']


class Ipv6AclOperatorEnumEnum(Enum):
    """
    Ipv6AclOperatorEnumEnum

    Ipv6 acl operator enum

    .. data:: equal = 1

    	Match only packets on a given port number

    .. data:: greater_than = 2

    	Match only packet with a greater port number

    .. data:: less_than = 3

    	Match only packet with a lower port number

    .. data:: not_equal = 4

    	Match only packets not on a given port number

    .. data:: range = 5

    	Match only packets in the range of port numbers

    """

    equal = 1

    greater_than = 2

    less_than = 3

    not_equal = 4

    range = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclOperatorEnumEnum']


class Ipv6AclPortNumberEnum(Enum):
    """
    Ipv6AclPortNumberEnum

    Ipv6 acl port number

    .. data:: echo = 7

    	Match on the 'echo' port number

    .. data:: discard = 9

    	Match on the 'discard' port number

    .. data:: daytime = 13

    	Match on the 'daytime' port number (TCP/SCTP

    	only)

    .. data:: char_gen = 19

    	Match on the 'chargen' port number (TCP/SCTP

    	only)

    .. data:: ftp_data = 20

    	Match on the FTP data connections port number

    	(TCP/SCTP only)

    .. data:: ftp = 21

    	Match on the 'ftp' port number (TCP/SCTP only)

    .. data:: telnet = 23

    	Match on the 'telnet' port number (TCP/SCTP

    	only)

    .. data:: smtp = 25

    	Match on the 'smtp' port number (TCP/SCTP

    	only)

    .. data:: time = 37

    	Match on the 'time' port number

    .. data:: name_server = 42

    	Match on the IEN116 name service port number

    	(UDP only)

    .. data:: who_is = 43

    	Match on the 'nicname' port number (TCP/SCTP

    	only)

    .. data:: tacacs = 49

    	Match on the 'tacacs' port number

    .. data:: dns = 53

    	Match on the 'dns' port number

    .. data:: boot_ps = 67

    	Match on the Bootstrap Protocol server port

    	number (UDP only)

    .. data:: boot_pc = 68

    	Match on the Bootstrap Protocol client port

    	number (UDP only)

    .. data:: tftp = 69

    	Match on the 'tftp' port number (UDP only)

    .. data:: gopher = 70

    	Match on the 'gopher' port number (TCP/SCTP

    	only)

    .. data:: finger = 79

    	Match on the 'finger' port number (TCP/SCTP

    	only)

    .. data:: www = 80

    	Match on the 'http' port number (TCP/SCTP

    	only)

    .. data:: host_name = 101

    	Match on the NIC hostname server port number

    	(TCP/SCTP only)

    .. data:: pop2 = 109

    	Match on the 'pop2' port number (TCP/SCTP

    	only)

    .. data:: pop3 = 110

    	Match on the 'pop3' port number (TCP/SCTP

    	only)

    .. data:: sun_rpc = 111

    	Match on the Sun RPC port number

    .. data:: ident = 113

    	Match on the 'ident' port number (TCP/SCTP

    	only)

    .. data:: nntp = 119

    	Match on the 'nntp' port number (TCP/SCTP

    	only)

    .. data:: ntp = 123

    	Match on the 'ntp' port number (UDP only)

    .. data:: net_bios_ns = 137

    	Match on the NetBIOS name service port number

    	(UDP only)

    .. data:: net_bios_dgs = 138

    	Match on the NetBIOS datagram service port

    	number (UDP only)

    .. data:: net_bios_ss = 139

    	Match on the NetBIOS session service port

    	number (UDP only)

    .. data:: snmp = 161

    	Match on the 'snmp' port number (UDP only)

    .. data:: snmp_trap = 162

    	Match on the SNMP traps port number (UDP only)

    .. data:: xdmcp = 177

    	Match on the 'xdmcp' port number (UDP only)

    .. data:: bgp = 179

    	Match on the 'bgp' port number (TCP/SCTP only)

    .. data:: irc = 194

    	Match on the 'irc' port number (TCP/SCTP only)

    .. data:: dnsix = 195

    	Match on the DNSIX security protocol auditing

    	port number (UDP only)

    .. data:: mobile_ip = 434

    	Match on the mobile IP registration port

    	number (UDP only)

    .. data:: pim_auto_rp = 496

    	Match on the PIM Auto-RP port number

    .. data:: isakmp = 500

    	Match on the 'isakmp' port number (UDP only)

    .. data:: exec_or_biff = 512

    	Match on the port used by TCP/SCTP for 'exec'

    	and by UDP for 'biff'

    .. data:: login_or_who = 513

    	Match on the port used by TCP/SCTP for 'login'

    	and by UDP for 'rwho'

    .. data:: cmd_or_syslog = 514

    	Match on the port used by TCP/SCTP for 'rcmd'

    	and by UDP for 'syslog'

    .. data:: lpd = 515

    	Match on the 'lpd' port number (TCP/SCTP only)

    .. data:: talk = 517

    	Match on the 'talk' port number

    .. data:: rip = 520

    	Match on the 'rip' port number (UDP only)

    .. data:: uucp = 540

    	Match on the 'uucp' port number (TCP/SCTP

    	only)

    .. data:: klogin = 543

    	Match on the Kerberos login port number

    	(TCP/SCTP only)

    .. data:: kshell = 544

    	Match on the Kerberos shell port number

    	(TCP/SCTP only)

    .. data:: ldp = 646

    	Match on the LDP port

    """

    echo = 7

    discard = 9

    daytime = 13

    char_gen = 19

    ftp_data = 20

    ftp = 21

    telnet = 23

    smtp = 25

    time = 37

    name_server = 42

    who_is = 43

    tacacs = 49

    dns = 53

    boot_ps = 67

    boot_pc = 68

    tftp = 69

    gopher = 70

    finger = 79

    www = 80

    host_name = 101

    pop2 = 109

    pop3 = 110

    sun_rpc = 111

    ident = 113

    nntp = 119

    ntp = 123

    net_bios_ns = 137

    net_bios_dgs = 138

    net_bios_ss = 139

    snmp = 161

    snmp_trap = 162

    xdmcp = 177

    bgp = 179

    irc = 194

    dnsix = 195

    mobile_ip = 434

    pim_auto_rp = 496

    isakmp = 500

    exec_or_biff = 512

    login_or_who = 513

    cmd_or_syslog = 514

    lpd = 515

    talk = 517

    rip = 520

    uucp = 540

    klogin = 543

    kshell = 544

    ldp = 646


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclPortNumberEnum']


class Ipv6AclPrecedenceNumberEnum(Enum):
    """
    Ipv6AclPrecedenceNumberEnum

    Ipv6 acl precedence number

    .. data:: critical = 5

    	Match packets with critical precedence

    .. data:: flash = 3

    	Match packets with flash precedence

    .. data:: flash_override = 4

    	Match packets with flash override precedence

    .. data:: immediate = 2

    	Match packets with immediate precedence

    .. data:: internet = 6

    	Match packets with internetwork control

    	precedence

    .. data:: network = 7

    	Match packets with network control precedence

    .. data:: priority = 1

    	Match packets with priority precedence

    .. data:: routine = 0

    	Match packets with routine precedence

    """

    critical = 5

    flash = 3

    flash_override = 4

    immediate = 2

    internet = 6

    network = 7

    priority = 1

    routine = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclPrecedenceNumberEnum']


class Ipv6AclProtocolNumberEnum(Enum):
    """
    Ipv6AclProtocolNumberEnum

    Ipv6 acl protocol number

    .. data:: ip = 0

    	Any IP protocol

    .. data:: icmp = 1

    	Internet Control Message Protocol

    .. data:: igmp = 2

    	Internet Gateway Message Protocol

    .. data:: ip_in_ip = 4

    	IP in IP tunneling

    .. data:: tcp = 6

    	Transport Control Protocol

    .. data:: igrp = 9

    	Cisco's IGRP Routing Protocol

    .. data:: udp = 17

    	User Datagram Protocol

    .. data:: gre = 47

    	Cisco's GRE tunneling

    .. data:: esp = 50

    	Encapsulation Security Protocol

    .. data:: ahp = 51

    	Authentication Header Protocol

    .. data:: eigrp = 88

    	Cisco's EIGRP Routing Protocol

    .. data:: ospf = 89

    	OSPF Routing Protocol

    .. data:: nos = 94

    	KA9Q NOS Compatible IP over IP tunneling

    .. data:: pim = 103

    	Protocol Independent Multicast

    .. data:: pcp = 108

    	Payload Compression Protocol

    .. data:: sctp = 132

    	Stream Control Transmission Protocol

    """

    ip = 0

    icmp = 1

    igmp = 2

    ip_in_ip = 4

    tcp = 6

    igrp = 9

    udp = 17

    gre = 47

    esp = 50

    ahp = 51

    eigrp = 88

    ospf = 89

    nos = 94

    pim = 103

    pcp = 108

    sctp = 132


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclProtocolNumberEnum']


class Ipv6AclStatusEnumEnum(Enum):
    """
    Ipv6AclStatusEnumEnum

    Ipv6 acl status enum

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = 0

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclStatusEnumEnum']


class Ipv6AclTcpBitsNumberEnum(Enum):
    """
    Ipv6AclTcpBitsNumberEnum

    Ipv6 acl tcp bits number

    .. data:: established = 20

    	Match established connections (0x14)

    .. data:: ack = 16

    	Match on the ACK bit (0x10)

    .. data:: rst = 4

    	Match on the RST bit (0x04)

    .. data:: fin = 1

    	Match on the FIN bit (0x01)

    .. data:: psh = 8

    	Match on the PSH bit (0x08)

    .. data:: syn = 2

    	Match on the SYN bit (0x02)

    .. data:: urg = 32

    	Match on the URG bit (0x20)

    """

    established = 20

    ack = 16

    rst = 4

    fin = 1

    psh = 8

    syn = 2

    urg = 32


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclTcpBitsNumberEnum']


class Ipv6AclTcpMatchOperatorEnumEnum(Enum):
    """
    Ipv6AclTcpMatchOperatorEnumEnum

    Ipv6 acl tcp match operator enum

    .. data:: match_all = 1

    	Match only packet with all the given TCP bits

    .. data:: match_any = 3

    	Match only packet with any of the given TCP

    	bits

    """

    match_all = 1

    match_any = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclTcpMatchOperatorEnumEnum']


class Ipv6AclTypeEnumEnum(Enum):
    """
    Ipv6AclTypeEnumEnum

    Ipv6 acl type enum

    .. data:: acl = 1

    	ACL

    .. data:: prefix_list = 2

    	Prefix List

    """

    acl = 1

    prefix_list = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclTypeEnumEnum']


class Ipv6PrefixMatchExactLengthEnum(Enum):
    """
    Ipv6PrefixMatchExactLengthEnum

    Ipv6 prefix match exact length

    .. data:: match_exact_length = 1

    	Prefix Length Exact match

    """

    match_exact_length = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6PrefixMatchExactLengthEnum']


class Ipv6PrefixMatchMaxLengthEnum(Enum):
    """
    Ipv6PrefixMatchMaxLengthEnum

    Ipv6 prefix match max length

    .. data:: match_max_length = 3

    	Enable matching of Prefix Lengths lesser than

    	MaxPrefixLength

    """

    match_max_length = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6PrefixMatchMaxLengthEnum']


class Ipv6PrefixMatchMinLengthEnum(Enum):
    """
    Ipv6PrefixMatchMinLengthEnum

    Ipv6 prefix match min length

    .. data:: match_min_length = 2

    	Enable matching of Prefix Lengths greater than

    	MinPrefixLength

    """

    match_min_length = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6PrefixMatchMinLengthEnum']



