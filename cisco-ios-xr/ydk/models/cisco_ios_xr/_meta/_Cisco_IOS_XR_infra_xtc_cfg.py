


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PceDisjointPathEnum' : _MetaInfoEnum('PceDisjointPathEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg',
        {
            'link':'link',
            'node':'node',
            'srlg':'srlg',
        }, 'Cisco-IOS-XR-infra-xtc-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg']),
    'PceExplicitPathHopEnum' : _MetaInfoEnum('PceExplicitPathHopEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg',
        {
            'address':'address',
            'sid-node':'sid_node',
            'sid-adjancency':'sid_adjancency',
            'binding-sid':'binding_sid',
        }, 'Cisco-IOS-XR-infra-xtc-cfg', _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg']),
    'Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity' : {
        'meta_info' : _MetaInfoClass('Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity',
            False, 
            [
            _MetaInfoClassMember('exclude-any', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Exclude-any affinity value
                ''',
                'exclude_any',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('include-all', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Include-all affinity value
                ''',
                'include_all',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('include-any', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Include-any affinity value
                ''',
                'include_any',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'affinity',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority' : {
        'meta_info' : _MetaInfoClass('Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority',
            False, 
            [
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Hold Priority
                ''',
                'hold_priority',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Setup Priority
                ''',
                'setup_priority',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe' : {
        'meta_info' : _MetaInfoClass('Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe',
            False, 
            [
            _MetaInfoClassMember('affinity', REFERENCE_CLASS, 'Affinity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity', 
                [], [], 
                '''                LSP Affinity
                ''',
                'affinity',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Bandwidth configuration
                ''',
                'bandwidth',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('fast-protect', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable fast protection
                ''',
                'fast_protect',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_CLASS, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority', 
                [], [], 
                '''                Tunnel Setup and Hold Priorities
                ''',
                'priority',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'rsvp-te',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.PccAddresses.PccAddress.LspNames.LspName' : {
        'meta_info' : _MetaInfoClass('Pce.PccAddresses.PccAddress.LspNames.LspName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                LSP name
                ''',
                'name',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('explicit-path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Explicit-path name
                ''',
                'explicit_path_name',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('rsvp-te', REFERENCE_CLASS, 'RsvpTe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe', 
                [], [], 
                '''                RSVP-TE configuration
                ''',
                'rsvp_te',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('undelegate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Undelegate LSP
                ''',
                'undelegate',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'lsp-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.PccAddresses.PccAddress.LspNames' : {
        'meta_info' : _MetaInfoClass('Pce.PccAddresses.PccAddress.LspNames',
            False, 
            [
            _MetaInfoClassMember('lsp-name', REFERENCE_LIST, 'LspName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.PccAddresses.PccAddress.LspNames.LspName', 
                [], [], 
                '''                MPLS label switched path
                ''',
                'lsp_name',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'lsp-names',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.PccAddresses.PccAddress' : {
        'meta_info' : _MetaInfoClass('Pce.PccAddresses.PccAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('lsp-names', REFERENCE_CLASS, 'LspNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.PccAddresses.PccAddress.LspNames', 
                [], [], 
                '''                MPLS label switched path
                ''',
                'lsp_names',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'pcc-address',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.PccAddresses' : {
        'meta_info' : _MetaInfoClass('Pce.PccAddresses',
            False, 
            [
            _MetaInfoClassMember('pcc-address', REFERENCE_LIST, 'PccAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.PccAddresses.PccAddress', 
                [], [], 
                '''                Path computation client address
                ''',
                'pcc_address',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'pcc-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.Logging' : {
        'meta_info' : _MetaInfoClass('Pce.Logging',
            False, 
            [
            _MetaInfoClassMember('fallback', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Logging fallback configuration
                ''',
                'fallback',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('no-path', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Logging NO-PATH configuration
                ''',
                'no_path',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.Backoff' : {
        'meta_info' : _MetaInfoClass('Pce.Backoff',
            False, 
            [
            _MetaInfoClassMember('difference', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Backoff common difference configuration
                ''',
                'difference',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Backoff common ratio configuration
                ''',
                'ratio',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Backoff threshold configuration
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'backoff',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.StateSyncs.StateSync' : {
        'meta_info' : _MetaInfoClass('Pce.StateSyncs.StateSync',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'state-sync',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.StateSyncs' : {
        'meta_info' : _MetaInfoClass('Pce.StateSyncs',
            False, 
            [
            _MetaInfoClassMember('state-sync', REFERENCE_LIST, 'StateSync' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.StateSyncs.StateSync', 
                [], [], 
                '''                Standby PCE ipv4 address
                ''',
                'state_sync',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'state-syncs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Pce.SegmentRouting',
            False, 
            [
            _MetaInfoClassMember('strict-sid-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use strict-sid-only configuration
                ''',
                'strict_sid_only',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('te-latency', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use te-latency algorithm configuration
                ''',
                'te_latency',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'segment-routing',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.Timers' : {
        'meta_info' : _MetaInfoClass('Pce.Timers',
            False, 
            [
            _MetaInfoClassMember('keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Keepalive interval in seconds, zero to disable
                ''',
                'keepalive',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('minimum-peer-keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Minimum acceptable peer proposed keepalive
                interval
                ''',
                'minimum_peer_keepalive',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('reoptimization-timer', ATTRIBUTE, 'int' , None, None, 
                [('10', '3600')], [], 
                '''                Topology reoptimization timer configuration
                ''',
                'reoptimization_timer',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.Netconf.NetconfSsh' : {
        'meta_info' : _MetaInfoClass('Pce.Netconf.NetconfSsh',
            False, 
            [
            _MetaInfoClassMember('netconf-ssh-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Password to use for NETCONF SSH connections
                ''',
                'netconf_ssh_password',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('netconf-ssh-user', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                User name to use for NETCONF SSH connections
                ''',
                'netconf_ssh_user',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'netconf-ssh',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.Netconf' : {
        'meta_info' : _MetaInfoClass('Pce.Netconf',
            False, 
            [
            _MetaInfoClassMember('netconf-ssh', REFERENCE_CLASS, 'NetconfSsh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.Netconf.NetconfSsh', 
                [], [], 
                '''                NETCONF SSH configuration
                ''',
                'netconf_ssh',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'netconf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.DisjointPath.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Pce.DisjointPath.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            _MetaInfoClassMember('dp-type', REFERENCE_ENUM_CLASS, 'PceDisjointPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceDisjointPathEnum', 
                [], [], 
                '''                Disjoiness type
                ''',
                'dp_type',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            _MetaInfoClassMember('sub-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sub group ID, 0 to unset
                ''',
                'sub_id',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            _MetaInfoClassMember('strict', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Fallback
                ''',
                'strict',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.DisjointPath.Groups' : {
        'meta_info' : _MetaInfoClass('Pce.DisjointPath.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.DisjointPath.Groups.Group', 
                [], [], 
                '''                Association Group Configuration
                ''',
                'group',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.DisjointPath' : {
        'meta_info' : _MetaInfoClass('Pce.DisjointPath',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.DisjointPath.Groups', 
                [], [], 
                '''                Association configuration
                ''',
                'groups',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'disjoint-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop' : {
        'meta_info' : _MetaInfoClass('Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Hop Index
                ''',
                'index',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address
                ''',
                'address',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'PceExplicitPathHopEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'PceExplicitPathHopEnum', 
                [], [], 
                '''                Path hop type
                ''',
                'hop_type',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('mpls-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                MPLS Label
                ''',
                'mpls_label',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote IPv4 address
                ''',
                'remote_address',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'path-hop',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.ExplicitPaths.ExplicitPath.PathHops' : {
        'meta_info' : _MetaInfoClass('Pce.ExplicitPaths.ExplicitPath.PathHops',
            False, 
            [
            _MetaInfoClassMember('path-hop', REFERENCE_LIST, 'PathHop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop', 
                [], [], 
                '''                Explicit path hop configuration
                ''',
                'path_hop',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'path-hops',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.ExplicitPaths.ExplicitPath' : {
        'meta_info' : _MetaInfoClass('Pce.ExplicitPaths.ExplicitPath',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Explicit-path name
                ''',
                'name',
                'Cisco-IOS-XR-infra-xtc-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('path-hops', REFERENCE_CLASS, 'PathHops' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.ExplicitPaths.ExplicitPath.PathHops', 
                [], [], 
                '''                Path Hops
                ''',
                'path_hops',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'explicit-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce.ExplicitPaths' : {
        'meta_info' : _MetaInfoClass('Pce.ExplicitPaths',
            False, 
            [
            _MetaInfoClassMember('explicit-path', REFERENCE_LIST, 'ExplicitPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.ExplicitPaths.ExplicitPath', 
                [], [], 
                '''                Explicit-path configuration
                ''',
                'explicit_path',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'explicit-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
    'Pce' : {
        'meta_info' : _MetaInfoClass('Pce',
            False, 
            [
            _MetaInfoClassMember('backoff', REFERENCE_CLASS, 'Backoff' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.Backoff', 
                [], [], 
                '''                PCE backoff configuration
                ''',
                'backoff',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('disjoint-path', REFERENCE_CLASS, 'DisjointPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.DisjointPath', 
                [], [], 
                '''                Disjoint path configuration
                ''',
                'disjoint_path',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                True only
                ''',
                'enable',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('explicit-paths', REFERENCE_CLASS, 'ExplicitPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.ExplicitPaths', 
                [], [], 
                '''                Explicit paths
                ''',
                'explicit_paths',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.Logging', 
                [], [], 
                '''                PCE logging configuration
                ''',
                'logging',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('netconf', REFERENCE_CLASS, 'Netconf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.Netconf', 
                [], [], 
                '''                NETCONF configuration
                ''',
                'netconf',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                MD5 password
                ''',
                'password',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('pcc-addresses', REFERENCE_CLASS, 'PccAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.PccAddresses', 
                [], [], 
                '''                Path computation client configuration
                ''',
                'pcc_addresses',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.SegmentRouting', 
                [], [], 
                '''                PCE segment-routing configuration
                ''',
                'segment_routing',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('server-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of PCE server
                ''',
                'server_address',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('state-syncs', REFERENCE_CLASS, 'StateSyncs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.StateSyncs', 
                [], [], 
                '''                Standby PCE configuration
                ''',
                'state_syncs',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg', 'Pce.Timers', 
                [], [], 
                '''                PCE Timers configuration
                ''',
                'timers',
                'Cisco-IOS-XR-infra-xtc-cfg', False),
            ],
            'Cisco-IOS-XR-infra-xtc-cfg',
            'pce',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-xtc-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_xtc_cfg'
        ),
    },
}
_meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Affinity']['meta_info'].parent =_meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe']['meta_info']
_meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe.Priority']['meta_info'].parent =_meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe']['meta_info']
_meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName.RsvpTe']['meta_info'].parent =_meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName']['meta_info']
_meta_table['Pce.PccAddresses.PccAddress.LspNames.LspName']['meta_info'].parent =_meta_table['Pce.PccAddresses.PccAddress.LspNames']['meta_info']
_meta_table['Pce.PccAddresses.PccAddress.LspNames']['meta_info'].parent =_meta_table['Pce.PccAddresses.PccAddress']['meta_info']
_meta_table['Pce.PccAddresses.PccAddress']['meta_info'].parent =_meta_table['Pce.PccAddresses']['meta_info']
_meta_table['Pce.StateSyncs.StateSync']['meta_info'].parent =_meta_table['Pce.StateSyncs']['meta_info']
_meta_table['Pce.Netconf.NetconfSsh']['meta_info'].parent =_meta_table['Pce.Netconf']['meta_info']
_meta_table['Pce.DisjointPath.Groups.Group']['meta_info'].parent =_meta_table['Pce.DisjointPath.Groups']['meta_info']
_meta_table['Pce.DisjointPath.Groups']['meta_info'].parent =_meta_table['Pce.DisjointPath']['meta_info']
_meta_table['Pce.ExplicitPaths.ExplicitPath.PathHops.PathHop']['meta_info'].parent =_meta_table['Pce.ExplicitPaths.ExplicitPath.PathHops']['meta_info']
_meta_table['Pce.ExplicitPaths.ExplicitPath.PathHops']['meta_info'].parent =_meta_table['Pce.ExplicitPaths.ExplicitPath']['meta_info']
_meta_table['Pce.ExplicitPaths.ExplicitPath']['meta_info'].parent =_meta_table['Pce.ExplicitPaths']['meta_info']
_meta_table['Pce.PccAddresses']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.Logging']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.Backoff']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.StateSyncs']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.SegmentRouting']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.Timers']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.Netconf']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.DisjointPath']['meta_info'].parent =_meta_table['Pce']['meta_info']
_meta_table['Pce.ExplicitPaths']['meta_info'].parent =_meta_table['Pce']['meta_info']
