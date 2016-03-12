


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AclTcpflagsOperator_Enum' : _MetaInfoEnum('AclTcpflagsOperator_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'match-none':'MATCH_NONE',
            'match-all':'MATCH_ALL',
            'match-any-old':'MATCH_ANY_OLD',
            'match-any':'MATCH_ANY',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'AclPortOperator_Enum' : _MetaInfoEnum('AclPortOperator_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'none':'NONE',
            'eq':'EQ',
            'gt':'GT',
            'lt':'LT',
            'neq':'NEQ',
            'range':'RANGE',
            'onebyte':'ONEBYTE',
            'twobytes':'TWOBYTES',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'AclAce1_Enum' : _MetaInfoEnum('AclAce1_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'normal':'NORMAL',
            'remark':'REMARK',
            'abf':'ABF',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'AclPortOperator_Enum' : _MetaInfoEnum('AclPortOperator_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'none':'NONE',
            'eq':'EQ',
            'gt':'GT',
            'lt':'LT',
            'neq':'NEQ',
            'range':'RANGE',
            'onebyte':'ONEBYTE',
            'twobytes':'TWOBYTES',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'BagAclNh_Enum' : _MetaInfoEnum('BagAclNh_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'nexthop-none':'NEXTHOP_NONE',
            'nexthop-default':'NEXTHOP_DEFAULT',
            'nexthop':'NEXTHOP',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'AclPortOperator_Enum' : _MetaInfoEnum('AclPortOperator_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'none':'NONE',
            'eq':'EQ',
            'gt':'GT',
            'lt':'LT',
            'neq':'NEQ',
            'range':'RANGE',
            'onebyte':'ONEBYTE',
            'twobytes':'TWOBYTES',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'AclAction_Enum' : _MetaInfoEnum('AclAction_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'deny':'DENY',
            'permit':'PERMIT',
            'encrypt':'ENCRYPT',
            'bypass':'BYPASS',
            'fallthrough':'FALLTHROUGH',
            'invalid':'INVALID',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'BagAclNhStatus_Enum' : _MetaInfoEnum('BagAclNhStatus_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'not-present':'NOT_PRESENT',
            'unknown':'UNKNOWN',
            'down':'DOWN',
            'up':'UP',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'AclLog_Enum' : _MetaInfoEnum('AclLog_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'log-none':'LOG_NONE',
            'log':'LOG',
            'log-input':'LOG_INPUT',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'AclAce1_Enum' : _MetaInfoEnum('AclAce1_Enum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper',
        {
            'normal':'NORMAL',
            'remark':'REMARK',
            'abf':'ABF',
        }, 'Cisco-IOS-XR-ipv4-acl-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper']),
    'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Next Hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BagAclNh_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'BagAclNh_Enum', 
                [], [], 
                '''                the next-hop type
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'hw-next-hop-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo',
            False, 
            [
            _MetaInfoClassMember('is-acl-next-hop-exist', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The nexthop exist
                ''',
                'is_acl_next_hop_exist',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The next hop
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'BagAclNhStatus_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'BagAclNhStatus_Enum', 
                [], [], 
                '''                The next hop status
                ''',
                'status',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Track name
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'next-hop-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483646)], [], 
                '''                ACLEntry Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv4-acl-oper', True),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('capture', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Capture option, TRUE if enabled
                ''',
                'capture',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('counter-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Counter name
                ''',
                'counter_name',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('destination-address-mask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination mask
                ''',
                'destination_address_mask',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('destination-operator', REFERENCE_ENUM_CLASS, 'AclPortOperator_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator_Enum', 
                [], [], 
                '''                Destination operator
                ''',
                'destination_operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('destination-port1', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Destination port 1
                ''',
                'destination_port1',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('destination-port2', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Destination port 2
                ''',
                'destination_port2',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('destination-port-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination port object-group
                ''',
                'destination_port_group',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('destination-prefix-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination prefix object-group
                ''',
                'destination_prefix_group',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                DSCP or DSCP range start
                ''',
                'dscp',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('dscp2', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                DSCP Range End
                ''',
                'dscp2',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('dscp-operator', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                DSCP Operator
                ''',
                'dscp_operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('dscp-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DSCP present
                ''',
                'dscp_present',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('dynamic', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is dynamic ACE
                ''',
                'dynamic',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('fragments', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Fragments
                ''',
                'fragments',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'AclAction_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclAction_Enum', 
                [], [], 
                '''                Permit/deny
                ''',
                'grant',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('hits', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Number of hits
                ''',
                'hits',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('hw-next-hop-info', REFERENCE_CLASS, 'HwNextHopInfo' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo', 
                [], [], 
                '''                HW Next hop info
                ''',
                'hw_next_hop_info',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('is-icmp-off', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if ICMP off
                ''',
                'is_icmp_off',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('item-type', REFERENCE_ENUM_CLASS, 'AclAce1_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclAce1_Enum', 
                [], [], 
                '''                ACE type (acl, remark)
                ''',
                'item_type',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('log-option', REFERENCE_ENUM_CLASS, 'AclLog_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclLog_Enum', 
                [], [], 
                '''                Log option
                ''',
                'log_option',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('next-hop-info', REFERENCE_LIST, 'NextHopInfo' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo', 
                [], [], 
                '''                Next hop info
                ''',
                'next_hop_info',
                'Cisco-IOS-XR-ipv4-acl-oper', False, max_elements=3),
            _MetaInfoClassMember('next-hop-type', REFERENCE_ENUM_CLASS, 'BagAclNh_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'BagAclNh_Enum', 
                [], [], 
                '''                Next hop type
                ''',
                'next_hop_type',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('no-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No stats
                ''',
                'no_stats',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('port-length1', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Port length 1
                ''',
                'port_length1',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('port-length2', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Port length 2
                ''',
                'port_length2',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('port-length-operator', REFERENCE_ENUM_CLASS, 'AclPortOperator_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator_Enum', 
                [], [], 
                '''                Port length operator
                ''',
                'port_length_operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Precedence
                ''',
                'precedence',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('precedence-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Precedence present
                ''',
                'precedence_present',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                IPv4 protocol type
                ''',
                'protocol',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remark String
                ''',
                'remark',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('sequence', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ACLE sequence number
                ''',
                'sequence',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('sorce-operator', REFERENCE_ENUM_CLASS, 'AclPortOperator_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator_Enum', 
                [], [], 
                '''                Deprecated by Source operator
                ''',
                'sorce_operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('sorce-port1', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Deprecated by SourcePort1
                ''',
                'sorce_port1',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('sorce-port2', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Deprecated by SourcePort2
                ''',
                'sorce_port2',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source mask
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('source-operator', REFERENCE_ENUM_CLASS, 'AclPortOperator_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator_Enum', 
                [], [], 
                '''                Source operator
                ''',
                'source_operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('source-port1', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Source port 1
                ''',
                'source_port1',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('source-port2', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Source port 2
                ''',
                'source_port2',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('source-port-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source port object-group
                ''',
                'source_port_group',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('source-prefix-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source prefix object-group
                ''',
                'source_prefix_group',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('tcp-flags', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                TCP flags
                ''',
                'tcp_flags',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('tcp-flags-mask', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                TCP flags mask
                ''',
                'tcp_flags_mask',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('tcp-flags-operator', REFERENCE_ENUM_CLASS, 'AclTcpflagsOperator_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclTcpflagsOperator_Enum', 
                [], [], 
                '''                TCP flags operator
                ''',
                'tcp_flags_operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('ttl1', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                TTL 1
                ''',
                'ttl1',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('ttl2', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                TTL 2
                ''',
                'ttl2',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('ttl-operator', REFERENCE_ENUM_CLASS, 'AclPortOperator_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator_Enum', 
                [], [], 
                '''                TTL operator
                ''',
                'ttl_operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'access-list-sequence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences',
            False, 
            [
            _MetaInfoClassMember('access-list-sequence', REFERENCE_LIST, 'AccessListSequence' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence', 
                [], [], 
                '''                Sequence Number of an access list entry
                ''',
                'access_list_sequence',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'access-list-sequences',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Accesses.Access',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Access List
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-acl-oper', True),
            _MetaInfoClassMember('access-list-sequences', REFERENCE_CLASS, 'AccessListSequences' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences', 
                [], [], 
                '''                Table of all the SequenceNumbers per access
                list
                ''',
                'access_list_sequences',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'access',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Accesses' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Accesses',
            False, 
            [
            _MetaInfoClassMember('access', REFERENCE_LIST, 'Access' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Accesses.Access', 
                [], [], 
                '''                Name of the Access List
                ''',
                'access',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'accesses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483646)], [], 
                '''                Sequence Number of the prefix list entry
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv4-acl-oper', True),
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ACL Name
                ''',
                'acl_name',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'AclAction_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclAction_Enum', 
                [], [], 
                '''                Grant value permit/deny 
                ''',
                'grant',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('hits', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of hits
                ''',
                'hits',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('item-type', REFERENCE_ENUM_CLASS, 'AclAce1_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclAce1_Enum', 
                [], [], 
                '''                ACE type (prefix, remark)
                ''',
                'item_type',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('maximum-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Maximum length
                ''',
                'maximum_length',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('minimum-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Min length
                ''',
                'minimum_length',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('operator', REFERENCE_ENUM_CLASS, 'AclPortOperator_Enum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'AclPortOperator_Enum', 
                [], [], 
                '''                Port Operator
                ''',
                'operator',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Prefix length 
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remark String
                ''',
                'remark',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('sequence', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ACLE sequence number
                ''',
                'sequence',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'prefix-list-sequence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences',
            False, 
            [
            _MetaInfoClassMember('prefix-list-sequence', REFERENCE_LIST, 'PrefixListSequence' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence', 
                [], [], 
                '''                Sequence Number of a prefix list entry
                ''',
                'prefix_list_sequence',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'prefix-list-sequences',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-ipv4-acl-oper', True),
            _MetaInfoClassMember('prefix-list-sequences', REFERENCE_CLASS, 'PrefixListSequences' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences', 
                [], [], 
                '''                Table of all the SequenceNumbers per prefix
                list
                ''',
                'prefix_list_sequences',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Prefixes' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Prefixes',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix', 
                [], [], 
                '''                Name of the prefix list
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Usages.Usage' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Usages.Usage',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the access list
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('application-id', REFERENCE_ENUM_CLASS, 'AclUsageAppIdEnum_Enum' , 'ydk.models.common.Cisco_IOS_XR_common_acl_datatypes', 'AclUsageAppIdEnum_Enum', 
                [], [], 
                '''                Application ID
                ''',
                'application_id',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node where access list is applied
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('usage-details', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Usage Statistics Details
                ''',
                'usage_details',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'usage',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager.Usages' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager.Usages',
            False, 
            [
            _MetaInfoClassMember('usage', REFERENCE_LIST, 'Usage' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Usages.Usage', 
                [], [], 
                '''                Usage statistics of an access list at a node
                ''',
                'usage',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'usages',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.AccessListManager' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.AccessListManager',
            False, 
            [
            _MetaInfoClassMember('accesses', REFERENCE_CLASS, 'Accesses' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Accesses', 
                [], [], 
                '''                Access listL class displaying Usage and Entries
                ''',
                'accesses',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('prefixes', REFERENCE_CLASS, 'Prefixes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Prefixes', 
                [], [], 
                '''                Table of prefix lists
                ''',
                'prefixes',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('usages', REFERENCE_CLASS, 'Usages' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager.Usages', 
                [], [], 
                '''                Table of Usage statistics of access lists at
                different nodes
                ''',
                'usages',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'access-list-manager',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.AccessListSummary.Details' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.AccessListSummary.Details',
            False, 
            [
            _MetaInfoClassMember('current-configured-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured aces
                ''',
                'current_configured_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured acls
                ''',
                'current_configured_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable aces
                ''',
                'current_max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable acls
                ''',
                'current_max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable aces
                ''',
                'default_max_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable acls
                ''',
                'default_max_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable aces
                ''',
                'max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable acls
                ''',
                'max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.AccessListSummary' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.AccessListSummary',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.AccessListSummary.Details', 
                [], [], 
                '''                Details containing the resource limits of the
                access lists
                ''',
                'details',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'access-list-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.Details' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.Details',
            False, 
            [
            _MetaInfoClassMember('current-configured-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured aces
                ''',
                'current_configured_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured acls
                ''',
                'current_configured_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable aces
                ''',
                'current_max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable acls
                ''',
                'current_max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable aces
                ''',
                'default_max_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable acls
                ''',
                'default_max_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable aces
                ''',
                'max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable acls
                ''',
                'max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the Access List
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-acl-oper', True),
            _MetaInfoClassMember('current-configured-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured aces
                ''',
                'current_configured_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured acls
                ''',
                'current_configured_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable aces
                ''',
                'current_max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable acls
                ''',
                'current_max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable aces
                ''',
                'default_max_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable acls
                ''',
                'default_max_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable aces
                ''',
                'max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable acls
                ''',
                'max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'oor-access',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.OorAccesses' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.OorAccesses',
            False, 
            [
            _MetaInfoClassMember('oor-access', REFERENCE_LIST, 'OorAccess' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess', 
                [], [], 
                '''                Resource occupation details for a particular
                access list
                ''',
                'oor_access',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'oor-accesses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of a prefix list
                ''',
                'prefix_list_name',
                'Cisco-IOS-XR-ipv4-acl-oper', True),
            _MetaInfoClassMember('current-configured-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured aces
                ''',
                'current_configured_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured acls
                ''',
                'current_configured_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable aces
                ''',
                'current_max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable acls
                ''',
                'current_max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable aces
                ''',
                'default_max_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable acls
                ''',
                'default_max_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable aces
                ''',
                'max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable acls
                ''',
                'max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'oor-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.OorPrefixes' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.OorPrefixes',
            False, 
            [
            _MetaInfoClassMember('oor-prefix', REFERENCE_LIST, 'OorPrefix' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix', 
                [], [], 
                '''                Resource occupation details for a particular
                prefix list
                ''',
                'oor_prefix',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'oor-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details',
            False, 
            [
            _MetaInfoClassMember('current-configured-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured aces
                ''',
                'current_configured_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-configured-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current configured acls
                ''',
                'current_configured_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable aces
                ''',
                'current_max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('current-max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Current max configurable acls
                ''',
                'current_max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable aces
                ''',
                'default_max_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('default-max-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                default max configurable acls
                ''',
                'default_max_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-es', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable aces
                ''',
                'max_configurable_ac_es',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('max-configurable-ac-ls', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                max configurable acls
                ''',
                'max_configurable_ac_ls',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor.PrefixListSummary' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor.PrefixListSummary',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details', 
                [], [], 
                '''                Summary Detail of the prefix list Resource
                Utilisation
                ''',
                'details',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'prefix-list-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList.Oor' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList.Oor',
            False, 
            [
            _MetaInfoClassMember('access-list-summary', REFERENCE_CLASS, 'AccessListSummary' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.AccessListSummary', 
                [], [], 
                '''                Resource limits pertaining to access lists only
                ''',
                'access_list_summary',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.Details', 
                [], [], 
                '''                Details of the Overall Out Of Resources Limits
                ''',
                'details',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('oor-accesses', REFERENCE_CLASS, 'OorAccesses' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.OorAccesses', 
                [], [], 
                '''                Resource occupation details for access lists
                ''',
                'oor_accesses',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('oor-prefixes', REFERENCE_CLASS, 'OorPrefixes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.OorPrefixes', 
                [], [], 
                '''                Resource occupation details for prefix lists
                ''',
                'oor_prefixes',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('prefix-list-summary', REFERENCE_CLASS, 'PrefixListSummary' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor.PrefixListSummary', 
                [], [], 
                '''                Summary of the prefix Lists resource
                utilization
                ''',
                'prefix_list_summary',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
    'Ipv4AclAndPrefixList' : {
        'meta_info' : _MetaInfoClass('Ipv4AclAndPrefixList',
            False, 
            [
            _MetaInfoClassMember('access-list-manager', REFERENCE_CLASS, 'AccessListManager' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.AccessListManager', 
                [], [], 
                '''                Access list manager containing access lists and
                prefix lists
                ''',
                'access_list_manager',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            _MetaInfoClassMember('oor', REFERENCE_CLASS, 'Oor' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper', 'Ipv4AclAndPrefixList.Oor', 
                [], [], 
                '''                Out Of Resources, Limits to the resources
                allocatable
                ''',
                'oor',
                'Cisco-IOS-XR-ipv4-acl-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-acl-oper',
            'ipv4-acl-and-prefix-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-acl-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_acl_oper'
        ),
    },
}
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.HwNextHopInfo']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence.NextHopInfo']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences.AccessListSequence']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access.AccessListSequences']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses.Access']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences.PrefixListSequence']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix.PrefixListSequences']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes.Prefix']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Usages.Usage']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager.Usages']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Accesses']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Prefixes']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager.Usages']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.AccessListManager']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.AccessListSummary.Details']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor.AccessListSummary']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.OorAccesses.OorAccess']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor.OorAccesses']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.OorPrefixes.OorPrefix']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor.OorPrefixes']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.PrefixListSummary.Details']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor.PrefixListSummary']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.AccessListSummary']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.Details']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.OorAccesses']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.OorPrefixes']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor.PrefixListSummary']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList.Oor']['meta_info']
_meta_table['Ipv4AclAndPrefixList.AccessListManager']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList']['meta_info']
_meta_table['Ipv4AclAndPrefixList.Oor']['meta_info'].parent =_meta_table['Ipv4AclAndPrefixList']['meta_info']
