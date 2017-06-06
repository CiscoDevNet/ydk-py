


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DefaultPolicyTypeEnum' : _MetaInfoEnum('DefaultPolicyTypeEnum', 'ydk.models.openconfig.openconfig_routing_policy',
        {
            'ACCEPT-ROUTE':'ACCEPT_ROUTE',
            'REJECT-ROUTE':'REJECT_ROUTE',
        }, 'openconfig-routing-policy', _yang_ns._namespaces['openconfig-routing-policy']),
    'RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix',
            False, 
            [
            _MetaInfoClassMember('ip-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The prefix member in CIDR notation -- while the
                prefix may be either IPv4 or IPv6, most
                implementations require all members of the prefix set
                to be the same address family.  Mixing address types in
                the same prefix set is likely to cause an error.
                ''',
                'ip_prefix',
                'openconfig-routing-policy', True, [
                    _MetaInfoClassMember('ip-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        The prefix member in CIDR notation -- while the
                        prefix may be either IPv4 or IPv6, most
                        implementations require all members of the prefix set
                        to be the same address family.  Mixing address types in
                        the same prefix set is likely to cause an error.
                        ''',
                        'ip_prefix',
                        'openconfig-routing-policy', True),
                    _MetaInfoClassMember('ip-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        The prefix member in CIDR notation -- while the
                        prefix may be either IPv4 or IPv6, most
                        implementations require all members of the prefix set
                        to be the same address family.  Mixing address types in
                        the same prefix set is likely to cause an error.
                        ''',
                        'ip_prefix',
                        'openconfig-routing-policy', True),
                ]),
            _MetaInfoClassMember('masklength-range', ATTRIBUTE, 'str' , None, None, 
                [], [b'^([0-9]+\\.\\.[0-9]+)|exact$'], 
                '''                Defines a range for the masklength, or 'exact' if
                the prefix has an exact length.
                
                Example: 10.3.192.0/21 through 10.3.192.0/24 would be
                expressed as prefix: 10.3.192.0/21,
                masklength-range: 21..24.
                
                Example: 10.3.192.0/21 would be expressed as
                prefix: 10.3.192.0/21,
                masklength-range: exact
                ''',
                'masklength_range',
                'openconfig-routing-policy', True),
            ],
            'openconfig-routing-policy',
            'prefix',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.PrefixSets.PrefixSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.PrefixSets.PrefixSet',
            False, 
            [
            _MetaInfoClassMember('prefix-set-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name / label of the prefix set -- this is used to
                reference the set in match conditions
                ''',
                'prefix_set_name',
                'openconfig-routing-policy', True),
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix', 
                [], [], 
                '''                List of prefix expressions that are part of the set
                ''',
                'prefix',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'prefix-set',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.PrefixSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.PrefixSets',
            False, 
            [
            _MetaInfoClassMember('prefix-set', REFERENCE_LIST, 'PrefixSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.PrefixSets.PrefixSet', 
                [], [], 
                '''                List of the defined prefix sets
                ''',
                'prefix_set',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'prefix-sets',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the neighbor set member
                ''',
                'address',
                'openconfig-routing-policy', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the neighbor set member
                        ''',
                        'address',
                        'openconfig-routing-policy', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the neighbor set member
                        ''',
                        'address',
                        'openconfig-routing-policy', True),
                ]),
            ],
            'openconfig-routing-policy',
            'neighbor',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.NeighborSets.NeighborSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.NeighborSets.NeighborSet',
            False, 
            [
            _MetaInfoClassMember('neighbor-set-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name / label of the neighbor set -- this is used to
                reference the set in match conditions
                ''',
                'neighbor_set_name',
                'openconfig-routing-policy', True),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor', 
                [], [], 
                '''                list of addresses that are part of the neighbor set
                ''',
                'neighbor',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'neighbor-set',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.NeighborSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.NeighborSets',
            False, 
            [
            _MetaInfoClassMember('neighbor-set', REFERENCE_LIST, 'NeighborSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.NeighborSets.NeighborSet', 
                [], [], 
                '''                Definitions for neighbor sets
                ''',
                'neighbor_set',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'neighbor-sets',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.TagSets.TagSet.Tag' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.TagSets.TagSet.Tag',
            False, 
            [
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the tag set member
                ''',
                'value',
                'openconfig-routing-policy', True, [
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Value of the tag set member
                        ''',
                        'value',
                        'openconfig-routing-policy', True),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                        [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Value of the tag set member
                        ''',
                        'value',
                        'openconfig-routing-policy', True),
                ]),
            ],
            'openconfig-routing-policy',
            'tag',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.TagSets.TagSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.TagSets.TagSet',
            False, 
            [
            _MetaInfoClassMember('tag-set-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name / label of the tag set -- this is used to reference
                the set in match conditions
                ''',
                'tag_set_name',
                'openconfig-routing-policy', True),
            _MetaInfoClassMember('tag', REFERENCE_LIST, 'Tag' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.TagSets.TagSet.Tag', 
                [], [], 
                '''                list of tags that are part of the tag set
                ''',
                'tag',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'tag-set',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.TagSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.TagSets',
            False, 
            [
            _MetaInfoClassMember('tag-set', REFERENCE_LIST, 'TagSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.TagSets.TagSet', 
                [], [], 
                '''                Definitions for tag sets
                ''',
                'tag_set',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'tag-sets',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet',
            False, 
            [
            _MetaInfoClassMember('community-set-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name / label of the community set -- this is used to
                reference the set in match conditions
                ''',
                'community_set_name',
                'openconfig-bgp-policy', True),
            _MetaInfoClassMember('community-member', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                members of the community set
                ''',
                'community_member',
                'openconfig-bgp-policy', False, [
                    _MetaInfoClassMember('community-member', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        members of the community set
                        ''',
                        'community_member',
                        'openconfig-bgp-policy', False, [
                            _MetaInfoClassMember('community-member', REFERENCE_LEAFLIST, 'int' , None, None, 
                                [('65536', '4294901759')], [], 
                                '''                                members of the community set
                                ''',
                                'community_member',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'([0-9]+:[0-9]+)'], 
                                '''                                members of the community set
                                ''',
                                'community_member',
                                'openconfig-bgp-policy', False),
                        ]),
                    _MetaInfoClassMember('community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [], 
                        '''                        members of the community set
                        ''',
                        'community_member',
                        'openconfig-bgp-policy', False),
                    _MetaInfoClassMember('community-member', REFERENCE_LEAFLIST, 'BgpWellKnownStdCommunityIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'BgpWellKnownStdCommunityIdentity', 
                        [], [], 
                        '''                        members of the community set
                        ''',
                        'community_member',
                        'openconfig-bgp-policy', False),
                ]),
            ],
            'openconfig-bgp-policy',
            'community-set',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets',
            False, 
            [
            _MetaInfoClassMember('community-set', REFERENCE_LIST, 'CommunitySet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet', 
                [], [], 
                '''                Definitions for community sets
                ''',
                'community_set',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'community-sets',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet',
            False, 
            [
            _MetaInfoClassMember('ext-community-set-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name / label of the extended community set -- this is
                used to reference the set in match conditions
                ''',
                'ext_community_set_name',
                'openconfig-bgp-policy', True),
            _MetaInfoClassMember('ext-community-member', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                members of the extended community set
                ''',
                'ext_community_member',
                'openconfig-bgp-policy', False, [
                    _MetaInfoClassMember('ext-community-member', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        members of the extended community set
                        ''',
                        'ext_community_member',
                        'openconfig-bgp-policy', False, [
                            _MetaInfoClassMember('ext-community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                                '''                                members of the extended community set
                                ''',
                                'ext_community_member',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('ext-community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                                '''                                members of the extended community set
                                ''',
                                'ext_community_member',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('ext-community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                                '''                                members of the extended community set
                                ''',
                                'ext_community_member',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('ext-community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                                '''                                members of the extended community set
                                ''',
                                'ext_community_member',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('ext-community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                                '''                                members of the extended community set
                                ''',
                                'ext_community_member',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('ext-community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                                '''                                members of the extended community set
                                ''',
                                'ext_community_member',
                                'openconfig-bgp-policy', False),
                        ]),
                    _MetaInfoClassMember('ext-community-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [], 
                        '''                        members of the extended community set
                        ''',
                        'ext_community_member',
                        'openconfig-bgp-policy', False),
                ]),
            ],
            'openconfig-bgp-policy',
            'ext-community-set',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets',
            False, 
            [
            _MetaInfoClassMember('ext-community-set', REFERENCE_LIST, 'ExtCommunitySet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet', 
                [], [], 
                '''                Definitions for extended community sets
                ''',
                'ext_community_set',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'ext-community-sets',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet',
            False, 
            [
            _MetaInfoClassMember('as-path-set-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name of the AS path set -- this is used to reference
                the set in match conditions
                ''',
                'as_path_set_name',
                'openconfig-bgp-policy', True),
            _MetaInfoClassMember('as-path-set-member', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                AS path expression -- list of ASes in the set
                ''',
                'as_path_set_member',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'as-path-set',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets',
            False, 
            [
            _MetaInfoClassMember('as-path-set', REFERENCE_LIST, 'AsPathSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet', 
                [], [], 
                '''                Definitions for AS path sets
                ''',
                'as_path_set',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'as-path-sets',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.BgpDefinedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.BgpDefinedSets',
            False, 
            [
            _MetaInfoClassMember('as-path-sets', REFERENCE_CLASS, 'AsPathSets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets', 
                [], [], 
                '''                Enclosing container for AS path sets
                ''',
                'as_path_sets',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('community-sets', REFERENCE_CLASS, 'CommunitySets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets', 
                [], [], 
                '''                Enclosing container for community sets
                ''',
                'community_sets',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('ext-community-sets', REFERENCE_CLASS, 'ExtCommunitySets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets', 
                [], [], 
                '''                Enclosing container for extended community sets
                ''',
                'ext_community_sets',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'bgp-defined-sets',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets',
            False, 
            [
            _MetaInfoClassMember('bgp-defined-sets', REFERENCE_CLASS, 'BgpDefinedSets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.BgpDefinedSets', 
                [], [], 
                '''                BGP-related set definitions for policy match conditions
                ''',
                'bgp_defined_sets',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('neighbor-sets', REFERENCE_CLASS, 'NeighborSets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.NeighborSets', 
                [], [], 
                '''                Enclosing container for defined neighbor sets for matching
                ''',
                'neighbor_sets',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('prefix-sets', REFERENCE_CLASS, 'PrefixSets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.PrefixSets', 
                [], [], 
                '''                Enclosing container for defined prefix sets for matching
                ''',
                'prefix_sets',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('tag-sets', REFERENCE_CLASS, 'TagSets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets.TagSets', 
                [], [], 
                '''                Enclosing container for defined tag sets for matching
                ''',
                'tag_sets',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'defined-sets',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet',
            False, 
            [
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsRestrictedTypeEnum' , 'ydk.models.openconfig.openconfig_policy_types', 'MatchSetOptionsRestrictedTypeEnum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation.  This leaf only supports matching on ANY
                member of the set or inverting the match.  Matching on ALL is
                not supported)
                ''',
                'match_set_options',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('prefix-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined prefix set
                ''',
                'prefix_set',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'match-prefix-set',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet',
            False, 
            [
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsRestrictedTypeEnum' , 'ydk.models.openconfig.openconfig_policy_types', 'MatchSetOptionsRestrictedTypeEnum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation.  This leaf only supports matching on ANY
                member of the set or inverting the match.  Matching on ALL is
                not supported)
                ''',
                'match_set_options',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('neighbor-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined neighbor set
                ''',
                'neighbor_set',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'match-neighbor-set',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet',
            False, 
            [
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsRestrictedTypeEnum' , 'ydk.models.openconfig.openconfig_policy_types', 'MatchSetOptionsRestrictedTypeEnum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation.  This leaf only supports matching on ANY
                member of the set or inverting the match.  Matching on ALL is
                not supported)
                ''',
                'match_set_options',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('tag-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined tag set
                ''',
                'tag_set',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'match-tag-set',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions',
            False, 
            [
            ],
            'openconfig-routing-policy',
            'igp-conditions',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet',
            False, 
            [
            _MetaInfoClassMember('community-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined community set
                ''',
                'community_set',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsTypeEnum' , 'ydk.models.openconfig.openconfig_policy_types', 'MatchSetOptionsTypeEnum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation
                ''',
                'match_set_options',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'match-community-set',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet',
            False, 
            [
            _MetaInfoClassMember('ext-community-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined extended community set
                ''',
                'ext_community_set',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsTypeEnum' , 'ydk.models.openconfig.openconfig_policy_types', 'MatchSetOptionsTypeEnum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation
                ''',
                'match_set_options',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'match-ext-community-set',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet',
            False, 
            [
            _MetaInfoClassMember('as-path-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined AS path set
                ''',
                'as_path_set',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsTypeEnum' , 'ydk.models.openconfig.openconfig_policy_types', 'MatchSetOptionsTypeEnum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation
                ''',
                'match_set_options',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'match-as-path-set',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount',
            False, 
            [
            _MetaInfoClassMember('operator', REFERENCE_IDENTITY_CLASS, 'AttributeComparisonIdentity' , 'ydk.models.openconfig.openconfig_policy_types', 'AttributeComparisonIdentity', 
                [], [], 
                '''                type of comparison to be performed
                ''',
                'operator',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                value to compare with the community count
                ''',
                'value',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'community-count',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength',
            False, 
            [
            _MetaInfoClassMember('operator', REFERENCE_IDENTITY_CLASS, 'AttributeComparisonIdentity' , 'ydk.models.openconfig.openconfig_policy_types', 'AttributeComparisonIdentity', 
                [], [], 
                '''                type of comparison to be performed
                ''',
                'operator',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                value to compare with the community count
                ''',
                'value',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'as-path-length',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.RouteTypeEnum' : _MetaInfoEnum('RouteTypeEnum', 'ydk.models.openconfig.openconfig_routing_policy',
        {
            'INTERNAL':'INTERNAL',
            'EXTERNAL':'EXTERNAL',
        }, 'openconfig-bgp-policy', _yang_ns._namespaces['openconfig-bgp-policy']),
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions',
            False, 
            [
            _MetaInfoClassMember('afi-safi-in', REFERENCE_LEAFLIST, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                List of address families which the NLRI may be
                within
                ''',
                'afi_safi_in',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('as-path-length', REFERENCE_CLASS, 'AsPathLength' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength', 
                [], [], 
                '''                Value and comparison operations for conditions based on the
                length of the AS path in the route update
                ''',
                'as_path_length',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('community-count', REFERENCE_CLASS, 'CommunityCount' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount', 
                [], [], 
                '''                Value and comparison operations for conditions based on the
                number of communities in the route update
                ''',
                'community_count',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('local-pref-eq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Condition to check if the local pref attribute is equal to
                the specified value
                ''',
                'local_pref_eq',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('match-as-path-set', REFERENCE_CLASS, 'MatchAsPathSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet', 
                [], [], 
                '''                Match a referenced as-path set according to the logic
                defined in the match-set-options leaf
                ''',
                'match_as_path_set',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('match-community-set', REFERENCE_CLASS, 'MatchCommunitySet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet', 
                [], [], 
                '''                Match a referenced community-set according to the logic
                defined in the match-set-options leaf
                ''',
                'match_community_set',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('match-ext-community-set', REFERENCE_CLASS, 'MatchExtCommunitySet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet', 
                [], [], 
                '''                Match a referenced extended community-set according to the
                logic defined in the match-set-options leaf
                ''',
                'match_ext_community_set',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('med-eq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Condition to check if the received MED value is equal to
                the specified value
                ''',
                'med_eq',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('next-hop-in', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of next hop addresses to check for in the route
                update
                ''',
                'next_hop_in',
                'openconfig-bgp-policy', False, [
                    _MetaInfoClassMember('next-hop-in', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        List of next hop addresses to check for in the route
                        update
                        ''',
                        'next_hop_in',
                        'openconfig-bgp-policy', False),
                    _MetaInfoClassMember('next-hop-in', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        List of next hop addresses to check for in the route
                        update
                        ''',
                        'next_hop_in',
                        'openconfig-bgp-policy', False),
                ]),
            _MetaInfoClassMember('origin-eq', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                Condition to check if the route origin is equal to the
                specified value
                ''',
                'origin_eq',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RouteTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.RouteTypeEnum', 
                [], [], 
                '''                Condition to check the route type in the route update
                ''',
                'route_type',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'bgp-conditions',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions',
            False, 
            [
            _MetaInfoClassMember('bgp-conditions', REFERENCE_CLASS, 'BgpConditions' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions', 
                [], [], 
                '''                Policy conditions for matching
                BGP-specific defined sets or comparing BGP-specific
                attributes
                ''',
                'bgp_conditions',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('call-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Applies the statements from the specified policy
                definition and then returns control the current
                policy statement. Note that the called policy may
                itself call other policies (subject to
                implementation limitations). This is intended to
                provide a policy 'subroutine' capability.  The
                called policy should contain an explicit or a
                default route disposition that returns an
                effective true (accept-route) or false
                (reject-route), otherwise the behavior may be
                ambiguous and implementation dependent
                ''',
                'call_policy',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('igp-conditions', REFERENCE_CLASS, 'IgpConditions' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions', 
                [], [], 
                '''                Policy conditions for IGP attributes
                ''',
                'igp_conditions',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('install-protocol-eq', REFERENCE_IDENTITY_CLASS, 'InstallProtocolTypeIdentity' , 'ydk.models.openconfig.openconfig_policy_types', 'InstallProtocolTypeIdentity', 
                [], [], 
                '''                Condition to check the protocol / method used to install
                which installed the route into the local routing table
                ''',
                'install_protocol_eq',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('match-neighbor-set', REFERENCE_CLASS, 'MatchNeighborSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet', 
                [], [], 
                '''                Match a referenced neighbor set according to the logic
                defined in the match-set-options-leaf
                ''',
                'match_neighbor_set',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('match-prefix-set', REFERENCE_CLASS, 'MatchPrefixSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet', 
                [], [], 
                '''                Match a referenced prefix-set according to the logic
                defined in the match-set-options leaf
                ''',
                'match_prefix_set',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('match-tag-set', REFERENCE_CLASS, 'MatchTagSet' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet', 
                [], [], 
                '''                Match a referenced tag set according to the logic defined
                in the match-options-set leaf
                ''',
                'match_tag_set',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'conditions',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions',
            False, 
            [
            _MetaInfoClassMember('set-tag', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the tag value for OSPF or IS-IS routes.
                ''',
                'set_tag',
                'openconfig-routing-policy', False, [
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Set the tag value for OSPF or IS-IS routes.
                        ''',
                        'set_tag',
                        'openconfig-routing-policy', False),
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'str' , None, None, 
                        [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Set the tag value for OSPF or IS-IS routes.
                        ''',
                        'set_tag',
                        'openconfig-routing-policy', False),
                ]),
            ],
            'openconfig-routing-policy',
            'igp-actions',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend',
            False, 
            [
            _MetaInfoClassMember('repeat-n', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                number of times to prepend the local AS
                number
                ''',
                'repeat_n',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'set-as-path-prepend',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity',
            False, 
            [
            _MetaInfoClassMember('communities', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the community values for the update inline with
                a list.
                ''',
                'communities',
                'openconfig-bgp-policy', False, [
                    _MetaInfoClassMember('communities', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Set the community values for the update inline with
                        a list.
                        ''',
                        'communities',
                        'openconfig-bgp-policy', False, [
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'int' , None, None, 
                                [('65536', '4294901759')], [], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'([0-9]+:[0-9]+)'], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                        ]),
                    _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'BgpWellKnownStdCommunityIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'BgpWellKnownStdCommunityIdentity', 
                        [], [], 
                        '''                        Set the community values for the update inline with
                        a list.
                        ''',
                        'communities',
                        'openconfig-bgp-policy', False),
                ]),
            _MetaInfoClassMember('community-set-ref', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined community set by name
                ''',
                'community_set_ref',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('options', REFERENCE_ENUM_CLASS, 'BgpSetCommunityOptionTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_policy', 'BgpSetCommunityOptionTypeEnum', 
                [], [], 
                '''                Options for modifying the community attribute with
                the specified values.  These options apply to both
                methods of setting the community attribute.
                ''',
                'options',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'set-community',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity',
            False, 
            [
            _MetaInfoClassMember('communities', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the community values for the update inline with
                a list.
                ''',
                'communities',
                'openconfig-bgp-policy', False, [
                    _MetaInfoClassMember('communities', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Set the community values for the update inline with
                        a list.
                        ''',
                        'communities',
                        'openconfig-bgp-policy', False, [
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'str' , None, None, 
                                [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                                '''                                Set the community values for the update inline with
                                a list.
                                ''',
                                'communities',
                                'openconfig-bgp-policy', False),
                        ]),
                    _MetaInfoClassMember('communities', REFERENCE_LEAFLIST, 'BgpWellKnownStdCommunityIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'BgpWellKnownStdCommunityIdentity', 
                        [], [], 
                        '''                        Set the community values for the update inline with
                        a list.
                        ''',
                        'communities',
                        'openconfig-bgp-policy', False),
                ]),
            _MetaInfoClassMember('ext-community-set-ref', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined extended community set by
                name
                ''',
                'ext_community_set_ref',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('options', REFERENCE_ENUM_CLASS, 'BgpSetCommunityOptionTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_policy', 'BgpSetCommunityOptionTypeEnum', 
                [], [], 
                '''                options for modifying the extended community
                attribute with the specified values. These options
                apply to both methods of setting the community
                attribute.
                ''',
                'options',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'set-ext-community',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions',
            False, 
            [
            _MetaInfoClassMember('set-as-path-prepend', REFERENCE_CLASS, 'SetAsPathPrepend' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend', 
                [], [], 
                '''                action to prepend local AS number to the AS-path a
                specified number of times
                ''',
                'set_as_path_prepend',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('set-community', REFERENCE_CLASS, 'SetCommunity' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity', 
                [], [], 
                '''                action to set the community attributes of the route, along
                with options to modify how the community is modified
                ''',
                'set_community',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('set-ext-community', REFERENCE_CLASS, 'SetExtCommunity' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity', 
                [], [], 
                '''                Action to set the extended community attributes of the
                route, along with options to modify how the community is
                modified
                ''',
                'set_ext_community',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('set-local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                set the local pref attribute on the route
                update
                ''',
                'set_local_pref',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('set-med', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                set the med metric attribute in the route
                update
                ''',
                'set_med',
                'openconfig-bgp-policy', False, [
                    _MetaInfoClassMember('set-med', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        set the med metric attribute in the route
                        update
                        ''',
                        'set_med',
                        'openconfig-bgp-policy', False),
                    _MetaInfoClassMember('set-med', ATTRIBUTE, 'str' , None, None, 
                        [], [b'^[+-][0-9]+'], 
                        '''                        set the med metric attribute in the route
                        update
                        ''',
                        'set_med',
                        'openconfig-bgp-policy', False),
                    _MetaInfoClassMember('set-med', REFERENCE_ENUM_CLASS, 'BgpSetMedTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_policy', 'BgpSetMedTypeEnum', 
                        [], [], 
                        '''                        set the med metric attribute in the route
                        update
                        ''',
                        'set_med',
                        'openconfig-bgp-policy', False),
                ]),
            _MetaInfoClassMember('set-next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                set the next-hop attribute in the route update
                ''',
                'set_next_hop',
                'openconfig-bgp-policy', False, [
                    _MetaInfoClassMember('set-next-hop', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        set the next-hop attribute in the route update
                        ''',
                        'set_next_hop',
                        'openconfig-bgp-policy', False, [
                            _MetaInfoClassMember('set-next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                set the next-hop attribute in the route update
                                ''',
                                'set_next_hop',
                                'openconfig-bgp-policy', False),
                            _MetaInfoClassMember('set-next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                set the next-hop attribute in the route update
                                ''',
                                'set_next_hop',
                                'openconfig-bgp-policy', False),
                        ]),
                    _MetaInfoClassMember('set-next-hop', REFERENCE_ENUM_CLASS, 'BgpNextHopTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_policy', 'BgpNextHopTypeEnum', 
                        [], [], 
                        '''                        set the next-hop attribute in the route update
                        ''',
                        'set_next_hop',
                        'openconfig-bgp-policy', False),
                ]),
            _MetaInfoClassMember('set-route-origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                set the origin attribute to the specified
                value
                ''',
                'set_route_origin',
                'openconfig-bgp-policy', False),
            ],
            'openconfig-bgp-policy',
            'bgp-actions',
            _yang_ns._namespaces['openconfig-bgp-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions',
            False, 
            [
            _MetaInfoClassMember('accept-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                accepts the route into the routing table
                ''',
                'accept_route',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('bgp-actions', REFERENCE_CLASS, 'BgpActions' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions', 
                [], [], 
                '''                Definitions for policy action statements that
                change BGP-specific attributes of the route
                ''',
                'bgp_actions',
                'openconfig-bgp-policy', False),
            _MetaInfoClassMember('igp-actions', REFERENCE_CLASS, 'IgpActions' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions', 
                [], [], 
                '''                Actions to set IGP route attributes; these actions
                apply to multiple IGPs
                ''',
                'igp_actions',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('reject-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                rejects the route
                ''',
                'reject_route',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'actions',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name of the policy statement
                ''',
                'name',
                'openconfig-routing-policy', True),
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions', 
                [], [], 
                '''                Action statements for this policy
                statement
                ''',
                'actions',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('conditions', REFERENCE_CLASS, 'Conditions' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions', 
                [], [], 
                '''                Condition statements for this
                policy statement
                ''',
                'conditions',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'statement',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements',
            False, 
            [
            _MetaInfoClassMember('statement', REFERENCE_LIST, 'Statement' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement', 
                [], [], 
                '''                Policy statements group conditions and actions
                within a policy definition.  They are evaluated in
                the order specified (see the description of policy
                evaluation at the top of this module.
                ''',
                'statement',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'statements',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the top-level policy definition -- this name
                 is used in references to the current policy
                ''',
                'name',
                'openconfig-routing-policy', True),
            _MetaInfoClassMember('statements', REFERENCE_CLASS, 'Statements' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements', 
                [], [], 
                '''                Enclosing container for policy statements
                ''',
                'statements',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'policy-definition',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions',
            False, 
            [
            _MetaInfoClassMember('policy-definition', REFERENCE_LIST, 'PolicyDefinition' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition', 
                [], [], 
                '''                List of top-level policy definitions, keyed by unique
                name.  These policy definitions are expected to be
                referenced (by name) in policy chains specified in import
                or export configuration statements.
                ''',
                'policy_definition',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'policy-definitions',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
    'RoutingPolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy',
            False, 
            [
            _MetaInfoClassMember('defined-sets', REFERENCE_CLASS, 'DefinedSets' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.DefinedSets', 
                [], [], 
                '''                Predefined sets of attributes used in policy match
                statements
                ''',
                'defined_sets',
                'openconfig-routing-policy', False),
            _MetaInfoClassMember('policy-definitions', REFERENCE_CLASS, 'PolicyDefinitions' , 'ydk.models.openconfig.openconfig_routing_policy', 'RoutingPolicy.PolicyDefinitions', 
                [], [], 
                '''                Enclosing container for the list of top-level policy
                definitions
                ''',
                'policy_definitions',
                'openconfig-routing-policy', False),
            ],
            'openconfig-routing-policy',
            'routing-policy',
            _yang_ns._namespaces['openconfig-routing-policy'],
        'ydk.models.openconfig.openconfig_routing_policy'
        ),
    },
}
_meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.PrefixSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.NeighborSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet.Tag']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.TagSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets.CommunitySet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets.ExtCommunitySet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets.AsPathSet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.CommunitySets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.ExtCommunitySets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets.AsPathSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.PrefixSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.NeighborSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.TagSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.BgpDefinedSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchCommunitySet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchExtCommunitySet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.MatchAsPathSet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.CommunityCount']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions.AsPathLength']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.BgpConditions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetAsPathPrepend']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetCommunity']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions.SetExtCommunity']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.BgpActions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions']['meta_info']
_meta_table['RoutingPolicy.DefinedSets']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
