


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SourcePolicyEnum' : _MetaInfoEnum('SourcePolicyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg',
        {
            'vrf':'vrf',
            'rfc':'rfc',
        }, 'Cisco-IOS-XR-ip-icmp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ip-icmp-cfg']),
    'Icmp.IpProtocol.RateLimit.Unreachable' : {
        'meta_info' : _MetaInfoClass('Icmp.IpProtocol.RateLimit.Unreachable',
            False, 
            [
            _MetaInfoClassMember('fragmentation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate Limit of Unreachable DF paclets
                ''',
                'fragmentation',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate Limit of Unreachable ICMP paclets
                ''',
                'rate',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'unreachable',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-icmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg'
        ),
    },
    'Icmp.IpProtocol.RateLimit' : {
        'meta_info' : _MetaInfoClass('Icmp.IpProtocol.RateLimit',
            False, 
            [
            _MetaInfoClassMember('unreachable', REFERENCE_CLASS, 'Unreachable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.IpProtocol.RateLimit.Unreachable', 
                [], [], 
                '''                Set unreachable ICMP packets ratelimit
                ''',
                'unreachable',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'rate-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-icmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg'
        ),
    },
    'Icmp.IpProtocol.Source' : {
        'meta_info' : _MetaInfoClass('Icmp.IpProtocol.Source',
            False, 
            [
            _MetaInfoClassMember('source-address-policy', REFERENCE_ENUM_CLASS, 'SourcePolicyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'SourcePolicyEnum', 
                [], [], 
                '''                Configure Source Address Policy
                ''',
                'source_address_policy',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'source',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-icmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg'
        ),
    },
    'Icmp.IpProtocol' : {
        'meta_info' : _MetaInfoClass('Icmp.IpProtocol',
            False, 
            [
            _MetaInfoClassMember('protocol-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IP Protocol Type; ipv4 or ipv6
                ''',
                'protocol_type',
                'Cisco-IOS-XR-ip-icmp-cfg', True),
            _MetaInfoClassMember('rate-limit', REFERENCE_CLASS, 'RateLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.IpProtocol.RateLimit', 
                [], [], 
                '''                Set ratelimit of ICMP packets
                ''',
                'rate_limit',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            _MetaInfoClassMember('source', REFERENCE_CLASS, 'Source' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.IpProtocol.Source', 
                [], [], 
                '''                IP ICMP Source Address Selection Policy
                ''',
                'source',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'ip-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-icmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg'
        ),
    },
    'Icmp' : {
        'meta_info' : _MetaInfoClass('Icmp',
            False, 
            [
            _MetaInfoClassMember('ip-protocol', REFERENCE_LIST, 'IpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg', 'Icmp.IpProtocol', 
                [], [], 
                '''                IP Protocol Type
                ''',
                'ip_protocol',
                'Cisco-IOS-XR-ip-icmp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-icmp-cfg',
            'icmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-icmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_icmp_cfg'
        ),
    },
}
_meta_table['Icmp.IpProtocol.RateLimit.Unreachable']['meta_info'].parent =_meta_table['Icmp.IpProtocol.RateLimit']['meta_info']
_meta_table['Icmp.IpProtocol.RateLimit']['meta_info'].parent =_meta_table['Icmp.IpProtocol']['meta_info']
_meta_table['Icmp.IpProtocol.Source']['meta_info'].parent =_meta_table['Icmp.IpProtocol']['meta_info']
_meta_table['Icmp.IpProtocol']['meta_info'].parent =_meta_table['Icmp']['meta_info']
