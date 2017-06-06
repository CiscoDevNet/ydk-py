


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NextHopTypeEnum' : _MetaInfoEnum('NextHopTypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg',
        {
            'none-next-hop':'none_next_hop',
            'regular-next-hop':'regular_next_hop',
            'default-next-hop':'default_next_hop',
        }, 'Cisco-IOS-XR-ipv6-acl-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg']),
    'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                Sequence number of prefix list
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('exact-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                If exact prefix length matching specified,
                set the length of prefix to be matched
                ''',
                'exact_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'Ipv6AclGrantEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclGrantEnumEnum', 
                [], [], 
                '''                Whether to forward or drop packets matching
                the prefix list
                ''',
                'grant',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('ipv6-address-as-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The IPv6 address if entered  with the
                ZoneMutually exclusive with Prefix and
                PrefixMask
                ''',
                'ipv6_address_as_string',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('match-exact-length', REFERENCE_ENUM_CLASS, 'Ipv6PrefixMatchExactLengthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchExactLengthEnum', 
                [], [], 
                '''                Set to perform an exact prefix length match.
                Item is mutually exclusive with minimum and
                maximum length match items
                ''',
                'match_exact_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('match-max-length', REFERENCE_ENUM_CLASS, 'Ipv6PrefixMatchMaxLengthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchMaxLengthEnum', 
                [], [], 
                '''                Set to perform a maximum length prefix match
                .  Item is mutually exclusive with exact
                length match item
                ''',
                'match_max_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('match-min-length', REFERENCE_ENUM_CLASS, 'Ipv6PrefixMatchMinLengthEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6PrefixMatchMinLengthEnum', 
                [], [], 
                '''                Set to perform a minimum length prefix match
                .  Item is mutually exclusive with exact
                length match item
                ''',
                'match_min_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('max-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                If maximum length prefix matching specified,
                set the maximum length of prefix to be
                matched
                ''',
                'max_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('min-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                If minimum length prefix matching specified,
                set the minimum length of prefix to be
                matched
                ''',
                'min_prefix_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address prefix to match
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('prefix-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                MaskLength of IPv6 address prefix
                ''',
                'prefix_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Comments or a description for the prefix
                list.  Item is mutually exclusive with all
                others in the object
                ''',
                'remark',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv6 Zone if entered  with the
                IPV6AddressMutually exclusive with Prefix
                and PrefixMask
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefix-list-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries',
            False, 
            [
            _MetaInfoClassMember('prefix-list-entry', REFERENCE_LIST, 'PrefixListEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry', 
                [], [], 
                '''                A prefix list entry; either a description
                (remark) or a prefix to match against
                ''',
                'prefix_list_entry',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefix-list-entries',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Prefixes.Prefix' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes.Prefix',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of a prefix list
                ''',
                'name',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('prefix-list-entries', REFERENCE_CLASS, 'PrefixListEntries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries', 
                [], [], 
                '''                Sequence of entries forming a prefix list
                ''',
                'prefix_list_entries',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Prefixes' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Prefixes',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes.Prefix', 
                [], [], 
                '''                Name of a prefix list
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.LogUpdate' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.LogUpdate',
            False, 
            [
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Log update rate (log messages per second)
                ''',
                'rate',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Log update threshold (number of hits)
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'log-update',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Source IPv6 address, leave unspecified
                if inputting as IPv6 address with wildcarding.
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Source address mask. Either
                source-wild-card-bits or source-mask is.
                supported, not both. Leave unspecified.
                for any.
                ''',
                'source_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-wild-card-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Wildcard bits to apply to source-address
                (if specified), leave unspecified for no
                wildcarding.
                ''',
                'source_wild_card_bits',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'source-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork',
            False, 
            [
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination IPv6 address, leave unspecified
                if inputting as IPv6 address with 
                wildcarding.
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Destination address mask. Either
                destination-wild-card-bits or destination-mask.
                is supported, not both. Leave unspecified
                for any.
                ''',
                'destination_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-wild-card-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Wildcard bits to apply to destination 
                destination-address (if specified), 
                leave unspecified for no wildcarding.
                ''',
                'destination_wild_card_bits',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'destination-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort',
            False, 
            [
            _MetaInfoClassMember('first-source-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First source port for comparison, 
                leave unspecified if source port comparison is
                not to be performed.
                ''',
                'first_source_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('first-source-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumberEnum', 
                        [], [], 
                        '''                        First source port for comparison, 
                        leave unspecified if source port comparison is
                        not to be performed.
                        ''',
                        'first_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('first-source-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        First source port for comparison, 
                        leave unspecified if source port comparison is
                        not to be performed.
                        ''',
                        'first_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('second-source-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Second source port for comparion, 
                leave unspecified if source port comparison is
                not to be performed.
                ''',
                'second_source_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('second-source-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumberEnum', 
                        [], [], 
                        '''                        Second source port for comparion, 
                        leave unspecified if source port comparison is
                        not to be performed.
                        ''',
                        'second_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('second-source-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        Second source port for comparion, 
                        leave unspecified if source port comparison is
                        not to be performed.
                        ''',
                        'second_source_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('source-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnumEnum', 
                [], [], 
                '''                Source comparison operator. Leave unspecified if
                no source port comparison is to be done.
                ''',
                'source_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'source-port',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort',
            False, 
            [
            _MetaInfoClassMember('destination-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnumEnum', 
                [], [], 
                '''                Destination comparison operator. Leave 
                unspecified if no destination port comparison 
                is to be done.
                ''',
                'destination_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('first-destination-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First destination port for comparison, leave 
                unspecified if destination port comparison is
                not to be performed.
                ''',
                'first_destination_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('first-destination-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumberEnum', 
                        [], [], 
                        '''                        First destination port for comparison, leave 
                        unspecified if destination port comparison is
                        not to be performed.
                        ''',
                        'first_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('first-destination-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        First destination port for comparison, leave 
                        unspecified if destination port comparison is
                        not to be performed.
                        ''',
                        'first_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('second-destination-port', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Second destination port for comparion, leave 
                unspecified if destination port comparison is
                not to be performed.
                ''',
                'second_destination_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('second-destination-port', REFERENCE_ENUM_CLASS, 'Ipv6AclPortNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPortNumberEnum', 
                        [], [], 
                        '''                        Second destination port for comparion, leave 
                        unspecified if destination port comparison is
                        not to be performed.
                        ''',
                        'second_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('second-destination-port', ATTRIBUTE, 'int' , None, None, 
                        [('0', '65535')], [], 
                        '''                        Second destination port for comparion, leave 
                        unspecified if destination port comparison is
                        not to be performed.
                        ''',
                        'second_destination_port',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'destination-port',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp',
            False, 
            [
            _MetaInfoClassMember('icmp-type-code', REFERENCE_ENUM_CLASS, 'Ipv6AclIcmpTypeCodeEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclIcmpTypeCodeEnumEnum', 
                [], [], 
                '''                Well known ICMP message code types to match, 
                leave unspecified if ICMP message code type 
                comparion is not to be performed.
                ''',
                'icmp_type_code',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'icmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp',
            False, 
            [
            _MetaInfoClassMember('tcp-bits', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TCP bits to match. Leave unspecified if 
                comparison of TCP bits is not required.
                ''',
                'tcp_bits',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('tcp-bits', REFERENCE_ENUM_CLASS, 'Ipv6AclTcpBitsNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclTcpBitsNumberEnum', 
                        [], [], 
                        '''                        TCP bits to match. Leave unspecified if 
                        comparison of TCP bits is not required.
                        ''',
                        'tcp_bits',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('tcp-bits', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TCP bits to match. Leave unspecified if 
                        comparison of TCP bits is not required.
                        ''',
                        'tcp_bits',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('tcp-bits-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TCP bits mask to use for flexible TCP matching.
                Leave unspecified if it is not required.
                ''',
                'tcp_bits_mask',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('tcp-bits-mask', REFERENCE_ENUM_CLASS, 'Ipv6AclTcpBitsNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclTcpBitsNumberEnum', 
                        [], [], 
                        '''                        TCP bits mask to use for flexible TCP matching.
                        Leave unspecified if it is not required.
                        ''',
                        'tcp_bits_mask',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('tcp-bits-mask', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TCP bits mask to use for flexible TCP matching.
                        Leave unspecified if it is not required.
                        ''',
                        'tcp_bits_mask',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('tcp-bits-match-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclTcpMatchOperatorEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclTcpMatchOperatorEnumEnum', 
                [], [], 
                '''                TCP Bits match operator. Leave unspecified if 
                flexible comparison of TCP bits is not 
                required.
                ''',
                'tcp_bits_match_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'tcp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength',
            False, 
            [
            _MetaInfoClassMember('packet-length-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Maximum packet length for comparion, leave 
                unspecified if packet length comparison is not
                to be performed or if only the minimum packet 
                length should be considered.
                ''',
                'packet_length_max',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('packet-length-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum packet length for comparison, leave 
                unspecified if packet length comparison is not
                to be performed or if only the maximum packet
                length should be considered.
                ''',
                'packet_length_min',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('packet-length-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnumEnum', 
                [], [], 
                '''                Packet length operator applicable if packet 
                length is to be compared. Leave unspecified if
                no Packet length comparison is to be done.
                ''',
                'packet_length_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'packet-length',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive',
            False, 
            [
            _MetaInfoClassMember('time-to-live-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Maximum TTL for comparion, leave unspecified if
                TTL comparison is not to be performed or if only
                the minimum TTL should be considered.
                ''',
                'time_to_live_max',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('time-to-live-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TTL value for comparison OR Minimum TTL value 
                for TTL range comparision, leave unspecified if
                TTL classification is not required.
                ''',
                'time_to_live_min',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('time-to-live-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnumEnum', 
                [], [], 
                '''                TTL operator is applicable if TTL is to be 
                compared. Leave unspecified if TTL 
                classification is not required.
                ''',
                'time_to_live_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'time-to-live',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address of the next-hop.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object tracking name for the next-hop.
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The VRF name of the next-hop.
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop-1',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address of the next-hop.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object tracking name for the next-hop.
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The VRF name of the next-hop.
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop-2',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3',
            False, 
            [
            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The IPv6 address of the next-hop.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object tracking name for the next-hop.
                ''',
                'track_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The VRF name of the next-hop.
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop-3',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop',
            False, 
            [
            _MetaInfoClassMember('next-hop-1', REFERENCE_CLASS, 'NextHop1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1', 
                [], [], 
                '''                The first next-hop settings.
                ''',
                'next_hop_1',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('next-hop-2', REFERENCE_CLASS, 'NextHop2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2', 
                [], [], 
                '''                The second next-hop settings.
                ''',
                'next_hop_2',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('next-hop-3', REFERENCE_CLASS, 'NextHop3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3', 
                [], [], 
                '''                The third next-hop settings.
                ''',
                'next_hop_3',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('next-hop-type', REFERENCE_ENUM_CLASS, 'NextHopTypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'NextHopTypeEnum', 
                [], [], 
                '''                The nexthop type.
                ''',
                'next_hop_type',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'next-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags',
            False, 
            [
            _MetaInfoClassMember('authen', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match if authen header is present.
                ''',
                'authen',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destopts', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match if destops header is present.
                ''',
                'destopts',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('fragments', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match if fragments header is present.
                ''',
                'fragments',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('hop-by-hop', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match if hop-by-hop header is present.
                ''',
                'hop_by_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('routing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match if routing header is present.
                ''',
                'routing',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'header-flags',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry',
            False, 
            [
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483646')], [], 
                '''                Sequence number of access list entry
                ''',
                'sequence_number',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('capture', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable capture.
                ''',
                'capture',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('counter-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Counter name.
                ''',
                'counter_name',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-network', REFERENCE_CLASS, 'DestinationNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork', 
                [], [], 
                '''                Destination network settings.
                ''',
                'destination_network',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-port', REFERENCE_CLASS, 'DestinationPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort', 
                [], [], 
                '''                Destination port settings.
                ''',
                'destination_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-port-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Destination port object group name.
                ''',
                'destination_port_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('destination-prefix-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                IPv6 destination network object group name.
                ''',
                'destination_prefix_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                DSCP value to match (if a protocol was specified),
                leave unspecified if DSCP comparion is not to be
                performed.
                ''',
                'dscp',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'Ipv6AclDscpNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclDscpNumberEnum', 
                        [], [], 
                        '''                        DSCP value to match (if a protocol was specified),
                        leave unspecified if DSCP comparion is not to be
                        performed.
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '64')], [], 
                        '''                        DSCP value to match (if a protocol was specified),
                        leave unspecified if DSCP comparion is not to be
                        performed.
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('grant', REFERENCE_ENUM_CLASS, 'Ipv6AclGrantEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclGrantEnumEnum', 
                [], [], 
                '''                Whether to forward or drop packets matching the 
                ACE.
                ''',
                'grant',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('header-flags', REFERENCE_CLASS, 'HeaderFlags' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags', 
                [], [], 
                '''                Match if header-flag is present.
                ''',
                'header_flags',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('icmp', REFERENCE_CLASS, 'Icmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp', 
                [], [], 
                '''                ICMP settings.
                ''',
                'icmp',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('icmp-off', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                To turn off ICMP generation for deny ACEs.
                ''',
                'icmp_off',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('log-option', REFERENCE_ENUM_CLASS, 'Ipv6AclLoggingEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclLoggingEnumEnum', 
                [], [], 
                '''                Whether and how to log matches against this 
                entry.
                ''',
                'log_option',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop', 
                [], [], 
                '''                Next-hop settings.
                ''',
                'next_hop',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('packet-length', REFERENCE_CLASS, 'PacketLength' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength', 
                [], [], 
                '''                Packet length settings.
                ''',
                'packet_length',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Precedence value to match (if a protocol was 
                specified), leave unspecified if precedence 
                comparion is not to be performed.
                ''',
                'precedence',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'Ipv6AclPrecedenceNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclPrecedenceNumberEnum', 
                        [], [], 
                        '''                        Precedence value to match (if a protocol was 
                        specified), leave unspecified if precedence 
                        comparion is not to be performed.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        Precedence value to match (if a protocol was 
                        specified), leave unspecified if precedence 
                        comparion is not to be performed.
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('protocol', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Protocol to match.
                ''',
                'protocol',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('protocol', REFERENCE_ENUM_CLASS, 'Ipv6AclProtocolNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclProtocolNumberEnum', 
                        [], [], 
                        '''                        Protocol to match.
                        ''',
                        'protocol',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                        [('0', '255')], [], 
                        '''                        Protocol to match.
                        ''',
                        'protocol',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('protocol2', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Protocol2 to match.
                ''',
                'protocol2',
                'Cisco-IOS-XR-ipv6-acl-cfg', False, [
                    _MetaInfoClassMember('protocol2', REFERENCE_ENUM_CLASS, 'Ipv6AclProtocolNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclProtocolNumberEnum', 
                        [], [], 
                        '''                        Protocol2 to match.
                        ''',
                        'protocol2',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                    _MetaInfoClassMember('protocol2', ATTRIBUTE, 'int' , None, None, 
                        [('0', '255')], [], 
                        '''                        Protocol2 to match.
                        ''',
                        'protocol2',
                        'Cisco-IOS-XR-ipv6-acl-cfg', False),
                ]),
            _MetaInfoClassMember('protocol-operator', REFERENCE_ENUM_CLASS, 'Ipv6AclOperatorEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_datatypes', 'Ipv6AclOperatorEnumEnum', 
                [], [], 
                '''                Protocol operator. Leave unspecified if
                no protocol comparison is to be done.
                ''',
                'protocol_operator',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('qos-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '512')], [], 
                '''                Set qos-group number
                ''',
                'qos_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('remark', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Comments or a description for the access list.
                ''',
                'remark',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('sequence-str', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Sequence String for the ace.
                ''',
                'sequence_str',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-network', REFERENCE_CLASS, 'SourceNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork', 
                [], [], 
                '''                Source network settings.
                ''',
                'source_network',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-port', REFERENCE_CLASS, 'SourcePort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort', 
                [], [], 
                '''                Source port settings.
                ''',
                'source_port',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-port-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Source port object group name.
                ''',
                'source_port_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('source-prefix-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                IPv6 source network object group name.
                ''',
                'source_prefix_group',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('tcp', REFERENCE_CLASS, 'Tcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp', 
                [], [], 
                '''                TCP settings.
                ''',
                'tcp',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('time-to-live', REFERENCE_CLASS, 'TimeToLive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive', 
                [], [], 
                '''                TTL settings.
                ''',
                'time_to_live',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('undetermined-transport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable undetermined-transport.
                ''',
                'undetermined_transport',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'access-list-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries',
            False, 
            [
            _MetaInfoClassMember('access-list-entry', REFERENCE_LIST, 'AccessListEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry', 
                [], [], 
                '''                An ACL entry; either a description (remark)
                or anAccess List Entry to match against
                ''',
                'access_list_entry',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'access-list-entries',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses.Access' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses.Access',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 65)], [], 
                '''                Name of the access list
                ''',
                'name',
                'Cisco-IOS-XR-ipv6-acl-cfg', True),
            _MetaInfoClassMember('access-list-entries', REFERENCE_CLASS, 'AccessListEntries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries', 
                [], [], 
                '''                ACL entry table; contains list of access list
                entries
                ''',
                'access_list_entries',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'access',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList.Accesses' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList.Accesses',
            False, 
            [
            _MetaInfoClassMember('access', REFERENCE_LIST, 'Access' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses.Access', 
                [], [], 
                '''                An ACL
                ''',
                'access',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'accesses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
    'Ipv6AclAndPrefixList' : {
        'meta_info' : _MetaInfoClass('Ipv6AclAndPrefixList',
            False, 
            [
            _MetaInfoClassMember('accesses', REFERENCE_CLASS, 'Accesses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Accesses', 
                [], [], 
                '''                Table of access lists
                ''',
                'accesses',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('log-update', REFERENCE_CLASS, 'LogUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.LogUpdate', 
                [], [], 
                '''                Control access lists log updates
                ''',
                'log_update',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            _MetaInfoClassMember('prefixes', REFERENCE_CLASS, 'Prefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg', 'Ipv6AclAndPrefixList.Prefixes', 
                [], [], 
                '''                Table of prefix lists
                ''',
                'prefixes',
                'Cisco-IOS-XR-ipv6-acl-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-acl-cfg',
            'ipv6-acl-and-prefix-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-acl-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_acl_cfg'
        ),
    },
}
_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries.PrefixListEntry']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix.PrefixListEntries']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Prefixes.Prefix']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Prefixes']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop1']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop2']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop.NextHop3']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourceNetwork']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationNetwork']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.SourcePort']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.DestinationPort']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Icmp']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.Tcp']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.PacketLength']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.TimeToLive']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.NextHop']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry.HeaderFlags']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries.AccessListEntry']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access.AccessListEntries']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses.Access']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses.Access']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList.Accesses']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Prefixes']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
_meta_table['Ipv6AclAndPrefixList.LogUpdate']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
_meta_table['Ipv6AclAndPrefixList.Accesses']['meta_info'].parent =_meta_table['Ipv6AclAndPrefixList']['meta_info']
