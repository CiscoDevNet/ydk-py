""" Cisco_IOS_XE_acl 

Cisco XE Native Access Control List (ACL) Yang model.
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AclPortType(Enum):
    """
    AclPortType

    .. data:: bgp = 179

    .. data:: chargen = 19

    .. data:: daytime = 13

    .. data:: discard = 9

    .. data:: domain = 53

    .. data:: echo = 7

    .. data:: finger = 79

    .. data:: ftp = 21

    .. data:: ftp_data = 20

    .. data:: gopher = 70

    .. data:: hostname = 101

    .. data:: ident = 113

    .. data:: irc = 194

    .. data:: klogin = 543

    .. data:: kshell = 544

    .. data:: lpd = 515

    .. data:: msrpc = 135

    .. data:: nntp = 119

    .. data:: pim_auto_rp = 496

    .. data:: pop2 = 109

    .. data:: pop3 = 110

    .. data:: smtp = 25

    .. data:: sunrpc = 111

    .. data:: tacacs = 49

    .. data:: talk = 517

    .. data:: telnet = 23

    .. data:: time = 37

    .. data:: uucp = 540

    .. data:: whois = 43

    .. data:: www = 80

    .. data:: biff = 512

    .. data:: bootpc = 68

    .. data:: bootps = 67

    .. data:: dnsix = 195

    .. data:: isakmp = 500

    .. data:: mobile_ip = 434

    .. data:: nameserver = 42

    .. data:: netbios_dgm = 138

    .. data:: netbios_ns = 137

    .. data:: netbios_ss = 139

    .. data:: non500_isakmp = 4500

    .. data:: ntp = 123

    .. data:: rip = 520

    .. data:: ripv6 = 521

    .. data:: snmp = 161

    .. data:: snmptrap = 162

    .. data:: syslog = 514

    .. data:: tftp = 69

    .. data:: who = 513

    .. data:: xdmcp = 177

    """

    bgp = Enum.YLeaf(179, "bgp")

    chargen = Enum.YLeaf(19, "chargen")

    daytime = Enum.YLeaf(13, "daytime")

    discard = Enum.YLeaf(9, "discard")

    domain = Enum.YLeaf(53, "domain")

    echo = Enum.YLeaf(7, "echo")

    finger = Enum.YLeaf(79, "finger")

    ftp = Enum.YLeaf(21, "ftp")

    ftp_data = Enum.YLeaf(20, "ftp-data")

    gopher = Enum.YLeaf(70, "gopher")

    hostname = Enum.YLeaf(101, "hostname")

    ident = Enum.YLeaf(113, "ident")

    irc = Enum.YLeaf(194, "irc")

    klogin = Enum.YLeaf(543, "klogin")

    kshell = Enum.YLeaf(544, "kshell")

    lpd = Enum.YLeaf(515, "lpd")

    msrpc = Enum.YLeaf(135, "msrpc")

    nntp = Enum.YLeaf(119, "nntp")

    pim_auto_rp = Enum.YLeaf(496, "pim-auto-rp")

    pop2 = Enum.YLeaf(109, "pop2")

    pop3 = Enum.YLeaf(110, "pop3")

    smtp = Enum.YLeaf(25, "smtp")

    sunrpc = Enum.YLeaf(111, "sunrpc")

    tacacs = Enum.YLeaf(49, "tacacs")

    talk = Enum.YLeaf(517, "talk")

    telnet = Enum.YLeaf(23, "telnet")

    time = Enum.YLeaf(37, "time")

    uucp = Enum.YLeaf(540, "uucp")

    whois = Enum.YLeaf(43, "whois")

    www = Enum.YLeaf(80, "www")

    biff = Enum.YLeaf(512, "biff")

    bootpc = Enum.YLeaf(68, "bootpc")

    bootps = Enum.YLeaf(67, "bootps")

    dnsix = Enum.YLeaf(195, "dnsix")

    isakmp = Enum.YLeaf(500, "isakmp")

    mobile_ip = Enum.YLeaf(434, "mobile-ip")

    nameserver = Enum.YLeaf(42, "nameserver")

    netbios_dgm = Enum.YLeaf(138, "netbios-dgm")

    netbios_ns = Enum.YLeaf(137, "netbios-ns")

    netbios_ss = Enum.YLeaf(139, "netbios-ss")

    non500_isakmp = Enum.YLeaf(4500, "non500-isakmp")

    ntp = Enum.YLeaf(123, "ntp")

    rip = Enum.YLeaf(520, "rip")

    ripv6 = Enum.YLeaf(521, "ripv6")

    snmp = Enum.YLeaf(161, "snmp")

    snmptrap = Enum.YLeaf(162, "snmptrap")

    syslog = Enum.YLeaf(514, "syslog")

    tftp = Enum.YLeaf(69, "tftp")

    who = Enum.YLeaf(513, "who")

    xdmcp = Enum.YLeaf(177, "xdmcp")



