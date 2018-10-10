""" Cisco_IOS_XR_ipv6_acl_datatypes 

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



class Ipv6AclDscpNumber(Enum):
    """
    Ipv6AclDscpNumber (Enum Class)

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

    default = Enum.YLeaf(0, "default")

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


class Ipv6AclGrantEnum(Enum):
    """
    Ipv6AclGrantEnum (Enum Class)

    Ipv6 acl grant enum

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    """

    deny = Enum.YLeaf(0, "deny")

    permit = Enum.YLeaf(1, "permit")


class Ipv6AclIcmpTypeCodeEnum(Enum):
    """
    Ipv6AclIcmpTypeCodeEnum (Enum Class)

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

    no_route_to_destination = Enum.YLeaf(65536, "no-route-to-destination")

    administratively_prohibited = Enum.YLeaf(65537, "administratively-prohibited")

    beyond_scope_of_source_address = Enum.YLeaf(65538, "beyond-scope-of-source-address")

    host_unreachable = Enum.YLeaf(65539, "host-unreachable")

    port_unreachable = Enum.YLeaf(65540, "port-unreachable")

    unreachable = Enum.YLeaf(131071, "unreachable")

    packet_too_big = Enum.YLeaf(131072, "packet-too-big")

    ttl_exceeded = Enum.YLeaf(196608, "ttl-exceeded")

    reassembly_timeout = Enum.YLeaf(196609, "reassembly-timeout")

    time_exceeded = Enum.YLeaf(262143, "time-exceeded")

    erronenous_header_field = Enum.YLeaf(262144, "erronenous-header-field")

    option_missing = Enum.YLeaf(262145, "option-missing")

    no_room_for_option = Enum.YLeaf(262146, "no-room-for-option")

    parameter_problem = Enum.YLeaf(327679, "parameter-problem")

    echo = Enum.YLeaf(8388608, "echo")

    echo_reply = Enum.YLeaf(8454144, "echo-reply")

    group_membership_query = Enum.YLeaf(8585215, "group-membership-query")

    group_membership_report = Enum.YLeaf(8650751, "group-membership-report")

    group_membership_reduction = Enum.YLeaf(8716287, "group-membership-reduction")

    router_solicitation = Enum.YLeaf(8716288, "router-solicitation")

    router_advertisement = Enum.YLeaf(8781824, "router-advertisement")

    neighbor_solicitation = Enum.YLeaf(8847360, "neighbor-solicitation")

    neighbor_advertisement = Enum.YLeaf(8912896, "neighbor-advertisement")

    redirect = Enum.YLeaf(8978432, "redirect")

    rr_command = Enum.YLeaf(9043968, "rr-command")

    rr_result = Enum.YLeaf(9043969, "rr-result")

    rr_seqnum_reset = Enum.YLeaf(9044223, "rr-seqnum-reset")

    router_renumbering = Enum.YLeaf(9109503, "router-renumbering")

    query_subject_is_ipv6_address = Enum.YLeaf(9109504, "query-subject-is-ipv6-address")

    query_subject_is_domain_name = Enum.YLeaf(9109505, "query-subject-is-domain-name")

    query_subject_is_ipv4_address = Enum.YLeaf(9109506, "query-subject-is-ipv4-address")

    who_are_you_request = Enum.YLeaf(9175039, "who-are-you-request")

    node_information_successful_reply = Enum.YLeaf(9175040, "node-information-successful-reply")

    node_information_request_is_refused = Enum.YLeaf(9175041, "node-information-request-is-refused")

    unknown_query_type = Enum.YLeaf(9175042, "unknown-query-type")

    who_are_you_reply = Enum.YLeaf(9240575, "who-are-you-reply")


class Ipv6AclLoggingEnum(Enum):
    """
    Ipv6AclLoggingEnum (Enum Class)

    Ipv6 acl logging enum

    .. data:: log = 1

    	Log matches against this entry

    .. data:: log_input = 2

    	Log matches against this entry, including input

    	interface

    """

    log = Enum.YLeaf(1, "log")

    log_input = Enum.YLeaf(2, "log-input")


class Ipv6AclOperatorEnum(Enum):
    """
    Ipv6AclOperatorEnum (Enum Class)

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

    equal = Enum.YLeaf(1, "equal")

    greater_than = Enum.YLeaf(2, "greater-than")

    less_than = Enum.YLeaf(3, "less-than")

    not_equal = Enum.YLeaf(4, "not-equal")

    range = Enum.YLeaf(5, "range")


class Ipv6AclPortNumber(Enum):
    """
    Ipv6AclPortNumber (Enum Class)

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

    echo = Enum.YLeaf(7, "echo")

    discard = Enum.YLeaf(9, "discard")

    daytime = Enum.YLeaf(13, "daytime")

    char_gen = Enum.YLeaf(19, "char-gen")

    ftp_data = Enum.YLeaf(20, "ftp-data")

    ftp = Enum.YLeaf(21, "ftp")

    telnet = Enum.YLeaf(23, "telnet")

    smtp = Enum.YLeaf(25, "smtp")

    time = Enum.YLeaf(37, "time")

    name_server = Enum.YLeaf(42, "name-server")

    who_is = Enum.YLeaf(43, "who-is")

    tacacs = Enum.YLeaf(49, "tacacs")

    dns = Enum.YLeaf(53, "dns")

    boot_ps = Enum.YLeaf(67, "boot-ps")

    boot_pc = Enum.YLeaf(68, "boot-pc")

    tftp = Enum.YLeaf(69, "tftp")

    gopher = Enum.YLeaf(70, "gopher")

    finger = Enum.YLeaf(79, "finger")

    www = Enum.YLeaf(80, "www")

    host_name = Enum.YLeaf(101, "host-name")

    pop2 = Enum.YLeaf(109, "pop2")

    pop3 = Enum.YLeaf(110, "pop3")

    sun_rpc = Enum.YLeaf(111, "sun-rpc")

    ident = Enum.YLeaf(113, "ident")

    nntp = Enum.YLeaf(119, "nntp")

    ntp = Enum.YLeaf(123, "ntp")

    net_bios_ns = Enum.YLeaf(137, "net-bios-ns")

    net_bios_dgs = Enum.YLeaf(138, "net-bios-dgs")

    net_bios_ss = Enum.YLeaf(139, "net-bios-ss")

    snmp = Enum.YLeaf(161, "snmp")

    snmp_trap = Enum.YLeaf(162, "snmp-trap")

    xdmcp = Enum.YLeaf(177, "xdmcp")

    bgp = Enum.YLeaf(179, "bgp")

    irc = Enum.YLeaf(194, "irc")

    dnsix = Enum.YLeaf(195, "dnsix")

    mobile_ip = Enum.YLeaf(434, "mobile-ip")

    pim_auto_rp = Enum.YLeaf(496, "pim-auto-rp")

    isakmp = Enum.YLeaf(500, "isakmp")

    exec_or_biff = Enum.YLeaf(512, "exec-or-biff")

    login_or_who = Enum.YLeaf(513, "login-or-who")

    cmd_or_syslog = Enum.YLeaf(514, "cmd-or-syslog")

    lpd = Enum.YLeaf(515, "lpd")

    talk = Enum.YLeaf(517, "talk")

    rip = Enum.YLeaf(520, "rip")

    uucp = Enum.YLeaf(540, "uucp")

    klogin = Enum.YLeaf(543, "klogin")

    kshell = Enum.YLeaf(544, "kshell")

    ldp = Enum.YLeaf(646, "ldp")


class Ipv6AclPrecedenceNumber(Enum):
    """
    Ipv6AclPrecedenceNumber (Enum Class)

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

    critical = Enum.YLeaf(5, "critical")

    flash = Enum.YLeaf(3, "flash")

    flash_override = Enum.YLeaf(4, "flash-override")

    immediate = Enum.YLeaf(2, "immediate")

    internet = Enum.YLeaf(6, "internet")

    network = Enum.YLeaf(7, "network")

    priority = Enum.YLeaf(1, "priority")

    routine = Enum.YLeaf(0, "routine")


class Ipv6AclProtocolNumber(Enum):
    """
    Ipv6AclProtocolNumber (Enum Class)

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

    .. data:: icmpv6 = 58

    	Internet Control Message Protocol

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

    ip = Enum.YLeaf(0, "ip")

    icmp = Enum.YLeaf(1, "icmp")

    igmp = Enum.YLeaf(2, "igmp")

    ip_in_ip = Enum.YLeaf(4, "ip-in-ip")

    tcp = Enum.YLeaf(6, "tcp")

    igrp = Enum.YLeaf(9, "igrp")

    udp = Enum.YLeaf(17, "udp")

    gre = Enum.YLeaf(47, "gre")

    esp = Enum.YLeaf(50, "esp")

    ahp = Enum.YLeaf(51, "ahp")

    icmpv6 = Enum.YLeaf(58, "icmpv6")

    eigrp = Enum.YLeaf(88, "eigrp")

    ospf = Enum.YLeaf(89, "ospf")

    nos = Enum.YLeaf(94, "nos")

    pim = Enum.YLeaf(103, "pim")

    pcp = Enum.YLeaf(108, "pcp")

    sctp = Enum.YLeaf(132, "sctp")


class Ipv6AclStatusEnum(Enum):
    """
    Ipv6AclStatusEnum (Enum Class)

    Ipv6 acl status enum

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


class Ipv6AclTcpMatchOperatorEnum(Enum):
    """
    Ipv6AclTcpMatchOperatorEnum (Enum Class)

    Ipv6 acl tcp match operator enum

    .. data:: match_all = 1

    	Match only packet with all the given TCP bits

    .. data:: match_any = 3

    	Match only packet with any of the given TCP

    	bits

    """

    match_all = Enum.YLeaf(1, "match-all")

    match_any = Enum.YLeaf(3, "match-any")


class Ipv6AclTypeEnum(Enum):
    """
    Ipv6AclTypeEnum (Enum Class)

    Ipv6 acl type enum

    .. data:: acl = 1

    	ACL

    .. data:: prefix_list = 2

    	Prefix List

    """

    acl = Enum.YLeaf(1, "acl")

    prefix_list = Enum.YLeaf(2, "prefix-list")


class Ipv6PrefixMatchExactLength(Enum):
    """
    Ipv6PrefixMatchExactLength (Enum Class)

    Ipv6 prefix match exact length

    .. data:: match_exact_length = 1

    	Prefix Length Exact match

    """

    match_exact_length = Enum.YLeaf(1, "match-exact-length")


class Ipv6PrefixMatchMaxLength(Enum):
    """
    Ipv6PrefixMatchMaxLength (Enum Class)

    Ipv6 prefix match max length

    .. data:: match_max_length = 3

    	Enable matching of Prefix Lengths lesser than

    	MaxPrefixLength

    """

    match_max_length = Enum.YLeaf(3, "match-max-length")


class Ipv6PrefixMatchMinLength(Enum):
    """
    Ipv6PrefixMatchMinLength (Enum Class)

    Ipv6 prefix match min length

    .. data:: match_min_length = 2

    	Enable matching of Prefix Lengths greater than

    	MinPrefixLength

    """

    match_min_length = Enum.YLeaf(2, "match-min-length")



