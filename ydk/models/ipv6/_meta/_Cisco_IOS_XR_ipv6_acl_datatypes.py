


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'Ipv6AclTcpMatchOperatorEnumEnum' : _MetaInfoEnum('Ipv6AclTcpMatchOperatorEnumEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'match-all':'MATCH_ALL',
            'match-any':'MATCH_ANY',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclIcmpTypeCodeEnumEnum' : _MetaInfoEnum('Ipv6AclIcmpTypeCodeEnumEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'administratively-prohibited':'ADMINISTRATIVELY_PROHIBITED',
            'host-unreachable':'HOST_UNREACHABLE',
            'port-unreachable':'PORT_UNREACHABLE',
            'unreachable':'UNREACHABLE',
            'reassembly-timeout':'REASSEMBLY_TIMEOUT',
            'time-exceeded':'TIME_EXCEEDED',
            'option-missing':'OPTION_MISSING',
            'no-room-for-option':'NO_ROOM_FOR_OPTION',
            'parameter-problem':'PARAMETER_PROBLEM',
            'echo':'ECHO',
            'echo-reply':'ECHO_REPLY',
            'router-solicitation':'ROUTER_SOLICITATION',
            'router-advertisement':'ROUTER_ADVERTISEMENT',
            'redirect':'REDIRECT',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclProtocolNumberEnum' : _MetaInfoEnum('Ipv6AclProtocolNumberEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'ip':'IP',
            'icmp':'ICMP',
            'igmp':'IGMP',
            'ip-in-ip':'IP_IN_IP',
            'tcp':'TCP',
            'igrp':'IGRP',
            'udp':'UDP',
            'gre':'GRE',
            'esp':'ESP',
            'ahp':'AHP',
            'eigrp':'EIGRP',
            'ospf':'OSPF',
            'nos':'NOS',
            'pim':'PIM',
            'pcp':'PCP',
            'sctp':'SCTP',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6PrefixMatchMinLengthEnum' : _MetaInfoEnum('Ipv6PrefixMatchMinLengthEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'match-min-length':'MATCH_MIN_LENGTH',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclGrantEnumEnum' : _MetaInfoEnum('Ipv6AclGrantEnumEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'deny':'DENY',
            'permit':'PERMIT',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6PrefixMatchMaxLengthEnum' : _MetaInfoEnum('Ipv6PrefixMatchMaxLengthEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'match-max-length':'MATCH_MAX_LENGTH',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclPrecedenceNumberEnum' : _MetaInfoEnum('Ipv6AclPrecedenceNumberEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'critical':'CRITICAL',
            'flash':'FLASH',
            'flash-override':'FLASH_OVERRIDE',
            'immediate':'IMMEDIATE',
            'internet':'INTERNET',
            'network':'NETWORK',
            'priority':'PRIORITY',
            'routine':'ROUTINE',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclOperatorEnumEnum' : _MetaInfoEnum('Ipv6AclOperatorEnumEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'equal':'EQUAL',
            'greater-than':'GREATER_THAN',
            'less-than':'LESS_THAN',
            'not-equal':'NOT_EQUAL',
            'range':'RANGE',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclDscpNumberEnum' : _MetaInfoEnum('Ipv6AclDscpNumberEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'default':'DEFAULT',
            'af11':'AF11',
            'af12':'AF12',
            'af13':'AF13',
            'af21':'AF21',
            'af22':'AF22',
            'af23':'AF23',
            'af31':'AF31',
            'af32':'AF32',
            'af33':'AF33',
            'af41':'AF41',
            'af42':'AF42',
            'af43':'AF43',
            'cs1':'CS1',
            'cs2':'CS2',
            'cs3':'CS3',
            'cs4':'CS4',
            'cs5':'CS5',
            'cs6':'CS6',
            'cs7':'CS7',
            'ef':'EF',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6PrefixMatchExactLengthEnum' : _MetaInfoEnum('Ipv6PrefixMatchExactLengthEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'match-exact-length':'MATCH_EXACT_LENGTH',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclPortNumberEnum' : _MetaInfoEnum('Ipv6AclPortNumberEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'echo':'ECHO',
            'discard':'DISCARD',
            'daytime':'DAYTIME',
            'char-gen':'CHAR_GEN',
            'ftp-data':'FTP_DATA',
            'ftp':'FTP',
            'telnet':'TELNET',
            'smtp':'SMTP',
            'time':'TIME',
            'name-server':'NAME_SERVER',
            'who-is':'WHO_IS',
            'tacacs':'TACACS',
            'dns':'DNS',
            'boot-ps':'BOOT_PS',
            'boot-pc':'BOOT_PC',
            'tftp':'TFTP',
            'gopher':'GOPHER',
            'finger':'FINGER',
            'www':'WWW',
            'host-name':'HOST_NAME',
            'pop2':'POP2',
            'pop3':'POP3',
            'sun-rpc':'SUN_RPC',
            'ident':'IDENT',
            'nntp':'NNTP',
            'ntp':'NTP',
            'net-bios-ns':'NET_BIOS_NS',
            'net-bios-dgs':'NET_BIOS_DGS',
            'net-bios-ss':'NET_BIOS_SS',
            'snmp':'SNMP',
            'snmp-trap':'SNMP_TRAP',
            'xdmcp':'XDMCP',
            'bgp':'BGP',
            'irc':'IRC',
            'dnsix':'DNSIX',
            'mobile-ip':'MOBILE_IP',
            'pim-auto-rp':'PIM_AUTO_RP',
            'isakmp':'ISAKMP',
            'exec-or-biff':'EXEC_OR_BIFF',
            'login-or-who':'LOGIN_OR_WHO',
            'cmd-or-syslog':'CMD_OR_SYSLOG',
            'lpd':'LPD',
            'talk':'TALK',
            'rip':'RIP',
            'uucp':'UUCP',
            'klogin':'KLOGIN',
            'kshell':'KSHELL',
            'ldp':'LDP',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclLoggingEnumEnum' : _MetaInfoEnum('Ipv6AclLoggingEnumEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'log':'LOG',
            'log-input':'LOG_INPUT',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclTypeEnumEnum' : _MetaInfoEnum('Ipv6AclTypeEnumEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'acl':'ACL',
            'prefix-list':'PREFIX_LIST',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclStatusEnumEnum' : _MetaInfoEnum('Ipv6AclStatusEnumEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'disabled':'DISABLED',
            'enabled':'ENABLED',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
    'Ipv6AclTcpBitsNumberEnum' : _MetaInfoEnum('Ipv6AclTcpBitsNumberEnum', 'ydk.models.ipv6.Cisco_IOS_XR_ipv6_acl_datatypes',
        {
            'established':'ESTABLISHED',
            'ack':'ACK',
            'rst':'RST',
            'fin':'FIN',
            'psh':'PSH',
            'syn':'SYN',
            'urg':'URG',
        }, 'Cisco-IOS-XR-ipv6-acl-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-datatypes']),
}
