


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IgmpFilterEnum' : _MetaInfoEnum('IgmpFilterEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg',
        {
            'include':'include',
            'exclude':'exclude',
            'star-g':'star_g',
        }, 'Cisco-IOS-XR-ipv4-igmp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg']),
    'Igmp.Vrfs.Vrf.Traffic' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Traffic',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure the route-policy profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup',
            False, 
            [
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.SsmAccessGroups' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.SsmAccessGroups',
            False, 
            [
            _MetaInfoClassMember('ssm-access-group', REFERENCE_LIST, 'SsmAccessGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup', 
                [], [], 
                '''                SSM static Access Group
                ''',
                'ssm_access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Maximum' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Maximum',
            False, 
            [
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure maximum number of groups accepted by
                this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Optional IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups',
            False, 
            [
            _MetaInfoClassMember('join-group', REFERENCE_LIST, 'JoinGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-group-source-address', REFERENCE_LIST, 'JoinGroupSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses',
            False, 
            [
            _MetaInfoClassMember('static-group-group-address', REFERENCE_LIST, 'StaticGroupGroupAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True),
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-groups', REFERENCE_CLASS, 'JoinGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups', 
                [], [], 
                '''                IGMP join multicast group
                ''',
                'join_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-addresses', REFERENCE_CLASS, 'StaticGroupGroupAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses', 
                [], [], 
                '''                IGMP static multicast group
                ''',
                'static_group_group_addresses',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name for this vrf
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.InheritableDefaults', 
                [], [], 
                '''                Inheritable Defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Interfaces', 
                [], [], 
                '''                Interface-level configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Maximum', 
                [], [], 
                '''                Configure IGMP State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('robustness', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Configure IGMP Robustness variable
                ''',
                'robustness',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssm-access-groups', REFERENCE_CLASS, 'SsmAccessGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.SsmAccessGroups', 
                [], [], 
                '''                IGMP Source specific mode
                ''',
                'ssm_access_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssmdns-query-group', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SSM mapping using DNS Query
                ''',
                'ssmdns_query_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf.Traffic', 
                [], [], 
                '''                Configure IGMP Traffic variables
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.Vrfs' : {
        'meta_info' : _MetaInfoClass('Igmp.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs.Vrf', 
                [], [], 
                '''                Configuration for a particular vrf
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Nsf' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Nsf',
            False, 
            [
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Maximum time for IGMP NSF mode in seconds
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'nsf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.UnicastQosAdjust' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.UnicastQosAdjust',
            False, 
            [
            _MetaInfoClassMember('adjustment-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Configure the QoS delay before programming (in
                seconds)
                ''',
                'adjustment_delay',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('download-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '500')], [], 
                '''                Configure the QoS download interval (in
                milliseconds)
                ''',
                'download_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('hold-off', ATTRIBUTE, 'int' , None, None, 
                [('5', '1800')], [], 
                '''                Configure the QoS hold off time (in seconds)
                ''',
                'hold_off',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'unicast-qos-adjust',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Accounting' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Accounting',
            False, 
            [
            _MetaInfoClassMember('max-history', ATTRIBUTE, 'int' , None, None, 
                [('0', '365')], [], 
                '''                Configure IGMP accounting Maximum History
                setting
                ''',
                'max_history',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Traffic' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Traffic',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure the route-policy profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.InheritableDefaults.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.InheritableDefaults.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.InheritableDefaults.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup',
            False, 
            [
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.SsmAccessGroups' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.SsmAccessGroups',
            False, 
            [
            _MetaInfoClassMember('ssm-access-group', REFERENCE_LIST, 'SsmAccessGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup', 
                [], [], 
                '''                SSM static Access Group
                ''',
                'ssm_access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Maximum' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Maximum',
            False, 
            [
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure maximum number of groups accepted by
                this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Optional IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.JoinGroups' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.JoinGroups',
            False, 
            [
            _MetaInfoClassMember('join-group', REFERENCE_LIST, 'JoinGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-group-source-address', REFERENCE_LIST, 'JoinGroupSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses',
            False, 
            [
            _MetaInfoClassMember('static-group-group-address', REFERENCE_LIST, 'StaticGroupGroupAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True),
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-groups', REFERENCE_CLASS, 'JoinGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.JoinGroups', 
                [], [], 
                '''                IGMP join multicast group
                ''',
                'join_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-addresses', REFERENCE_CLASS, 'StaticGroupGroupAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses', 
                [], [], 
                '''                IGMP static multicast group
                ''',
                'static_group_group_addresses',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext.Interfaces' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp.DefaultContext' : {
        'meta_info' : _MetaInfoClass('Igmp.DefaultContext',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Accounting', 
                [], [], 
                '''                Configure IGMP accounting for logging
                join/leave records
                ''',
                'accounting',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.InheritableDefaults', 
                [], [], 
                '''                Inheritable Defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Interfaces', 
                [], [], 
                '''                Interface-level configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Maximum', 
                [], [], 
                '''                Configure IGMP State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Nsf', 
                [], [], 
                '''                Configure NSF specific options
                ''',
                'nsf',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('robustness', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Configure IGMP Robustness variable
                ''',
                'robustness',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssm-access-groups', REFERENCE_CLASS, 'SsmAccessGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.SsmAccessGroups', 
                [], [], 
                '''                IGMP Source specific mode
                ''',
                'ssm_access_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssmdns-query-group', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SSM mapping using DNS Query
                ''',
                'ssmdns_query_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.Traffic', 
                [], [], 
                '''                Configure IGMP Traffic variables
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('unicast-qos-adjust', REFERENCE_CLASS, 'UnicastQosAdjust' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext.UnicastQosAdjust', 
                [], [], 
                '''                Configure IGMP QoS shapers for subscriber
                interfaces
                ''',
                'unicast_qos_adjust',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'default-context',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Igmp' : {
        'meta_info' : _MetaInfoClass('Igmp',
            False, 
            [
            _MetaInfoClassMember('default-context', REFERENCE_CLASS, 'DefaultContext' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.DefaultContext', 
                [], [], 
                '''                Default Context
                ''',
                'default_context',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Igmp.Vrfs', 
                [], [], 
                '''                VRF related configuration
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'igmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Amt.RelayAdvAdd' : {
        'meta_info' : _MetaInfoClass('Amt.RelayAdvAdd',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                AMT Relay IPv4 Advertisement Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Relay Advertisement Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'relay-adv-add',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Amt.RelayAnycastPrefix' : {
        'meta_info' : _MetaInfoClass('Amt.RelayAnycastPrefix',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Anycast-Prefix Address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                Mask Length for Anycast Prefix
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'relay-anycast-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Amt' : {
        'meta_info' : _MetaInfoClass('Amt',
            False, 
            [
            _MetaInfoClassMember('amtmtu', ATTRIBUTE, 'int' , None, None, 
                [('100', '65535')], [], 
                '''                Configure AMT Relay MTU
                ''',
                'amtmtu',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('amtqqic', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Configure AMT QQIC value
                ''',
                'amtqqic',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('amttos', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Configure AMT Relay TOS
                ''',
                'amttos',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('amtttl', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Configure AMT Relay TTL
                ''',
                'amtttl',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('gateway-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list for Gateway Filter
                ''',
                'gateway_filter',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-gateway', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Configure AMT maximum number of Gateways
                ''',
                'maximum_gateway',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-v4-route-gateway', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Configure Maximum number of IPv4 route-gateways
                (Tunnels)
                ''',
                'maximum_v4_route_gateway',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-v4-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Configure Maximum number of IPv4 Routes
                ''',
                'maximum_v4_routes',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-v6-route-gateway', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Configure Maximum number of IPv6 route-gateways
                (Tunnels)
                ''',
                'maximum_v6_route_gateway',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-v6-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Configure Maximum number of IPv6 Routes
                ''',
                'maximum_v6_routes',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('relay-adv-add', REFERENCE_CLASS, 'RelayAdvAdd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Amt.RelayAdvAdd', 
                [], [], 
                '''                Configure AMT Relay IPv4 Advertisement Address
                ''',
                'relay_adv_add',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('relay-anycast-prefix', REFERENCE_CLASS, 'RelayAnycastPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Amt.RelayAnycastPrefix', 
                [], [], 
                '''                Configure AMT Relay IPv4 Anycast-Prefix
                ''',
                'relay_anycast_prefix',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'amt',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Traffic' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Traffic',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure the route-policy profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup',
            False, 
            [
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.SsmAccessGroups' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.SsmAccessGroups',
            False, 
            [
            _MetaInfoClassMember('ssm-access-group', REFERENCE_LIST, 'SsmAccessGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup', 
                [], [], 
                '''                SSM static Access Group
                ''',
                'ssm_access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Maximum' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Maximum',
            False, 
            [
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure maximum number of groups accepted by
                this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Optional IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups',
            False, 
            [
            _MetaInfoClassMember('join-group', REFERENCE_LIST, 'JoinGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-group-source-address', REFERENCE_LIST, 'JoinGroupSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses',
            False, 
            [
            _MetaInfoClassMember('static-group-group-address', REFERENCE_LIST, 'StaticGroupGroupAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True),
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-groups', REFERENCE_CLASS, 'JoinGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups', 
                [], [], 
                '''                IGMP join multicast group
                ''',
                'join_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-addresses', REFERENCE_CLASS, 'StaticGroupGroupAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses', 
                [], [], 
                '''                IGMP static multicast group
                ''',
                'static_group_group_addresses',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name for this vrf
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.InheritableDefaults', 
                [], [], 
                '''                Inheritable Defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Interfaces', 
                [], [], 
                '''                Interface-level configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Maximum', 
                [], [], 
                '''                Configure IGMP State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('robustness', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Configure IGMP Robustness variable
                ''',
                'robustness',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssm-access-groups', REFERENCE_CLASS, 'SsmAccessGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.SsmAccessGroups', 
                [], [], 
                '''                IGMP Source specific mode
                ''',
                'ssm_access_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssmdns-query-group', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SSM mapping using DNS Query
                ''',
                'ssmdns_query_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf.Traffic', 
                [], [], 
                '''                Configure IGMP Traffic variables
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.Vrfs' : {
        'meta_info' : _MetaInfoClass('Mld.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs.Vrf', 
                [], [], 
                '''                Configuration for a particular vrf
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Nsf' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Nsf',
            False, 
            [
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Maximum time for IGMP NSF mode in seconds
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'nsf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.UnicastQosAdjust' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.UnicastQosAdjust',
            False, 
            [
            _MetaInfoClassMember('adjustment-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Configure the QoS delay before programming (in
                seconds)
                ''',
                'adjustment_delay',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('download-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '500')], [], 
                '''                Configure the QoS download interval (in
                milliseconds)
                ''',
                'download_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('hold-off', ATTRIBUTE, 'int' , None, None, 
                [('5', '1800')], [], 
                '''                Configure the QoS hold off time (in seconds)
                ''',
                'hold_off',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'unicast-qos-adjust',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Accounting' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Accounting',
            False, 
            [
            _MetaInfoClassMember('max-history', ATTRIBUTE, 'int' , None, None, 
                [('0', '365')], [], 
                '''                Configure IGMP accounting Maximum History
                setting
                ''',
                'max_history',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Traffic' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Traffic',
            False, 
            [
            _MetaInfoClassMember('profile', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure the route-policy profile
                ''',
                'profile',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'traffic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.InheritableDefaults.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.InheritableDefaults.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.InheritableDefaults.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup',
            False, 
            [
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.SsmAccessGroups' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.SsmAccessGroups',
            False, 
            [
            _MetaInfoClassMember('ssm-access-group', REFERENCE_LIST, 'SsmAccessGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup', 
                [], [], 
                '''                SSM static Access Group
                ''',
                'ssm_access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'ssm-access-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Maximum' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Maximum',
            False, 
            [
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure maximum number of groups accepted by
                this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Optional IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Optional IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'IgmpFilterEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'IgmpFilterEnum', 
                [], [], 
                '''                Filter mode
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-group-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.JoinGroups' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.JoinGroups',
            False, 
            [
            _MetaInfoClassMember('join-group', REFERENCE_LIST, 'JoinGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-group-source-address', REFERENCE_LIST, 'JoinGroupSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'join_group_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'join-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask',
            False, 
            [
            _MetaInfoClassMember('group-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP group address
                ''',
                'group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP group address
                        ''',
                        'group_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Group Address
                ''',
                'group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('group-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Group Address
                        ''',
                        'group_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP source address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP source address
                        ''',
                        'source_address',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('source-address-mask', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Mask for Source Address
                ''',
                'source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True, [
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                    _MetaInfoClassMember('source-address-mask', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Mask for Source Address
                        ''',
                        'source_address_mask',
                        'Cisco-IOS-XR-ipv4-igmp-cfg', True),
                ]),
            _MetaInfoClassMember('group-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of groups to join (do not set without
                GroupAddressMask)
                ''',
                'group_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('source-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Number of sources to join (do not set
                without SourceAddressMask)
                ''',
                'source_count',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('suppress-report', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress reports
                ''',
                'suppress_report',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-address-group-address-mask-source-address-source-address-mask',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses',
            False, 
            [
            _MetaInfoClassMember('static-group-group-address', REFERENCE_LIST, 'StaticGroupGroupAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-group-address-mask-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_group_address_mask_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-address-source-address-source-address-mask', REFERENCE_LIST, 'StaticGroupGroupAddressSourceAddressSourceAddressMask' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask', 
                [], [], 
                '''                IP group address and optional source address
                to include
                ''',
                'static_group_group_address_source_address_source_address_mask',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'static-group-group-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                Maximum number of groups accepted per interface
                by this router
                ''',
                'maximum_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '40000')], [], 
                '''                 WarningThreshold for number of groups accepted
                per interface by this router
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'maximum-groups-per-interface-oor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface.ExplicitTracking' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface.ExplicitTracking',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying tracking group range
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or
                FALSE respectively
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'explicit-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-igmp-cfg', True),
            _MetaInfoClassMember('access-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list specifying access group range
                ''',
                'access_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('explicit-tracking', REFERENCE_CLASS, 'ExplicitTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.ExplicitTracking', 
                [], [], 
                '''                IGMPv3 explicit host tracking
                ''',
                'explicit_tracking',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('join-groups', REFERENCE_CLASS, 'JoinGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.JoinGroups', 
                [], [], 
                '''                IGMP join multicast group
                ''',
                'join_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum-groups-per-interface-oor', REFERENCE_CLASS, 'MaximumGroupsPerInterfaceOor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor', 
                [], [], 
                '''                Configure maximum number of groups accepted per
                interface by this router
                ''',
                'maximum_groups_per_interface_oor',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Query interval in seconds
                ''',
                'query_interval',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-max-response-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                Query response value in seconds
                ''',
                'query_max_response_time',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('query-timeout', ATTRIBUTE, 'int' , None, None, 
                [('60', '300')], [], 
                '''                IGMP previous querier timeout
                ''',
                'query_timeout',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('router-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enabled or disabled, when value is TRUE or FALSE
                respectively
                ''',
                'router_enable',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('static-group-group-addresses', REFERENCE_CLASS, 'StaticGroupGroupAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses', 
                [], [], 
                '''                IGMP static multicast group
                ''',
                'static_group_group_addresses',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                Version number
                ''',
                'version',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld.DefaultContext' : {
        'meta_info' : _MetaInfoClass('Mld.DefaultContext',
            False, 
            [
            _MetaInfoClassMember('accounting', REFERENCE_CLASS, 'Accounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Accounting', 
                [], [], 
                '''                Configure IGMP accounting for logging
                join/leave records
                ''',
                'accounting',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.InheritableDefaults', 
                [], [], 
                '''                Inheritable Defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Interfaces', 
                [], [], 
                '''                Interface-level configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Maximum', 
                [], [], 
                '''                Configure IGMP State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Nsf', 
                [], [], 
                '''                Configure NSF specific options
                ''',
                'nsf',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('robustness', ATTRIBUTE, 'int' , None, None, 
                [('2', '10')], [], 
                '''                Configure IGMP Robustness variable
                ''',
                'robustness',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssm-access-groups', REFERENCE_CLASS, 'SsmAccessGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.SsmAccessGroups', 
                [], [], 
                '''                IGMP Source specific mode
                ''',
                'ssm_access_groups',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('ssmdns-query-group', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SSM mapping using DNS Query
                ''',
                'ssmdns_query_group',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('traffic', REFERENCE_CLASS, 'Traffic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.Traffic', 
                [], [], 
                '''                Configure IGMP Traffic variables
                ''',
                'traffic',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('unicast-qos-adjust', REFERENCE_CLASS, 'UnicastQosAdjust' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext.UnicastQosAdjust', 
                [], [], 
                '''                Configure IGMP QoS shapers for subscriber
                interfaces
                ''',
                'unicast_qos_adjust',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'default-context',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
    'Mld' : {
        'meta_info' : _MetaInfoClass('Mld',
            False, 
            [
            _MetaInfoClassMember('default-context', REFERENCE_CLASS, 'DefaultContext' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.DefaultContext', 
                [], [], 
                '''                Default Context
                ''',
                'default_context',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg', 'Mld.Vrfs', 
                [], [], 
                '''                VRF related configuration
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-igmp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-igmp-cfg',
            'mld',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-igmp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_igmp_cfg'
        ),
    },
}
_meta_table['Igmp.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.InheritableDefaults']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.InheritableDefaults.ExplicitTracking']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.InheritableDefaults']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.SsmAccessGroups']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf.Interfaces']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Traffic']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.InheritableDefaults']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.SsmAccessGroups']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Maximum']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf']['meta_info']
_meta_table['Igmp.Vrfs.Vrf.Interfaces']['meta_info'].parent =_meta_table['Igmp.Vrfs.Vrf']['meta_info']
_meta_table['Igmp.Vrfs.Vrf']['meta_info'].parent =_meta_table['Igmp.Vrfs']['meta_info']
_meta_table['Igmp.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Igmp.DefaultContext.InheritableDefaults']['meta_info']
_meta_table['Igmp.DefaultContext.InheritableDefaults.ExplicitTracking']['meta_info'].parent =_meta_table['Igmp.DefaultContext.InheritableDefaults']['meta_info']
_meta_table['Igmp.DefaultContext.SsmAccessGroups.SsmAccessGroup']['meta_info'].parent =_meta_table['Igmp.DefaultContext.SsmAccessGroups']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface.ExplicitTracking']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces.Interface']['meta_info'].parent =_meta_table['Igmp.DefaultContext.Interfaces']['meta_info']
_meta_table['Igmp.DefaultContext.Nsf']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.DefaultContext.UnicastQosAdjust']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.DefaultContext.Accounting']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.DefaultContext.Traffic']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.DefaultContext.InheritableDefaults']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.DefaultContext.SsmAccessGroups']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.DefaultContext.Maximum']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.DefaultContext.Interfaces']['meta_info'].parent =_meta_table['Igmp.DefaultContext']['meta_info']
_meta_table['Igmp.Vrfs']['meta_info'].parent =_meta_table['Igmp']['meta_info']
_meta_table['Igmp.DefaultContext']['meta_info'].parent =_meta_table['Igmp']['meta_info']
_meta_table['Amt.RelayAdvAdd']['meta_info'].parent =_meta_table['Amt']['meta_info']
_meta_table['Amt.RelayAnycastPrefix']['meta_info'].parent =_meta_table['Amt']['meta_info']
_meta_table['Mld.Vrfs.Vrf.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.InheritableDefaults']['meta_info']
_meta_table['Mld.Vrfs.Vrf.InheritableDefaults.ExplicitTracking']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.InheritableDefaults']['meta_info']
_meta_table['Mld.Vrfs.Vrf.SsmAccessGroups.SsmAccessGroup']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.SsmAccessGroups']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.JoinGroups']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface.ExplicitTracking']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf.Interfaces']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Traffic']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf']['meta_info']
_meta_table['Mld.Vrfs.Vrf.InheritableDefaults']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf']['meta_info']
_meta_table['Mld.Vrfs.Vrf.SsmAccessGroups']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Maximum']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf']['meta_info']
_meta_table['Mld.Vrfs.Vrf.Interfaces']['meta_info'].parent =_meta_table['Mld.Vrfs.Vrf']['meta_info']
_meta_table['Mld.Vrfs.Vrf']['meta_info'].parent =_meta_table['Mld.Vrfs']['meta_info']
_meta_table['Mld.DefaultContext.InheritableDefaults.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Mld.DefaultContext.InheritableDefaults']['meta_info']
_meta_table['Mld.DefaultContext.InheritableDefaults.ExplicitTracking']['meta_info'].parent =_meta_table['Mld.DefaultContext.InheritableDefaults']['meta_info']
_meta_table['Mld.DefaultContext.SsmAccessGroups.SsmAccessGroup']['meta_info'].parent =_meta_table['Mld.DefaultContext.SsmAccessGroups']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroup']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups.JoinGroupSourceAddress']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddress']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddress']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMask']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddress']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses.StaticGroupGroupAddressGroupAddressMaskSourceAddressSourceAddressMask']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.JoinGroups']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.StaticGroupGroupAddresses']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.MaximumGroupsPerInterfaceOor']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface.ExplicitTracking']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces.Interface']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces.Interface']['meta_info'].parent =_meta_table['Mld.DefaultContext.Interfaces']['meta_info']
_meta_table['Mld.DefaultContext.Nsf']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.DefaultContext.UnicastQosAdjust']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.DefaultContext.Accounting']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.DefaultContext.Traffic']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.DefaultContext.InheritableDefaults']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.DefaultContext.SsmAccessGroups']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.DefaultContext.Maximum']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.DefaultContext.Interfaces']['meta_info'].parent =_meta_table['Mld.DefaultContext']['meta_info']
_meta_table['Mld.Vrfs']['meta_info'].parent =_meta_table['Mld']['meta_info']
_meta_table['Mld.DefaultContext']['meta_info'].parent =_meta_table['Mld']['meta_info']
