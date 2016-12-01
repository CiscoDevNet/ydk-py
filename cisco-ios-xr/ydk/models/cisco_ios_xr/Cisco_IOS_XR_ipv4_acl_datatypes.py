""" Cisco_IOS_XR_ipv4_acl_datatypes 

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



class Ipv4AclDscpNumberEnum(Enum):
    """
    Ipv4AclDscpNumberEnum

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclDscpNumberEnum']


class Ipv4AclGrantEnumEnum(Enum):
    """
    Ipv4AclGrantEnumEnum

    Ipv4 acl grant enum

    .. data:: deny = 0

    	Deny

    .. data:: permit = 1

    	Permit

    """

    deny = 0

    permit = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclGrantEnumEnum']


class Ipv4AclIcmpTypeCodeEnumEnum(Enum):
    """
    Ipv4AclIcmpTypeCodeEnumEnum

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

    echo_reply = 65535

    network_unreachable = 196608

    host_unreachable = 196609

    protocol_unreachable = 196610

    port_unreachable = 196611

    packet_too_big = 196612

    source_route_failed = 196613

    network_unknown = 196614

    host_unknown = 196615

    host_isolated = 196616

    dod_net_prohibited = 196617

    dod_host_prohibited = 196618

    host_tos_unreachable = 196619

    net_tos_unreachable = 196620

    administratively_prohibited = 196621

    host_precedence_unreachable = 196622

    precedence_unreachable = 196623

    unreachable = 262143

    source_quench = 327679

    network_redirect = 327680

    host_redirect = 327681

    net_tos_redirect = 327682

    host_tos_redirect = 327683

    redirect = 393215

    alternate_address = 458751

    echo = 589823

    router_advertisement = 655359

    router_solicitation = 720895

    ttl_exceeded = 720896

    reassembly_timeout = 720897

    time_exceeded = 786431

    general_parameter_problem = 786432

    option_missing = 786433

    no_room_for_option = 786434

    parameter_problem = 851967

    timestamp_request = 917503

    timestamp_reply = 983039

    information_request = 1048575

    information_reply = 1114111

    mask_request = 1179647

    mask_reply = 1245183

    traceroute = 2031615

    conversion_error = 2097151

    mobile_redirect = 2162687


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclIcmpTypeCodeEnumEnum']


class Ipv4AclIgmpNumberEnum(Enum):
    """
    Ipv4AclIgmpNumberEnum

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

    host_query = 17

    host_report = 18

    dvmrp = 19

    pim = 20

    trace = 21

    v2_report = 22

    v2_leave = 23

    mtrace_response = 30

    mtrace = 31

    v3_report = 34


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclIgmpNumberEnum']


class Ipv4AclLoggingEnumEnum(Enum):
    """
    Ipv4AclLoggingEnumEnum

    Ipv4 acl logging enum

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclLoggingEnumEnum']


class Ipv4AclOperatorEnumEnum(Enum):
    """
    Ipv4AclOperatorEnumEnum

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

    equal = 1

    greater_than = 2

    less_than = 3

    not_equal = 4

    range = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclOperatorEnumEnum']


class Ipv4AclPortNumberEnum(Enum):
    """
    Ipv4AclPortNumberEnum

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclPortNumberEnum']


class Ipv4AclPrecedenceNumberEnum(Enum):
    """
    Ipv4AclPrecedenceNumberEnum

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclPrecedenceNumberEnum']


class Ipv4AclProtocolNumberEnum(Enum):
    """
    Ipv4AclProtocolNumberEnum

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclProtocolNumberEnum']


class Ipv4AclStatusEnumEnum(Enum):
    """
    Ipv4AclStatusEnumEnum

    Ipv4 acl status enum

    .. data:: disabled = 0

    	Disabled

    .. data:: enabled = 1

    	Enabled

    """

    disabled = 0

    enabled = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclStatusEnumEnum']


class Ipv4AclTcpBitsNumberEnum(Enum):
    """
    Ipv4AclTcpBitsNumberEnum

    Ipv4 acl tcp bits number

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclTcpBitsNumberEnum']


class Ipv4AclTcpMatchOperatorEnumEnum(Enum):
    """
    Ipv4AclTcpMatchOperatorEnumEnum

    Ipv4 acl tcp match operator enum

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
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclTcpMatchOperatorEnumEnum']



