


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SrmsMiAfEBEnum' : _MetaInfoEnum('SrmsMiAfEBEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper',
        {
            'none':'none',
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-segment-routing-ms-oper', _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper']),
    'SrmsMiFlagEBEnum' : _MetaInfoEnum('SrmsMiFlagEBEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper',
        {
            'false':'false',
            'true':'true',
        }, 'Cisco-IOS-XR-segment-routing-ms-oper', _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper']),
    'SrmsMiSrcEBEnum' : _MetaInfoEnum('SrmsMiSrcEBEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper',
        {
            'none':'none',
            'local':'local',
            'remote':'remote',
        }, 'Cisco-IOS-XR-segment-routing-ms-oper', _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper']),
    'Srms.Mapping.MappingIpv4.MappingMi.Addr' : {
        'meta_info' : _MetaInfoClass('Srms.Mapping.MappingIpv4.MappingMi.Addr',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'SrmsMiAfEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEBEnum', 
                [], [], 
                '''                AF
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'addr',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Mapping.MappingIpv4.MappingMi' : {
        'meta_info' : _MetaInfoClass('Srms.Mapping.MappingIpv4.MappingMi',
            False, 
            [
            _MetaInfoClassMember('addr', REFERENCE_CLASS, 'Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Mapping.MappingIpv4.MappingMi.Addr', 
                [], [], 
                '''                addr
                ''',
                'addr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('area', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Area (OSPF) or Level (ISIS)
                ''',
                'area',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlagEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEBEnum', 
                [], [], 
                '''                Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IP
                ''',
                'ip',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Last IP Prefix
                ''',
                'last_prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-sid-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last SID Index
                ''',
                'last_sid_index',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('router', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Router ID
                ''',
                'router',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SID range
                ''',
                'sid_count',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Starting SID
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('src', REFERENCE_ENUM_CLASS, 'SrmsMiSrcEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEBEnum', 
                [], [], 
                '''                src
                ''',
                'src',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'mapping-mi',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Mapping.MappingIpv4' : {
        'meta_info' : _MetaInfoClass('Srms.Mapping.MappingIpv4',
            False, 
            [
            _MetaInfoClassMember('mapping-mi', REFERENCE_LIST, 'MappingMi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Mapping.MappingIpv4.MappingMi', 
                [], [], 
                '''                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                ''',
                'mapping_mi',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'mapping-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Mapping.MappingIpv6.MappingMi.Addr' : {
        'meta_info' : _MetaInfoClass('Srms.Mapping.MappingIpv6.MappingMi.Addr',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'SrmsMiAfEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEBEnum', 
                [], [], 
                '''                AF
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'addr',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Mapping.MappingIpv6.MappingMi' : {
        'meta_info' : _MetaInfoClass('Srms.Mapping.MappingIpv6.MappingMi',
            False, 
            [
            _MetaInfoClassMember('addr', REFERENCE_CLASS, 'Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Mapping.MappingIpv6.MappingMi.Addr', 
                [], [], 
                '''                addr
                ''',
                'addr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('area', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Area (OSPF) or Level (ISIS)
                ''',
                'area',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlagEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEBEnum', 
                [], [], 
                '''                Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IP
                ''',
                'ip',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Last IP Prefix
                ''',
                'last_prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-sid-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last SID Index
                ''',
                'last_sid_index',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('router', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Router ID
                ''',
                'router',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SID range
                ''',
                'sid_count',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Starting SID
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('src', REFERENCE_ENUM_CLASS, 'SrmsMiSrcEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEBEnum', 
                [], [], 
                '''                src
                ''',
                'src',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'mapping-mi',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Mapping.MappingIpv6' : {
        'meta_info' : _MetaInfoClass('Srms.Mapping.MappingIpv6',
            False, 
            [
            _MetaInfoClassMember('mapping-mi', REFERENCE_LIST, 'MappingMi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Mapping.MappingIpv6.MappingMi', 
                [], [], 
                '''                IP prefix to SID mapping item. It's not possible
                to list all of the IP prefix to SID mappings, as
                the set of valid prefixes could be very large.
                Instead, SID map information must be retrieved
                individually for each prefix of interest.
                ''',
                'mapping_mi',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'mapping-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Mapping' : {
        'meta_info' : _MetaInfoClass('Srms.Mapping',
            False, 
            [
            _MetaInfoClassMember('mapping-ipv4', REFERENCE_CLASS, 'MappingIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Mapping.MappingIpv4', 
                [], [], 
                '''                IPv4 prefix to SID mappings
                ''',
                'mapping_ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('mapping-ipv6', REFERENCE_CLASS, 'MappingIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Mapping.MappingIpv6', 
                [], [], 
                '''                IPv6 prefix to SID mappings
                ''',
                'mapping_ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'SrmsMiAfEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEBEnum', 
                [], [], 
                '''                AF
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'addr',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi',
            False, 
            [
            _MetaInfoClassMember('mi-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Mapping Item ID (0, 1, 2, ...)
                ''',
                'mi_id',
                'Cisco-IOS-XR-segment-routing-ms-oper', True),
            _MetaInfoClassMember('addr', REFERENCE_CLASS, 'Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr', 
                [], [], 
                '''                addr
                ''',
                'addr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('area', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Area (OSPF) or Level (ISIS)
                ''',
                'area',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlagEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEBEnum', 
                [], [], 
                '''                Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Last IP Prefix
                ''',
                'last_prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-sid-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last SID Index
                ''',
                'last_sid_index',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('router', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Router ID
                ''',
                'router',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SID range
                ''',
                'sid_count',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Starting SID
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('src', REFERENCE_ENUM_CLASS, 'SrmsMiSrcEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEBEnum', 
                [], [], 
                '''                src
                ''',
                'src',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-mi',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv4.PolicyIpv4Backup' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv4.PolicyIpv4Backup',
            False, 
            [
            _MetaInfoClassMember('policy-mi', REFERENCE_LIST, 'PolicyMi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi', 
                [], [], 
                '''                Mapping Item
                ''',
                'policy_mi',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-ipv4-backup',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'SrmsMiAfEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEBEnum', 
                [], [], 
                '''                AF
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'addr',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi',
            False, 
            [
            _MetaInfoClassMember('mi-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Mapping Item ID (0, 1, 2, ...)
                ''',
                'mi_id',
                'Cisco-IOS-XR-segment-routing-ms-oper', True),
            _MetaInfoClassMember('addr', REFERENCE_CLASS, 'Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr', 
                [], [], 
                '''                addr
                ''',
                'addr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('area', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Area (OSPF) or Level (ISIS)
                ''',
                'area',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlagEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEBEnum', 
                [], [], 
                '''                Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Last IP Prefix
                ''',
                'last_prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-sid-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last SID Index
                ''',
                'last_sid_index',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('router', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Router ID
                ''',
                'router',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SID range
                ''',
                'sid_count',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Starting SID
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('src', REFERENCE_ENUM_CLASS, 'SrmsMiSrcEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEBEnum', 
                [], [], 
                '''                src
                ''',
                'src',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-mi',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv4.PolicyIpv4Active' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv4.PolicyIpv4Active',
            False, 
            [
            _MetaInfoClassMember('policy-mi', REFERENCE_LIST, 'PolicyMi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi', 
                [], [], 
                '''                Mapping Item
                ''',
                'policy_mi',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-ipv4-active',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv4' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv4',
            False, 
            [
            _MetaInfoClassMember('policy-ipv4-active', REFERENCE_CLASS, 'PolicyIpv4Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv4.PolicyIpv4Active', 
                [], [], 
                '''                IPv4 active policy operational data
                ''',
                'policy_ipv4_active',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('policy-ipv4-backup', REFERENCE_CLASS, 'PolicyIpv4Backup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv4.PolicyIpv4Backup', 
                [], [], 
                '''                IPv4 backup policy operational data
                ''',
                'policy_ipv4_backup',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'SrmsMiAfEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEBEnum', 
                [], [], 
                '''                AF
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'addr',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi',
            False, 
            [
            _MetaInfoClassMember('mi-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Mapping Item ID (0, 1, 2, ...)
                ''',
                'mi_id',
                'Cisco-IOS-XR-segment-routing-ms-oper', True),
            _MetaInfoClassMember('addr', REFERENCE_CLASS, 'Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr', 
                [], [], 
                '''                addr
                ''',
                'addr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('area', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Area (OSPF) or Level (ISIS)
                ''',
                'area',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlagEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEBEnum', 
                [], [], 
                '''                Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Last IP Prefix
                ''',
                'last_prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-sid-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last SID Index
                ''',
                'last_sid_index',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('router', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Router ID
                ''',
                'router',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SID range
                ''',
                'sid_count',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Starting SID
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('src', REFERENCE_ENUM_CLASS, 'SrmsMiSrcEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEBEnum', 
                [], [], 
                '''                src
                ''',
                'src',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-mi',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv6.PolicyIpv6Backup' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv6.PolicyIpv6Backup',
            False, 
            [
            _MetaInfoClassMember('policy-mi', REFERENCE_LIST, 'PolicyMi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi', 
                [], [], 
                '''                Mapping Item
                ''',
                'policy_mi',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-ipv6-backup',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_ENUM_CLASS, 'SrmsMiAfEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiAfEBEnum', 
                [], [], 
                '''                AF
                ''',
                'af',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4
                ''',
                'ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6
                ''',
                'ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'addr',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi',
            False, 
            [
            _MetaInfoClassMember('mi-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Mapping Item ID (0, 1, 2, ...)
                ''',
                'mi_id',
                'Cisco-IOS-XR-segment-routing-ms-oper', True),
            _MetaInfoClassMember('addr', REFERENCE_CLASS, 'Addr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr', 
                [], [], 
                '''                addr
                ''',
                'addr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('area', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Area (OSPF) or Level (ISIS)
                ''',
                'area',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('flag-attached', REFERENCE_ENUM_CLASS, 'SrmsMiFlagEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiFlagEBEnum', 
                [], [], 
                '''                Attached flag
                ''',
                'flag_attached',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-prefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Last IP Prefix
                ''',
                'last_prefix',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('last-sid-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last SID Index
                ''',
                'last_sid_index',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('prefix-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length
                ''',
                'prefix_xr',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('router', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Router ID
                ''',
                'router',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SID range
                ''',
                'sid_count',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('sid-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Starting SID
                ''',
                'sid_start',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('src', REFERENCE_ENUM_CLASS, 'SrmsMiSrcEBEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'SrmsMiSrcEBEnum', 
                [], [], 
                '''                src
                ''',
                'src',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-mi',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv6.PolicyIpv6Active' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv6.PolicyIpv6Active',
            False, 
            [
            _MetaInfoClassMember('policy-mi', REFERENCE_LIST, 'PolicyMi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi', 
                [], [], 
                '''                Mapping Item
                ''',
                'policy_mi',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-ipv6-active',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy.PolicyIpv6' : {
        'meta_info' : _MetaInfoClass('Srms.Policy.PolicyIpv6',
            False, 
            [
            _MetaInfoClassMember('policy-ipv6-active', REFERENCE_CLASS, 'PolicyIpv6Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv6.PolicyIpv6Active', 
                [], [], 
                '''                IPv6 active policy operational data
                ''',
                'policy_ipv6_active',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('policy-ipv6-backup', REFERENCE_CLASS, 'PolicyIpv6Backup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv6.PolicyIpv6Backup', 
                [], [], 
                '''                IPv6 backup policy operational data
                ''',
                'policy_ipv6_backup',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy-ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms.Policy' : {
        'meta_info' : _MetaInfoClass('Srms.Policy',
            False, 
            [
            _MetaInfoClassMember('policy-ipv4', REFERENCE_CLASS, 'PolicyIpv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv4', 
                [], [], 
                '''                IPv4 policy operational data
                ''',
                'policy_ipv4',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('policy-ipv6', REFERENCE_CLASS, 'PolicyIpv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy.PolicyIpv6', 
                [], [], 
                '''                IPv6 policy operational data
                ''',
                'policy_ipv6',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'policy',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
    'Srms' : {
        'meta_info' : _MetaInfoClass('Srms',
            False, 
            [
            _MetaInfoClassMember('mapping', REFERENCE_CLASS, 'Mapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Mapping', 
                [], [], 
                '''                IP prefix to SID mappings
                ''',
                'mapping',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper', 'Srms.Policy', 
                [], [], 
                '''                Policy operational data
                ''',
                'policy',
                'Cisco-IOS-XR-segment-routing-ms-oper', False),
            ],
            'Cisco-IOS-XR-segment-routing-ms-oper',
            'srms',
            _yang_ns._namespaces['Cisco-IOS-XR-segment-routing-ms-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_segment_routing_ms_oper'
        ),
    },
}
_meta_table['Srms.Mapping.MappingIpv4.MappingMi.Addr']['meta_info'].parent =_meta_table['Srms.Mapping.MappingIpv4.MappingMi']['meta_info']
_meta_table['Srms.Mapping.MappingIpv4.MappingMi']['meta_info'].parent =_meta_table['Srms.Mapping.MappingIpv4']['meta_info']
_meta_table['Srms.Mapping.MappingIpv6.MappingMi.Addr']['meta_info'].parent =_meta_table['Srms.Mapping.MappingIpv6.MappingMi']['meta_info']
_meta_table['Srms.Mapping.MappingIpv6.MappingMi']['meta_info'].parent =_meta_table['Srms.Mapping.MappingIpv6']['meta_info']
_meta_table['Srms.Mapping.MappingIpv4']['meta_info'].parent =_meta_table['Srms.Mapping']['meta_info']
_meta_table['Srms.Mapping.MappingIpv6']['meta_info'].parent =_meta_table['Srms.Mapping']['meta_info']
_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi.Addr']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi']['meta_info']
_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup.PolicyMi']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup']['meta_info']
_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi.Addr']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi']['meta_info']
_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active.PolicyMi']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active']['meta_info']
_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Backup']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv4']['meta_info']
_meta_table['Srms.Policy.PolicyIpv4.PolicyIpv4Active']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv4']['meta_info']
_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi.Addr']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi']['meta_info']
_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup.PolicyMi']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup']['meta_info']
_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi.Addr']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi']['meta_info']
_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active.PolicyMi']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active']['meta_info']
_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Backup']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv6']['meta_info']
_meta_table['Srms.Policy.PolicyIpv6.PolicyIpv6Active']['meta_info'].parent =_meta_table['Srms.Policy.PolicyIpv6']['meta_info']
_meta_table['Srms.Policy.PolicyIpv4']['meta_info'].parent =_meta_table['Srms.Policy']['meta_info']
_meta_table['Srms.Policy.PolicyIpv6']['meta_info'].parent =_meta_table['Srms.Policy']['meta_info']
_meta_table['Srms.Mapping']['meta_info'].parent =_meta_table['Srms']['meta_info']
_meta_table['Srms.Policy']['meta_info'].parent =_meta_table['Srms']['meta_info']
