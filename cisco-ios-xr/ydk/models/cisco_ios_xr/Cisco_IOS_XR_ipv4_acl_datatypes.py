""" Cisco_IOS_XR_ipv4_acl_datatypes 

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



class Ipv4AclDscpNumber(Enum):
    """
    Ipv4AclDscpNumber (Enum Class)

    Ipv4 acl dscp number

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


class Ipv4AclFragFlags(Enum):
    """
    Ipv4AclFragFlags (Enum Class)

    Ipv4 acl frag flags

    .. data:: dont_fragment = 1

    	Match don't fragment flag

    .. data:: is_fragment = 2

    	Match is fragment flag

    .. data:: first_fragment = 4

    	Match first fragment flag

    .. data:: last_fragment = 8

    	Match last fragment flag

    .. data:: dont_fragment_is_fragment = 3

    	Match don't fragment and is fragment flag

    .. data:: dont_fragment_first_fragment = 5

    	Match don't fragment and first fragment flag

    .. data:: dont_fragment_last_fragment = 9

    	Match don't fragment and last fragment flag

    """

    dont_fragment = Enum.YLeaf(1, "dont-fragment")

    is_fragment = Enum.YLeaf(2, "is-fragment")

    first_fragment = Enum.YLeaf(4, "first-fragment")

    last_fragment = Enum.YLeaf(8, "last-fragment")

    dont_fragment_is_fragment = Enum.YLeaf(3, "dont-fragment-is-fragment")

    dont_fragment_first_fragment = Enum.YLeaf(5, "dont-fragment-first-fragment")

    dont_fragment_last_fragment = Enum.YLeaf(9, "dont-fragment-last-fragment")


class Ipv4AclGrantEnum(Enum):
    """
    Ipv4AclGrantEnum (Enum Class)

    Ipv4 acl grant enum

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    """

    deny = Enum.YLeaf(0, "deny")

    permit = Enum.YLeaf(1, "permit")


class Ipv4AclIcmpTypeCodeEnum(Enum):
    """
    Ipv4AclIcmpTypeCodeEnum (Enum Class)

    Ipv4 acl icmp type code enum

    .. data:: echo_reply = 65535

    	Echo reply

    .. data:: network_unreachable = 196608

    	Network unreachable

    .. data:: host_unreachable = 196609

    	Host unreachable

    .. data:: protocol_unreachable = 196610

    	Protocol unreachable

    .. data:: port_unreachable = 196611

    	Port unreachable

    .. data:: packet_too_big = 196612

    	Fragmentation needed and DF set

    .. data:: source_route_failed = 196613

    	Source route failed

    .. data:: network_unknown = 196614

    	Network unknown

    .. data:: host_unknown = 196615

    	Host unknown

    .. data:: host_isolated = 196616

    	Host isolated

    .. data:: dod_net_prohibited = 196617

    	Network prohibited

    .. data:: dod_host_prohibited = 196618

    	Host prohibited

    .. data:: host_tos_unreachable = 196619

    	Host unreachable for TOS

    .. data:: net_tos_unreachable = 196620

    	Network unreachable for TOS

    .. data:: administratively_prohibited = 196621

    	Administratively prohibited

    .. data:: host_precedence_unreachable = 196622

    	Host unreachable for precedence

    .. data:: precedence_unreachable = 196623

    	Precedence cutoff

    .. data:: unreachable = 262143

    	All unreachables

    .. data:: source_quench = 327679

    	Source quenches

    .. data:: network_redirect = 327680

    	Network redirect

    .. data:: host_redirect = 327681

    	Host redirect

    .. data:: net_tos_redirect = 327682

    	Network redirect for TOS

    .. data:: host_tos_redirect = 327683

    	Host redirect for TOS

    .. data:: redirect = 393215

    	All redirects

    .. data:: alternate_address = 458751

    	Alternate address

    .. data:: echo = 589823

    	Echo (ping)

    .. data:: router_advertisement = 655359

    	Router discovery advertisements

    .. data:: router_solicitation = 720895

    	Router discovery solicitations

    .. data:: ttl_exceeded = 720896

    	TTL exceeded

    .. data:: reassembly_timeout = 720897

    	Reassembly timeout

    .. data:: time_exceeded = 786431

    	All time exceeds

    .. data:: general_parameter_problem = 786432

    	Parameter problem

    .. data:: option_missing = 786433

    	Parameter required but not present

    .. data:: no_room_for_option = 786434

    	Parameter required but no room

    .. data:: parameter_problem = 851967

    	All parameter problems

    .. data:: timestamp_request = 917503

    	Timestamp requests

    .. data:: timestamp_reply = 983039

    	Timestamp replies

    .. data:: information_request = 1048575

    	Information request

    .. data:: information_reply = 1114111

    	Information replies

    .. data:: mask_request = 1179647

    	Mask requests

    .. data:: mask_reply = 1245183

    	Mask replies

    .. data:: traceroute = 2031615

    	Traceroute

    .. data:: conversion_error = 2097151

    	Datagram conversion

    .. data:: mobile_redirect = 2162687

    	Mobile host redirect

    """

    echo_reply = Enum.YLeaf(65535, "echo-reply")

    network_unreachable = Enum.YLeaf(196608, "network-unreachable")

    host_unreachable = Enum.YLeaf(196609, "host-unreachable")

    protocol_unreachable = Enum.YLeaf(196610, "protocol-unreachable")

    port_unreachable = Enum.YLeaf(196611, "port-unreachable")

    packet_too_big = Enum.YLeaf(196612, "packet-too-big")

    source_route_failed = Enum.YLeaf(196613, "source-route-failed")

    network_unknown = Enum.YLeaf(196614, "network-unknown")

    host_unknown = Enum.YLeaf(196615, "host-unknown")

    host_isolated = Enum.YLeaf(196616, "host-isolated")

    dod_net_prohibited = Enum.YLeaf(196617, "dod-net-prohibited")

    dod_host_prohibited = Enum.YLeaf(196618, "dod-host-prohibited")

    host_tos_unreachable = Enum.YLeaf(196619, "host-tos-unreachable")

    net_tos_unreachable = Enum.YLeaf(196620, "net-tos-unreachable")

    administratively_prohibited = Enum.YLeaf(196621, "administratively-prohibited")

    host_precedence_unreachable = Enum.YLeaf(196622, "host-precedence-unreachable")

    precedence_unreachable = Enum.YLeaf(196623, "precedence-unreachable")

    unreachable = Enum.YLeaf(262143, "unreachable")

    source_quench = Enum.YLeaf(327679, "source-quench")

    network_redirect = Enum.YLeaf(327680, "network-redirect")

    host_redirect = Enum.YLeaf(327681, "host-redirect")

    net_tos_redirect = Enum.YLeaf(327682, "net-tos-redirect")

    host_tos_redirect = Enum.YLeaf(327683, "host-tos-redirect")

    redirect = Enum.YLeaf(393215, "redirect")

    alternate_address = Enum.YLeaf(458751, "alternate-address")

    echo = Enum.YLeaf(589823, "echo")

    router_advertisement = Enum.YLeaf(655359, "router-advertisement")

    router_solicitation = Enum.YLeaf(720895, "router-solicitation")

    ttl_exceeded = Enum.YLeaf(720896, "ttl-exceeded")

    reassembly_timeout = Enum.YLeaf(720897, "reassembly-timeout")

    time_exceeded = Enum.YLeaf(786431, "time-exceeded")

    general_parameter_problem = Enum.YLeaf(786432, "general-parameter-problem")

    option_missing = Enum.YLeaf(786433, "option-missing")

    no_room_for_option = Enum.YLeaf(786434, "no-room-for-option")

    parameter_problem = Enum.YLeaf(851967, "parameter-problem")

    timestamp_request = Enum.YLeaf(917503, "timestamp-request")

    timestamp_reply = Enum.YLeaf(983039, "timestamp-reply")

    information_request = Enum.YLeaf(1048575, "information-request")

    information_reply = Enum.YLeaf(1114111, "information-reply")

    mask_request = Enum.YLeaf(1179647, "mask-request")

    mask_reply = Enum.YLeaf(1245183, "mask-reply")

    traceroute = Enum.YLeaf(2031615, "traceroute")

    conversion_error = Enum.YLeaf(2097151, "conversion-error")

    mobile_redirect = Enum.YLeaf(2162687, "mobile-redirect")


class Ipv4AclIgmpNumber(Enum):
    """
    Ipv4AclIgmpNumber (Enum Class)

    Ipv4 acl igmp number

    .. data:: host_query = 17

    	Host query

    .. data:: host_report = 18

    	Host report

    .. data:: dvmrp = 19

    	Distance Vector Multicast Routing Protocol

    .. data:: pim = 20

    	Portocol Independent Multicast

    .. data:: trace = 21

    	Multicast Trace

    .. data:: v2_report = 22

    	Version 2 report

    .. data:: v2_leave = 23

    	Version 2 leave

    .. data:: mtrace_response = 30

    	MTrace response

    .. data:: mtrace = 31

    	MTrace

    .. data:: v3_report = 34

    	Version 3 report

    """

    host_query = Enum.YLeaf(17, "host-query")

    host_report = Enum.YLeaf(18, "host-report")

    dvmrp = Enum.YLeaf(19, "dvmrp")

    pim = Enum.YLeaf(20, "pim")

    trace = Enum.YLeaf(21, "trace")

    v2_report = Enum.YLeaf(22, "v2-report")

    v2_leave = Enum.YLeaf(23, "v2-leave")

    mtrace_response = Enum.YLeaf(30, "mtrace-response")

    mtrace = Enum.YLeaf(31, "mtrace")

    v3_report = Enum.YLeaf(34, "v3-report")


class Ipv4AclLoggingEnum(Enum):
    """
    Ipv4AclLoggingEnum (Enum Class)

    Ipv4 acl logging enum

    .. data:: log = 1

    	Log matches against this entry

    .. data:: log_input = 2

    	Log matches against this entry, including input

    	interface

    """

    log = Enum.YLeaf(1, "log")

    log_input = Enum.YLeaf(2, "log-input")


class Ipv4AclOperatorEnum(Enum):
    """
    Ipv4AclOperatorEnum (Enum Class)

    Ipv4 acl operator enum

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


class Ipv4AclPortNumber(Enum):
    """
    Ipv4AclPortNumber (Enum Class)

    Ipv4 acl port number

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


class Ipv4AclPrecedenceNumber(Enum):
    """
    Ipv4AclPrecedenceNumber (Enum Class)

    Ipv4 acl precedence number

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


class Ipv4AclProtocolNumber(Enum):
    """
    Ipv4AclProtocolNumber (Enum Class)

    Ipv4 acl protocol number

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

    eigrp = Enum.YLeaf(88, "eigrp")

    ospf = Enum.YLeaf(89, "ospf")

    nos = Enum.YLeaf(94, "nos")

    pim = Enum.YLeaf(103, "pim")

    pcp = Enum.YLeaf(108, "pcp")

    sctp = Enum.YLeaf(132, "sctp")


class Ipv4AclStatusEnum(Enum):
    """
    Ipv4AclStatusEnum (Enum Class)

    Ipv4 acl status enum

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = Enum.YLeaf(0, "disabled")

    enabled = Enum.YLeaf(1, "enabled")


class Ipv4AclTcpMatchOperatorEnum(Enum):
    """
    Ipv4AclTcpMatchOperatorEnum (Enum Class)

    Ipv4 acl tcp match operator enum

    .. data:: match_all = 1

    	Match only packet with all the given TCP bits

    .. data:: match_any = 3

    	Match only packet with any of the given TCP

    	bits

    """

    match_all = Enum.YLeaf(1, "match-all")

    match_any = Enum.YLeaf(3, "match-any")



