


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AddressFamilyEnum' : _MetaInfoEnum('AddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'l2vpn':'l2vpn',
            'ls':'ls',
            'af-none':'af_none',
            'af-unknown':'af_unknown',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper']),
    'ObjectStatusEnum' : _MetaInfoEnum('ObjectStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
        {
            'active':'active',
            'inactive':'inactive',
            'unused':'unused',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper']),
    'AttachPointDirectionEnum' : _MetaInfoEnum('AttachPointDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
        {
            'in':'in_',
            'out':'out',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper']),
    'SubAddressFamilyEnum' : _MetaInfoEnum('SubAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'label':'label',
            'tunnel':'tunnel',
            'vpn':'vpn',
            'mdt':'mdt',
            'vpls':'vpls',
            'rt-constraint':'rt_constraint',
            'mvpn':'mvpn',
            'flow':'flow',
            'vpn-mcast':'vpn_mcast',
            'saf-none':'saf_none',
            'saf-unknown':'saf_unknown',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper']),
    'GroupEnum' : _MetaInfoEnum('GroupEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper',
        {
            'address-family-group':'address_family_group',
            'session-group':'session_group',
            'neighbor-group':'neighbor_group',
            'neighbor':'neighbor',
            'error-group':'error_group',
        }, 'Cisco-IOS-XR-policy-repository-oper', _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper']),
    'RoutingPolicy.Limits' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Limits',
            False, 
            [
            _MetaInfoClassMember('compiled-policies-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total compiled length of all policies
                ''',
                'compiled_policies_length',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('current-lines-of-policy-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of lines of configuration for
                policies/sets currently allowed
                ''',
                'current_lines_of_policy_limit',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('current-lines-of-policy-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current number of lines configured for all
                policies and sets
                ''',
                'current_lines_of_policy_used',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('current-number-of-policies-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of policies currently allowed
                ''',
                'current_number_of_policies_limit',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('current-number-of-policies-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current number of policies configured
                ''',
                'current_number_of_policies_used',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('maximum-lines-of-policy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum lines of configuration allowable for all
                policies and sets
                ''',
                'maximum_lines_of_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('maximum-number-of-policies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of policies allowable
                ''',
                'maximum_number_of_policies',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'limits',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'directly-used-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets',
            False, 
            [
            _MetaInfoClassMember('set-domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain of sets
                ''',
                'set_domain',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('set-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Names of sets in this domain
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_LIST, 'Sets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets', 
                [], [], 
                '''                List of sets in several domains
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'all-used-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets',
            False, 
            [
            _MetaInfoClassMember('set-domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Domain of sets
                ''',
                'set_domain',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('set-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Names of sets in this domain
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets',
            False, 
            [
            _MetaInfoClassMember('sets', REFERENCE_LIST, 'Sets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets', 
                [], [], 
                '''                List of sets in several domains
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'directly-used-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'all-used-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses',
            False, 
            [
            _MetaInfoClassMember('all-used-policies', REFERENCE_CLASS, 'AllUsedPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies', 
                [], [], 
                '''                Policies used by this policy, or by policies
                that it uses
                ''',
                'all_used_policies',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('all-used-sets', REFERENCE_CLASS, 'AllUsedSets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets', 
                [], [], 
                '''                Sets used by this policy, or by policies
                that it uses
                ''',
                'all_used_sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('directly-used-policies', REFERENCE_CLASS, 'DirectlyUsedPolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies', 
                [], [], 
                '''                Policies that this policy uses directly
                ''',
                'directly_used_policies',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('directly-used-sets', REFERENCE_CLASS, 'DirectlyUsedSets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets', 
                [], [], 
                '''                Sets that this policy uses directly
                ''',
                'directly_used_sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'policy-uses',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies.RoutePolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies.RoutePolicy',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('policy-uses', REFERENCE_CLASS, 'PolicyUses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses', 
                [], [], 
                '''                Information about which policies and sets
                this policy uses
                ''',
                'policy_uses',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'route-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.RoutePolicies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.RoutePolicies',
            False, 
            [
            _MetaInfoClassMember('route-policy', REFERENCE_LIST, 'RoutePolicy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies.RoutePolicy', 
                [], [], 
                '''                Information about an individual policy
                ''',
                'route_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'route-policies',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Policies' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Policies',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policies', REFERENCE_CLASS, 'RoutePolicies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.RoutePolicies', 
                [], [], 
                '''                Information about individual policies
                ''',
                'route_policies',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'policies',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Etag' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Etag',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'etag',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.OspfArea' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.OspfArea',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'ospf-area',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityOpaque' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityOpaque',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-opaque',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySegNh' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySegNh',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-seg-nh',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunitySoo' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunitySoo',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-soo',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Tag' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Tag',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'tag',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Prefix' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Prefix',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Community' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Community',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'community',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.AsPath' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.AsPath',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'as-path',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Esi' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Esi',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'esi',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityBandwidth' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityBandwidth',
            False, 
            [
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-bandwidth',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityRt' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityRt',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-rt',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Rd' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Rd',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'rd',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.Mac' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.Mac',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of policy
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ObjectStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'ObjectStatusEnum', 
                [], [], 
                '''                Active, Inactive, or Unused
                ''',
                'status',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-directly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the policy uses this object directly or
                indirectly
                ''',
                'used_directly',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'reference',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy',
            False, 
            [
            _MetaInfoClassMember('reference', REFERENCE_LIST, 'Reference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference', 
                [], [], 
                '''                Information about policies referring to this
                object
                ''',
                'reference',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'used-by',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Address Family Identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('aggregate-network-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Aggregate IP address or Network IP Address      
                in IPv4 or IPv6 Format
                ''',
                'aggregate_network_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF Area ID in Decimal Integer Format
                ''',
                'area_id',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attach-point', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of attach point where policy is attached
                ''',
                'attach_point',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('attached-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The attached policy that (maybe indirectly) uses
                the object in question
                ''',
                'attached_policy',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'AttachPointDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AttachPointDirectionEnum', 
                [], [], 
                '''                Direction In or Out
                ''',
                'direction',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group', REFERENCE_ENUM_CLASS, 'GroupEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'GroupEnum', 
                [], [], 
                '''                Neighbor Group 
                ''',
                'group',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor Group Name
                ''',
                'group_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance
                ''',
                'instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP Address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('neighbor-af-name', REFERENCE_ENUM_CLASS, 'AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'AddressFamilyEnum', 
                [], [], 
                '''                Neighbor IP Address Family
                ''',
                'neighbor_af_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-from', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate From Level
                ''',
                'propogate_from',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('propogate-to', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ISIS Propogate To Level
                ''',
                'propogate_to',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('proto-instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol instance
                ''',
                'proto_instance',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol to which policy attached
                ''',
                'protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy that uses object in question
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'SubAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'SubAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family Identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('source-protocol', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Protocol to redistribute,                
                Source Protocol can be one of the following
                values                               {all,
                connected, local, static, bgp, rip, isis, ospf, 
                ospfv3, eigrp, unknown }
                ''',
                'source_protocol',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'binding',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached',
            False, 
            [
            _MetaInfoClassMember('binding', REFERENCE_LIST, 'Binding' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding', 
                [], [], 
                '''                bindings list
                ''',
                'binding',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'attached',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set',
            False, 
            [
            _MetaInfoClassMember('set-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Set name
                ''',
                'set_name',
                'Cisco-IOS-XR-policy-repository-oper', True),
            _MetaInfoClassMember('attached', REFERENCE_CLASS, 'Attached' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached', 
                [], [], 
                '''                Information about where this policy or set is
                attached
                ''',
                'attached',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('used-by', REFERENCE_CLASS, 'UsedBy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy', 
                [], [], 
                '''                Policies that use this object, directly or
                indirectly
                ''',
                'used_by',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'set',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Sets_',
            False, 
            [
            _MetaInfoClassMember('set', REFERENCE_LIST, 'Set' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set', 
                [], [], 
                '''                Information about an individual set
                ''',
                'set',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Unused' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Unused',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'unused',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Inactive' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Inactive',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'inactive',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost.Active' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost.Active',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Policy objects
                ''',
                'object',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'active',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets.ExtendedCommunityCost' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets.ExtendedCommunityCost',
            False, 
            [
            _MetaInfoClassMember('active', REFERENCE_CLASS, 'Active' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Active', 
                [], [], 
                '''                All objects of a given type that are attached to
                a protocol
                ''',
                'active',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('inactive', REFERENCE_CLASS, 'Inactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Inactive', 
                [], [], 
                '''                All objects of a given type that are not
                attached to a protocol
                ''',
                'inactive',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Sets_', 
                [], [], 
                '''                Information about individual sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('unused', REFERENCE_CLASS, 'Unused' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost.Unused', 
                [], [], 
                '''                All objects of a given type that are not
                referenced at all
                ''',
                'unused',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'extended-community-cost',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy.Sets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.Sets',
            False, 
            [
            _MetaInfoClassMember('as-path', REFERENCE_CLASS, 'AsPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.AsPath', 
                [], [], 
                '''                Information about AS Path sets
                ''',
                'as_path',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('community', REFERENCE_CLASS, 'Community' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Community', 
                [], [], 
                '''                Information about Community sets
                ''',
                'community',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('esi', REFERENCE_CLASS, 'Esi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Esi', 
                [], [], 
                '''                Information about Esi sets
                ''',
                'esi',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('etag', REFERENCE_CLASS, 'Etag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Etag', 
                [], [], 
                '''                Information about Etag sets
                ''',
                'etag',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('extended-community-bandwidth', REFERENCE_CLASS, 'ExtendedCommunityBandwidth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityBandwidth', 
                [], [], 
                '''                Information about Extended Community Bandwidth
                sets
                ''',
                'extended_community_bandwidth',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('extended-community-cost', REFERENCE_CLASS, 'ExtendedCommunityCost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityCost', 
                [], [], 
                '''                Information about Extended Community Cost sets
                ''',
                'extended_community_cost',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('extended-community-opaque', REFERENCE_CLASS, 'ExtendedCommunityOpaque' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityOpaque', 
                [], [], 
                '''                Information about Extended Community Opaque
                sets
                ''',
                'extended_community_opaque',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('extended-community-rt', REFERENCE_CLASS, 'ExtendedCommunityRt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunityRt', 
                [], [], 
                '''                Information about Extended Community RT sets
                ''',
                'extended_community_rt',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('extended-community-seg-nh', REFERENCE_CLASS, 'ExtendedCommunitySegNh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySegNh', 
                [], [], 
                '''                Information about Extended Community SegNH sets
                ''',
                'extended_community_seg_nh',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('extended-community-soo', REFERENCE_CLASS, 'ExtendedCommunitySoo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.ExtendedCommunitySoo', 
                [], [], 
                '''                Information about Extended Community SOO sets
                ''',
                'extended_community_soo',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Mac', 
                [], [], 
                '''                Information about Mac sets
                ''',
                'mac',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('ospf-area', REFERENCE_CLASS, 'OspfArea' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.OspfArea', 
                [], [], 
                '''                Information about OSPF Area sets
                ''',
                'ospf_area',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('prefix', REFERENCE_CLASS, 'Prefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Prefix', 
                [], [], 
                '''                Information about AS Path sets
                ''',
                'prefix',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('rd', REFERENCE_CLASS, 'Rd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Rd', 
                [], [], 
                '''                Information about RD sets
                ''',
                'rd',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('tag', REFERENCE_CLASS, 'Tag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets.Tag', 
                [], [], 
                '''                Information about Tag sets
                ''',
                'tag',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'sets',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
    'RoutingPolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy',
            False, 
            [
            _MetaInfoClassMember('limits', REFERENCE_CLASS, 'Limits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Limits', 
                [], [], 
                '''                Information about configured limits and the
                current values
                ''',
                'limits',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('policies', REFERENCE_CLASS, 'Policies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Policies', 
                [], [], 
                '''                Information about configured route policies
                ''',
                'policies',
                'Cisco-IOS-XR-policy-repository-oper', False),
            _MetaInfoClassMember('sets', REFERENCE_CLASS, 'Sets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper', 'RoutingPolicy.Sets', 
                [], [], 
                '''                Information about configured sets
                ''',
                'sets',
                'Cisco-IOS-XR-policy-repository-oper', False),
            ],
            'Cisco-IOS-XR-policy-repository-oper',
            'routing-policy',
            _yang_ns._namespaces['Cisco-IOS-XR-policy-repository-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_policy_repository_oper'
        ),
    },
}
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets.Sets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets.Sets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedPolicies']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedSets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.DirectlyUsedSets']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses.AllUsedPolicies']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.PolicyUses']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies.RoutePolicy']['meta_info'].parent =_meta_table['RoutingPolicy.Policies.RoutePolicies']['meta_info']
_meta_table['RoutingPolicy.Policies.RoutePolicies']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Policies.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Policies.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Policies.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Policies']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Etag']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Tag']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Prefix']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.Community.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Community']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.AsPath']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Esi']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Rd']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.Mac']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy.Reference']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached.Binding']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.UsedBy']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set.Attached']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_.Set']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Sets_']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Unused']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Inactive']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost.Active']['meta_info'].parent =_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info']
_meta_table['RoutingPolicy.Sets.Etag']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.OspfArea']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityOpaque']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySegNh']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunitySoo']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Tag']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Prefix']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Community']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.AsPath']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Esi']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityBandwidth']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityRt']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Rd']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.Mac']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Sets.ExtendedCommunityCost']['meta_info'].parent =_meta_table['RoutingPolicy.Sets']['meta_info']
_meta_table['RoutingPolicy.Limits']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Policies']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.Sets']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
