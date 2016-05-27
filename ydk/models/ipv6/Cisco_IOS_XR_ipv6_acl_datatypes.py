""" Cisco_IOS_XR_ipv6_acl_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv6AclDscpNumberEnum(Enum):
    """
    Ipv6AclDscpNumberEnum

    Ipv6 acl dscp number

    .. data:: DEFAULT = 0

    	Default DSCP

    .. data:: AF11 = 10

    	Match packets with AF11 DSCP

    .. data:: AF12 = 12

    	Match packets with AF12 DSCP

    .. data:: AF13 = 14

    	Match packets with AF13 DSCP

    .. data:: AF21 = 18

    	Match packets with AF21 DSCP

    .. data:: AF22 = 20

    	Match packets with AF22 DSCP

    .. data:: AF23 = 22

    	Match packets with AF23 DSCP

    .. data:: AF31 = 26

    	Match packets with AF31 DSCP

    .. data:: AF32 = 28

    	Match packets with AF32 DSCP

    .. data:: AF33 = 30

    	Match packets with AF33 DSCP

    .. data:: AF41 = 34

    	Match packets with AF41 DSCP

    .. data:: AF42 = 36

    	Match packets with AF42 DSCP

    .. data:: AF43 = 38

    	Match packets with AF43 DSCP

    .. data:: CS1 = 8

    	Match packets with CS1 (precedence 1) DSCP

    .. data:: CS2 = 16

    	Match packets with CS2 (precedence 2) DSCP

    .. data:: CS3 = 24

    	Match packets with CS3 (precedence 3) DSCP

    .. data:: CS4 = 32

    	Match packets with CS4 (precedence 4) DSCP

    .. data:: CS5 = 40

    	Match packets with CS5 (precedence 5) DSCP

    .. data:: CS6 = 48

    	Match packets with CS6 (precedence 6) DSCP

    .. data:: CS7 = 56

    	Match packets with CS7 (precedence 7) DSCP

    .. data:: EF = 46

    	Match packets with EF DSCP

    """

    DEFAULT = 0

    AF11 = 10

    AF12 = 12

    AF13 = 14

    AF21 = 18

    AF22 = 20

    AF23 = 22

    AF31 = 26

    AF32 = 28

    AF33 = 30

    AF41 = 34

    AF42 = 36

    AF43 = 38

    CS1 = 8

    CS2 = 16

    CS3 = 24

    CS4 = 32

    CS5 = 40

    CS6 = 48

    CS7 = 56

    EF = 46


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclDscpNumberEnum']


class Ipv6AclGrantEnumEnum(Enum):
    """
    Ipv6AclGrantEnumEnum

    Ipv6 acl grant enum

    .. data:: DENY = 0

    	Deny

    .. data:: PERMIT = 1

    	Permit

    """

    DENY = 0

    PERMIT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclGrantEnumEnum']


class Ipv6AclIcmpTypeCodeEnumEnum(Enum):
    """
    Ipv6AclIcmpTypeCodeEnumEnum

    Ipv6 acl icmp type code enum

    .. data:: ADMINISTRATIVELY_PROHIBITED = 65537

    	Administratively prohibited

    .. data:: HOST_UNREACHABLE = 65539

    	Host unreachable

    .. data:: PORT_UNREACHABLE = 65540

    	Port unreachable

    .. data:: UNREACHABLE = 131071

    	All unreachables

    .. data:: REASSEMBLY_TIMEOUT = 196609

    	Reassembly timeout

    .. data:: TIME_EXCEEDED = 262143

    	All time exceeds

    .. data:: OPTION_MISSING = 262145

    	Parameter required but not present

    .. data:: NO_ROOM_FOR_OPTION = 262146

    	Parameter required but no room

    .. data:: PARAMETER_PROBLEM = 327679

    	All parameter problems

    .. data:: ECHO = 8388608

    	Echo ping

    .. data:: ECHO_REPLY = 8454144

    	Echo reply

    .. data:: ROUTER_SOLICITATION = 8716288

    	Router discovery solicitations

    .. data:: ROUTER_ADVERTISEMENT = 8781824

    	Router discovery advertisements

    .. data:: REDIRECT = 8978432

    	All redirects

    """

    ADMINISTRATIVELY_PROHIBITED = 65537

    HOST_UNREACHABLE = 65539

    PORT_UNREACHABLE = 65540

    UNREACHABLE = 131071

    REASSEMBLY_TIMEOUT = 196609

    TIME_EXCEEDED = 262143

    OPTION_MISSING = 262145

    NO_ROOM_FOR_OPTION = 262146

    PARAMETER_PROBLEM = 327679

    ECHO = 8388608

    ECHO_REPLY = 8454144

    ROUTER_SOLICITATION = 8716288

    ROUTER_ADVERTISEMENT = 8781824

    REDIRECT = 8978432


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclIcmpTypeCodeEnumEnum']


class Ipv6AclLoggingEnumEnum(Enum):
    """
    Ipv6AclLoggingEnumEnum

    Ipv6 acl logging enum

    .. data:: LOG = 1

    	Log matches against this entry

    .. data:: LOG_INPUT = 2

    	Log matches against this entry, including input

    	interface

    """

    LOG = 1

    LOG_INPUT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclLoggingEnumEnum']


class Ipv6AclOperatorEnumEnum(Enum):
    """
    Ipv6AclOperatorEnumEnum

    Ipv6 acl operator enum

    .. data:: EQUAL = 1

    	Match only packets on a given port number

    .. data:: GREATER_THAN = 2

    	Match only packet with a greater port number

    .. data:: LESS_THAN = 3

    	Match only packet with a lower port number

    .. data:: NOT_EQUAL = 4

    	Match only packets not on a given port number

    .. data:: RANGE = 5

    	Match only packets in the range of port numbers

    """

    EQUAL = 1

    GREATER_THAN = 2

    LESS_THAN = 3

    NOT_EQUAL = 4

    RANGE = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclOperatorEnumEnum']


class Ipv6AclPortNumberEnum(Enum):
    """
    Ipv6AclPortNumberEnum

    Ipv6 acl port number

    .. data:: ECHO = 7

    	Match on the 'echo' port number

    .. data:: DISCARD = 9

    	Match on the 'discard' port number

    .. data:: DAYTIME = 13

    	Match on the 'daytime' port number (TCP/SCTP

    	only)

    .. data:: CHAR_GEN = 19

    	Match on the 'chargen' port number (TCP/SCTP

    	only)

    .. data:: FTP_DATA = 20

    	Match on the FTP data connections port number

    	(TCP/SCTP only)

    .. data:: FTP = 21

    	Match on the 'ftp' port number (TCP/SCTP only)

    .. data:: TELNET = 23

    	Match on the 'telnet' port number (TCP/SCTP

    	only)

    .. data:: SMTP = 25

    	Match on the 'smtp' port number (TCP/SCTP

    	only)

    .. data:: TIME = 37

    	Match on the 'time' port number

    .. data:: NAME_SERVER = 42

    	Match on the IEN116 name service port number

    	(UDP only)

    .. data:: WHO_IS = 43

    	Match on the 'nicname' port number (TCP/SCTP

    	only)

    .. data:: TACACS = 49

    	Match on the 'tacacs' port number

    .. data:: DNS = 53

    	Match on the 'dns' port number

    .. data:: BOOT_PS = 67

    	Match on the Bootstrap Protocol server port

    	number (UDP only)

    .. data:: BOOT_PC = 68

    	Match on the Bootstrap Protocol client port

    	number (UDP only)

    .. data:: TFTP = 69

    	Match on the 'tftp' port number (UDP only)

    .. data:: GOPHER = 70

    	Match on the 'gopher' port number (TCP/SCTP

    	only)

    .. data:: FINGER = 79

    	Match on the 'finger' port number (TCP/SCTP

    	only)

    .. data:: WWW = 80

    	Match on the 'http' port number (TCP/SCTP

    	only)

    .. data:: HOST_NAME = 101

    	Match on the NIC hostname server port number

    	(TCP/SCTP only)

    .. data:: POP2 = 109

    	Match on the 'pop2' port number (TCP/SCTP

    	only)

    .. data:: POP3 = 110

    	Match on the 'pop3' port number (TCP/SCTP

    	only)

    .. data:: SUN_RPC = 111

    	Match on the Sun RPC port number

    .. data:: IDENT = 113

    	Match on the 'ident' port number (TCP/SCTP

    	only)

    .. data:: NNTP = 119

    	Match on the 'nntp' port number (TCP/SCTP

    	only)

    .. data:: NTP = 123

    	Match on the 'ntp' port number (UDP only)

    .. data:: NET_BIOS_NS = 137

    	Match on the NetBIOS name service port number

    	(UDP only)

    .. data:: NET_BIOS_DGS = 138

    	Match on the NetBIOS datagram service port

    	number (UDP only)

    .. data:: NET_BIOS_SS = 139

    	Match on the NetBIOS session service port

    	number (UDP only)

    .. data:: SNMP = 161

    	Match on the 'snmp' port number (UDP only)

    .. data:: SNMP_TRAP = 162

    	Match on the SNMP traps port number (UDP only)

    .. data:: XDMCP = 177

    	Match on the 'xdmcp' port number (UDP only)

    .. data:: BGP = 179

    	Match on the 'bgp' port number (TCP/SCTP only)

    .. data:: IRC = 194

    	Match on the 'irc' port number (TCP/SCTP only)

    .. data:: DNSIX = 195

    	Match on the DNSIX security protocol auditing

    	port number (UDP only)

    .. data:: MOBILE_IP = 434

    	Match on the mobile IP registration port

    	number (UDP only)

    .. data:: PIM_AUTO_RP = 496

    	Match on the PIM Auto-RP port number

    .. data:: ISAKMP = 500

    	Match on the 'isakmp' port number (UDP only)

    .. data:: EXEC_OR_BIFF = 512

    	Match on the port used by TCP/SCTP for 'exec'

    	and by UDP for 'biff'

    .. data:: LOGIN_OR_WHO = 513

    	Match on the port used by TCP/SCTP for 'login'

    	and by UDP for 'rwho'

    .. data:: CMD_OR_SYSLOG = 514

    	Match on the port used by TCP/SCTP for 'rcmd'

    	and by UDP for 'syslog'

    .. data:: LPD = 515

    	Match on the 'lpd' port number (TCP/SCTP only)

    .. data:: TALK = 517

    	Match on the 'talk' port number

    .. data:: RIP = 520

    	Match on the 'rip' port number (UDP only)

    .. data:: UUCP = 540

    	Match on the 'uucp' port number (TCP/SCTP

    	only)

    .. data:: KLOGIN = 543

    	Match on the Kerberos login port number

    	(TCP/SCTP only)

    .. data:: KSHELL = 544

    	Match on the Kerberos shell port number

    	(TCP/SCTP only)

    .. data:: LDP = 646

    	Match on the LDP port

    """

    ECHO = 7

    DISCARD = 9

    DAYTIME = 13

    CHAR_GEN = 19

    FTP_DATA = 20

    FTP = 21

    TELNET = 23

    SMTP = 25

    TIME = 37

    NAME_SERVER = 42

    WHO_IS = 43

    TACACS = 49

    DNS = 53

    BOOT_PS = 67

    BOOT_PC = 68

    TFTP = 69

    GOPHER = 70

    FINGER = 79

    WWW = 80

    HOST_NAME = 101

    POP2 = 109

    POP3 = 110

    SUN_RPC = 111

    IDENT = 113

    NNTP = 119

    NTP = 123

    NET_BIOS_NS = 137

    NET_BIOS_DGS = 138

    NET_BIOS_SS = 139

    SNMP = 161

    SNMP_TRAP = 162

    XDMCP = 177

    BGP = 179

    IRC = 194

    DNSIX = 195

    MOBILE_IP = 434

    PIM_AUTO_RP = 496

    ISAKMP = 500

    EXEC_OR_BIFF = 512

    LOGIN_OR_WHO = 513

    CMD_OR_SYSLOG = 514

    LPD = 515

    TALK = 517

    RIP = 520

    UUCP = 540

    KLOGIN = 543

    KSHELL = 544

    LDP = 646


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclPortNumberEnum']


class Ipv6AclPrecedenceNumberEnum(Enum):
    """
    Ipv6AclPrecedenceNumberEnum

    Ipv6 acl precedence number

    .. data:: CRITICAL = 5

    	Match packets with critical precedence

    .. data:: FLASH = 3

    	Match packets with flash precedence

    .. data:: FLASH_OVERRIDE = 4

    	Match packets with flash override precedence

    .. data:: IMMEDIATE = 2

    	Match packets with immediate precedence

    .. data:: INTERNET = 6

    	Match packets with internetwork control

    	precedence

    .. data:: NETWORK = 7

    	Match packets with network control precedence

    .. data:: PRIORITY = 1

    	Match packets with priority precedence

    .. data:: ROUTINE = 0

    	Match packets with routine precedence

    """

    CRITICAL = 5

    FLASH = 3

    FLASH_OVERRIDE = 4

    IMMEDIATE = 2

    INTERNET = 6

    NETWORK = 7

    PRIORITY = 1

    ROUTINE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclPrecedenceNumberEnum']


class Ipv6AclProtocolNumberEnum(Enum):
    """
    Ipv6AclProtocolNumberEnum

    Ipv6 acl protocol number

    .. data:: IP = 0

    	Any IP protocol

    .. data:: ICMP = 1

    	Internet Control Message Protocol

    .. data:: IGMP = 2

    	Internet Gateway Message Protocol

    .. data:: IP_IN_IP = 4

    	IP in IP tunneling

    .. data:: TCP = 6

    	Transport Control Protocol

    .. data:: IGRP = 9

    	Cisco's IGRP Routing Protocol

    .. data:: UDP = 17

    	User Datagram Protocol

    .. data:: GRE = 47

    	Cisco's GRE tunneling

    .. data:: ESP = 50

    	Encapsulation Security Protocol

    .. data:: AHP = 51

    	Authentication Header Protocol

    .. data:: EIGRP = 88

    	Cisco's EIGRP Routing Protocol

    .. data:: OSPF = 89

    	OSPF Routing Protocol

    .. data:: NOS = 94

    	KA9Q NOS Compatible IP over IP tunneling

    .. data:: PIM = 103

    	Protocol Independent Multicast

    .. data:: PCP = 108

    	Payload Compression Protocol

    .. data:: SCTP = 132

    	Stream Control Transmission Protocol

    """

    IP = 0

    ICMP = 1

    IGMP = 2

    IP_IN_IP = 4

    TCP = 6

    IGRP = 9

    UDP = 17

    GRE = 47

    ESP = 50

    AHP = 51

    EIGRP = 88

    OSPF = 89

    NOS = 94

    PIM = 103

    PCP = 108

    SCTP = 132


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclProtocolNumberEnum']


class Ipv6AclStatusEnumEnum(Enum):
    """
    Ipv6AclStatusEnumEnum

    Ipv6 acl status enum

    .. data:: DISABLED = 0

    	Disabled

    .. data:: ENABLED = 1

    	Enabled

    """

    DISABLED = 0

    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclStatusEnumEnum']


class Ipv6AclTcpBitsNumberEnum(Enum):
    """
    Ipv6AclTcpBitsNumberEnum

    Ipv6 acl tcp bits number

    .. data:: ESTABLISHED = 20

    	Match established connections (0x14)

    .. data:: ACK = 16

    	Match on the ACK bit (0x10)

    .. data:: RST = 4

    	Match on the RST bit (0x04)

    .. data:: FIN = 1

    	Match on the FIN bit (0x01)

    .. data:: PSH = 8

    	Match on the PSH bit (0x08)

    .. data:: SYN = 2

    	Match on the SYN bit (0x02)

    .. data:: URG = 32

    	Match on the URG bit (0x20)

    """

    ESTABLISHED = 20

    ACK = 16

    RST = 4

    FIN = 1

    PSH = 8

    SYN = 2

    URG = 32


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclTcpBitsNumberEnum']


class Ipv6AclTcpMatchOperatorEnumEnum(Enum):
    """
    Ipv6AclTcpMatchOperatorEnumEnum

    Ipv6 acl tcp match operator enum

    .. data:: MATCH_ALL = 1

    	Match only packet with all the given TCP bits

    .. data:: MATCH_ANY = 3

    	Match only packet with any of the given TCP

    	bits

    """

    MATCH_ALL = 1

    MATCH_ANY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclTcpMatchOperatorEnumEnum']


class Ipv6AclTypeEnumEnum(Enum):
    """
    Ipv6AclTypeEnumEnum

    Ipv6 acl type enum

    .. data:: ACL = 1

    	ACL

    .. data:: PREFIX_LIST = 2

    	Prefix List

    """

    ACL = 1

    PREFIX_LIST = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6AclTypeEnumEnum']


class Ipv6PrefixMatchExactLengthEnum(Enum):
    """
    Ipv6PrefixMatchExactLengthEnum

    Ipv6 prefix match exact length

    .. data:: MATCH_EXACT_LENGTH = 1

    	Prefix Length Exact match

    """

    MATCH_EXACT_LENGTH = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6PrefixMatchExactLengthEnum']


class Ipv6PrefixMatchMaxLengthEnum(Enum):
    """
    Ipv6PrefixMatchMaxLengthEnum

    Ipv6 prefix match max length

    .. data:: MATCH_MAX_LENGTH = 3

    	Enable matching of Prefix Lengths lesser than

    	MaxPrefixLength

    """

    MATCH_MAX_LENGTH = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6PrefixMatchMaxLengthEnum']


class Ipv6PrefixMatchMinLengthEnum(Enum):
    """
    Ipv6PrefixMatchMinLengthEnum

    Ipv6 prefix match min length

    .. data:: MATCH_MIN_LENGTH = 2

    	Enable matching of Prefix Lengths greater than

    	MinPrefixLength

    """

    MATCH_MIN_LENGTH = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv6._meta import _Cisco_IOS_XR_ipv6_acl_datatypes as meta
        return meta._meta_table['Ipv6PrefixMatchMinLengthEnum']



