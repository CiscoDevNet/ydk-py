""" Cisco_IOS_XE_types 

Cisco XE Native Common Type Definitions
Copyright (c) 2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AccessListInOutTypeEnum(Enum):
    """
    AccessListInOutTypeEnum

    .. data:: in_ = 0

    .. data:: out = 1

    """

    in_ = 0

    out = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['AccessListInOutTypeEnum']


class AclTcpPortTypeEnum(Enum):
    """
    AclTcpPortTypeEnum

    .. data:: bgp = 0

    .. data:: chargen = 1

    .. data:: cmd = 2

    .. data:: connectedapps_plain = 3

    .. data:: connectedapps_tls = 4

    .. data:: daytime = 5

    .. data:: discard = 6

    .. data:: domain = 7

    .. data:: echo = 8

    .. data:: exec_ = 9

    .. data:: finger = 10

    .. data:: ftp = 11

    .. data:: ftp_data = 12

    .. data:: gopher = 13

    .. data:: hostname = 14

    .. data:: ident = 15

    .. data:: irc = 16

    .. data:: klogin = 17

    .. data:: kshell = 18

    .. data:: login = 19

    .. data:: lpd = 20

    .. data:: msrpc = 21

    .. data:: nntp = 22

    .. data:: pim_auto_rp = 23

    .. data:: pop2 = 24

    .. data:: pop3 = 25

    .. data:: smtp = 26

    .. data:: sunrpc = 27

    .. data:: syslog = 28

    .. data:: tacacs = 29

    .. data:: talk = 30

    .. data:: telnet = 31

    .. data:: time = 32

    .. data:: uucp = 33

    .. data:: whois = 34

    .. data:: www = 35

    """

    bgp = 0

    chargen = 1

    cmd = 2

    connectedapps_plain = 3

    connectedapps_tls = 4

    daytime = 5

    discard = 6

    domain = 7

    echo = 8

    exec_ = 9

    finger = 10

    ftp = 11

    ftp_data = 12

    gopher = 13

    hostname = 14

    ident = 15

    irc = 16

    klogin = 17

    kshell = 18

    login = 19

    lpd = 20

    msrpc = 21

    nntp = 22

    pim_auto_rp = 23

    pop2 = 24

    pop3 = 25

    smtp = 26

    sunrpc = 27

    syslog = 28

    tacacs = 29

    talk = 30

    telnet = 31

    time = 32

    uucp = 33

    whois = 34

    www = 35


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['AclTcpPortTypeEnum']


class AclUdpPortTypeEnum(Enum):
    """
    AclUdpPortTypeEnum

    .. data:: biff = 0

    .. data:: bootpc = 1

    .. data:: bootps = 2

    .. data:: discard = 3

    .. data:: dnsix = 4

    .. data:: domain = 5

    .. data:: echo = 6

    .. data:: isakmp = 7

    .. data:: mobile_ip = 8

    .. data:: nameserver = 9

    .. data:: netbios_dgm = 10

    .. data:: netbios_ns = 11

    .. data:: netbios_ss = 12

    .. data:: non500_isakmp = 13

    .. data:: ntp = 14

    .. data:: pim_auto_rp = 15

    .. data:: rip = 16

    .. data:: ripv6 = 17

    .. data:: snmp = 18

    .. data:: snmptrap = 19

    .. data:: sunrpc = 20

    .. data:: syslog = 21

    .. data:: tacacs = 22

    .. data:: talk = 23

    .. data:: tftp = 24

    .. data:: time = 25

    .. data:: who = 26

    .. data:: xdmcp = 27

    """

    biff = 0

    bootpc = 1

    bootps = 2

    discard = 3

    dnsix = 4

    domain = 5

    echo = 6

    isakmp = 7

    mobile_ip = 8

    nameserver = 9

    netbios_dgm = 10

    netbios_ns = 11

    netbios_ss = 12

    non500_isakmp = 13

    ntp = 14

    pim_auto_rp = 15

    rip = 16

    ripv6 = 17

    snmp = 18

    snmptrap = 19

    sunrpc = 20

    syslog = 21

    tacacs = 22

    talk = 23

    tftp = 24

    time = 25

    who = 26

    xdmcp = 27


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['AclUdpPortTypeEnum']


class Bgp_Ipv4_Af_TypeEnum(Enum):
    """
    Bgp\_Ipv4\_Af\_TypeEnum

    .. data:: unicast = 0

    .. data:: multicast = 1

    .. data:: mdt = 2

    .. data:: tunnel = 3

    .. data:: labeled_unicast = 4

    .. data:: flowspec = 5

    .. data:: mvpn = 6

    """

    unicast = 0

    multicast = 1

    mdt = 2

    tunnel = 3

    labeled_unicast = 4

    flowspec = 5

    mvpn = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['Bgp_Ipv4_Af_TypeEnum']


class Bgp_Ipv6_Af_TypeEnum(Enum):
    """
    Bgp\_Ipv6\_Af\_TypeEnum

    .. data:: unicast = 0

    .. data:: multicast = 1

    .. data:: mdt = 2

    .. data:: flowspec = 3

    .. data:: mvpn = 4

    """

    unicast = 0

    multicast = 1

    mdt = 2

    flowspec = 3

    mvpn = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['Bgp_Ipv6_Af_TypeEnum']


class CommunityWellKnownTypeEnum(Enum):
    """
    CommunityWellKnownTypeEnum

    .. data:: gshut = 0

    .. data:: internet = 1

    .. data:: local_AS = 2

    .. data:: no_advertise = 3

    .. data:: no_export = 4

    """

    gshut = 0

    internet = 1

    local_AS = 2

    no_advertise = 3

    no_export = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['CommunityWellKnownTypeEnum']


class Cos_ValueTypeEnum(Enum):
    """
    Cos\_ValueTypeEnum

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = 0

    dscp = 1

    exp = 2

    precedence = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['Cos_ValueTypeEnum']


class DscpTypeEnum(Enum):
    """
    DscpTypeEnum

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

    default = 0

    dscp = 57

    ef = 46

    precedence = 58


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['DscpTypeEnum']


class Exp_ValueTypeEnum(Enum):
    """
    Exp\_ValueTypeEnum

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = 0

    dscp = 1

    exp = 2

    precedence = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['Exp_ValueTypeEnum']


class InterfaceTypeEnum(Enum):
    """
    InterfaceTypeEnum

    .. data:: BDI = 0

    .. data:: FastEthernet = 1

    .. data:: GigabitEthernet = 2

    .. data:: Loopback = 3

    .. data:: Port_channel = 4

    .. data:: Serial = 5

    .. data:: TenGigabitEthernet = 6

    .. data:: Vlan = 7

    """

    BDI = 0

    FastEthernet = 1

    GigabitEthernet = 2

    Loopback = 3

    Port_channel = 4

    Serial = 5

    TenGigabitEthernet = 6

    Vlan = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['InterfaceTypeEnum']


class LimitDcNonDcTypeEnum(Enum):
    """
    LimitDcNonDcTypeEnum

    .. data:: disable = 0

    """

    disable = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['LimitDcNonDcTypeEnum']


class MobilityTypeEnum(Enum):
    """
    MobilityTypeEnum

    .. data:: bind_acknowledgement = 0

    .. data:: bind_error = 1

    .. data:: bind_refresh = 2

    .. data:: bind_update = 3

    .. data:: cot = 4

    .. data:: coti = 5

    .. data:: hot = 6

    .. data:: hoti = 7

    """

    bind_acknowledgement = 0

    bind_error = 1

    bind_refresh = 2

    bind_update = 3

    cot = 4

    coti = 5

    hot = 6

    hoti = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['MobilityTypeEnum']


class MonthTypeEnum(Enum):
    """
    MonthTypeEnum

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

    Jan = 0

    Feb = 1

    Mar = 2

    Apr = 3

    May = 4

    Jun = 5

    Jul = 6

    Aug = 7

    Sep = 8

    Oct = 9

    Nov = 10

    Dec = 11


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['MonthTypeEnum']


class Prec_ValueTypeEnum(Enum):
    """
    Prec\_ValueTypeEnum

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = 0

    dscp = 1

    exp = 2

    precedence = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['Prec_ValueTypeEnum']


class PrecedenceTypeEnum(Enum):
    """
    PrecedenceTypeEnum

    .. data:: critical = 0

    .. data:: flash = 1

    .. data:: flash_override = 2

    .. data:: immediate = 3

    .. data:: internet = 4

    .. data:: network = 5

    .. data:: priority = 6

    .. data:: routine = 7

    """

    critical = 0

    flash = 1

    flash_override = 2

    immediate = 3

    internet = 4

    network = 5

    priority = 6

    routine = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['PrecedenceTypeEnum']


class Qos_ValueTypeEnum(Enum):
    """
    Qos\_ValueTypeEnum

    .. data:: cos = 0

    .. data:: dscp = 1

    .. data:: exp = 2

    .. data:: precedence = 3

    """

    cos = 0

    dscp = 1

    exp = 2

    precedence = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['Qos_ValueTypeEnum']


class RedistOspfExternalTypeEnum(Enum):
    """
    RedistOspfExternalTypeEnum

    .. data:: Y_1 = 0

    .. data:: Y_2 = 1

    """

    Y_1 = 0

    Y_2 = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['RedistOspfExternalTypeEnum']


class WeekdayTypeEnum(Enum):
    """
    WeekdayTypeEnum

    .. data:: Mon = 0

    .. data:: Tue = 1

    .. data:: Wed = 2

    .. data:: Thu = 3

    .. data:: Fri = 4

    .. data:: Sat = 5

    .. data:: Sun = 6

    """

    Mon = 0

    Tue = 1

    Wed = 2

    Thu = 3

    Fri = 4

    Sat = 5

    Sun = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_types as meta
        return meta._meta_table['WeekdayTypeEnum']



