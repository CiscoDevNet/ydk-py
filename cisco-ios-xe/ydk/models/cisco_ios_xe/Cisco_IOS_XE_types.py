""" Cisco_IOS_XE_types 

Cisco XE Native Common Type Definitions
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AccessListInOutType(Enum):
    """
    AccessListInOutType

    .. data:: in_ = 0

    .. data:: out = 1

    """

    in_ = Enum.YLeaf(0, "in")

    out = Enum.YLeaf(1, "out")


class AclTcpPortType(Enum):
    """
    AclTcpPortType

    .. data:: bgp = 179

    .. data:: chargen = 19

    .. data:: cmd = 514

    .. data:: daytime = 13

    .. data:: discard = 9

    .. data:: domain = 53

    .. data:: echo = 7

    .. data:: exec_ = 512

    .. data:: finger = 79

    .. data:: ftp = 21

    .. data:: ftp_data = 20

    .. data:: gopher = 70

    .. data:: hostname = 101

    .. data:: ident = 113

    .. data:: irc = 194

    .. data:: klogin = 543

    .. data:: kshell = 544

    .. data:: login = 513

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

    """

    bgp = Enum.YLeaf(179, "bgp")

    chargen = Enum.YLeaf(19, "chargen")

    cmd = Enum.YLeaf(514, "cmd")

    daytime = Enum.YLeaf(13, "daytime")

    discard = Enum.YLeaf(9, "discard")

    domain = Enum.YLeaf(53, "domain")

    echo = Enum.YLeaf(7, "echo")

    exec_ = Enum.YLeaf(512, "exec")

    finger = Enum.YLeaf(79, "finger")

    ftp = Enum.YLeaf(21, "ftp")

    ftp_data = Enum.YLeaf(20, "ftp-data")

    gopher = Enum.YLeaf(70, "gopher")

    hostname = Enum.YLeaf(101, "hostname")

    ident = Enum.YLeaf(113, "ident")

    irc = Enum.YLeaf(194, "irc")

    klogin = Enum.YLeaf(543, "klogin")

    kshell = Enum.YLeaf(544, "kshell")

    login = Enum.YLeaf(513, "login")

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


class AclUdpPortType(Enum):
    """
    AclUdpPortType

    .. data:: biff = 512

    .. data:: bootpc = 68

    .. data:: bootps = 67

    .. data:: discard = 9

    .. data:: dnsix = 195

    .. data:: domain = 53

    .. data:: echo = 7

    .. data:: isakmp = 500

    .. data:: mobile_ip = 434

    .. data:: nameserver = 42

    .. data:: netbios_dgm = 138

    .. data:: netbios_ns = 137

    .. data:: netbios_ss = 139

    .. data:: non500_isakmp = 4500

    .. data:: ntp = 123

    .. data:: pim_auto_rp = 496

    .. data:: rip = 520

    .. data:: ripv6 = 521

    .. data:: snmp = 161

    .. data:: snmptrap = 162

    .. data:: sunrpc = 111

    .. data:: syslog = 514

    .. data:: tacacs = 49

    .. data:: talk = 517

    .. data:: tftp = 69

    .. data:: time = 37

    .. data:: who = 513

    .. data:: xdmcp = 177

    """

    biff = Enum.YLeaf(512, "biff")

    bootpc = Enum.YLeaf(68, "bootpc")

    bootps = Enum.YLeaf(67, "bootps")

    discard = Enum.YLeaf(9, "discard")

    dnsix = Enum.YLeaf(195, "dnsix")

    domain = Enum.YLeaf(53, "domain")

    echo = Enum.YLeaf(7, "echo")

    isakmp = Enum.YLeaf(500, "isakmp")

    mobile_ip = Enum.YLeaf(434, "mobile-ip")

    nameserver = Enum.YLeaf(42, "nameserver")

    netbios_dgm = Enum.YLeaf(138, "netbios-dgm")

    netbios_ns = Enum.YLeaf(137, "netbios-ns")

    netbios_ss = Enum.YLeaf(139, "netbios-ss")

    non500_isakmp = Enum.YLeaf(4500, "non500-isakmp")

    ntp = Enum.YLeaf(123, "ntp")

    pim_auto_rp = Enum.YLeaf(496, "pim-auto-rp")

    rip = Enum.YLeaf(520, "rip")

    ripv6 = Enum.YLeaf(521, "ripv6")

    snmp = Enum.YLeaf(161, "snmp")

    snmptrap = Enum.YLeaf(162, "snmptrap")

    sunrpc = Enum.YLeaf(111, "sunrpc")

    syslog = Enum.YLeaf(514, "syslog")

    tacacs = Enum.YLeaf(49, "tacacs")

    talk = Enum.YLeaf(517, "talk")

    tftp = Enum.YLeaf(69, "tftp")

    time = Enum.YLeaf(37, "time")

    who = Enum.YLeaf(513, "who")

    xdmcp = Enum.YLeaf(177, "xdmcp")


class Bgp_Ipv4_Af_Type(Enum):
    """
    Bgp\_Ipv4\_Af\_Type

    .. data:: unicast = 0

    .. data:: multicast = 1

    .. data:: mdt = 2

    .. data:: tunnel = 3

    .. data:: labeled_unicast = 4

    .. data:: flowspec = 5

    .. data:: mvpn = 6

    """

    unicast = Enum.YLeaf(0, "unicast")

    multicast = Enum.YLeaf(1, "multicast")

    mdt = Enum.YLeaf(2, "mdt")

    tunnel = Enum.YLeaf(3, "tunnel")

    labeled_unicast = Enum.YLeaf(4, "labeled-unicast")

    flowspec = Enum.YLeaf(5, "flowspec")

    mvpn = Enum.YLeaf(6, "mvpn")


class Bgp_Ipv6_Af_Type(Enum):
    """
    Bgp\_Ipv6\_Af\_Type

    .. data:: unicast = 0

    .. data:: multicast = 1

    .. data:: mdt = 2

    .. data:: flowspec = 3

    .. data:: mvpn = 4

    """

    unicast = Enum.YLeaf(0, "unicast")

    multicast = Enum.YLeaf(1, "multicast")

    mdt = Enum.YLeaf(2, "mdt")

    flowspec = Enum.YLeaf(3, "flowspec")

    mvpn = Enum.YLeaf(4, "mvpn")


class CommunityWellKnownAddType(Enum):
    """
    CommunityWellKnownAddType

    .. data:: gshut = 0

    .. data:: internet = 1

    .. data:: local_AS = 2

    .. data:: no_advertise = 3

    .. data:: no_export = 4

    .. data:: additive = 5

    """

    gshut = Enum.YLeaf(0, "gshut")

    internet = Enum.YLeaf(1, "internet")

    local_AS = Enum.YLeaf(2, "local-AS")

    no_advertise = Enum.YLeaf(3, "no-advertise")

    no_export = Enum.YLeaf(4, "no-export")

    additive = Enum.YLeaf(5, "additive")


class CommunityWellKnownType(Enum):
    """
    CommunityWellKnownType

    .. data:: gshut = 0

    .. data:: internet = 1

    .. data:: local_AS = 2

    .. data:: no_advertise = 3

    .. data:: no_export = 4

    """

    gshut = Enum.YLeaf(0, "gshut")

    internet = Enum.YLeaf(1, "internet")

    local_AS = Enum.YLeaf(2, "local-AS")

    no_advertise = Enum.YLeaf(3, "no-advertise")

    no_export = Enum.YLeaf(4, "no-export")


class Cos_ValueType(Enum):
    """
    Cos\_ValueType

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = Enum.YLeaf(0, "cos")

    dscp = Enum.YLeaf(1, "dscp")

    exp = Enum.YLeaf(2, "exp")

    precedence = Enum.YLeaf(3, "precedence")


class DscpType(Enum):
    """
    DscpType

    .. data:: af11 = 10

    .. data:: af12 = 12

    .. data:: af13 = 14

    .. data:: af21 = 18

    .. data:: af22 = 20

    .. data:: af23 = 22

    .. data:: af31 = 26

    .. data:: af32 = 28

    .. data:: af33 = 30

    .. data:: af41 = 34

    .. data:: af42 = 36

    .. data:: af43 = 38

    .. data:: cs1 = 8

    .. data:: cs2 = 16

    .. data:: cs3 = 24

    .. data:: cs4 = 32

    .. data:: cs5 = 40

    .. data:: cs6 = 48

    .. data:: cs7 = 56

    .. data:: default = 0

    .. data:: dscp = 57

    .. data:: ef = 46

    .. data:: precedence = 58

    """

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

    default = Enum.YLeaf(0, "default")

    dscp = Enum.YLeaf(57, "dscp")

    ef = Enum.YLeaf(46, "ef")

    precedence = Enum.YLeaf(58, "precedence")


class Exp_ValueType(Enum):
    """
    Exp\_ValueType

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = Enum.YLeaf(0, "cos")

    dscp = Enum.YLeaf(1, "dscp")

    exp = Enum.YLeaf(2, "exp")

    precedence = Enum.YLeaf(3, "precedence")


class InterfaceType(Enum):
    """
    InterfaceType

    .. data:: BDI = 0

    .. data:: FastEthernet = 1

    .. data:: GigabitEthernet = 2

    .. data:: Loopback = 3

    .. data:: Port_channel = 4

    .. data:: Serial = 5

    .. data:: TenGigabitEthernet = 6

    .. data:: Vlan = 7

    """

    BDI = Enum.YLeaf(0, "BDI")

    FastEthernet = Enum.YLeaf(1, "FastEthernet")

    GigabitEthernet = Enum.YLeaf(2, "GigabitEthernet")

    Loopback = Enum.YLeaf(3, "Loopback")

    Port_channel = Enum.YLeaf(4, "Port-channel")

    Serial = Enum.YLeaf(5, "Serial")

    TenGigabitEthernet = Enum.YLeaf(6, "TenGigabitEthernet")

    Vlan = Enum.YLeaf(7, "Vlan")


class LimitDcNonDcType(Enum):
    """
    LimitDcNonDcType

    .. data:: disable = 0

    """

    disable = Enum.YLeaf(0, "disable")


class MobilityType(Enum):
    """
    MobilityType

    .. data:: bind_acknowledgement = 0

    .. data:: bind_error = 1

    .. data:: bind_refresh = 2

    .. data:: bind_update = 3

    .. data:: cot = 4

    .. data:: coti = 5

    .. data:: hot = 6

    .. data:: hoti = 7

    """

    bind_acknowledgement = Enum.YLeaf(0, "bind-acknowledgement")

    bind_error = Enum.YLeaf(1, "bind-error")

    bind_refresh = Enum.YLeaf(2, "bind-refresh")

    bind_update = Enum.YLeaf(3, "bind-update")

    cot = Enum.YLeaf(4, "cot")

    coti = Enum.YLeaf(5, "coti")

    hot = Enum.YLeaf(6, "hot")

    hoti = Enum.YLeaf(7, "hoti")


class MonthType(Enum):
    """
    MonthType

    .. data:: Jan = 0

    .. data:: Feb = 1

    .. data:: Mar = 2

    .. data:: Apr = 3

    .. data:: May = 4

    .. data:: Jun = 5

    .. data:: Jul = 6

    .. data:: Aug = 7

    .. data:: Sep = 8

    .. data:: Oct = 9

    .. data:: Nov = 10

    .. data:: Dec = 11

    """

    Jan = Enum.YLeaf(0, "Jan")

    Feb = Enum.YLeaf(1, "Feb")

    Mar = Enum.YLeaf(2, "Mar")

    Apr = Enum.YLeaf(3, "Apr")

    May = Enum.YLeaf(4, "May")

    Jun = Enum.YLeaf(5, "Jun")

    Jul = Enum.YLeaf(6, "Jul")

    Aug = Enum.YLeaf(7, "Aug")

    Sep = Enum.YLeaf(8, "Sep")

    Oct = Enum.YLeaf(9, "Oct")

    Nov = Enum.YLeaf(10, "Nov")

    Dec = Enum.YLeaf(11, "Dec")


class Prec_ValueType(Enum):
    """
    Prec\_ValueType

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = Enum.YLeaf(0, "cos")

    dscp = Enum.YLeaf(1, "dscp")

    exp = Enum.YLeaf(2, "exp")

    precedence = Enum.YLeaf(3, "precedence")


class PrecedenceType(Enum):
    """
    PrecedenceType

    .. data:: critical = 0

    .. data:: flash = 1

    .. data:: flash_override = 2

    .. data:: immediate = 3

    .. data:: internet = 4

    .. data:: network = 5

    .. data:: priority = 6

    .. data:: routine = 7

    """

    critical = Enum.YLeaf(0, "critical")

    flash = Enum.YLeaf(1, "flash")

    flash_override = Enum.YLeaf(2, "flash-override")

    immediate = Enum.YLeaf(3, "immediate")

    internet = Enum.YLeaf(4, "internet")

    network = Enum.YLeaf(5, "network")

    priority = Enum.YLeaf(6, "priority")

    routine = Enum.YLeaf(7, "routine")


class Qos_ValueType(Enum):
    """
    Qos\_ValueType

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = Enum.YLeaf(0, "cos")

    dscp = Enum.YLeaf(1, "dscp")

    exp = Enum.YLeaf(2, "exp")

    precedence = Enum.YLeaf(3, "precedence")


class RedistOspfExternalType(Enum):
    """
    RedistOspfExternalType

    .. data:: Y_1 = 0

    .. data:: Y_2 = 1

    """

    Y_1 = Enum.YLeaf(0, "1")

    Y_2 = Enum.YLeaf(1, "2")


class WeekdayType(Enum):
    """
    WeekdayType

    .. data:: Mon = 0

    .. data:: Tue = 1

    .. data:: Wed = 2

    .. data:: Thu = 3

    .. data:: Fri = 4

    .. data:: Sat = 5

    .. data:: Sun = 6

    """

    Mon = Enum.YLeaf(0, "Mon")

    Tue = Enum.YLeaf(1, "Tue")

    Wed = Enum.YLeaf(2, "Wed")

    Thu = Enum.YLeaf(3, "Thu")

    Fri = Enum.YLeaf(4, "Fri")

    Sat = Enum.YLeaf(5, "Sat")

    Sun = Enum.YLeaf(6, "Sun")



