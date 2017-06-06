


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AclPortTypeEnum' : _MetaInfoEnum('AclPortTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_acl',
        {
            'biff':'biff',
            'bootpc':'bootpc',
            'bootps':'bootps',
            'discard':'discard',
            'dnsix':'dnsix',
            'domain':'domain',
            'echo':'echo',
            'isakmp':'isakmp',
            'mobile-ip':'mobile_ip',
            'nameserver':'nameserver',
            'netbios-dgm':'netbios_dgm',
            'netbios-ns':'netbios_ns',
            'netbios-ss':'netbios_ss',
            'non500-isakmp':'non500_isakmp',
            'ntp':'ntp',
            'pim-auto-rp':'pim_auto_rp',
            'rip':'rip',
            'ripv6':'ripv6',
            'snmp':'snmp',
            'snmptrap':'snmptrap',
            'sunrpc':'sunrpc',
            'syslog':'syslog',
            'tacacs':'tacacs',
            'talk':'talk',
            'tftp':'tftp',
            'time':'time',
            'who':'who',
            'xdmcp':'xdmcp',
            'bgp':'bgp',
            'chargen':'chargen',
            'cmd':'cmd',
            'connectedapps-plain':'connectedapps_plain',
            'connectedapps-tls':'connectedapps_tls',
            'daytime':'daytime',
            'exec':'exec_',
            'finger':'finger',
            'ftp':'ftp',
            'ftp-data':'ftp_data',
            'gopher':'gopher',
            'hostname':'hostname',
            'ident':'ident',
            'irc':'irc',
            'klogin':'klogin',
            'kshell':'kshell',
            'login':'login',
            'lpd':'lpd',
            'msrpc':'msrpc',
            'nntp':'nntp',
            'pop2':'pop2',
            'pop3':'pop3',
            'smtp':'smtp',
            'telnet':'telnet',
            'uucp':'uucp',
            'whois':'whois',
            'www':'www',
        }, 'Cisco-IOS-XE-acl', _yang_ns._namespaces['Cisco-IOS-XE-acl']),
}
