""" Cisco_IOS_XR_ipv4_acl_datatypes 

This module contains a collection of generally useful
derived YANG data types.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class Ipv4AclDscpNumber_Enum(Enum):
    """
    Ipv4AclDscpNumber_Enum

    Ipv4 acl dscp number

    """

    """

    Default DSCP

    """
    DEFAULT = 0

    """

    Match packets with AF11 DSCP

    """
    AF11 = 10

    """

    Match packets with AF12 DSCP

    """
    AF12 = 12

    """

    Match packets with AF13 DSCP

    """
    AF13 = 14

    """

    Match packets with AF21 DSCP

    """
    AF21 = 18

    """

    Match packets with AF22 DSCP

    """
    AF22 = 20

    """

    Match packets with AF23 DSCP

    """
    AF23 = 22

    """

    Match packets with AF31 DSCP

    """
    AF31 = 26

    """

    Match packets with AF32 DSCP

    """
    AF32 = 28

    """

    Match packets with AF33 DSCP

    """
    AF33 = 30

    """

    Match packets with AF41 DSCP

    """
    AF41 = 34

    """

    Match packets with AF42 DSCP

    """
    AF42 = 36

    """

    Match packets with AF43 DSCP

    """
    AF43 = 38

    """

    Match packets with CS1 (precedence 1) DSCP

    """
    CS1 = 8

    """

    Match packets with CS2 (precedence 2) DSCP

    """
    CS2 = 16

    """

    Match packets with CS3 (precedence 3) DSCP

    """
    CS3 = 24

    """

    Match packets with CS4 (precedence 4) DSCP

    """
    CS4 = 32

    """

    Match packets with CS5 (precedence 5) DSCP

    """
    CS5 = 40

    """

    Match packets with CS6 (precedence 6) DSCP

    """
    CS6 = 48

    """

    Match packets with CS7 (precedence 7) DSCP

    """
    CS7 = 56

    """

    Match packets with EF DSCP

    """
    EF = 46


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclDscpNumber_Enum']


class Ipv4AclGrantEnum_Enum(Enum):
    """
    Ipv4AclGrantEnum_Enum

    Ipv4 acl grant enum

    """

    """

    Deny

    """
    DENY = 0

    """

    Permit

    """
    PERMIT = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclGrantEnum_Enum']


class Ipv4AclIcmpTypeCodeEnum_Enum(Enum):
    """
    Ipv4AclIcmpTypeCodeEnum_Enum

    Ipv4 acl icmp type code enum

    """

    """

    Echo reply

    """
    ECHO_REPLY = 65535

    """

    Network unreachable

    """
    NETWORK_UNREACHABLE = 196608

    """

    Host unreachable

    """
    HOST_UNREACHABLE = 196609

    """

    Protocol unreachable

    """
    PROTOCOL_UNREACHABLE = 196610

    """

    Port unreachable

    """
    PORT_UNREACHABLE = 196611

    """

    Fragmentation needed and DF set

    """
    PACKET_TOO_BIG = 196612

    """

    Source route failed

    """
    SOURCE_ROUTE_FAILED = 196613

    """

    Network unknown

    """
    NETWORK_UNKNOWN = 196614

    """

    Host unknown

    """
    HOST_UNKNOWN = 196615

    """

    Host isolated

    """
    HOST_ISOLATED = 196616

    """

    Network prohibited

    """
    DOD_NET_PROHIBITED = 196617

    """

    Host prohibited

    """
    DOD_HOST_PROHIBITED = 196618

    """

    Host unreachable for TOS

    """
    HOST_TOS_UNREACHABLE = 196619

    """

    Network unreachable for TOS

    """
    NET_TOS_UNREACHABLE = 196620

    """

    Administratively prohibited

    """
    ADMINISTRATIVELY_PROHIBITED = 196621

    """

    Host unreachable for precedence

    """
    HOST_PRECEDENCE_UNREACHABLE = 196622

    """

    Precedence cutoff

    """
    PRECEDENCE_UNREACHABLE = 196623

    """

    All unreachables

    """
    UNREACHABLE = 262143

    """

    Source quenches

    """
    SOURCE_QUENCH = 327679

    """

    Network redirect

    """
    NETWORK_REDIRECT = 327680

    """

    Host redirect

    """
    HOST_REDIRECT = 327681

    """

    Network redirect for TOS

    """
    NET_TOS_REDIRECT = 327682

    """

    Host redirect for TOS

    """
    HOST_TOS_REDIRECT = 327683

    """

    All redirects

    """
    REDIRECT = 393215

    """

    Alternate address

    """
    ALTERNATE_ADDRESS = 458751

    """

    Echo (ping)

    """
    ECHO = 589823

    """

    Router discovery advertisements

    """
    ROUTER_ADVERTISEMENT = 655359

    """

    Router discovery solicitations

    """
    ROUTER_SOLICITATION = 720895

    """

    TTL exceeded

    """
    TTL_EXCEEDED = 720896

    """

    Reassembly timeout

    """
    REASSEMBLY_TIMEOUT = 720897

    """

    All time exceeds

    """
    TIME_EXCEEDED = 786431

    """

    Parameter problem

    """
    GENERAL_PARAMETER_PROBLEM = 786432

    """

    Parameter required but not present

    """
    OPTION_MISSING = 786433

    """

    Parameter required but no room

    """
    NO_ROOM_FOR_OPTION = 786434

    """

    All parameter problems

    """
    PARAMETER_PROBLEM = 851967

    """

    Timestamp requests

    """
    TIMESTAMP_REQUEST = 917503

    """

    Timestamp replies

    """
    TIMESTAMP_REPLY = 983039

    """

    Information request

    """
    INFORMATION_REQUEST = 1048575

    """

    Information replies

    """
    INFORMATION_REPLY = 1114111

    """

    Mask requests

    """
    MASK_REQUEST = 1179647

    """

    Mask replies

    """
    MASK_REPLY = 1245183

    """

    Traceroute

    """
    TRACEROUTE = 2031615

    """

    Datagram conversion

    """
    CONVERSION_ERROR = 2097151

    """

    Mobile host redirect

    """
    MOBILE_REDIRECT = 2162687


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclIcmpTypeCodeEnum_Enum']


class Ipv4AclIgmpNumber_Enum(Enum):
    """
    Ipv4AclIgmpNumber_Enum

    Ipv4 acl igmp number

    """

    """

    Host query

    """
    HOST_QUERY = 17

    """

    Host report

    """
    HOST_REPORT = 18

    """

    Distance Vector Multicast Routing Protocol

    """
    DVMRP = 19

    """

    Portocol Independent Multicast

    """
    PIM = 20

    """

    Multicast Trace

    """
    TRACE = 21

    """

    Version 2 report

    """
    V2_REPORT = 22

    """

    Version 2 leave

    """
    V2_LEAVE = 23

    """

    MTrace response

    """
    MTRACE_RESPONSE = 30

    """

    MTrace

    """
    MTRACE = 31

    """

    Version 3 report

    """
    V3_REPORT = 34


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclIgmpNumber_Enum']


class Ipv4AclLoggingEnum_Enum(Enum):
    """
    Ipv4AclLoggingEnum_Enum

    Ipv4 acl logging enum

    """

    """

    Log matches against this entry

    """
    LOG = 1

    """

    Log matches against this entry, including input
    interface

    """
    LOG_INPUT = 2


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclLoggingEnum_Enum']


class Ipv4AclOperatorEnum_Enum(Enum):
    """
    Ipv4AclOperatorEnum_Enum

    Ipv4 acl operator enum

    """

    """

    Match only packets on a given port number

    """
    EQUAL = 1

    """

    Match only packet with a greater port number

    """
    GREATER_THAN = 2

    """

    Match only packet with a lower port number

    """
    LESS_THAN = 3

    """

    Match only packets not on a given port number

    """
    NOT_EQUAL = 4

    """

    Match only packets in the range of port numbers

    """
    RANGE = 5


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclOperatorEnum_Enum']


class Ipv4AclPortNumber_Enum(Enum):
    """
    Ipv4AclPortNumber_Enum

    Ipv4 acl port number

    """

    """

    Match on the 'echo' port number

    """
    ECHO = 7

    """

    Match on the 'discard' port number

    """
    DISCARD = 9

    """

    Match on the 'daytime' port number (TCP/SCTP
    only)

    """
    DAYTIME = 13

    """

    Match on the 'chargen' port number (TCP/SCTP
    only)

    """
    CHAR_GEN = 19

    """

    Match on the FTP data connections port number
    (TCP/SCTP only)

    """
    FTP_DATA = 20

    """

    Match on the 'ftp' port number (TCP/SCTP only)

    """
    FTP = 21

    """

    Match on the 'telnet' port number (TCP/SCTP
    only)

    """
    TELNET = 23

    """

    Match on the 'smtp' port number (TCP/SCTP
    only)

    """
    SMTP = 25

    """

    Match on the 'time' port number

    """
    TIME = 37

    """

    Match on the IEN116 name service port number
    (UDP only)

    """
    NAME_SERVER = 42

    """

    Match on the 'nicname' port number (TCP/SCTP
    only)

    """
    WHO_IS = 43

    """

    Match on the 'tacacs' port number

    """
    TACACS = 49

    """

    Match on the 'dns' port number

    """
    DNS = 53

    """

    Match on the Bootstrap Protocol server port
    number (UDP only)

    """
    BOOT_PS = 67

    """

    Match on the Bootstrap Protocol client port
    number (UDP only)

    """
    BOOT_PC = 68

    """

    Match on the 'tftp' port number (UDP only)

    """
    TFTP = 69

    """

    Match on the 'gopher' port number (TCP/SCTP
    only)

    """
    GOPHER = 70

    """

    Match on the 'finger' port number (TCP/SCTP
    only)

    """
    FINGER = 79

    """

    Match on the 'http' port number (TCP/SCTP
    only)

    """
    WWW = 80

    """

    Match on the NIC hostname server port number
    (TCP/SCTP only)

    """
    HOST_NAME = 101

    """

    Match on the 'pop2' port number (TCP/SCTP
    only)

    """
    POP2 = 109

    """

    Match on the 'pop3' port number (TCP/SCTP
    only)

    """
    POP3 = 110

    """

    Match on the Sun RPC port number

    """
    SUN_RPC = 111

    """

    Match on the 'ident' port number (TCP/SCTP
    only)

    """
    IDENT = 113

    """

    Match on the 'nntp' port number (TCP/SCTP
    only)

    """
    NNTP = 119

    """

    Match on the 'ntp' port number (UDP only)

    """
    NTP = 123

    """

    Match on the NetBIOS name service port number
    (UDP only)

    """
    NET_BIOS_NS = 137

    """

    Match on the NetBIOS datagram service port
    number (UDP only)

    """
    NET_BIOS_DGS = 138

    """

    Match on the NetBIOS session service port
    number (UDP only)

    """
    NET_BIOS_SS = 139

    """

    Match on the 'snmp' port number (UDP only)

    """
    SNMP = 161

    """

    Match on the SNMP traps port number (UDP only)

    """
    SNMP_TRAP = 162

    """

    Match on the 'xdmcp' port number (UDP only)

    """
    XDMCP = 177

    """

    Match on the 'bgp' port number (TCP/SCTP only)

    """
    BGP = 179

    """

    Match on the 'irc' port number (TCP/SCTP only)

    """
    IRC = 194

    """

    Match on the DNSIX security protocol auditing
    port number (UDP only)

    """
    DNSIX = 195

    """

    Match on the mobile IP registration port
    number (UDP only)

    """
    MOBILE_IP = 434

    """

    Match on the PIM Auto\-RP port number

    """
    PIM_AUTO_RP = 496

    """

    Match on the 'isakmp' port number (UDP only)

    """
    ISAKMP = 500

    """

    Match on the port used by TCP/SCTP for 'exec'
    and by UDP for 'biff'

    """
    EXEC_OR_BIFF = 512

    """

    Match on the port used by TCP/SCTP for 'login'
    and by UDP for 'rwho'

    """
    LOGIN_OR_WHO = 513

    """

    Match on the port used by TCP/SCTP for 'rcmd'
    and by UDP for 'syslog'

    """
    CMD_OR_SYSLOG = 514

    """

    Match on the 'lpd' port number (TCP/SCTP only)

    """
    LPD = 515

    """

    Match on the 'talk' port number

    """
    TALK = 517

    """

    Match on the 'rip' port number (UDP only)

    """
    RIP = 520

    """

    Match on the 'uucp' port number (TCP/SCTP
    only)

    """
    UUCP = 540

    """

    Match on the Kerberos login port number
    (TCP/SCTP only)

    """
    KLOGIN = 543

    """

    Match on the Kerberos shell port number
    (TCP/SCTP only)

    """
    KSHELL = 544

    """

    Match on the LDP port

    """
    LDP = 646


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclPortNumber_Enum']


class Ipv4AclPrecedenceNumber_Enum(Enum):
    """
    Ipv4AclPrecedenceNumber_Enum

    Ipv4 acl precedence number

    """

    """

    Match packets with critical precedence

    """
    CRITICAL = 5

    """

    Match packets with flash precedence

    """
    FLASH = 3

    """

    Match packets with flash override precedence

    """
    FLASH_OVERRIDE = 4

    """

    Match packets with immediate precedence

    """
    IMMEDIATE = 2

    """

    Match packets with internetwork control
    precedence

    """
    INTERNET = 6

    """

    Match packets with network control precedence

    """
    NETWORK = 7

    """

    Match packets with priority precedence

    """
    PRIORITY = 1

    """

    Match packets with routine precedence

    """
    ROUTINE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclPrecedenceNumber_Enum']


class Ipv4AclProtocolNumber_Enum(Enum):
    """
    Ipv4AclProtocolNumber_Enum

    Ipv4 acl protocol number

    """

    """

    Any IP protocol

    """
    IP = 0

    """

    Internet Control Message Protocol

    """
    ICMP = 1

    """

    Internet Gateway Message Protocol

    """
    IGMP = 2

    """

    IP in IP tunneling

    """
    IP_IN_IP = 4

    """

    Transport Control Protocol

    """
    TCP = 6

    """

    Cisco's IGRP Routing Protocol

    """
    IGRP = 9

    """

    User Datagram Protocol

    """
    UDP = 17

    """

    Cisco's GRE tunneling

    """
    GRE = 47

    """

    Encapsulation Security Protocol

    """
    ESP = 50

    """

    Authentication Header Protocol

    """
    AHP = 51

    """

    Cisco's EIGRP Routing Protocol

    """
    EIGRP = 88

    """

    OSPF Routing Protocol

    """
    OSPF = 89

    """

    KA9Q NOS Compatible IP over IP tunneling

    """
    NOS = 94

    """

    Protocol Independent Multicast

    """
    PIM = 103

    """

    Payload Compression Protocol

    """
    PCP = 108

    """

    Stream Control Transmission Protocol

    """
    SCTP = 132


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclProtocolNumber_Enum']


class Ipv4AclStatusEnum_Enum(Enum):
    """
    Ipv4AclStatusEnum_Enum

    Ipv4 acl status enum

    """

    """

    Disabled

    """
    DISABLED = 0

    """

    Enabled

    """
    ENABLED = 1


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclStatusEnum_Enum']


class Ipv4AclTcpBitsNumber_Enum(Enum):
    """
    Ipv4AclTcpBitsNumber_Enum

    Ipv4 acl tcp bits number

    """

    """

    Match established connections (0x14)

    """
    ESTABLISHED = 20

    """

    Match on the ACK bit (0x10)

    """
    ACK = 16

    """

    Match on the RST bit (0x04)

    """
    RST = 4

    """

    Match on the FIN bit (0x01)

    """
    FIN = 1

    """

    Match on the PSH bit (0x08)

    """
    PSH = 8

    """

    Match on the SYN bit (0x02)

    """
    SYN = 2

    """

    Match on the URG bit (0x20)

    """
    URG = 32


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclTcpBitsNumber_Enum']


class Ipv4AclTcpMatchOperatorEnum_Enum(Enum):
    """
    Ipv4AclTcpMatchOperatorEnum_Enum

    Ipv4 acl tcp match operator enum

    """

    """

    Match only packet with all the given TCP bits

    """
    MATCH_ALL = 1

    """

    Match only packet with any of the given TCP
    bits

    """
    MATCH_ANY = 3


    @staticmethod
    def _meta_info():
        from ydk.models.ipv4._meta import _Cisco_IOS_XR_ipv4_acl_datatypes as meta
        return meta._meta_table['Ipv4AclTcpMatchOperatorEnum_Enum']



