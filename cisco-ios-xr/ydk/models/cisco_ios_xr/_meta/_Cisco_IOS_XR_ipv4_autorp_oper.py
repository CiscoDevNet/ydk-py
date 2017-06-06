


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AutorpProtocolModeEnum' : _MetaInfoEnum('AutorpProtocolModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper',
        {
            'sparse':'sparse',
            'bidirectional':'bidirectional',
        }, 'Cisco-IOS-XR-ipv4-autorp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper']),
    'AutoRp.Standby.CandidateRp.Traffic' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.CandidateRp.Traffic',
            False, 
            [
            _MetaInfoClassMember('active-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets sent in active role
                ''',
                'active_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('standby-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped in send path in
                standby role
                ''',
                'standby_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.CandidateRp.Rps.Rp' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.CandidateRp.Rps.Rp',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL Name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('announce-period', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Announce Period
                ''',
                'announce_period',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('candidate-rp-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Candidate RP IP Address
                ''',
                'candidate_rp_address',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('protocol-mode', REFERENCE_ENUM_CLASS, 'AutoRpProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes', 'AutoRpProtocolModeEnum', 
                [], [], 
                '''                Protocol Mode
                ''',
                'protocol_mode',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('protocol-mode-xr', REFERENCE_ENUM_CLASS, 'AutorpProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolModeEnum', 
                [], [], 
                '''                Protocol Mode
                ''',
                'protocol_mode_xr',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.CandidateRp.Rps' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.CandidateRp.Rps',
            False, 
            [
            _MetaInfoClassMember('rp', REFERENCE_LIST, 'Rp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.CandidateRp.Rps.Rp', 
                [], [], 
                '''                AutoRP Candidate RP Entry
                ''',
                'rp',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rps',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.CandidateRp' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.CandidateRp',
            False, 
            [
            _MetaInfoClassMember('rps', REFERENCE_CLASS, 'Rps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.CandidateRp.Rps', 
                [], [], 
                '''                AutoRP Candidate RP Table
                ''',
                'rps',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.CandidateRp.Traffic', 
                [], [], 
                '''                AutoRP Candidate Traffic Counters
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'candidate-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.MappingAgent.Traffic' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.MappingAgent.Traffic',
            False, 
            [
            _MetaInfoClassMember('active-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received in active role
                ''',
                'active_received_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('active-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets sent in active role
                ''',
                'active_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('standby-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped in receive path in
                standby role
                ''',
                'standby_received_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('standby-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped in send path in
                standby role
                ''',
                'standby_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range',
            False, 
            [
            _MetaInfoClassMember('check-point-object-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Checkpoint object id
                ''',
                'check_point_object_id',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('create-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Source of the entry
                ''',
                'create_type',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('is-advertised', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this entry advertised ?
                ''',
                'is_advertised',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix of the range
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length of the range
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('protocol-mode', REFERENCE_ENUM_CLASS, 'AutorpProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolModeEnum', 
                [], [], 
                '''                Protocol Mode
                ''',
                'protocol_mode',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Uptime in seconds
                ''',
                'uptime',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.MappingAgent.RpAddresses.RpAddress' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.MappingAgent.RpAddresses.RpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RP Address
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-autorp-oper', True),
            _MetaInfoClassMember('expiry-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time for expiration in seconds
                ''',
                'expiry_time',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('pim-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PIM version of the CRP
                ''',
                'pim_version',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range', 
                [], [], 
                '''                Array of ranges
                ''',
                'range',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('rp-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Candidate-RP address
                ''',
                'rp_address_xr',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.MappingAgent.RpAddresses' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.MappingAgent.RpAddresses',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_LIST, 'RpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.MappingAgent.RpAddresses.RpAddress', 
                [], [], 
                '''                AutoRP Mapping Agent Entry
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.MappingAgent.Summary' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.MappingAgent.Summary',
            False, 
            [
            _MetaInfoClassMember('cache-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of group to RP mapping entries in the
                cache
                ''',
                'cache_count',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('cache-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum group to RP mapping entries allowed
                ''',
                'cache_limit',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('is-maximum-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is maximum enforcement disabled ?
                ''',
                'is_maximum_disabled',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby.MappingAgent' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby.MappingAgent',
            False, 
            [
            _MetaInfoClassMember('rp-addresses', REFERENCE_CLASS, 'RpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.MappingAgent.RpAddresses', 
                [], [], 
                '''                AutoRP Mapping Agent Table Entries
                ''',
                'rp_addresses',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.MappingAgent.Summary', 
                [], [], 
                '''                AutoRP Mapping Agent Summary Information
                ''',
                'summary',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.MappingAgent.Traffic', 
                [], [], 
                '''                AutoRP Mapping Agent Traffic Counters
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'mapping-agent',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Standby' : {
        'meta_info' : _MetaInfoClass('AutoRp.Standby',
            False, 
            [
            _MetaInfoClassMember('candidate-rp', REFERENCE_CLASS, 'CandidateRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.CandidateRp', 
                [], [], 
                '''                AutoRP Candidate RP
                ''',
                'candidate_rp',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('mapping-agent', REFERENCE_CLASS, 'MappingAgent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby.MappingAgent', 
                [], [], 
                '''                AutoRP Mapping Agent Table
                ''',
                'mapping_agent',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'standby',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.CandidateRp.Traffic' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.CandidateRp.Traffic',
            False, 
            [
            _MetaInfoClassMember('active-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets sent in active role
                ''',
                'active_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('standby-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped in send path in
                standby role
                ''',
                'standby_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.CandidateRp.Rps.Rp' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.CandidateRp.Rps.Rp',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL Name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('announce-period', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Announce Period
                ''',
                'announce_period',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('candidate-rp-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Candidate RP IP Address
                ''',
                'candidate_rp_address',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('protocol-mode', REFERENCE_ENUM_CLASS, 'AutoRpProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes', 'AutoRpProtocolModeEnum', 
                [], [], 
                '''                Protocol Mode
                ''',
                'protocol_mode',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('protocol-mode-xr', REFERENCE_ENUM_CLASS, 'AutorpProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolModeEnum', 
                [], [], 
                '''                Protocol Mode
                ''',
                'protocol_mode_xr',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                TTL
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.CandidateRp.Rps' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.CandidateRp.Rps',
            False, 
            [
            _MetaInfoClassMember('rp', REFERENCE_LIST, 'Rp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.CandidateRp.Rps.Rp', 
                [], [], 
                '''                AutoRP Candidate RP Entry
                ''',
                'rp',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rps',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.CandidateRp' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.CandidateRp',
            False, 
            [
            _MetaInfoClassMember('rps', REFERENCE_CLASS, 'Rps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.CandidateRp.Rps', 
                [], [], 
                '''                AutoRP Candidate RP Table
                ''',
                'rps',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.CandidateRp.Traffic', 
                [], [], 
                '''                AutoRP Candidate Traffic Counters
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'candidate-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.MappingAgent.Traffic' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.MappingAgent.Traffic',
            False, 
            [
            _MetaInfoClassMember('active-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets received in active role
                ''',
                'active_received_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('active-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets sent in active role
                ''',
                'active_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('standby-received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped in receive path in
                standby role
                ''',
                'standby_received_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('standby-sent-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped in send path in
                standby role
                ''',
                'standby_sent_packets',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range',
            False, 
            [
            _MetaInfoClassMember('check-point-object-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Checkpoint object id
                ''',
                'check_point_object_id',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('create-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Source of the entry
                ''',
                'create_type',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('is-advertised', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this entry advertised ?
                ''',
                'is_advertised',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix of the range
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Prefix length of the range
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('protocol-mode', REFERENCE_ENUM_CLASS, 'AutorpProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutorpProtocolModeEnum', 
                [], [], 
                '''                Protocol Mode
                ''',
                'protocol_mode',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Uptime in seconds
                ''',
                'uptime',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.MappingAgent.RpAddresses.RpAddress' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.MappingAgent.RpAddresses.RpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RP Address
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-autorp-oper', True),
            _MetaInfoClassMember('expiry-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time for expiration in seconds
                ''',
                'expiry_time',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('pim-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PIM version of the CRP
                ''',
                'pim_version',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range', 
                [], [], 
                '''                Array of ranges
                ''',
                'range',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('rp-address-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Candidate-RP address
                ''',
                'rp_address_xr',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.MappingAgent.RpAddresses' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.MappingAgent.RpAddresses',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_LIST, 'RpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.MappingAgent.RpAddresses.RpAddress', 
                [], [], 
                '''                AutoRP Mapping Agent Entry
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.MappingAgent.Summary' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.MappingAgent.Summary',
            False, 
            [
            _MetaInfoClassMember('cache-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of group to RP mapping entries in the
                cache
                ''',
                'cache_count',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('cache-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum group to RP mapping entries allowed
                ''',
                'cache_limit',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('is-maximum-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is maximum enforcement disabled ?
                ''',
                'is_maximum_disabled',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active.MappingAgent' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active.MappingAgent',
            False, 
            [
            _MetaInfoClassMember('rp-addresses', REFERENCE_CLASS, 'RpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.MappingAgent.RpAddresses', 
                [], [], 
                '''                AutoRP Mapping Agent Table Entries
                ''',
                'rp_addresses',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.MappingAgent.Summary', 
                [], [], 
                '''                AutoRP Mapping Agent Summary Information
                ''',
                'summary',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.MappingAgent.Traffic', 
                [], [], 
                '''                AutoRP Mapping Agent Traffic Counters
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'mapping-agent',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp.Active' : {
        'meta_info' : _MetaInfoClass('AutoRp.Active',
            False, 
            [
            _MetaInfoClassMember('candidate-rp', REFERENCE_CLASS, 'CandidateRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.CandidateRp', 
                [], [], 
                '''                AutoRP Candidate RP
                ''',
                'candidate_rp',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('mapping-agent', REFERENCE_CLASS, 'MappingAgent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active.MappingAgent', 
                [], [], 
                '''                AutoRP Mapping Agent Table
                ''',
                'mapping_agent',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
    'AutoRp' : {
        'meta_info' : _MetaInfoClass('AutoRp',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Active', 
                [], [], 
                '''                Active Process
                ''',
                'active',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            _MetaInfoClassMember('standby', REFERENCE_CLASS, 'Standby' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper', 'AutoRp.Standby', 
                [], [], 
                '''                Standby Process
                ''',
                'standby',
                'Cisco-IOS-XR-ipv4-autorp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-autorp-oper',
            'auto-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-autorp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_oper'
        ),
    },
}
_meta_table['AutoRp.Standby.CandidateRp.Rps.Rp']['meta_info'].parent =_meta_table['AutoRp.Standby.CandidateRp.Rps']['meta_info']
_meta_table['AutoRp.Standby.CandidateRp.Traffic']['meta_info'].parent =_meta_table['AutoRp.Standby.CandidateRp']['meta_info']
_meta_table['AutoRp.Standby.CandidateRp.Rps']['meta_info'].parent =_meta_table['AutoRp.Standby.CandidateRp']['meta_info']
_meta_table['AutoRp.Standby.MappingAgent.RpAddresses.RpAddress.Range']['meta_info'].parent =_meta_table['AutoRp.Standby.MappingAgent.RpAddresses.RpAddress']['meta_info']
_meta_table['AutoRp.Standby.MappingAgent.RpAddresses.RpAddress']['meta_info'].parent =_meta_table['AutoRp.Standby.MappingAgent.RpAddresses']['meta_info']
_meta_table['AutoRp.Standby.MappingAgent.Traffic']['meta_info'].parent =_meta_table['AutoRp.Standby.MappingAgent']['meta_info']
_meta_table['AutoRp.Standby.MappingAgent.RpAddresses']['meta_info'].parent =_meta_table['AutoRp.Standby.MappingAgent']['meta_info']
_meta_table['AutoRp.Standby.MappingAgent.Summary']['meta_info'].parent =_meta_table['AutoRp.Standby.MappingAgent']['meta_info']
_meta_table['AutoRp.Standby.CandidateRp']['meta_info'].parent =_meta_table['AutoRp.Standby']['meta_info']
_meta_table['AutoRp.Standby.MappingAgent']['meta_info'].parent =_meta_table['AutoRp.Standby']['meta_info']
_meta_table['AutoRp.Active.CandidateRp.Rps.Rp']['meta_info'].parent =_meta_table['AutoRp.Active.CandidateRp.Rps']['meta_info']
_meta_table['AutoRp.Active.CandidateRp.Traffic']['meta_info'].parent =_meta_table['AutoRp.Active.CandidateRp']['meta_info']
_meta_table['AutoRp.Active.CandidateRp.Rps']['meta_info'].parent =_meta_table['AutoRp.Active.CandidateRp']['meta_info']
_meta_table['AutoRp.Active.MappingAgent.RpAddresses.RpAddress.Range']['meta_info'].parent =_meta_table['AutoRp.Active.MappingAgent.RpAddresses.RpAddress']['meta_info']
_meta_table['AutoRp.Active.MappingAgent.RpAddresses.RpAddress']['meta_info'].parent =_meta_table['AutoRp.Active.MappingAgent.RpAddresses']['meta_info']
_meta_table['AutoRp.Active.MappingAgent.Traffic']['meta_info'].parent =_meta_table['AutoRp.Active.MappingAgent']['meta_info']
_meta_table['AutoRp.Active.MappingAgent.RpAddresses']['meta_info'].parent =_meta_table['AutoRp.Active.MappingAgent']['meta_info']
_meta_table['AutoRp.Active.MappingAgent.Summary']['meta_info'].parent =_meta_table['AutoRp.Active.MappingAgent']['meta_info']
_meta_table['AutoRp.Active.CandidateRp']['meta_info'].parent =_meta_table['AutoRp.Active']['meta_info']
_meta_table['AutoRp.Active.MappingAgent']['meta_info'].parent =_meta_table['AutoRp.Active']['meta_info']
_meta_table['AutoRp.Standby']['meta_info'].parent =_meta_table['AutoRp']['meta_info']
_meta_table['AutoRp.Active']['meta_info'].parent =_meta_table['AutoRp']['meta_info']
