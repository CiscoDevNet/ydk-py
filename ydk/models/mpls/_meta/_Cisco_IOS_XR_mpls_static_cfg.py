


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MplsStaticOutLabelTypes_Enum' : _MetaInfoEnum('MplsStaticOutLabelTypes_Enum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg',
        {
            'none':'NONE',
            'out-label':'OUT_LABEL',
            'pop':'POP',
            'exp-null':'EXP_NULL',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticLabelMode_Enum' : _MetaInfoEnum('MplsStaticLabelMode_Enum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg',
        {
            'per-vrf':'PER_VRF',
            'per-prefix':'PER_PREFIX',
            'lsp':'LSP',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticPath_Enum' : _MetaInfoEnum('MplsStaticPath_Enum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg',
        {
            'pop-and-lookup':'POP_AND_LOOKUP',
            'cross-connect':'CROSS_CONNECT',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStaticAddressFamily_Enum' : _MetaInfoEnum('MplsStaticAddressFamily_Enum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg',
        {
            'ipv4-unicast':'IPV4_UNICAST',
        }, 'Cisco-IOS-XR-mpls-static-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg']),
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelMode_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode_Enum', 
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form
                <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypes_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes_Enum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IPv4 Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPath_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath_Enum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelMode_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode_Enum', 
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form
                <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypes_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes_Enum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IPv4 Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPath_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath_Enum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af.TopLabelHash',
            False, 
            [
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'top-label-hash',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticAddressFamily_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticAddressFamily_Enum', 
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
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('top-label-hash', REFERENCE_CLASS, 'TopLabelHash' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af.TopLabelHash', 
                [], [], 
                '''                Top Label Hash
                ''',
                'top_label_hash',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs.Af', 
                [], [], 
                '''                Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('MplsStatic.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf.Afs', 
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
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Interfaces.Interface', 
                [], [], 
                '''                MPLS Static Interface Enable
                ''',
                'interface',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelMode_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode_Enum', 
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form
                <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypes_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes_Enum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IPv4 Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPath_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath_Enum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType',
            False, 
            [
            _MetaInfoClassMember('label-mode', REFERENCE_ENUM_CLASS, 'MplsStaticLabelMode_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticLabelMode_Enum', 
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
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address (IPv4/6 depending on AFI)
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'label-type',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path',
            False, 
            [
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of paths
                ''',
                'path_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Next hop Interface with form
                <Interface>R/S/I/P
                ''',
                'interface_name',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('label-type', REFERENCE_ENUM_CLASS, 'MplsStaticOutLabelTypes_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticOutLabelTypes_Enum', 
                [], [], 
                '''                Type of label (Outlabel, ExpNull or Pop)
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('next-hop-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next Hop IPv4 Address
                ''',
                'next_hop_address',
                'Cisco-IOS-XR-mpls-static-cfg', False, [
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                    _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Next Hop IPv4 Address
                        ''',
                        'next_hop_address',
                        'Cisco-IOS-XR-mpls-static-cfg', False),
                ]),
            _MetaInfoClassMember('next-hop-label', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                NH Label
                ''',
                'next_hop_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('path-type', REFERENCE_ENUM_CLASS, 'MplsStaticPath_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticPath_Enum', 
                [], [], 
                '''                Type of Path (PopAndLookup, CrossConnect)
                ''',
                'path_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths',
            False, 
            [
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path', 
                [], [], 
                '''                Path Information
                ''',
                'path',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'paths',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel',
            False, 
            [
            _MetaInfoClassMember('local-label-id', ATTRIBUTE, 'int' , None, None, 
                [(16, 1048575)], [], 
                '''                Local Label
                ''',
                'local_label_id',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('label-type', REFERENCE_CLASS, 'LabelType' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType', 
                [], [], 
                '''                MPLS Static Local Label Value
                ''',
                'label_type',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('paths', REFERENCE_CLASS, 'Paths' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths', 
                [], [], 
                '''                Forward Path Parameters
                ''',
                'paths',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-label',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels',
            False, 
            [
            _MetaInfoClassMember('local-label', REFERENCE_LIST, 'LocalLabel' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel', 
                [], [], 
                '''                Specify Local Label
                ''',
                'local_label',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'local-labels',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash',
            False, 
            [
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'top-label-hash',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs.Af' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs.Af',
            False, 
            [
            _MetaInfoClassMember('afi', REFERENCE_ENUM_CLASS, 'MplsStaticAddressFamily_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStaticAddressFamily_Enum', 
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
            _MetaInfoClassMember('local-labels', REFERENCE_CLASS, 'LocalLabels' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels', 
                [], [], 
                '''                Local Label
                ''',
                'local_labels',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('top-label-hash', REFERENCE_CLASS, 'TopLabelHash' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash', 
                [], [], 
                '''                Top Label Hash
                ''',
                'top_label_hash',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf.Afs' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf.Afs',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_LIST, 'Af' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs.Af', 
                [], [], 
                '''                Address Family
                ''',
                'af',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'afs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-mpls-static-cfg', True),
            _MetaInfoClassMember('afs', REFERENCE_CLASS, 'Afs' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf.Afs', 
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
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic.Vrfs' : {
        'meta_info' : _MetaInfoClass('MplsStatic.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs.Vrf', 
                [], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
    'MplsStatic' : {
        'meta_info' : _MetaInfoClass('MplsStatic',
            False, 
            [
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.DefaultVrf', 
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
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Interfaces', 
                [], [], 
                '''                MPLS Static Interface Table
                ''',
                'interfaces',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg', 'MplsStatic.Vrfs', 
                [], [], 
                '''                VRF table
                ''',
                'vrfs',
                'Cisco-IOS-XR-mpls-static-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-static-cfg',
            'mpls-static',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-static-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_static_cfg'
        ),
    },
}
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af.TopLabelHash']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs.Af']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf.Afs']['meta_info']
_meta_table['MplsStatic.DefaultVrf.Afs']['meta_info'].parent =_meta_table['MplsStatic.DefaultVrf']['meta_info']
_meta_table['MplsStatic.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsStatic.Interfaces']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths.Path']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.LabelType']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel.Paths']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels.LocalLabel']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.LocalLabels']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af.TopLabelHash']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs.Af']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf.Afs']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf.Afs']['meta_info'].parent =_meta_table['MplsStatic.Vrfs.Vrf']['meta_info']
_meta_table['MplsStatic.Vrfs.Vrf']['meta_info'].parent =_meta_table['MplsStatic.Vrfs']['meta_info']
_meta_table['MplsStatic.DefaultVrf']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
_meta_table['MplsStatic.Interfaces']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
_meta_table['MplsStatic.Vrfs']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
