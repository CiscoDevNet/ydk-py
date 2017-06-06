


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PimProtocolModeEnum' : _MetaInfoEnum('PimProtocolModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg',
        {
            'sm':'sm',
            'bidir':'bidir',
        }, 'Cisco-IOS-XR-ipv4-pim-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg']),
    'PimMultipathEnum' : _MetaInfoEnum('PimMultipathEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg',
        {
            'enable':'enable',
            'interface-hash':'interface_hash',
            'source-hash':'source_hash',
            'source-next-hop-hash':'source_next_hop_hash',
            'source-group-hash':'source_group_hash',
        }, 'Cisco-IOS-XR-ipv4-pim-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg']),
    'Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a 
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses',
            False, 
            [
            _MetaInfoClassMember('sparse-mode-rp-address', REFERENCE_LIST, 'SparseModeRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'sparse_mode_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.MulticastOnlyFrr' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.MulticastOnlyFrr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Multicast Only FRR
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('flow-multicast-only-frr', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying SG that should do FLOW
                MOFRR
                ''',
                'flow_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('non-revertive-multicast-only-frr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Non-revertive Multicast Only FRR
                ''',
                'non_revertive_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rib-multicast-only-frr', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying SG that should do RIB
                MOFRR
                ''',
                'rib_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'multicast-only-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr',
            False, 
            [
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Original address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('backup', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Backup address
                ''',
                'backup',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cs-multicast-only-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs',
            False, 
            [
            _MetaInfoClassMember('cs-multicast-only-frr', REFERENCE_LIST, 'CsMulticastOnlyFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr', 
                [], [], 
                '''                Clone Source Multicast Only FRR
                ''',
                'cs_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cs-multicast-only-frrs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('convergency', ATTRIBUTE, 'int' , None, None, 
                [('1800', '2400')], [], 
                '''                Convergency timeout in seconds
                ''',
                'convergency',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Rpf' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Rpf',
            False, 
            [
            _MetaInfoClassMember('route-policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy to select RPF topology
                ''',
                'route_policy',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp',
            False, 
            [
            _MetaInfoClassMember('maximum-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from
                autorp
                ''',
                'maximum_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Warning threshold number of PIM group mappings
                from autorp
                ''',
                'threshold_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'group-mappings-auto-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-group-ranges', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from BSR
                ''',
                'bsr_maximum_group_ranges',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-group-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates',
            False, 
            [
            _MetaInfoClassMember('maximum-register-states', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Maximum number of PIM Sparse-Mode register
                states
                ''',
                'maximum_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'register-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces',
            False, 
            [
            _MetaInfoClassMember('maximum-route-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of PIM route-interfaces
                ''',
                'maximum_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'route-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-candidate-rp-cache', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of BSR C-RP cache setting
                ''',
                'bsr_maximum_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-candidate-rp-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Maximum.Routes' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Maximum.Routes',
            False, 
            [
            _MetaInfoClassMember('maximum-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Maximum number of PIM routes
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Maximum' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Maximum',
            False, 
            [
            _MetaInfoClassMember('bsr-candidate-rp-cache', REFERENCE_CLASS, 'BsrCandidateRpCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache', 
                [], [], 
                '''                Override default maximum and threshold for BSR
                C-RP cache setting
                ''',
                'bsr_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-group-mappings', REFERENCE_CLASS, 'BsrGroupMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings', 
                [], [], 
                '''                Override default maximum and threshold for
                number of group mappings from BSR
                ''',
                'bsr_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('group-mappings-auto-rp', REFERENCE_CLASS, 'GroupMappingsAutoRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp', 
                [], [], 
                '''                Override default maximum for number of group
                mappings from autorp mapping agent
                ''',
                'group_mappings_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-states', REFERENCE_CLASS, 'RegisterStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates', 
                [], [], 
                '''                Override default maximum for number of
                sparse-mode source registers
                ''',
                'register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('route-interfaces', REFERENCE_CLASS, 'RouteInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces', 
                [], [], 
                '''                Override default maximum for number of
                route-interfaces
                ''',
                'route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Maximum.Routes', 
                [], [], 
                '''                Override default maximum for number of routes
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of applicable S,G routes
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('40', '57600')], [], 
                '''                (S,G) expiry time in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sg-expiry-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable',
            False, 
            [
            _MetaInfoClassMember('allow-ebgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow RPF Vector origination over eBGP sessions
                ''',
                'allow_ebgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('disable-ibgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable RPF Vector origination over iBGP
                sessions
                ''',
                'disable_ibgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPF Vector is turned on if configured
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf-vector-enable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Ssm' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Ssm',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if SSM is disabled on this router
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('range', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups enabled with SSM
                ''',
                'range',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ssm',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Injects.Inject' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Injects.Inject',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('rpf-proxy-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RPF Proxy Address
                ''',
                'rpf_proxy_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False, max_elements=22, min_elements=1),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'inject',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Injects' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Injects',
            False, 
            [
            _MetaInfoClassMember('inject', REFERENCE_LIST, 'Inject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Injects.Inject', 
                [], [], 
                '''                Inject Explicit PIM RPF Vector Proxy's
                ''',
                'inject',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'injects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses',
            False, 
            [
            _MetaInfoClassMember('bidir-rp-address', REFERENCE_LIST, 'BidirRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'bidir_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BSR Address configured
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BSR Address configured
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BSR Address configured
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Hash Mask Length for this candidate BSR
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the Candidate BSR
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of Candidate-RP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'PimProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolModeEnum', 
                [], [], 
                '''                SM or Bidir
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('group-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying the group range for the
                Candidate-RP
                ''',
                'group_list',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('30', '600')], [], 
                '''                Advertisement interval
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the CRP
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps',
            False, 
            [
            _MetaInfoClassMember('candidate-rp', REFERENCE_LIST, 'CandidateRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp', 
                [], [], 
                '''                Address of PIM SM BSR Candidate-RP
                ''',
                'candidate_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rps',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Bsr' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Bsr',
            False, 
            [
            _MetaInfoClassMember('candidate-bsr', REFERENCE_CLASS, 'CandidateBsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr', 
                [], [], 
                '''                PIM Candidate BSR configuration
                ''',
                'candidate_bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('candidate-rps', REFERENCE_CLASS, 'CandidateRps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps', 
                [], [], 
                '''                PIM RP configuration
                ''',
                'candidate_rps',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Paths.Path' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('rpf-proxy-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RPF Proxy Address
                ''',
                'rpf_proxy_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False, max_elements=22, min_elements=1),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Paths' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Paths.Path', 
                [], [], 
                '''                Inject PIM RPF Vector Proxy's
                ''',
                'path',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.AllowRp' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.AllowRp',
            False, 
            [
            _MetaInfoClassMember('group-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable groups
                ''',
                'group_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable RPs
                ''',
                'rp_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'allow-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Convergence' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Convergence',
            False, 
            [
            _MetaInfoClassMember('link-down-prune-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Delay prunes if route join state transitions to
                not-joined on link down
                ''',
                'link_down_prune_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-conflict-join-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Dampen first join if RPF path is through one of
                the downstream neighbor
                ''',
                'rpf_conflict_join_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of routes for this interface
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detection multiplier for BFD sessions created
                by PIM
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by PIM
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-border', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BSR Border configuration for Interface
                ''',
                'bsr_border',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter PIM Interface processing
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interface-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable PIM processing on the interface
                ''',
                'interface_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum-routes', REFERENCE_CLASS, 'MaximumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes', 
                [], [], 
                '''                Maximum number of allowed routes for this
                interface
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr',
            False, 
            [
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Original address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('backup', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Backup address
                ''',
                'backup',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cj-multicast-only-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs',
            False, 
            [
            _MetaInfoClassMember('cj-multicast-only-frr', REFERENCE_LIST, 'CjMulticastOnlyFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr', 
                [], [], 
                '''                Clone Join Multicast Only FRR
                ''',
                'cj_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cj-multicast-only-frrs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv4' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv4',
            False, 
            [
            _MetaInfoClassMember('accept-register', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list which specifies unauthorized sources
                ''',
                'accept_register',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('allow-rp', REFERENCE_CLASS, 'AllowRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.AllowRp', 
                [], [], 
                '''                Enable allow-rp filtering for SM joins
                ''',
                'allow_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Rendezvous Point discovery through the
                AutoRP protocol
                ''',
                'auto_rp_disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bidir-rp-addresses', REFERENCE_CLASS, 'BidirRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses', 
                [], [], 
                '''                Configure Bidirectional PIM Rendezvous Point
                ''',
                'bidir_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr', REFERENCE_CLASS, 'Bsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Bsr', 
                [], [], 
                '''                PIM BSR configuration
                ''',
                'bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('cj-multicast-only-frrs', REFERENCE_CLASS, 'CjMulticastOnlyFrrs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs', 
                [], [], 
                '''                Clone Join Multicast Only FRR
                ''',
                'cj_multicast_only_frrs',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('convergence', REFERENCE_CLASS, 'Convergence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Convergence', 
                [], [], 
                '''                Configure convergence parameters
                ''',
                'convergence',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('cs-multicast-only-frrs', REFERENCE_CLASS, 'CsMulticastOnlyFrrs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs', 
                [], [], 
                '''                Clone Source Multicast Only FRR
                ''',
                'cs_multicast_only_frrs',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.InheritableDefaults', 
                [], [], 
                '''                Inheritable defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('injects', REFERENCE_CLASS, 'Injects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Injects', 
                [], [], 
                '''                Inject Explicit PIM RPF Vector Proxy's
                ''',
                'injects',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('log-neighbor-changes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PIM neighbor state change logging is turned on
                if configured
                ''',
                'log_neighbor_changes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Maximum', 
                [], [], 
                '''                Configure PIM State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('multicast-only-frr', REFERENCE_CLASS, 'MulticastOnlyFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.MulticastOnlyFrr', 
                [], [], 
                '''                Multicast Only FRR
                ''',
                'multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('multipath', REFERENCE_ENUM_CLASS, 'PimMultipathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipathEnum', 
                [], [], 
                '''                Enable equal-cost multipath routing
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-receive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when receiving PIM
                messages
                ''',
                'neighbor_check_on_receive',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-send', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when sending
                join-prunes
                ''',
                'neighbor_check_on_send',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('old-register-checksum', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Generate registers compatible with older IOS
                versions
                ''',
                'old_register_checksum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Paths', 
                [], [], 
                '''                Inject PIM RPF Vector Proxy's
                ''',
                'paths',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source address to use for register messages
                ''',
                'register_source',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-static-deny', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure static RP deny range
                ''',
                'rp_static_deny',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Rpf', 
                [], [], 
                '''                Configure RPF options
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-vector-enable', REFERENCE_CLASS, 'RpfVectorEnable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable', 
                [], [], 
                '''                Enable PIM RPF Vector Proxy's
                ''',
                'rpf_vector_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sg-expiry-timer', REFERENCE_CLASS, 'SgExpiryTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer', 
                [], [], 
                '''                Configure expiry timer for S,G routes
                ''',
                'sg_expiry_timer',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sparse-mode-rp-addresses', REFERENCE_CLASS, 'SparseModeRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses', 
                [], [], 
                '''                Configure Sparse-Mode Rendezvous Point
                ''',
                'sparse_mode_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('spt-threshold-infinity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure threshold of infinity for switching to
                SPT on last-hop
                ''',
                'spt_threshold_infinity',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm', REFERENCE_CLASS, 'Ssm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4.Ssm', 
                [], [], 
                '''                Configure IP Multicast SSM
                ''',
                'ssm',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm-allow-override', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow SSM ranges to be overridden by more
                specific ranges
                ''',
                'ssm_allow_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-data-registers', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress data registers after initial state
                setup
                ''',
                'suppress_data_registers',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-rpf-prunes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress prunes triggered as a result of RPF
                changes
                ''',
                'suppress_rpf_prunes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a 
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses',
            False, 
            [
            _MetaInfoClassMember('sparse-mode-rp-address', REFERENCE_LIST, 'SparseModeRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'sparse_mode_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('convergency', ATTRIBUTE, 'int' , None, None, 
                [('1800', '2400')], [], 
                '''                Convergency timeout in seconds
                ''',
                'convergency',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Rpf' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Rpf',
            False, 
            [
            _MetaInfoClassMember('route-policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy to select RPF topology
                ''',
                'route_policy',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp',
            False, 
            [
            _MetaInfoClassMember('maximum-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from
                autorp
                ''',
                'maximum_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Warning threshold number of PIM group mappings
                from autorp
                ''',
                'threshold_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'group-mappings-auto-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-group-ranges', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from BSR
                ''',
                'bsr_maximum_group_ranges',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-group-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates',
            False, 
            [
            _MetaInfoClassMember('maximum-register-states', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Maximum number of PIM Sparse-Mode register
                states
                ''',
                'maximum_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'register-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces',
            False, 
            [
            _MetaInfoClassMember('maximum-route-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of PIM route-interfaces
                ''',
                'maximum_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'route-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-candidate-rp-cache', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of BSR C-RP cache setting
                ''',
                'bsr_maximum_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-candidate-rp-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Maximum.Routes' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Maximum.Routes',
            False, 
            [
            _MetaInfoClassMember('maximum-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Maximum number of PIM routes
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Maximum' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Maximum',
            False, 
            [
            _MetaInfoClassMember('bsr-candidate-rp-cache', REFERENCE_CLASS, 'BsrCandidateRpCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache', 
                [], [], 
                '''                Override default maximum and threshold for BSR
                C-RP cache setting
                ''',
                'bsr_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-group-mappings', REFERENCE_CLASS, 'BsrGroupMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings', 
                [], [], 
                '''                Override default maximum and threshold for
                number of group mappings from BSR
                ''',
                'bsr_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('group-mappings-auto-rp', REFERENCE_CLASS, 'GroupMappingsAutoRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp', 
                [], [], 
                '''                Override default maximum for number of group
                mappings from autorp mapping agent
                ''',
                'group_mappings_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-states', REFERENCE_CLASS, 'RegisterStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates', 
                [], [], 
                '''                Override default maximum for number of
                sparse-mode source registers
                ''',
                'register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('route-interfaces', REFERENCE_CLASS, 'RouteInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces', 
                [], [], 
                '''                Override default maximum for number of
                route-interfaces
                ''',
                'route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Maximum.Routes', 
                [], [], 
                '''                Override default maximum for number of routes
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of applicable S,G routes
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('40', '57600')], [], 
                '''                (S,G) expiry time in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sg-expiry-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable',
            False, 
            [
            _MetaInfoClassMember('allow-ebgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow RPF Vector origination over eBGP sessions
                ''',
                'allow_ebgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('disable-ibgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable RPF Vector origination over iBGP
                sessions
                ''',
                'disable_ibgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPF Vector is turned on if configured
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf-vector-enable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Ssm' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Ssm',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if SSM is disabled on this router
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('range', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups enabled with SSM
                ''',
                'range',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ssm',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses',
            False, 
            [
            _MetaInfoClassMember('bidir-rp-address', REFERENCE_LIST, 'BidirRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'bidir_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                BSR Address configured
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Hash Mask Length for this candidate BSR
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the Candidate BSR
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of Candidate-RP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'PimProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolModeEnum', 
                [], [], 
                '''                SM or Bidir
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('group-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying the group range for the
                Candidate-RP
                ''',
                'group_list',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('30', '600')], [], 
                '''                Advertisement interval
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the CRP
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps',
            False, 
            [
            _MetaInfoClassMember('candidate-rp', REFERENCE_LIST, 'CandidateRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp', 
                [], [], 
                '''                Address of PIM SM BSR Candidate-RP
                ''',
                'candidate_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rps',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Bsr' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Bsr',
            False, 
            [
            _MetaInfoClassMember('candidate-bsr', REFERENCE_CLASS, 'CandidateBsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr', 
                [], [], 
                '''                PIM Candidate BSR configuration
                ''',
                'candidate_bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('candidate-rps', REFERENCE_CLASS, 'CandidateRps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps', 
                [], [], 
                '''                PIM RP configuration
                ''',
                'candidate_rps',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.AllowRp' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.AllowRp',
            False, 
            [
            _MetaInfoClassMember('group-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable groups
                ''',
                'group_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable RPs
                ''',
                'rp_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'allow-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of the Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of the Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of the Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'embedded-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses',
            False, 
            [
            _MetaInfoClassMember('embedded-rp-address', REFERENCE_LIST, 'EmbeddedRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress', 
                [], [], 
                '''                Set Embedded RP processing support
                ''',
                'embedded_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'embedded-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Convergence' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Convergence',
            False, 
            [
            _MetaInfoClassMember('link-down-prune-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Delay prunes if route join state transitions to
                not-joined on link down
                ''',
                'link_down_prune_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-conflict-join-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Dampen first join if RPF path is through one of
                the downstream neighbor
                ''',
                'rpf_conflict_join_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of routes for this interface
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detection multiplier for BFD sessions created
                by PIM
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by PIM
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-border', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BSR Border configuration for Interface
                ''',
                'bsr_border',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter PIM Interface processing
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interface-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable PIM processing on the interface
                ''',
                'interface_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum-routes', REFERENCE_CLASS, 'MaximumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes', 
                [], [], 
                '''                Maximum number of allowed routes for this
                interface
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf.Ipv6' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf.Ipv6',
            False, 
            [
            _MetaInfoClassMember('accept-register', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list which specifies unauthorized sources
                ''',
                'accept_register',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('allow-rp', REFERENCE_CLASS, 'AllowRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.AllowRp', 
                [], [], 
                '''                Enable allow-rp filtering for SM joins
                ''',
                'allow_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bidir-rp-addresses', REFERENCE_CLASS, 'BidirRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses', 
                [], [], 
                '''                Configure Bidirectional PIM Rendezvous Point
                ''',
                'bidir_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr', REFERENCE_CLASS, 'Bsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Bsr', 
                [], [], 
                '''                PIM BSR configuration
                ''',
                'bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('convergence', REFERENCE_CLASS, 'Convergence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Convergence', 
                [], [], 
                '''                Configure convergence parameters
                ''',
                'convergence',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('embedded-rp-addresses', REFERENCE_CLASS, 'EmbeddedRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses', 
                [], [], 
                '''                Set Embedded RP processing support
                ''',
                'embedded_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('embedded-rp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set Embedded RP processing support
                ''',
                'embedded_rp_disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.InheritableDefaults', 
                [], [], 
                '''                Inheritable defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('log-neighbor-changes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PIM neighbor state change logging is turned on
                if configured
                ''',
                'log_neighbor_changes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Maximum', 
                [], [], 
                '''                Configure PIM State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('multipath', REFERENCE_ENUM_CLASS, 'PimMultipathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipathEnum', 
                [], [], 
                '''                Enable equal-cost multipath routing
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-receive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when receiving PIM
                messages
                ''',
                'neighbor_check_on_receive',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-send', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when sending
                join-prunes
                ''',
                'neighbor_check_on_send',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('old-register-checksum', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Generate registers compatible with older IOS
                versions
                ''',
                'old_register_checksum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source address to use for register messages
                ''',
                'register_source',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-static-deny', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure static RP deny range
                ''',
                'rp_static_deny',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Rpf', 
                [], [], 
                '''                Configure RPF options
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-vector-enable', REFERENCE_CLASS, 'RpfVectorEnable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable', 
                [], [], 
                '''                Enable PIM RPF Vector Proxy's
                ''',
                'rpf_vector_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sg-expiry-timer', REFERENCE_CLASS, 'SgExpiryTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer', 
                [], [], 
                '''                Configure expiry timer for S,G routes
                ''',
                'sg_expiry_timer',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sparse-mode-rp-addresses', REFERENCE_CLASS, 'SparseModeRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses', 
                [], [], 
                '''                Configure Sparse-Mode Rendezvous Point
                ''',
                'sparse_mode_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('spt-threshold-infinity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure threshold of infinity for switching to
                SPT on last-hop
                ''',
                'spt_threshold_infinity',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm', REFERENCE_CLASS, 'Ssm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6.Ssm', 
                [], [], 
                '''                Configure IP Multicast SSM
                ''',
                'ssm',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm-allow-override', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow SSM ranges to be overridden by more
                specific ranges
                ''',
                'ssm_allow_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-data-registers', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress data registers after initial state
                setup
                ''',
                'suppress_data_registers',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-rpf-prunes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress prunes triggered as a result of RPF
                changes
                ''',
                'suppress_rpf_prunes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv4', 
                [], [], 
                '''                IPV4 commands
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf.Ipv6', 
                [], [], 
                '''                IPV6 commands
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.Vrfs' : {
        'meta_info' : _MetaInfoClass('Pim.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs.Vrf', 
                [], [], 
                '''                VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of routes for this interface
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detection multiplier for BFD sessions created
                by PIM
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by PIM
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-border', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BSR Border configuration for Interface
                ''',
                'bsr_border',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter PIM Interface processing
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interface-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable PIM processing on the interface
                ''',
                'interface_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum-routes', REFERENCE_CLASS, 'MaximumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes', 
                [], [], 
                '''                Maximum number of allowed routes for this
                interface
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a 
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.SparseModeRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.SparseModeRpAddresses',
            False, 
            [
            _MetaInfoClassMember('sparse-mode-rp-address', REFERENCE_LIST, 'SparseModeRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'sparse_mode_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('convergency', ATTRIBUTE, 'int' , None, None, 
                [('1800', '2400')], [], 
                '''                Convergency timeout in seconds
                ''',
                'convergency',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Rpf' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Rpf',
            False, 
            [
            _MetaInfoClassMember('route-policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy to select RPF topology
                ''',
                'route_policy',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.SgExpiryTimer' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.SgExpiryTimer',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of applicable S,G routes
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('40', '57600')], [], 
                '''                (S,G) expiry time in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sg-expiry-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.RpfVectorEnable' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.RpfVectorEnable',
            False, 
            [
            _MetaInfoClassMember('allow-ebgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow RPF Vector origination over eBGP sessions
                ''',
                'allow_ebgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('disable-ibgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable RPF Vector origination over iBGP
                sessions
                ''',
                'disable_ibgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPF Vector is turned on if configured
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf-vector-enable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Nsf' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Nsf',
            False, 
            [
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Override default maximum lifetime for PIM NSF
                mode
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'nsf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-global-group-mappings', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Global Maximum number of PIM group mapping
                ranges from BSR
                ''',
                'bsr_maximum_global_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-global-group-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes',
            False, 
            [
            _MetaInfoClassMember('maximum-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Maximum number of PIM routes
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp',
            False, 
            [
            _MetaInfoClassMember('maximum-global-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from
                autorp
                ''',
                'maximum_global_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-global-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Warning threshold number of PIM group mappings
                from autorp
                ''',
                'threshold_global_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-group-mappings-auto-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-global-candidate-rp-cache', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Global Maximum number of PIM C-RP Sets from
                BSR
                ''',
                'bsr_maximum_global_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-global-candidate-rp-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates',
            False, 
            [
            _MetaInfoClassMember('maximum-register-states', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Maximum number of PIM Sparse-Mode register
                states
                ''',
                'maximum_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-register-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces',
            False, 
            [
            _MetaInfoClassMember('maximum-route-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of PIM route-interfaces
                ''',
                'maximum_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-route-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp',
            False, 
            [
            _MetaInfoClassMember('maximum-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from
                autorp
                ''',
                'maximum_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Warning threshold number of PIM group mappings
                from autorp
                ''',
                'threshold_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'group-mappings-auto-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-group-ranges', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from BSR
                ''',
                'bsr_maximum_group_ranges',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-group-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.RegisterStates' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.RegisterStates',
            False, 
            [
            _MetaInfoClassMember('maximum-register-states', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Maximum number of PIM Sparse-Mode register
                states
                ''',
                'maximum_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'register-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces',
            False, 
            [
            _MetaInfoClassMember('maximum-route-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of PIM route-interfaces
                ''',
                'maximum_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'route-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-candidate-rp-cache', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of BSR C-RP cache setting
                ''',
                'bsr_maximum_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-candidate-rp-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum.Routes' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum.Routes',
            False, 
            [
            _MetaInfoClassMember('maximum-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Maximum number of PIM routes
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Maximum' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Maximum',
            False, 
            [
            _MetaInfoClassMember('bsr-candidate-rp-cache', REFERENCE_CLASS, 'BsrCandidateRpCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache', 
                [], [], 
                '''                Override default maximum and threshold for BSR
                C-RP cache setting
                ''',
                'bsr_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-global-candidate-rp-cache', REFERENCE_CLASS, 'BsrGlobalCandidateRpCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache', 
                [], [], 
                '''                Override default global maximum and threshold
                for C-RP set in BSR
                ''',
                'bsr_global_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-global-group-mappings', REFERENCE_CLASS, 'BsrGlobalGroupMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings', 
                [], [], 
                '''                Override default global maximum and threshold
                for PIM group mapping ranges from BSR
                ''',
                'bsr_global_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-group-mappings', REFERENCE_CLASS, 'BsrGroupMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings', 
                [], [], 
                '''                Override default maximum and threshold for
                number of group mappings from BSR
                ''',
                'bsr_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-group-mappings-auto-rp', REFERENCE_CLASS, 'GlobalGroupMappingsAutoRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp', 
                [], [], 
                '''                Maximum for number of group mappings from
                autorp mapping agent
                ''',
                'global_group_mappings_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-high-priority-packet-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483648')], [], 
                '''                Maximum packet queue size in bytes
                ''',
                'global_high_priority_packet_queue',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-low-priority-packet-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483648')], [], 
                '''                Maximum packet queue size in bytes
                ''',
                'global_low_priority_packet_queue',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-register-states', REFERENCE_CLASS, 'GlobalRegisterStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates', 
                [], [], 
                '''                Override default maximum for number of
                sparse-mode source registers
                ''',
                'global_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-route-interfaces', REFERENCE_CLASS, 'GlobalRouteInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces', 
                [], [], 
                '''                Override default maximum for number of
                route-interfaces
                ''',
                'global_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-routes', REFERENCE_CLASS, 'GlobalRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes', 
                [], [], 
                '''                Override default maximum for number of routes
                ''',
                'global_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('group-mappings-auto-rp', REFERENCE_CLASS, 'GroupMappingsAutoRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp', 
                [], [], 
                '''                Override default maximum for number of group
                mappings from autorp mapping agent
                ''',
                'group_mappings_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-states', REFERENCE_CLASS, 'RegisterStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.RegisterStates', 
                [], [], 
                '''                Override default maximum for number of
                sparse-mode source registers
                ''',
                'register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('route-interfaces', REFERENCE_CLASS, 'RouteInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces', 
                [], [], 
                '''                Override default maximum for number of
                route-interfaces
                ''',
                'route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum.Routes', 
                [], [], 
                '''                Override default maximum for number of routes
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Ssm' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Ssm',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if SSM is disabled on this router
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('range', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups enabled with SSM
                ''',
                'range',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ssm',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.BidirRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.BidirRpAddresses',
            False, 
            [
            _MetaInfoClassMember('bidir-rp-address', REFERENCE_LIST, 'BidirRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'bidir_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Bsr.CandidateBsr' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Bsr.CandidateBsr',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                BSR Address configured
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Hash Mask Length for this candidate BSR
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the Candidate BSR
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of Candidate-RP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'PimProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolModeEnum', 
                [], [], 
                '''                SM or Bidir
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('group-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying the group range for the
                Candidate-RP
                ''',
                'group_list',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('30', '600')], [], 
                '''                Advertisement interval
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the CRP
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Bsr.CandidateRps' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Bsr.CandidateRps',
            False, 
            [
            _MetaInfoClassMember('candidate-rp', REFERENCE_LIST, 'CandidateRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp', 
                [], [], 
                '''                Address of PIM SM BSR Candidate-RP
                ''',
                'candidate_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rps',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Bsr' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Bsr',
            False, 
            [
            _MetaInfoClassMember('candidate-bsr', REFERENCE_CLASS, 'CandidateBsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Bsr.CandidateBsr', 
                [], [], 
                '''                PIM Candidate BSR configuration
                ''',
                'candidate_bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('candidate-rps', REFERENCE_CLASS, 'CandidateRps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Bsr.CandidateRps', 
                [], [], 
                '''                PIM RP configuration
                ''',
                'candidate_rps',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.AllowRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.AllowRp',
            False, 
            [
            _MetaInfoClassMember('group-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable groups
                ''',
                'group_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable RPs
                ''',
                'rp_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'allow-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of the Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of the Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of the Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'embedded-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.EmbeddedRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.EmbeddedRpAddresses',
            False, 
            [
            _MetaInfoClassMember('embedded-rp-address', REFERENCE_LIST, 'EmbeddedRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress', 
                [], [], 
                '''                Set Embedded RP processing support
                ''',
                'embedded_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'embedded-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6.Convergence' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6.Convergence',
            False, 
            [
            _MetaInfoClassMember('link-down-prune-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Delay prunes if route join state transitions to
                not-joined on link down
                ''',
                'link_down_prune_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-conflict-join-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Dampen first join if RPF path is through one of
                the downstream neighbor
                ''',
                'rpf_conflict_join_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv6' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv6',
            False, 
            [
            _MetaInfoClassMember('accept-register', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list which specifies unauthorized sources
                ''',
                'accept_register',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('allow-rp', REFERENCE_CLASS, 'AllowRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.AllowRp', 
                [], [], 
                '''                Enable allow-rp filtering for SM joins
                ''',
                'allow_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bidir-rp-addresses', REFERENCE_CLASS, 'BidirRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.BidirRpAddresses', 
                [], [], 
                '''                Configure Bidirectional PIM Rendezvous Point
                ''',
                'bidir_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr', REFERENCE_CLASS, 'Bsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Bsr', 
                [], [], 
                '''                PIM BSR configuration
                ''',
                'bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('convergence', REFERENCE_CLASS, 'Convergence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Convergence', 
                [], [], 
                '''                Configure convergence parameters
                ''',
                'convergence',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('embedded-rp-addresses', REFERENCE_CLASS, 'EmbeddedRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.EmbeddedRpAddresses', 
                [], [], 
                '''                Set Embedded RP processing support
                ''',
                'embedded_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('embedded-rp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set Embedded RP processing support
                ''',
                'embedded_rp_disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.InheritableDefaults', 
                [], [], 
                '''                Inheritable defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('log-neighbor-changes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PIM neighbor state change logging is turned on
                if configured
                ''',
                'log_neighbor_changes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Maximum', 
                [], [], 
                '''                Configure PIM State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('multipath', REFERENCE_ENUM_CLASS, 'PimMultipathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipathEnum', 
                [], [], 
                '''                Enable equal-cost multipath routing
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-receive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when receiving PIM
                messages
                ''',
                'neighbor_check_on_receive',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-send', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when sending
                join-prunes
                ''',
                'neighbor_check_on_send',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Nsf', 
                [], [], 
                '''                Configure Non-stop forwarding (NSF) options
                ''',
                'nsf',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('old-register-checksum', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Generate registers compatible with older IOS
                versions
                ''',
                'old_register_checksum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source address to use for register messages
                ''',
                'register_source',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-static-deny', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure static RP deny range
                ''',
                'rp_static_deny',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Rpf', 
                [], [], 
                '''                Configure RPF options
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-vector-enable', REFERENCE_CLASS, 'RpfVectorEnable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.RpfVectorEnable', 
                [], [], 
                '''                Enable PIM RPF Vector Proxy's
                ''',
                'rpf_vector_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sg-expiry-timer', REFERENCE_CLASS, 'SgExpiryTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.SgExpiryTimer', 
                [], [], 
                '''                Configure expiry timer for S,G routes
                ''',
                'sg_expiry_timer',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sparse-mode-rp-addresses', REFERENCE_CLASS, 'SparseModeRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.SparseModeRpAddresses', 
                [], [], 
                '''                Configure Sparse-Mode Rendezvous Point
                ''',
                'sparse_mode_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('spt-threshold-infinity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure threshold of infinity for switching to
                SPT on last-hop
                ''',
                'spt_threshold_infinity',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm', REFERENCE_CLASS, 'Ssm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6.Ssm', 
                [], [], 
                '''                Configure IP Multicast SSM
                ''',
                'ssm',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm-allow-override', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow SSM ranges to be overridden by more
                specific ranges
                ''',
                'ssm_allow_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-data-registers', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress data registers after initial state
                setup
                ''',
                'suppress_data_registers',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-rpf-prunes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress prunes triggered as a result of RPF
                changes
                ''',
                'suppress_rpf_prunes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.RpfRedirect' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.RpfRedirect',
            False, 
            [
            _MetaInfoClassMember('route-policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy to select RPF topology
                ''',
                'route_policy',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf-redirect',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle',
            False, 
            [
            _MetaInfoClassMember('bundle-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Bundle name
                ''',
                'bundle_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interface-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '100000000')], [], 
                '''                Interface bandwidth in Kbps
                ''',
                'interface_bandwidth',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '100000000')], [], 
                '''                Threshold bandwidth in Kbps
                ''',
                'threshold_bandwidth',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'redirect-bundle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list to account for
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of routes for this interface
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detection multiplier for BFD sessions created
                by PIM
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BFD. FALSE to disable and to
                prevent inheritance from a parent
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by PIM
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-border', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BSR Border configuration for Interface
                ''',
                'bsr_border',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter PIM Interface processing
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interface-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable PIM processing on the interface
                ''',
                'interface_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum-routes', REFERENCE_CLASS, 'MaximumRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes', 
                [], [], 
                '''                Maximum number of allowed routes for this
                interface
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('redirect-bundle', REFERENCE_CLASS, 'RedirectBundle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle', 
                [], [], 
                '''                Configure RPF-redirect bundle for interface.
                Applicable for IPv4 only
                ''',
                'redirect_bundle',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Interfaces.Interface', 
                [], [], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface from which Candidate-RP packets
                will be sourced
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('protocol-mode', REFERENCE_ENUM_CLASS, 'AutoRpProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_autorp_datatypes', 'AutoRpProtocolModeEnum', 
                [], [], 
                '''                Protocol Mode
                ''',
                'protocol_mode',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying the group range for
                the Candidate-RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('announce-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                Time between announcements <in seconds> 
                ''',
                'announce_period',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                TTL in Hops
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'auto-rp-candidate-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.AutoRpCandidateRps' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.AutoRpCandidateRps',
            False, 
            [
            _MetaInfoClassMember('auto-rp-candidate-rp', REFERENCE_LIST, 'AutoRpCandidateRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp', 
                [], [], 
                '''                Specifications for a Candidate-RP
                ''',
                'auto_rp_candidate_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'auto-rp-candidate-rps',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters',
            False, 
            [
            _MetaInfoClassMember('announce-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                Time between discovery messages <in seconds>
                ''',
                'announce_period',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface from which mapping packets will be
                sourced 
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ttl', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                TTL in Hops
                ''',
                'ttl',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'parameters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit',
            False, 
            [
            _MetaInfoClassMember('maximum-cache-entry', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Maximum number of mapping cache entries
                ''',
                'maximum_cache_entry',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-cache-entry', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Warning threshold number of cache entries
                ''',
                'threshold_cache_entry',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cache-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.AutoRpMappingAgent' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.AutoRpMappingAgent',
            False, 
            [
            _MetaInfoClassMember('cache-limit', REFERENCE_CLASS, 'CacheLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit', 
                [], [], 
                '''                Mapping Agent cache size limit
                ''',
                'cache_limit',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('parameters', REFERENCE_CLASS, 'Parameters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters', 
                [], [], 
                '''                Specifications for Mapping Agent configured
                on this box
                ''',
                'parameters',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'auto-rp-mapping-agent',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a 
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.SparseModeRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.SparseModeRpAddresses',
            False, 
            [
            _MetaInfoClassMember('sparse-mode-rp-address', REFERENCE_LIST, 'SparseModeRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'sparse_mode_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sparse-mode-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.MulticastOnlyFrr' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.MulticastOnlyFrr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Multicast Only FRR
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('flow-multicast-only-frr', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying SG that should do FLOW
                MOFRR
                ''',
                'flow_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('non-revertive-multicast-only-frr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Non-revertive Multicast Only FRR
                ''',
                'non_revertive_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rib-multicast-only-frr', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying SG that should do RIB
                MOFRR
                ''',
                'rib_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'multicast-only-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr',
            False, 
            [
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Original address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('backup', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Backup address
                ''',
                'backup',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cs-multicast-only-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs',
            False, 
            [
            _MetaInfoClassMember('cs-multicast-only-frr', REFERENCE_LIST, 'CsMulticastOnlyFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr', 
                [], [], 
                '''                Clone Source Multicast Only FRR
                ''',
                'cs_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cs-multicast-only-frrs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.InheritableDefaults' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.InheritableDefaults',
            False, 
            [
            _MetaInfoClassMember('convergency', ATTRIBUTE, 'int' , None, None, 
                [('1800', '2400')], [], 
                '''                Convergency timeout in seconds
                ''',
                'convergency',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('dr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello DR priority, preference given to larger
                value
                ''',
                'dr_priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Hello interval in seconds
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('join-prune-mtu', ATTRIBUTE, 'int' , None, None, 
                [('576', '65535')], [], 
                '''                Join-Prune MTU in Bytes
                ''',
                'join_prune_mtu',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('jp-interval', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Join-Prune interval in seconds
                ''',
                'jp_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('override-interval', ATTRIBUTE, 'int' , None, None, 
                [('400', '65535')], [], 
                '''                Override interval in milliseconds
                ''',
                'override_interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('propagation-delay', ATTRIBUTE, 'int' , None, None, 
                [('100', '32767')], [], 
                '''                Propagation delay in milli seconds
                ''',
                'propagation_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'inheritable-defaults',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Rpf' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Rpf',
            False, 
            [
            _MetaInfoClassMember('route-policy', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Route policy to select RPF topology
                ''',
                'route_policy',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.SgExpiryTimer' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.SgExpiryTimer',
            False, 
            [
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of applicable S,G routes
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('40', '57600')], [], 
                '''                (S,G) expiry time in seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'sg-expiry-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.RpfVectorEnable' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.RpfVectorEnable',
            False, 
            [
            _MetaInfoClassMember('allow-ebgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow RPF Vector origination over eBGP sessions
                ''',
                'allow_ebgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('disable-ibgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable RPF Vector origination over iBGP
                sessions
                ''',
                'disable_ibgp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPF Vector is turned on if configured
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'rpf-vector-enable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Nsf' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Nsf',
            False, 
            [
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('10', '600')], [], 
                '''                Override default maximum lifetime for PIM NSF
                mode
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'nsf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-global-group-mappings', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Global Maximum number of PIM group mapping
                ranges from BSR
                ''',
                'bsr_maximum_global_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-global-group-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes',
            False, 
            [
            _MetaInfoClassMember('maximum-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Maximum number of PIM routes
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp',
            False, 
            [
            _MetaInfoClassMember('maximum-global-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from
                autorp
                ''',
                'maximum_global_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-global-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Warning threshold number of PIM group mappings
                from autorp
                ''',
                'threshold_global_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-group-mappings-auto-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-global-candidate-rp-cache', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Global Maximum number of PIM C-RP Sets from
                BSR
                ''',
                'bsr_maximum_global_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-global-candidate-rp-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates',
            False, 
            [
            _MetaInfoClassMember('maximum-register-states', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Maximum number of PIM Sparse-Mode register
                states
                ''',
                'maximum_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-register-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces',
            False, 
            [
            _MetaInfoClassMember('maximum-route-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of PIM route-interfaces
                ''',
                'maximum_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'global-route-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp',
            False, 
            [
            _MetaInfoClassMember('maximum-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from
                autorp
                ''',
                'maximum_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('threshold-group-ranges-auto-rp', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Warning threshold number of PIM group mappings
                from autorp
                ''',
                'threshold_group_ranges_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'group-mappings-auto-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-group-ranges', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of PIM group mappings from BSR
                ''',
                'bsr_maximum_group_ranges',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-group-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.RegisterStates' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.RegisterStates',
            False, 
            [
            _MetaInfoClassMember('maximum-register-states', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Maximum number of PIM Sparse-Mode register
                states
                ''',
                'maximum_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '75000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'register-states',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces',
            False, 
            [
            _MetaInfoClassMember('maximum-route-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Maximum number of PIM route-interfaces
                ''',
                'maximum_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '1100000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'route-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache',
            False, 
            [
            _MetaInfoClassMember('bsr-maximum-candidate-rp-cache', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Maximum number of BSR C-RP cache setting
                ''',
                'bsr_maximum_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr-candidate-rp-cache',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum.Routes' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum.Routes',
            False, 
            [
            _MetaInfoClassMember('maximum-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Maximum number of PIM routes
                ''',
                'maximum_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '200000')], [], 
                '''                Set threshold to print warning
                ''',
                'warning_threshold',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Maximum' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Maximum',
            False, 
            [
            _MetaInfoClassMember('bsr-candidate-rp-cache', REFERENCE_CLASS, 'BsrCandidateRpCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache', 
                [], [], 
                '''                Override default maximum and threshold for BSR
                C-RP cache setting
                ''',
                'bsr_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-global-candidate-rp-cache', REFERENCE_CLASS, 'BsrGlobalCandidateRpCache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache', 
                [], [], 
                '''                Override default global maximum and threshold
                for C-RP set in BSR
                ''',
                'bsr_global_candidate_rp_cache',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-global-group-mappings', REFERENCE_CLASS, 'BsrGlobalGroupMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings', 
                [], [], 
                '''                Override default global maximum and threshold
                for PIM group mapping ranges from BSR
                ''',
                'bsr_global_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr-group-mappings', REFERENCE_CLASS, 'BsrGroupMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings', 
                [], [], 
                '''                Override default maximum and threshold for
                number of group mappings from BSR
                ''',
                'bsr_group_mappings',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-group-mappings-auto-rp', REFERENCE_CLASS, 'GlobalGroupMappingsAutoRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp', 
                [], [], 
                '''                Maximum for number of group mappings from
                autorp mapping agent
                ''',
                'global_group_mappings_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-high-priority-packet-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483648')], [], 
                '''                Maximum packet queue size in bytes
                ''',
                'global_high_priority_packet_queue',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-low-priority-packet-queue', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483648')], [], 
                '''                Maximum packet queue size in bytes
                ''',
                'global_low_priority_packet_queue',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-register-states', REFERENCE_CLASS, 'GlobalRegisterStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates', 
                [], [], 
                '''                Override default maximum for number of
                sparse-mode source registers
                ''',
                'global_register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-route-interfaces', REFERENCE_CLASS, 'GlobalRouteInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces', 
                [], [], 
                '''                Override default maximum for number of
                route-interfaces
                ''',
                'global_route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('global-routes', REFERENCE_CLASS, 'GlobalRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes', 
                [], [], 
                '''                Override default maximum for number of routes
                ''',
                'global_routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('group-mappings-auto-rp', REFERENCE_CLASS, 'GroupMappingsAutoRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp', 
                [], [], 
                '''                Override default maximum for number of group
                mappings from autorp mapping agent
                ''',
                'group_mappings_auto_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-states', REFERENCE_CLASS, 'RegisterStates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.RegisterStates', 
                [], [], 
                '''                Override default maximum for number of
                sparse-mode source registers
                ''',
                'register_states',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('route-interfaces', REFERENCE_CLASS, 'RouteInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces', 
                [], [], 
                '''                Override default maximum for number of
                route-interfaces
                ''',
                'route_interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum.Routes', 
                [], [], 
                '''                Override default maximum for number of routes
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Ssm' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Ssm',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if SSM is disabled on this router
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('range', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups enabled with SSM
                ''',
                'range',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ssm',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Injects.Inject' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Injects.Inject',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('rpf-proxy-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RPF Proxy Address
                ''',
                'rpf_proxy_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False, max_elements=22, min_elements=1),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'inject',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Injects' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Injects',
            False, 
            [
            _MetaInfoClassMember('inject', REFERENCE_LIST, 'Inject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Injects.Inject', 
                [], [], 
                '''                Inject Explicit PIM RPF Vector Proxy's
                ''',
                'inject',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'injects',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress',
            False, 
            [
            _MetaInfoClassMember('rp-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RP address of Rendezvous Point
                ''',
                'rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('rp-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RP address of Rendezvous Point
                        ''',
                        'rp_address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list of groups that should map to a
                given RP
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE Indicates if static RP config overrides
                AutoRP and BSR
                ''',
                'auto_rp_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.BidirRpAddresses' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.BidirRpAddresses',
            False, 
            [
            _MetaInfoClassMember('bidir-rp-address', REFERENCE_LIST, 'BidirRpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress', 
                [], [], 
                '''                Address of the Rendezvous Point
                ''',
                'bidir_rp_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bidir-rp-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Bsr.CandidateBsr' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Bsr.CandidateBsr',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BSR Address configured
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BSR Address configured
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BSR Address configured
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Hash Mask Length for this candidate BSR
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the Candidate BSR
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of Candidate-RP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of Candidate-RP
                        ''',
                        'address',
                        'Cisco-IOS-XR-ipv4-pim-cfg', True),
                ]),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'PimProtocolModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimProtocolModeEnum', 
                [], [], 
                '''                SM or Bidir
                ''',
                'mode',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('group-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifying the group range for the
                Candidate-RP
                ''',
                'group_list',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('30', '600')], [], 
                '''                Advertisement interval
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Priority of the CRP
                ''',
                'priority',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Bsr.CandidateRps' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Bsr.CandidateRps',
            False, 
            [
            _MetaInfoClassMember('candidate-rp', REFERENCE_LIST, 'CandidateRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp', 
                [], [], 
                '''                Address of PIM SM BSR Candidate-RP
                ''',
                'candidate_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'candidate-rps',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Bsr' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Bsr',
            False, 
            [
            _MetaInfoClassMember('candidate-bsr', REFERENCE_CLASS, 'CandidateBsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Bsr.CandidateBsr', 
                [], [], 
                '''                PIM Candidate BSR configuration
                ''',
                'candidate_bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('candidate-rps', REFERENCE_CLASS, 'CandidateRps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Bsr.CandidateRps', 
                [], [], 
                '''                PIM RP configuration
                ''',
                'candidate_rps',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'bsr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Paths.Path' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Source Address
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('rpf-proxy-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                RPF Proxy Address
                ''',
                'rpf_proxy_address',
                'Cisco-IOS-XR-ipv4-pim-cfg', False, max_elements=22, min_elements=1),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Paths' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Paths.Path', 
                [], [], 
                '''                Inject PIM RPF Vector Proxy's
                ''',
                'path',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.AllowRp' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.AllowRp',
            False, 
            [
            _MetaInfoClassMember('group-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable groups
                ''',
                'group_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list specifiying applicable RPs
                ''',
                'rp_list_name',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'allow-rp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.Convergence' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.Convergence',
            False, 
            [
            _MetaInfoClassMember('link-down-prune-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Delay prunes if route join state transitions to
                not-joined on link down
                ''',
                'link_down_prune_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-conflict-join-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '15')], [], 
                '''                Dampen first join if RPF path is through one of
                the downstream neighbor
                ''',
                'rpf_conflict_join_delay',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'convergence',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr',
            False, 
            [
            _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Original address
                ''',
                'source',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary address
                ''',
                'primary',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('backup', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Backup address
                ''',
                'backup',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Masklen
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-pim-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cj-multicast-only-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs',
            False, 
            [
            _MetaInfoClassMember('cj-multicast-only-frr', REFERENCE_LIST, 'CjMulticastOnlyFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr', 
                [], [], 
                '''                Clone Join Multicast Only FRR
                ''',
                'cj_multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'cj-multicast-only-frrs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext.Ipv4' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext.Ipv4',
            False, 
            [
            _MetaInfoClassMember('accept-register', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list which specifies unauthorized sources
                ''',
                'accept_register',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('allow-rp', REFERENCE_CLASS, 'AllowRp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.AllowRp', 
                [], [], 
                '''                Enable allow-rp filtering for SM joins
                ''',
                'allow_rp',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-candidate-rps', REFERENCE_CLASS, 'AutoRpCandidateRps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.AutoRpCandidateRps', 
                [], [], 
                '''                Configure Candidate-RPs
                ''',
                'auto_rp_candidate_rps',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Rendezvous Point discovery through the
                AutoRP protocol
                ''',
                'auto_rp_disable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('auto-rp-mapping-agent', REFERENCE_CLASS, 'AutoRpMappingAgent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.AutoRpMappingAgent', 
                [], [], 
                '''                Configure AutoRP Mapping Agent
                ''',
                'auto_rp_mapping_agent',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bidir-rp-addresses', REFERENCE_CLASS, 'BidirRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.BidirRpAddresses', 
                [], [], 
                '''                Configure Bidirectional PIM Rendezvous Point
                ''',
                'bidir_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('bsr', REFERENCE_CLASS, 'Bsr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Bsr', 
                [], [], 
                '''                PIM BSR configuration
                ''',
                'bsr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('cj-multicast-only-frrs', REFERENCE_CLASS, 'CjMulticastOnlyFrrs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs', 
                [], [], 
                '''                Clone Join Multicast Only FRR
                ''',
                'cj_multicast_only_frrs',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('convergence', REFERENCE_CLASS, 'Convergence' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Convergence', 
                [], [], 
                '''                Configure convergence parameters
                ''',
                'convergence',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('cs-multicast-only-frrs', REFERENCE_CLASS, 'CsMulticastOnlyFrrs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs', 
                [], [], 
                '''                Clone Source Multicast Only FRR
                ''',
                'cs_multicast_only_frrs',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('inheritable-defaults', REFERENCE_CLASS, 'InheritableDefaults' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.InheritableDefaults', 
                [], [], 
                '''                Inheritable defaults
                ''',
                'inheritable_defaults',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('injects', REFERENCE_CLASS, 'Injects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Injects', 
                [], [], 
                '''                Inject Explicit PIM RPF Vector Proxy's
                ''',
                'injects',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Interfaces', 
                [], [], 
                '''                Interface-level Configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('log-neighbor-changes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                PIM neighbor state change logging is turned on
                if configured
                ''',
                'log_neighbor_changes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Maximum', 
                [], [], 
                '''                Configure PIM State Limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('multicast-only-frr', REFERENCE_CLASS, 'MulticastOnlyFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.MulticastOnlyFrr', 
                [], [], 
                '''                Multicast Only FRR
                ''',
                'multicast_only_frr',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('multipath', REFERENCE_ENUM_CLASS, 'PimMultipathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'PimMultipathEnum', 
                [], [], 
                '''                Enable equal-cost multipath routing
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-receive', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when receiving PIM
                messages
                ''',
                'neighbor_check_on_receive',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-check-on-send', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable PIM neighbor checking when sending
                join-prunes
                ''',
                'neighbor_check_on_send',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('neighbor-filter', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list of neighbors to be filtered
                ''',
                'neighbor_filter',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('nsf', REFERENCE_CLASS, 'Nsf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Nsf', 
                [], [], 
                '''                Configure Non-stop forwarding (NSF) options
                ''',
                'nsf',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('old-register-checksum', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Generate registers compatible with older IOS
                versions
                ''',
                'old_register_checksum',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Paths', 
                [], [], 
                '''                Inject PIM RPF Vector Proxy's
                ''',
                'paths',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('register-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source address to use for register messages
                ''',
                'register_source',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rp-static-deny', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Configure static RP deny range
                ''',
                'rp_static_deny',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf', REFERENCE_CLASS, 'Rpf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Rpf', 
                [], [], 
                '''                Configure RPF options
                ''',
                'rpf',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-redirect', REFERENCE_CLASS, 'RpfRedirect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.RpfRedirect', 
                [], [], 
                '''                Configure RPF-redirect feature
                ''',
                'rpf_redirect',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('rpf-vector-enable', REFERENCE_CLASS, 'RpfVectorEnable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.RpfVectorEnable', 
                [], [], 
                '''                Enable PIM RPF Vector Proxy's
                ''',
                'rpf_vector_enable',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sg-expiry-timer', REFERENCE_CLASS, 'SgExpiryTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.SgExpiryTimer', 
                [], [], 
                '''                Configure expiry timer for S,G routes
                ''',
                'sg_expiry_timer',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('sparse-mode-rp-addresses', REFERENCE_CLASS, 'SparseModeRpAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.SparseModeRpAddresses', 
                [], [], 
                '''                Configure Sparse-Mode Rendezvous Point
                ''',
                'sparse_mode_rp_addresses',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('spt-threshold-infinity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure threshold of infinity for switching to
                SPT on last-hop
                ''',
                'spt_threshold_infinity',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm', REFERENCE_CLASS, 'Ssm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4.Ssm', 
                [], [], 
                '''                Configure IP Multicast SSM
                ''',
                'ssm',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ssm-allow-override', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow SSM ranges to be overridden by more
                specific ranges
                ''',
                'ssm_allow_override',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-data-registers', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress data registers after initial state
                setup
                ''',
                'suppress_data_registers',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('suppress-rpf-prunes', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Suppress prunes triggered as a result of RPF
                changes
                ''',
                'suppress_rpf_prunes',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim.DefaultContext' : {
        'meta_info' : _MetaInfoClass('Pim.DefaultContext',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv4', 
                [], [], 
                '''                IPV4 commands
                ''',
                'ipv4',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext.Ipv6', 
                [], [], 
                '''                IPV6 commands
                ''',
                'ipv6',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'default-context',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
    'Pim' : {
        'meta_info' : _MetaInfoClass('Pim',
            False, 
            [
            _MetaInfoClassMember('default-context', REFERENCE_CLASS, 'DefaultContext' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.DefaultContext', 
                [], [], 
                '''                Default Context
                ''',
                'default_context',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg', 'Pim.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-pim-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-pim-cfg',
            'pim',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-pim-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_pim_cfg'
        ),
    },
}
_meta_table['Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses.SparseModeRpAddress']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.GroupMappingsAutoRp']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.BsrGroupMappings']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.RegisterStates']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.RouteInterfaces']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.BsrCandidateRpCache']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum.Routes']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Injects.Inject']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Injects']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses.BidirRpAddress']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps.CandidateRp']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateBsr']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr.CandidateRps']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Paths.Path']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Paths']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.MaximumRoutes']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces.Interface']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.SparseModeRpAddresses']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.MulticastOnlyFrr']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.CsMulticastOnlyFrrs']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.InheritableDefaults']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Rpf']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Maximum']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.SgExpiryTimer']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.RpfVectorEnable']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Ssm']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Injects']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.BidirRpAddresses']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Bsr']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Paths']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.AllowRp']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Convergence']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.Interfaces']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4.CjMulticastOnlyFrrs']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses.SparseModeRpAddress']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.GroupMappingsAutoRp']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.BsrGroupMappings']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.RegisterStates']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.RouteInterfaces']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.BsrCandidateRpCache']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum.Routes']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses.BidirRpAddress']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps.CandidateRp']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateBsr']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr.CandidateRps']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.MaximumRoutes']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.SparseModeRpAddresses']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.InheritableDefaults']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Rpf']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Maximum']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.SgExpiryTimer']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.RpfVectorEnable']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Ssm']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.BidirRpAddresses']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Bsr']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.AllowRp']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.EmbeddedRpAddresses']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Convergence']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6.Interfaces']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv4']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf']['meta_info']
_meta_table['Pim.Vrfs.Vrf.Ipv6']['meta_info'].parent =_meta_table['Pim.Vrfs.Vrf']['meta_info']
_meta_table['Pim.Vrfs.Vrf']['meta_info'].parent =_meta_table['Pim.Vrfs']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface.MaximumRoutes']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Interfaces.Interface']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Interfaces']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.SparseModeRpAddresses.SparseModeRpAddress']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.SparseModeRpAddresses']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrGlobalGroupMappings']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalRoutes']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalGroupMappingsAutoRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrGlobalCandidateRpCache']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalRegisterStates']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.GlobalRouteInterfaces']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.GroupMappingsAutoRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrGroupMappings']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.RegisterStates']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.RouteInterfaces']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.BsrCandidateRpCache']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum.Routes']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.BidirRpAddresses.BidirRpAddress']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.BidirRpAddresses']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Bsr.CandidateRps.CandidateRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Bsr.CandidateRps']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Bsr.CandidateBsr']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Bsr']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Bsr.CandidateRps']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.Bsr']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.EmbeddedRpAddresses.EmbeddedRpAddress']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6.EmbeddedRpAddresses']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Interfaces']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.SparseModeRpAddresses']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.InheritableDefaults']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Rpf']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.SgExpiryTimer']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.RpfVectorEnable']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Nsf']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Maximum']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Ssm']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.BidirRpAddresses']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Bsr']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.AllowRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.EmbeddedRpAddresses']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6.Convergence']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv6']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface.RedirectBundle']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface.MaximumRoutes']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Interfaces.Interface']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Interfaces']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.AutoRpCandidateRps.AutoRpCandidateRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.AutoRpCandidateRps']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent.Parameters']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent.CacheLimit']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.SparseModeRpAddresses.SparseModeRpAddress']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.SparseModeRpAddresses']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs.CsMulticastOnlyFrr']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrGlobalGroupMappings']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalRoutes']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalGroupMappingsAutoRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrGlobalCandidateRpCache']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalRegisterStates']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.GlobalRouteInterfaces']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.GroupMappingsAutoRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrGroupMappings']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.RegisterStates']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.RouteInterfaces']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.BsrCandidateRpCache']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum.Routes']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Injects.Inject']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Injects']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.BidirRpAddresses.BidirRpAddress']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.BidirRpAddresses']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Bsr.CandidateRps.CandidateRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Bsr.CandidateRps']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Bsr.CandidateBsr']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Bsr']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Bsr.CandidateRps']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Bsr']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Paths.Path']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.Paths']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs.CjMulticastOnlyFrr']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.RpfRedirect']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Interfaces']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.AutoRpCandidateRps']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.AutoRpMappingAgent']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.SparseModeRpAddresses']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.MulticastOnlyFrr']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.CsMulticastOnlyFrrs']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.InheritableDefaults']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Rpf']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.SgExpiryTimer']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.RpfVectorEnable']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Nsf']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Maximum']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Ssm']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Injects']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.BidirRpAddresses']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Bsr']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Paths']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.AllowRp']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.Convergence']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4.CjMulticastOnlyFrrs']['meta_info'].parent =_meta_table['Pim.DefaultContext.Ipv4']['meta_info']
_meta_table['Pim.DefaultContext.Ipv6']['meta_info'].parent =_meta_table['Pim.DefaultContext']['meta_info']
_meta_table['Pim.DefaultContext.Ipv4']['meta_info'].parent =_meta_table['Pim.DefaultContext']['meta_info']
_meta_table['Pim.Vrfs']['meta_info'].parent =_meta_table['Pim']['meta_info']
_meta_table['Pim.DefaultContext']['meta_info'].parent =_meta_table['Pim']['meta_info']
