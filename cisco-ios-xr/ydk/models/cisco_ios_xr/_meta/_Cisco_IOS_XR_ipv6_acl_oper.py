


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AclAce1Enum' : _MetaInfoEnum('AclAce1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'normal':'normal',
            'remark':'remark',
            'abf':'abf',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'BagAclNhStatusEnum' : _MetaInfoEnum('BagAclNhStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'not-present':'not_present',
            'unknown':'unknown',
            'down':'down',
            'up':'up',
            'max':'max',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclPortOperatorEnum' : _MetaInfoEnum('AclPortOperatorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'none':'none',
            'eq':'eq',
            'gt':'gt',
            'lt':'lt',
            'neq':'neq',
            'range':'range',
            'onebyte':'onebyte',
            'twobytes':'twobytes',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclActionEnum' : _MetaInfoEnum('AclActionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'deny':'deny',
            'permit':'permit',
            'encrypt':'encrypt',
            'bypass':'bypass',
            'fallthrough':'fallthrough',
            'invalid':'invalid',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclTcpflagsOperatorEnum' : _MetaInfoEnum('AclTcpflagsOperatorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'match-none':'match_none',
            'match-all':'match_all',
            'match-any-old':'match_any_old',
            'match-any':'match_any',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'BagAclNhAtStatusEnum' : _MetaInfoEnum('BagAclNhAtStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'unknown':'unknown',
            'up':'up',
            'down':'down',
            'not-present':'not_present',
            'max':'max',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclPortOperatorEnum' : _MetaInfoEnum('AclPortOperatorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'none':'none',
            'eq':'eq',
            'gt':'gt',
            'lt':'lt',
            'neq':'neq',
            'range':'range',
            'onebyte':'onebyte',
            'twobytes':'twobytes',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclLogEnum' : _MetaInfoEnum('AclLogEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'log-none':'log_none',
            'log':'log',
            'log-input':'log_input',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclPortOperatorEnum' : _MetaInfoEnum('AclPortOperatorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'none':'none',
            'eq':'eq',
            'gt':'gt',
            'lt':'lt',
            'neq':'neq',
            'range':'range',
            'onebyte':'onebyte',
            'twobytes':'twobytes',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'BagAclNhEnum' : _MetaInfoEnum('BagAclNhEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'nexthop-none':'nexthop_none',
            'nexthop-default':'nexthop_default',
            'nexthop':'nexthop',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclAce1Enum' : _MetaInfoEnum('AclAce1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'normal':'normal',
            'remark':'remark',
            'abf':'abf',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'AclPortOperatorEnum' : _MetaInfoEnum('AclPortOperatorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper',
        {
            'none':'none',
            'eq':'eq',
            'gt':'gt',
            'lt':'lt',
            'neq':'neq',
            'range':'range',
            'onebyte':'onebyte',
            'twobytes':'twobytes',
        }, 'Cisco-IOS-XR-ipv6-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper']),
    'Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                Sequence Number of the prefix list entry
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv6-acl-oper', True),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('hits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of hits
                ''',
                'hits',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-ace-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ACLE sequence number
                ''',
                'is_ace_sequence_number',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-ace-type', REFERENCE_ENUM_CLASS, 'AclAce1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclAce1Enum', 
                [], [], 
                '''                ACE type (acl, remark)
                ''',
                'is_ace_type',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-address-in-numbers', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix
                ''',
                'is_address_in_numbers',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-address-mask-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length 
                ''',
                'is_address_mask_length',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-comment-for-entry', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remark String
                ''',
                'is_comment_for_entry',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-length-operator', REFERENCE_ENUM_CLASS, 'AclPortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperatorEnum', 
                [], [], 
                '''                Port Operator
                ''',
                'is_length_operator',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-packet-allow-or-deny', REFERENCE_ENUM_CLASS, 'AclActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclActionEnum', 
                [], [], 
                '''                Grant value permit/deny 
                ''',
                'is_packet_allow_or_deny',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-packet-maximum-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum length
                ''',
                'is_packet_maximum_length',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-packet-minimum-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Min length
                ''',
                'is_packet_minimum_length',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'prefix-list-sequence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences',
            False, 
            [
            _MetaInfoClassMember('prefix-list-sequence', REFERENCE_LIST, 'PrefixListSequence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence', 
                [], [], 
                '''                Sequence Number of a prefix list entry
                ''',
                'prefix_list_sequence',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'prefix-list-sequences',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-ipv6-acl-oper', True),
            _MetaInfoClassMember('prefix-list-sequences', REFERENCE_CLASS, 'PrefixListSequences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences', 
                [], [], 
                '''                Table of all the SequenceNumbers per prefix
                list
                ''',
                'prefix_list_sequences',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Prefixes' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Prefixes',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix', 
                [], [], 
                '''                Name of the prefix list
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Usages.Usage' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Usages.Usage',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the ACL
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('application-id', REFERENCE_ENUM_CLASS, 'AclUsageAppIdEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_common_acl_datatypes', 'AclUsageAppIdEnumEnum', 
                [], [], 
                '''                Application ID
                ''',
                'application_id',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node where ACL is applied
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('usage-details', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Usage Statistics Details
                ''',
                'usage_details',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'usage',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Usages' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Usages',
            False, 
            [
            _MetaInfoClassMember('usage', REFERENCE_LIST, 'Usage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Usages.Usage', 
                [], [], 
                '''                Usage statistics of an ACL at a node
                ''',
                'usage',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'usages',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table ID
                ''',
                'table_id',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BagAclNhEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNhEnum', 
                [], [], 
                '''                The next-hop type
                ''',
                'type',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Vrf Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'hw-next-hop-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo',
            False, 
            [
            _MetaInfoClassMember('acl-nh-exist', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The nexthop exist
                ''',
                'acl_nh_exist',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('at-status', REFERENCE_ENUM_CLASS, 'BagAclNhAtStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNhAtStatusEnum', 
                [], [], 
                '''                The next hop at status
                ''',
                'at_status',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The next hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'BagAclNhStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNhStatusEnum', 
                [], [], 
                '''                The next hop status
                ''',
                'status',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Track name
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Vrf Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'next-hop-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf',
            False, 
            [
            _MetaInfoClassMember('udf-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDF Mask
                ''',
                'udf_mask',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('udf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 17)], [], 
                '''                UDF Name
                ''',
                'udf_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('udf-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                UDF Value
                ''',
                'udf_value',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'udf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                ACL entry sequence number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv6-acl-oper', True),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('capture', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Capture option, TRUE if enabled
                ''',
                'capture',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('counter-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Counter name
                ''',
                'counter_name',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('destination-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination Mask
                ''',
                'destination_mask',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('destination-port-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination port object-group
                ''',
                'destination_port_group',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('destination-prefix-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination prefix object-group
                ''',
                'destination_prefix_group',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('hits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                hits
                ''',
                'hits',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('hw-next-hop-info', REFERENCE_CLASS, 'HwNextHopInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo', 
                [], [], 
                '''                HW Next hop info
                ''',
                'hw_next_hop_info',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-ace-sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ACLE sequence number
                ''',
                'is_ace_sequence_number',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-ace-type', REFERENCE_ENUM_CLASS, 'AclAce1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclAce1Enum', 
                [], [], 
                '''                ACE type (acl, remark)
                ''',
                'is_ace_type',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-comment-for-entry', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IsCommentForEntry
                ''',
                'is_comment_for_entry',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-destination-address-in-numbers', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IsDestinationAddressInNumbers
                ''',
                'is_destination_address_in_numbers',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-destination-address-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsDestinationAddressPrefixLength
                ''',
                'is_destination_address_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-destination-operator', REFERENCE_ENUM_CLASS, 'AclPortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperatorEnum', 
                [], [], 
                '''                eq, ne, lt, etc...
                ''',
                'is_destination_operator',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-destination-port1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsDestinationPort1
                ''',
                'is_destination_port1',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-destination-port2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsDestinationPort2
                ''',
                'is_destination_port2',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-dscp-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                IsDSCPPresent
                ''',
                'is_dscp_present',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-dscp-valu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsDSCPValu
                ''',
                'is_dscp_valu',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsFlowId
                ''',
                'is_flow_id',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-header-matches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Match if routing header is presant
                ''',
                'is_header_matches',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-icmp-message-off', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Don't generate the icmp message
                ''',
                'is_icmp_message_off',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-ipv6-protocol2-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Protocol 2
                ''',
                'is_ipv6_protocol2_type',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-ipv6-protocol-type', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Protocol 1
                ''',
                'is_ipv6_protocol_type',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-log-option', REFERENCE_ENUM_CLASS, 'AclLogEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclLogEnum', 
                [], [], 
                '''                IsLogOption
                ''',
                'is_log_option',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-packet-allow-or-deny', REFERENCE_ENUM_CLASS, 'AclActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclActionEnum', 
                [], [], 
                '''                Grant value permit/deny 
                ''',
                'is_packet_allow_or_deny',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-packet-length-end', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsPacketLengthEnd
                ''',
                'is_packet_length_end',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-packet-length-operator', REFERENCE_ENUM_CLASS, 'AclPortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperatorEnum', 
                [], [], 
                '''                Match if routing header is presant
                ''',
                'is_packet_length_operator',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-packet-length-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsPacketLengthStart
                ''',
                'is_packet_length_start',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-precedence-present', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                IsPrecedencePresent
                ''',
                'is_precedence_present',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-precedence-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                range from 0 to 7
                ''',
                'is_precedence_value',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-protocol-operator', REFERENCE_ENUM_CLASS, 'AclPortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperatorEnum', 
                [], [], 
                '''                Protocol operator
                ''',
                'is_protocol_operator',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-source-address-in-numbers', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IsSourceAddressInNumbers
                ''',
                'is_source_address_in_numbers',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-source-address-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsSourceAddressPrefixLength
                ''',
                'is_source_address_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-source-operator', REFERENCE_ENUM_CLASS, 'AclPortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperatorEnum', 
                [], [], 
                '''                eq, ne, lt, etc...
                ''',
                'is_source_operator',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-source-port1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsSourcePort1
                ''',
                'is_source_port1',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-source-port2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsSourcePort2
                ''',
                'is_source_port2',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-tcp-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsTCPBits
                ''',
                'is_tcp_bits',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-tcp-bits-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsTCPBitsMask
                ''',
                'is_tcp_bits_mask',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-tcp-bits-operator', REFERENCE_ENUM_CLASS, 'AclTcpflagsOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclTcpflagsOperatorEnum', 
                [], [], 
                '''                IsTCPBitsOperator
                ''',
                'is_tcp_bits_operator',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-time-to-live-end', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsTimeToLiveEnd
                ''',
                'is_time_to_live_end',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-time-to-live-operator', REFERENCE_ENUM_CLASS, 'AclPortOperatorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'AclPortOperatorEnum', 
                [], [], 
                '''                IsTimeToLiveOperator
                ''',
                'is_time_to_live_operator',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-time-to-live-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IsTimeToLiveStart
                ''',
                'is_time_to_live_start',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('next-hop-info', REFERENCE_LIST, 'NextHopInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo', 
                [], [], 
                '''                Next hop info
                ''',
                'next_hop_info',
                'Cisco-IOS-XR-ipv6-acl-oper', False, max_elements=3),
            _MetaInfoClassMember('next-hop-type', REFERENCE_ENUM_CLASS, 'BagAclNhEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'BagAclNhEnum', 
                [], [], 
                '''                Next hop type
                ''',
                'next_hop_type',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('no-stats', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                no stats
                ''',
                'no_stats',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set qos-group
                ''',
                'qos_group',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('sequence-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence String
                ''',
                'sequence_str',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('source-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Mask
                ''',
                'source_mask',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('source-port-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source port object-group
                ''',
                'source_port_group',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('source-prefix-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source prefix object-group
                ''',
                'source_prefix_group',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('udf', REFERENCE_LIST, 'Udf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf', 
                [], [], 
                '''                UDF
                ''',
                'udf',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('undetermined-transport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Undetermined transport option, TRUE if enabled
                ''',
                'undetermined_transport',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'access-list-sequence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences',
            False, 
            [
            _MetaInfoClassMember('access-list-sequence', REFERENCE_LIST, 'AccessListSequence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence', 
                [], [], 
                '''                Sequence number of an ACL entry
                ''',
                'access_list_sequence',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'access-list-sequences',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Accesses.Access',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the Access List
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv6-acl-oper', True),
            _MetaInfoClassMember('access-list-sequences', REFERENCE_CLASS, 'AccessListSequences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences', 
                [], [], 
                '''                Table of all the sequence numbers per ACL
                ''',
                'access_list_sequences',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'access',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager.Accesses' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager.Accesses',
            False, 
            [
            _MetaInfoClassMember('access', REFERENCE_LIST, 'Access' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Accesses.Access', 
                [], [], 
                '''                Name of the Access List
                ''',
                'access',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'accesses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.AccessListManager' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.AccessListManager',
            False, 
            [
            _MetaInfoClassMember('accesses', REFERENCE_CLASS, 'Accesses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Accesses', 
                [], [], 
                '''                ACL class displaying Usage and Entries
                ''',
                'accesses',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('prefixes', REFERENCE_CLASS, 'Prefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Prefixes', 
                [], [], 
                '''                Table of prefix lists
                ''',
                'prefixes',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('usages', REFERENCE_CLASS, 'Usages' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager.Usages', 
                [], [], 
                '''                Table of Usage statistics of ACLs at different
                nodes
                ''',
                'usages',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'access-list-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.Details' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.Details',
            False, 
            [
            _MetaInfoClassMember('is-current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured acls
                ''',
                'is_current_configured_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-configured-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured aces
                ''',
                'is_current_configured_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable aces
                ''',
                'is_current_maximum_configurable_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-acls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable acls
                ''',
                'is_current_maximum_configurable_acls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable aces
                ''',
                'is_default_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable acls
                ''',
                'is_default_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable aces
                ''',
                'is_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable acls
                ''',
                'is_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details',
            False, 
            [
            _MetaInfoClassMember('is-current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured acls
                ''',
                'is_current_configured_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-configured-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured aces
                ''',
                'is_current_configured_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable aces
                ''',
                'is_current_maximum_configurable_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-acls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable acls
                ''',
                'is_current_maximum_configurable_acls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable aces
                ''',
                'is_default_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable acls
                ''',
                'is_default_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable aces
                ''',
                'is_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable acls
                ''',
                'is_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.PrefixListSummary' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.PrefixListSummary',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details', 
                [], [], 
                '''                Summary Detail of the prefix list Resource
                Utilisation
                ''',
                'details',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'prefix-list-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the Access List
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv6-acl-oper', True),
            _MetaInfoClassMember('is-current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured acls
                ''',
                'is_current_configured_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-configured-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured aces
                ''',
                'is_current_configured_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable aces
                ''',
                'is_current_maximum_configurable_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-acls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable acls
                ''',
                'is_current_maximum_configurable_acls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable aces
                ''',
                'is_default_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable acls
                ''',
                'is_default_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable aces
                ''',
                'is_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable acls
                ''',
                'is_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'oor-access',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.OorAccesses' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.OorAccesses',
            False, 
            [
            _MetaInfoClassMember('oor-access', REFERENCE_LIST, 'OorAccess' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess', 
                [], [], 
                '''                Resource occupation details for a particular
                ACL
                ''',
                'oor_access',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'oor-accesses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of a prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-ipv6-acl-oper', True),
            _MetaInfoClassMember('is-current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured acls
                ''',
                'is_current_configured_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-configured-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured aces
                ''',
                'is_current_configured_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable aces
                ''',
                'is_current_maximum_configurable_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-acls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable acls
                ''',
                'is_current_maximum_configurable_acls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable aces
                ''',
                'is_default_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable acls
                ''',
                'is_default_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable aces
                ''',
                'is_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable acls
                ''',
                'is_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'oor-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.OorPrefixes' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.OorPrefixes',
            False, 
            [
            _MetaInfoClassMember('oor-prefix', REFERENCE_LIST, 'OorPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix', 
                [], [], 
                '''                Resource occupation details for a particular
                prefix list
                ''',
                'oor_prefix',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'oor-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.AccessListSummary.Details' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.AccessListSummary.Details',
            False, 
            [
            _MetaInfoClassMember('is-current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured acls
                ''',
                'is_current_configured_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-configured-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current configured aces
                ''',
                'is_current_configured_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-aces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable aces
                ''',
                'is_current_maximum_configurable_aces',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-current-maximum-configurable-acls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current max configurable acls
                ''',
                'is_current_maximum_configurable_acls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable aces
                ''',
                'is_default_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-default-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                default max configurable acls
                ''',
                'is_default_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable aces
                ''',
                'is_maximum_configurable_ac_es',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('is-maximum-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                max configurable acls
                ''',
                'is_maximum_configurable_ac_ls',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor.AccessListSummary' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor.AccessListSummary',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.AccessListSummary.Details', 
                [], [], 
                '''                Details containing the resource limits of the
                ACLs
                ''',
                'details',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'access-list-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList.Oor' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Oor',
            False, 
            [
            _MetaInfoClassMember('access-list-summary', REFERENCE_CLASS, 'AccessListSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.AccessListSummary', 
                [], [], 
                '''                Resource Limits pertaining to ACLs only
                ''',
                'access_list_summary',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.Details', 
                [], [], 
                '''                Details of the overall out of resource limit
                ''',
                'details',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('oor-accesses', REFERENCE_CLASS, 'OorAccesses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.OorAccesses', 
                [], [], 
                '''                Resource occupation details for ACLs
                ''',
                'oor_accesses',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('oor-prefixes', REFERENCE_CLASS, 'OorPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.OorPrefixes', 
                [], [], 
                '''                Resource occupation details for prefix lists
                ''',
                'oor_prefixes',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('prefix-list-summary', REFERENCE_CLASS, 'PrefixListSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor.PrefixListSummary', 
                [], [], 
                '''                Summary of the prefix Lists resource
                utilization
                ''',
                'prefix_list_summary',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
    'Ipv6AclAndPrefixList' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList',
            False, 
            [
            _MetaInfoClassMember('access-list-manager', REFERENCE_CLASS, 'AccessListManager' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.AccessListManager', 
                [], [], 
                '''                AccessListManager containing ACLs and prefix
                lists
                ''',
                'access_list_manager',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            _MetaInfoClassMember('oor', REFERENCE_CLASS, 'Oor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper', 'Ipv6AclAndPrefixList.Oor', 
                [], [], 
                '''                Out Of Resources, Limits to the resources
                allocatable
                ''',
                'oor',
                'Cisco-IOS-XR-ipv6-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-oper',
            'ipv6-acl-and-prefix-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_oper'
        ),
    },
}
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes.Prefix']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Usages.Usage']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Usages']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.Udf']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses.Access']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Prefixes']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Usages']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager.Accesses']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.AccessListManager']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.PrefixListSummary.Details']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor.PrefixListSummary']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.OorAccesses.OorAccess']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor.OorAccesses']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.OorPrefixes.OorPrefix']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor.OorPrefixes']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.AccessListSummary.Details']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor.AccessListSummary']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.Details']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.PrefixListSummary']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.OorAccesses']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.OorPrefixes']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor.AccessListSummary']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv6AclAndPrefixList.AccessListManager']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Oor']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
