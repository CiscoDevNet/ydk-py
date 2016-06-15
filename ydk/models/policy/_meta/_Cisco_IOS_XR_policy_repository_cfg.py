


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'RoutingPolicy.RoutePolicies.RoutePolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.RoutePolicies.RoutePolicy',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy statements
                ''',
                'rpl_route_policy',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'route-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.RoutePolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.RoutePolicies',
            False, 
            [
            _MetaInfoClassMember('route-policy', REFERENCE_LIST, 'RoutePolicy' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.RoutePolicies.RoutePolicy', 
                [], [], 
                '''                Information about an individual policy
                ''',
                'route_policy',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'route-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrefixSets.PrefixSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrefixSets.PrefixSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-prefix-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                prefix statements
                ''',
                'rpl_prefix_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prefix-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrefixSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrefixSets',
            False, 
            [
            _MetaInfoClassMember('prefix-set', REFERENCE_LIST, 'PrefixSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrefixSets.PrefixSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'prefix_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prefix-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets.AppendExtendedCommunityOpaqueSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets.AppendExtendedCommunityOpaqueSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-opaque-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community Opaque Set
                ''',
                'rpl_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'append-extended-community-opaque-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets',
            False, 
            [
            _MetaInfoClassMember('append-extended-community-opaque-set', REFERENCE_LIST, 'AppendExtendedCommunityOpaqueSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets.AppendExtendedCommunityOpaqueSet', 
                [], [], 
                '''                Append the entries to the existing set
                ''',
                'append_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'append-extended-community-opaque-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets.AppendExtendedCommunitySegNhSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets.AppendExtendedCommunitySegNhSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-seg-nh-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community SegNH Set
                ''',
                'rpl_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'append-extended-community-seg-nh-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets',
            False, 
            [
            _MetaInfoClassMember('append-extended-community-seg-nh-set', REFERENCE_LIST, 'AppendExtendedCommunitySegNhSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets.AppendExtendedCommunitySegNhSet', 
                [], [], 
                '''                Append the entries to the existing set
                ''',
                'append_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'append-extended-community-seg-nh-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets.RemoveExtendedCommunityOpaqueSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets.RemoveExtendedCommunityOpaqueSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-opaque-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community Opaque Set
                ''',
                'rpl_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'remove-extended-community-opaque-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets',
            False, 
            [
            _MetaInfoClassMember('remove-extended-community-opaque-set', REFERENCE_LIST, 'RemoveExtendedCommunityOpaqueSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets.RemoveExtendedCommunityOpaqueSet', 
                [], [], 
                '''                Remove the entries from the existing set
                ''',
                'remove_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'remove-extended-community-opaque-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-opaque-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community Opaque Set
                ''',
                'rpl_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-opaque-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaqueSets',
            False, 
            [
            _MetaInfoClassMember('extended-community-opaque-set', REFERENCE_LIST, 'ExtendedCommunityOpaqueSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-opaque-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets.RemoveExtendedCommunitySegNhSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets.RemoveExtendedCommunitySegNhSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-seg-nh-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community SegNH Set
                ''',
                'rpl_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'remove-extended-community-seg-nh-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets',
            False, 
            [
            _MetaInfoClassMember('remove-extended-community-seg-nh-set', REFERENCE_LIST, 'RemoveExtendedCommunitySegNhSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets.RemoveExtendedCommunitySegNhSet', 
                [], [], 
                '''                Remove the entries from the existing set
                ''',
                'remove_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'remove-extended-community-seg-nh-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RemoveOspfAreaSets.RemoveOspfAreaSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RemoveOspfAreaSets.RemoveOspfAreaSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplospf-area-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area Set
                ''',
                'rplospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'remove-ospf-area-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RemoveOspfAreaSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RemoveOspfAreaSets',
            False, 
            [
            _MetaInfoClassMember('remove-ospf-area-set', REFERENCE_LIST, 'RemoveOspfAreaSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RemoveOspfAreaSets.RemoveOspfAreaSet', 
                [], [], 
                '''                Remove the entries from the existing set.
                ''',
                'remove_ospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'remove-ospf-area-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplospf-area-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area Set
                ''',
                'rplospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'ospf-area-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.OspfAreaSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfAreaSets',
            False, 
            [
            _MetaInfoClassMember('ospf-area-set', REFERENCE_LIST, 'OspfAreaSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet', 
                [], [], 
                '''                Information about an individual OSPF area set.
                Usage: OSPF area set allows to define named
                set of area numbers        which can be
                referenced in the route-policy. Area sets     
                may be used during redistribution of the ospf
                protocol.  Example: ospf-area-set EXAMPLE     
                1,                                            
                192.168.1.255                                 
                end-set                                       
                Syntax: OSPF area number can be entered as 32
                bit number or in          the ip address
                format. See example.                    
                Semantic: Area numbers listed in the set will
                be searched for             a match. In the
                example these are areas 1 and                 
                192.168.1.255.                                
                ''',
                'ospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'ospf-area-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-cost-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community Cost Set
                ''',
                'rpl_extended_community_cost_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-cost-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCostSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCostSets',
            False, 
            [
            _MetaInfoClassMember('extended-community-cost-set', REFERENCE_LIST, 'ExtendedCommunityCostSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'extended_community_cost_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-cost-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-soo-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community SOO Set
                ''',
                'rpl_extended_community_soo_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-soo-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySooSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySooSets',
            False, 
            [
            _MetaInfoClassMember('extended-community-soo-set', REFERENCE_LIST, 'ExtendedCommunitySooSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'extended_community_soo_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-soo-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets.PrependExtendedCommunityOpaqueSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets.PrependExtendedCommunityOpaqueSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-opaque-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community Opaque Set
                ''',
                'rpl_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prepend-extended-community-opaque-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets',
            False, 
            [
            _MetaInfoClassMember('prepend-extended-community-opaque-set', REFERENCE_LIST, 'PrependExtendedCommunityOpaqueSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets.PrependExtendedCommunityOpaqueSet', 
                [], [], 
                '''                Prepend the entries to the existing set
                ''',
                'prepend_extended_community_opaque_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prepend-extended-community-opaque-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-seg-nh-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community SegNH Set
                ''',
                'rpl_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-seg-nh-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNhSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNhSets',
            False, 
            [
            _MetaInfoClassMember('extended-community-seg-nh-set', REFERENCE_LIST, 'ExtendedCommunitySegNhSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-seg-nh-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RdSets.RdSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RdSets.RdSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplrd-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RD Set
                ''',
                'rplrd_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'rd-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.RdSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.RdSets',
            False, 
            [
            _MetaInfoClassMember('rd-set', REFERENCE_LIST, 'RdSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RdSets.RdSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'rd_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'rd-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PolicyGlobalSetTable' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PolicyGlobalSetTable',
            False, 
            [
            _MetaInfoClassMember('policy-global-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Information about an individual set
                ''',
                'policy_global_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'policy-global-set-table',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets.PrependExtendedCommunitySegNhSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets.PrependExtendedCommunitySegNhSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-seg-nh-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community SegNH Set
                ''',
                'rpl_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prepend-extended-community-seg-nh-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets',
            False, 
            [
            _MetaInfoClassMember('prepend-extended-community-seg-nh-set', REFERENCE_LIST, 'PrependExtendedCommunitySegNhSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets.PrependExtendedCommunitySegNhSet', 
                [], [], 
                '''                Prepend the entries to the existing set
                ''',
                'prepend_extended_community_seg_nh_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prepend-extended-community-seg-nh-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-bandwidth-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community Bandwidth Set
                ''',
                'rpl_extended_community_bandwidth_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-bandwidth-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidthSets',
            False, 
            [
            _MetaInfoClassMember('extended-community-bandwidth-set', REFERENCE_LIST, 'ExtendedCommunityBandwidthSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'extended_community_bandwidth_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-bandwidth-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.CommunitySets.CommunitySet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.CommunitySets.CommunitySet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-community-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Community Set
                ''',
                'rpl_community_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'community-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.CommunitySets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.CommunitySets',
            False, 
            [
            _MetaInfoClassMember('community-set', REFERENCE_LIST, 'CommunitySet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.CommunitySets.CommunitySet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'community_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'community-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrependOspfAreaSets.PrependOspfAreaSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrependOspfAreaSets.PrependOspfAreaSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplospf-area-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area Set
                ''',
                'rplospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prepend-ospf-area-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.PrependOspfAreaSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.PrependOspfAreaSets',
            False, 
            [
            _MetaInfoClassMember('prepend-ospf-area-set', REFERENCE_LIST, 'PrependOspfAreaSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrependOspfAreaSets.PrependOspfAreaSet', 
                [], [], 
                '''                Prepend the entries to the existing set
                ''',
                'prepend_ospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'prepend-ospf-area-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AppendOspfAreaSets.AppendOspfAreaSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AppendOspfAreaSets.AppendOspfAreaSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplospf-area-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area Set
                ''',
                'rplospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'append-ospf-area-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AppendOspfAreaSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AppendOspfAreaSets',
            False, 
            [
            _MetaInfoClassMember('append-ospf-area-set', REFERENCE_LIST, 'AppendOspfAreaSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AppendOspfAreaSets.AppendOspfAreaSet', 
                [], [], 
                '''                Append the entries to the existing set
                ''',
                'append_ospf_area_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'append-ospf-area-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AsPathSets.AsPathSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPathSets.AsPathSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rplas-path-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ASPath Set
                ''',
                'rplas_path_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'as-path-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.AsPathSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPathSets',
            False, 
            [
            _MetaInfoClassMember('as-path-set', REFERENCE_LIST, 'AsPathSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AsPathSets.AsPathSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'as_path_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'as-path-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.TagSets.TagSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.TagSets.TagSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-tag-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Tag Set
                ''',
                'rpl_tag_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'tag-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.TagSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.TagSets',
            False, 
            [
            _MetaInfoClassMember('tag-set', REFERENCE_LIST, 'TagSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.TagSets.TagSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'tag_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'tag-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-cfg', True),
            _MetaInfoClassMember('rpl-extended-community-rt-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Extended Community RT Set
                ''',
                'rpl_extended_community_rt_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-rt-set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRtSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRtSets',
            False, 
            [
            _MetaInfoClassMember('extended-community-rt-set', REFERENCE_LIST, 'ExtendedCommunityRtSet' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet', 
                [], [], 
                '''                Information about an individual set
                ''',
                'extended_community_rt_set',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'extended-community-rt-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets',
            False, 
            [
            _MetaInfoClassMember('append-extended-community-opaque-sets', REFERENCE_CLASS, 'AppendExtendedCommunityOpaqueSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets', 
                [], [], 
                '''                Information about Opaque sets
                ''',
                'append_extended_community_opaque_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('append-extended-community-seg-nh-sets', REFERENCE_CLASS, 'AppendExtendedCommunitySegNhSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets', 
                [], [], 
                '''                Information about SegNH sets
                ''',
                'append_extended_community_seg_nh_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('append-ospf-area-sets', REFERENCE_CLASS, 'AppendOspfAreaSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AppendOspfAreaSets', 
                [], [], 
                '''                Information about OSPF Area sets
                ''',
                'append_ospf_area_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('as-path-sets', REFERENCE_CLASS, 'AsPathSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.AsPathSets', 
                [], [], 
                '''                Information about AS Path sets
                ''',
                'as_path_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('community-sets', REFERENCE_CLASS, 'CommunitySets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.CommunitySets', 
                [], [], 
                '''                Information about Community sets
                ''',
                'community_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-bandwidth-sets', REFERENCE_CLASS, 'ExtendedCommunityBandwidthSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityBandwidthSets', 
                [], [], 
                '''                Information about Bandwidth sets
                ''',
                'extended_community_bandwidth_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-cost-sets', REFERENCE_CLASS, 'ExtendedCommunityCostSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityCostSets', 
                [], [], 
                '''                Information about Cost sets
                ''',
                'extended_community_cost_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-opaque-sets', REFERENCE_CLASS, 'ExtendedCommunityOpaqueSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityOpaqueSets', 
                [], [], 
                '''                Information about Opaque sets
                ''',
                'extended_community_opaque_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-rt-sets', REFERENCE_CLASS, 'ExtendedCommunityRtSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunityRtSets', 
                [], [], 
                '''                Information about RT sets
                ''',
                'extended_community_rt_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-seg-nh-sets', REFERENCE_CLASS, 'ExtendedCommunitySegNhSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySegNhSets', 
                [], [], 
                '''                Information about SegNH sets
                ''',
                'extended_community_seg_nh_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('extended-community-soo-sets', REFERENCE_CLASS, 'ExtendedCommunitySooSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.ExtendedCommunitySooSets', 
                [], [], 
                '''                Information about SOO sets
                ''',
                'extended_community_soo_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('ospf-area-sets', REFERENCE_CLASS, 'OspfAreaSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.OspfAreaSets', 
                [], [], 
                '''                Information about OSPF Area sets
                ''',
                'ospf_area_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('policy-global-set-table', REFERENCE_CLASS, 'PolicyGlobalSetTable' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PolicyGlobalSetTable', 
                [], [], 
                '''                Information about PolicyGlobal sets
                ''',
                'policy_global_set_table',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('prefix-sets', REFERENCE_CLASS, 'PrefixSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrefixSets', 
                [], [], 
                '''                Information about Prefix sets
                ''',
                'prefix_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('prepend-extended-community-opaque-sets', REFERENCE_CLASS, 'PrependExtendedCommunityOpaqueSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets', 
                [], [], 
                '''                Information about Opaque sets
                ''',
                'prepend_extended_community_opaque_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('prepend-extended-community-seg-nh-sets', REFERENCE_CLASS, 'PrependExtendedCommunitySegNhSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets', 
                [], [], 
                '''                Information about SegNH sets
                ''',
                'prepend_extended_community_seg_nh_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('prepend-ospf-area-sets', REFERENCE_CLASS, 'PrependOspfAreaSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.PrependOspfAreaSets', 
                [], [], 
                '''                Information about OSPF Area sets
                ''',
                'prepend_ospf_area_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('rd-sets', REFERENCE_CLASS, 'RdSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RdSets', 
                [], [], 
                '''                Information about RD sets
                ''',
                'rd_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('remove-extended-community-opaque-sets', REFERENCE_CLASS, 'RemoveExtendedCommunityOpaqueSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets', 
                [], [], 
                '''                Information about Opaque sets
                ''',
                'remove_extended_community_opaque_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('remove-extended-community-seg-nh-sets', REFERENCE_CLASS, 'RemoveExtendedCommunitySegNhSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets', 
                [], [], 
                '''                Information about SegNH sets
                ''',
                'remove_extended_community_seg_nh_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('remove-ospf-area-sets', REFERENCE_CLASS, 'RemoveOspfAreaSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.RemoveOspfAreaSets', 
                [], [], 
                '''                Information about OSPF Area sets
                ''',
                'remove_ospf_area_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('tag-sets', REFERENCE_CLASS, 'TagSets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets.TagSets', 
                [], [], 
                '''                Information about Tag sets
                ''',
                'tag_sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy.Limits' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Limits',
            False, 
            [
            _MetaInfoClassMember('maximum-lines-of-policy', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Maximum number of lines of policy configuration
                that may be configured in total
                ''',
                'maximum_lines_of_policy',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('maximum-number-of-policies', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Maximum number of policies that may be
                configured
                ''',
                'maximum_number_of_policies',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'limits',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
    'RoutingPolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy',
            False, 
            [
            _MetaInfoClassMember('editor', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                'emacs' or 'vim' or 'nano'
                ''',
                'editor',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('limits', REFERENCE_CLASS, 'Limits' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Limits', 
                [], [], 
                '''                Limits for Routing Policy
                ''',
                'limits',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('route-policies', REFERENCE_CLASS, 'RoutePolicies' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.RoutePolicies', 
                [], [], 
                '''                All configured policies
                ''',
                'route_policies',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets' , 'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg', 'RoutingPolicy.Sets', 
                [], [], 
                '''                All configured sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-cfg', False),
            ],
            'Cisco-IOS-XR-policy-repository-cfg',
            'routing-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-cfg'],
        'ydk.models.policy.Cisco_IOS_XR_policy_repository_cfg'
        ),
    },
}
_meta_table['RoutingPolicy.RoutePolicies.RoutePolicy']['meta_info'].parent =_meta_table['RoutingPolicy.RoutePolicies']['meta_info']
_meta_table['RoutingPolicy.Sets.PrefixSets.PrefixSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.PrefixSets']['meta_info']
_meta_table['RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets.AppendExtendedCommunityOpaqueSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets']['meta_info']
_meta_table['RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets.AppendExtendedCommunitySegNhSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets']['meta_info']
_meta_table['RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets.RemoveExtendedCommunityOpaqueSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets.ExtendedCommunityOpaqueSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets']['meta_info']
_meta_table['RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets.RemoveExtendedCommunitySegNhSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets']['meta_info']
_meta_table['RoutingPolicy.Sets.RemoveOspfAreaSets.RemoveOspfAreaSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.RemoveOspfAreaSets']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfAreaSets.OspfAreaSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfAreaSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets.ExtendedCommunityCostSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets.ExtendedCommunitySooSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets.PrependExtendedCommunityOpaqueSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets.ExtendedCommunitySegNhSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets']['meta_info']
_meta_table['RoutingPolicy.Sets.RdSets.RdSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.RdSets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets.PrependExtendedCommunitySegNhSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets.ExtendedCommunityBandwidthSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets']['meta_info']
_meta_table['RoutingPolicy.Sets.CommunitySets.CommunitySet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.CommunitySets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrependOspfAreaSets.PrependOspfAreaSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.PrependOspfAreaSets']['meta_info']
_meta_table['RoutingPolicy.Sets.AppendOspfAreaSets.AppendOspfAreaSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AppendOspfAreaSets']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPathSets.AsPathSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPathSets']['meta_info']
_meta_table['RoutingPolicy.Sets.TagSets.TagSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.TagSets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets.ExtendedCommunityRtSet']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrefixSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.AppendExtendedCommunityOpaqueSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.AppendExtendedCommunitySegNhSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.RemoveExtendedCommunityOpaqueSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaqueSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.RemoveExtendedCommunitySegNhSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.RemoveOspfAreaSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfAreaSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCostSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySooSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrependExtendedCommunityOpaqueSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNhSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.RdSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.PolicyGlobalSetTable']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrependExtendedCommunitySegNhSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidthSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.CommunitySets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.PrependOspfAreaSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.AppendOspfAreaSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPathSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.TagSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRtSets']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.RoutePolicies']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Sets']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Limits']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
