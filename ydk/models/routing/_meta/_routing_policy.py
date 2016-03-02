


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'DefaultPolicyType_Enum' : _MetaInfoEnum('DefaultPolicyType_Enum', 'ydk.models.routing.routing_policy',
        {
            'ACCEPT-ROUTE':'ACCEPT_ROUTE',
            'REJECT-ROUTE':'REJECT_ROUTE',
        }, 'routing-policy', _yang_ns._namespaces['routing-policy']),
    'RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the neighbor set member
                ''',
                'address',
                'routing-policy', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the neighbor set member
                        ''',
                        'address',
                        'routing-policy', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the neighbor set member
                        ''',
                        'address',
                        'routing-policy', True),
                ]),
            ],
            'routing-policy',
            'neighbor',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', True),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor', 
                [], [], 
                '''                list of addresses that are part of the neighbor set
                ''',
                'neighbor',
                'routing-policy', False),
            ],
            'routing-policy',
            'neighbor-set',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.NeighborSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.NeighborSets',
            False, 
            [
            _MetaInfoClassMember('neighbor-set', REFERENCE_LIST, 'NeighborSet' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.NeighborSets.NeighborSet', 
                [], [], 
                '''                Definitions for neighbor sets
                ''',
                'neighbor_set',
                'routing-policy', False),
            ],
            'routing-policy',
            'neighbor-sets',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
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
                'routing-policy', True, [
                    _MetaInfoClassMember('ip-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        The prefix member in CIDR notation -- while the
                        prefix may be either IPv4 or IPv6, most
                        implementations require all members of the prefix set
                        to be the same address family.  Mixing address types in
                        the same prefix set is likely to cause an error.
                        ''',
                        'ip_prefix',
                        'routing-policy', True),
                    _MetaInfoClassMember('ip-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        The prefix member in CIDR notation -- while the
                        prefix may be either IPv4 or IPv6, most
                        implementations require all members of the prefix set
                        to be the same address family.  Mixing address types in
                        the same prefix set is likely to cause an error.
                        ''',
                        'ip_prefix',
                        'routing-policy', True),
                ]),
            _MetaInfoClassMember('masklength-range', ATTRIBUTE, 'str' , None, None, 
                [], ['^([0-9]+\\.\\.[0-9]+)|exact$'], 
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
                'routing-policy', True),
            ],
            'routing-policy',
            'prefix',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', True),
            _MetaInfoClassMember('prefix', REFERENCE_LIST, 'Prefix' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix', 
                [], [], 
                '''                List of prefix expressions that are part of the set
                ''',
                'prefix',
                'routing-policy', False),
            ],
            'routing-policy',
            'prefix-set',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.PrefixSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.PrefixSets',
            False, 
            [
            _MetaInfoClassMember('prefix-set', REFERENCE_LIST, 'PrefixSet' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.PrefixSets.PrefixSet', 
                [], [], 
                '''                List of the defined prefix sets
                ''',
                'prefix_set',
                'routing-policy', False),
            ],
            'routing-policy',
            'prefix-sets',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', True, [
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [(0, 4294967295)], [], 
                        '''                        Value of the tag set member
                        ''',
                        'value',
                        'routing-policy', True),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                        [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Value of the tag set member
                        ''',
                        'value',
                        'routing-policy', True),
                ]),
            ],
            'routing-policy',
            'tag',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', True),
            _MetaInfoClassMember('tag', REFERENCE_LIST, 'Tag' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.TagSets.TagSet.Tag', 
                [], [], 
                '''                list of tags that are part of the tag set
                ''',
                'tag',
                'routing-policy', False),
            ],
            'routing-policy',
            'tag-set',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets.TagSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets.TagSets',
            False, 
            [
            _MetaInfoClassMember('tag-set', REFERENCE_LIST, 'TagSet' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.TagSets.TagSet', 
                [], [], 
                '''                Definitions for tag sets
                ''',
                'tag_set',
                'routing-policy', False),
            ],
            'routing-policy',
            'tag-sets',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.DefinedSets' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.DefinedSets',
            False, 
            [
            _MetaInfoClassMember('neighbor-sets', REFERENCE_CLASS, 'NeighborSets' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.NeighborSets', 
                [], [], 
                '''                Enclosing container for defined neighbor sets for matching
                ''',
                'neighbor_sets',
                'routing-policy', False),
            _MetaInfoClassMember('prefix-sets', REFERENCE_CLASS, 'PrefixSets' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.PrefixSets', 
                [], [], 
                '''                Enclosing container for defined prefix sets for matching
                ''',
                'prefix_sets',
                'routing-policy', False),
            _MetaInfoClassMember('tag-sets', REFERENCE_CLASS, 'TagSets' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets.TagSets', 
                [], [], 
                '''                Enclosing container for defined tag sets for matching
                ''',
                'tag_sets',
                'routing-policy', False),
            ],
            'routing-policy',
            'defined-sets',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', False, [
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'int' , None, None, 
                        [(0, 4294967295)], [], 
                        '''                        Set the tag value for OSPF or IS-IS routes.
                        ''',
                        'set_tag',
                        'routing-policy', False),
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'str' , None, None, 
                        [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Set the tag value for OSPF or IS-IS routes.
                        ''',
                        'set_tag',
                        'routing-policy', False),
                ]),
            ],
            'routing-policy',
            'igp-actions',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', False),
            _MetaInfoClassMember('igp-actions', REFERENCE_CLASS, 'IgpActions' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions', 
                [], [], 
                '''                Actions to set IGP route attributes; these actions
                apply to multiple IGPs
                ''',
                'igp_actions',
                'routing-policy', False),
            _MetaInfoClassMember('reject-route', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                rejects the route
                ''',
                'reject_route',
                'routing-policy', False),
            ],
            'routing-policy',
            'actions',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions',
            False, 
            [
            ],
            'routing-policy',
            'igp-conditions',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet',
            False, 
            [
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsRestrictedType_Enum' , 'ydk.models.policy.policy_types', 'MatchSetOptionsRestrictedType_Enum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation.  This leaf only supports matching on ANY
                member of the set or inverting the match.  Matching on ALL is
                not supported)
                ''',
                'match_set_options',
                'routing-policy', False),
            _MetaInfoClassMember('neighbor-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined neighbor set
                ''',
                'neighbor_set',
                'routing-policy', False),
            ],
            'routing-policy',
            'match-neighbor-set',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet',
            False, 
            [
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsRestrictedType_Enum' , 'ydk.models.policy.policy_types', 'MatchSetOptionsRestrictedType_Enum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation.  This leaf only supports matching on ANY
                member of the set or inverting the match.  Matching on ALL is
                not supported)
                ''',
                'match_set_options',
                'routing-policy', False),
            _MetaInfoClassMember('prefix-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined prefix set
                ''',
                'prefix_set',
                'routing-policy', False),
            ],
            'routing-policy',
            'match-prefix-set',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet',
            False, 
            [
            _MetaInfoClassMember('match-set-options', REFERENCE_ENUM_CLASS, 'MatchSetOptionsRestrictedType_Enum' , 'ydk.models.policy.policy_types', 'MatchSetOptionsRestrictedType_Enum', 
                [], [], 
                '''                Optional parameter that governs the behaviour of the
                match operation.  This leaf only supports matching on ANY
                member of the set or inverting the match.  Matching on ALL is
                not supported)
                ''',
                'match_set_options',
                'routing-policy', False),
            _MetaInfoClassMember('tag-set', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                References a defined tag set
                ''',
                'tag_set',
                'routing-policy', False),
            ],
            'routing-policy',
            'match-tag-set',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions',
            False, 
            [
            _MetaInfoClassMember('call-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Applies the statements from the specified policy
                definition and then returns control the current
                policy statement. Note that the called policy may
                itself call other policies (subject to
                implementation limitations). This is intended to
                provide a policy 'subroutine' capability.  The
                called policy should contain an explicit or a
                default route disposition that returns an effective
                true (accept-route) or false (reject-route),
                otherwise the behavior may be ambiguous and
                implementation dependent
                ''',
                'call_policy',
                'routing-policy', False),
            _MetaInfoClassMember('igp-conditions', REFERENCE_CLASS, 'IgpConditions' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions', 
                [], [], 
                '''                Policy conditions for IGP attributes
                ''',
                'igp_conditions',
                'routing-policy', False),
            _MetaInfoClassMember('install-protocol-eq', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Condition to check the protocol / method used to install
                which installed the route into the local routing table
                ''',
                'install_protocol_eq',
                'routing-policy', False),
            _MetaInfoClassMember('match-neighbor-set', REFERENCE_CLASS, 'MatchNeighborSet' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet', 
                [], [], 
                '''                Match a referenced neighbor set according to the logic
                defined in the match-set-options-leaf
                ''',
                'match_neighbor_set',
                'routing-policy', False),
            _MetaInfoClassMember('match-prefix-set', REFERENCE_CLASS, 'MatchPrefixSet' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet', 
                [], [], 
                '''                Match a referenced prefix-set according to the logic
                defined in the match-set-options leaf
                ''',
                'match_prefix_set',
                'routing-policy', False),
            _MetaInfoClassMember('match-tag-set', REFERENCE_CLASS, 'MatchTagSet' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet', 
                [], [], 
                '''                Match a referenced tag set according to the logic defined
                in the match-options-set leaf
                ''',
                'match_tag_set',
                'routing-policy', False),
            ],
            'routing-policy',
            'conditions',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', True),
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions', 
                [], [], 
                '''                Action statements for this policy
                statement
                ''',
                'actions',
                'routing-policy', False),
            _MetaInfoClassMember('conditions', REFERENCE_CLASS, 'Conditions' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions', 
                [], [], 
                '''                Condition statements for this
                policy statement
                ''',
                'conditions',
                'routing-policy', False),
            ],
            'routing-policy',
            'statement',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements',
            False, 
            [
            _MetaInfoClassMember('statement', REFERENCE_LIST, 'Statement' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement', 
                [], [], 
                '''                Policy statements group conditions and actions within
                a policy definition.  They are evaluated in the order
                specified (see the description of policy evaluation
                at the top of this module.
                ''',
                'statement',
                'routing-policy', False),
            ],
            'routing-policy',
            'statements',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
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
                'routing-policy', True),
            _MetaInfoClassMember('statements', REFERENCE_CLASS, 'Statements' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements', 
                [], [], 
                '''                Enclosing container for policy statements
                ''',
                'statements',
                'routing-policy', False),
            ],
            'routing-policy',
            'policy-definition',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy.PolicyDefinitions' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy.PolicyDefinitions',
            False, 
            [
            _MetaInfoClassMember('policy-definition', REFERENCE_LIST, 'PolicyDefinition' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions.PolicyDefinition', 
                [], [], 
                '''                List of top-level policy definitions, keyed by unique
                name.  These policy definitions are expected to be
                referenced (by name) in policy chains specified in import/
                export configuration statements.
                ''',
                'policy_definition',
                'routing-policy', False),
            ],
            'routing-policy',
            'policy-definitions',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
    'RoutingPolicy' : {
        'meta_info' : _MetaInfoClass('RoutingPolicy',
            False, 
            [
            _MetaInfoClassMember('defined-sets', REFERENCE_CLASS, 'DefinedSets' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.DefinedSets', 
                [], [], 
                '''                Predefined sets of attributes used in policy match
                statements
                ''',
                'defined_sets',
                'routing-policy', False),
            _MetaInfoClassMember('policy-definitions', REFERENCE_CLASS, 'PolicyDefinitions' , 'ydk.models.routing.routing_policy', 'RoutingPolicy.PolicyDefinitions', 
                [], [], 
                '''                Enclosing container for the list of top-level policy
                definitions
                ''',
                'policy_definitions',
                'routing-policy', False),
            ],
            'routing-policy',
            'routing-policy',
            _yang_ns._namespaces['routing-policy'],
        'ydk.models.routing.routing_policy'
        ),
    },
}
_meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet.Neighbor']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.NeighborSets.NeighborSet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.NeighborSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet.Prefix']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.PrefixSets.PrefixSet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.PrefixSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet.Tag']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.TagSets.TagSet']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets.TagSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.NeighborSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.PrefixSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets']['meta_info']
_meta_table['RoutingPolicy.DefinedSets.TagSets']['meta_info'].parent =_meta_table['RoutingPolicy.DefinedSets']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions.IgpActions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.IgpConditions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchNeighborSet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchPrefixSet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions.MatchTagSet']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Actions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement.Conditions']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements.Statement']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition.Statements']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions.PolicyDefinition']['meta_info'].parent =_meta_table['RoutingPolicy.PolicyDefinitions']['meta_info']
_meta_table['RoutingPolicy.DefinedSets']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
_meta_table['RoutingPolicy.PolicyDefinitions']['meta_info'].parent =_meta_table['RoutingPolicy']['meta_info']
