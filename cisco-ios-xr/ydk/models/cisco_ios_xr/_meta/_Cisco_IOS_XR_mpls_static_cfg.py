


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsStaticPathRoleEnum' : _MetaInfoEnum('MplsStaticPathRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg',
        {
            'primary':'primary',
            'backup':'backup',
            'primary-backup':'primary_backup',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticPathEnum' : _MetaInfoEnum('MplsStaticPathEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg',
        {
            'pop-and-lookup':'pop_and_lookup',
            'cross-connect':'cross_connect',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticLabelModeEnum' : _MetaInfoEnum('MplsStaticLabelModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg',
        {
            'per-vrf':'per_vrf',
            'per-prefix':'per_prefix',
            'lsp':'lsp',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticOutLabelTypesEnum' : _MetaInfoEnum('MplsStaticOutLabelTypesEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg',
        {
            'none':'none',
            'out-label':'out_label',
            'pop':'pop',
            'exp-null':'exp_null',
            'ipv6-explicit-null':'ipv6_explicit_null',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticAddressFamilyEnum' : _MetaInfoEnum('MplsStaticAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg',
        {
            'ipv4-unicast':'ipv4_unicast',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticNhAddressFamilyEnum' : _MetaInfoEnum('MplsStaticNhAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticNhModeEnum' : _MetaInfoEnum('MplsStaticNhModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg',
        {
            'configured':'configured',
            'resolve':'resolve',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'backup-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel',
            False, 
            [
            _MetaInfoClassMember('in-label-value', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'in_label_value',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode (PerVRF, PerPrefix or LSP)
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address (IPv4/6 depending on AFI)
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('tlh-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Top Label Hashing Mode
                ''',
                'tlh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'in-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath',
            False, 
            [
            _MetaInfoClassMember('lsp-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                LSP Name
                ''',
                'lsp_name',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('backup-paths', REFERENCE_CLASS, 'BackupPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths', 
                [], [], 
                '''                Backup Path Parameters
                ''',
                'backup_paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS Static Apply Enable
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('in-label', REFERENCE_CLASS, 'InLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-switched-path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.LabelSwitchedPaths',
            False, 
            [
            _MetaInfoClassMember('label-switched-path', REFERENCE_LIST, 'LabelSwitchedPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath', 
                [], [], 
                '''                Label Switched Path
                ''',
                'label_switched_path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-switched-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode (PerVRF, PerPrefix or LSP)
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address (IPv4/6 depending on AFI)
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash',
            False, 
            [
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'top-label-hash',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode (PerVRF, PerPrefix or LSP)
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address (IPv4/6 depending on AFI)
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticAddressFamilyEnum', 
                [], [], 
                '''                Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS Static Apply Enable
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('top-label-hash', REFERENCE_CLASS, 'TopLabelHash' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash', 
                [], [], 
                '''                Top Label Hash
                ''',
                'top_label_hash',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af', 
                [], [], 
                '''                Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs', 
                [], [], 
                '''                Address Family Table
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS Static Apply Enable
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-switched-paths', REFERENCE_CLASS, 'LabelSwitchedPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.LabelSwitchedPaths', 
                [], [], 
                '''                Table of the Label Switched Paths
                ''',
                'label_switched_paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf', 
                [], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Interfaces.Interface', 
                [], [], 
                '''                MPLS Static Interface Enable
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'backup-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel',
            False, 
            [
            _MetaInfoClassMember('in-label-value', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'in_label_value',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode (PerVRF, PerPrefix or LSP)
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address (IPv4/6 depending on AFI)
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('tlh-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Top Label Hashing Mode
                ''',
                'tlh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'in-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath',
            False, 
            [
            _MetaInfoClassMember('lsp-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                LSP Name
                ''',
                'lsp_name',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('backup-paths', REFERENCE_CLASS, 'BackupPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths', 
                [], [], 
                '''                Backup Path Parameters
                ''',
                'backup_paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS Static Apply Enable
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('in-label', REFERENCE_CLASS, 'InLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'in_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-switched-path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.LabelSwitchedPaths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.LabelSwitchedPaths',
            False, 
            [
            _MetaInfoClassMember('label-switched-path', REFERENCE_LIST, 'LabelSwitchedPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath', 
                [], [], 
                '''                Label Switched Path
                ''',
                'label_switched_path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-switched-paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode (PerVRF, PerPrefix or LSP)
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address (IPv4/6 depending on AFI)
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash',
            False, 
            [
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'top-label-hash',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelModeEnum', 
                [], [], 
                '''                Label Mode (PerVRF, PerPrefix or LSP)
                ''',
                'label_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address (IPv4/6 depending on AFI)
                ''',
                'prefix',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '16')], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticNhAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhAddressFamilyEnum', 
                [], [], 
                '''                Next hop Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('backup-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16')], [], 
                '''                Backup ID
                ''',
                'backup_id',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypesEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypesEnum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '254')], [], 
                '''                NH Path Metric
                ''',
                'metric',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IP Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IP Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Outgoing/NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('nh-mode', REFERENCE_ENUM_CLASS, 'MplsStaticNhModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticNhModeEnum', 
                [], [], 
                '''                Next hop mode
                ''',
                'nh_mode',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-role', REFERENCE_ENUM_CLASS, 'MplsStaticPathRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathRoleEnum', 
                [], [], 
                '''                Path Role
                ''',
                'path_role',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPathEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPathEnum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticAddressFamilyEnum', 
                [], [], 
                '''                Address Family
                ''',
                'afi',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS Static Apply Enable
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('top-label-hash', REFERENCE_CLASS, 'TopLabelHash' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash', 
                [], [], 
                '''                Top Label Hash
                ''',
                'top_label_hash',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af', 
                [], [], 
                '''                Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs', 
                [], [], 
                '''                Address Family Table
                ''',
                'afs',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS Static Apply Enable
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-switched-paths', REFERENCE_CLASS, 'LabelSwitchedPaths' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.LabelSwitchedPaths', 
                [], [], 
                '''                Table of the Label Switched Paths
                ''',
                'label_switched_paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic' : {
        'meta_info' : _MetaInfoClass('MplsStatic',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf', 
                [], [], 
                '''                Default VRF
                ''',
                'default_vrf',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MPLS Static Apply Enable
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Interfaces', 
                [], [], 
                '''                MPLS Static Interface Table
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'mpls-static',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
}
_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath.Paths']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.LabelSwitchedPaths']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf']['meta_info'].parent =_meta_table['MplsStatic.Vrfs']['meta_info']
_meta_table['MplsStatic.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsStatic.Interfaces']['meta_info']
_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths.Path']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths']['meta_info']
_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths']['meta_info']
_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.BackupPaths']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.InLabel']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath.Paths']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths.LabelSwitchedPath']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs']['meta_info']
_meta_table['MplsStatic.DefaultVrf.LabelSwitchedPaths']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf']['meta_info']
_meta_table['MplsStatic.Vrfs']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
_meta_table['MplsStatic.Interfaces']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
_meta_table['MplsStatic.DefaultVrf']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
