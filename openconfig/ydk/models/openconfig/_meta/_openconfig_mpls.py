


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'TeBandwidthTypeEnum' : _MetaInfoEnum('TeBandwidthTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'SPECIFIED':'SPECIFIED',
            'AUTO':'AUTO',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'MplsHopTypeEnum' : _MetaInfoEnum('MplsHopTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'LOOSE':'LOOSE',
            'STRICT':'STRICT',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'CspfTieBreakingEnum' : _MetaInfoEnum('CspfTieBreakingEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'RANDOM':'RANDOM',
            'LEAST_FILL':'LEAST_FILL',
            'MOST_FILL':'MOST_FILL',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'TeMetricTypeEnum' : _MetaInfoEnum('TeMetricTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'IGP':'IGP',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'MplsSrlgFloodingTypeEnum' : _MetaInfoEnum('MplsSrlgFloodingTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'FLOODED-SRLG':'FLOODED_SRLG',
            'STATIC-SRLG':'STATIC_SRLG',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'PathComputationMethodIdentity' : {
        'meta_info' : _MetaInfoClass('PathComputationMethodIdentity',
            False, 
            [
            ],
            'openconfig-mpls',
            'path-computation-method',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Global_.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_.Config',
            False, 
            [
            _MetaInfoClassMember('null-label', REFERENCE_IDENTITY_CLASS, 'NullLabelTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'NullLabelTypeIdentity', 
                [], [], 
                '''                The null-label type used, implicit or explicit
                ''',
                'null_label',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Global_.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_.State',
            False, 
            [
            _MetaInfoClassMember('null-label', REFERENCE_IDENTITY_CLASS, 'NullLabelTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'NullLabelTypeIdentity', 
                [], [], 
                '''                The null-label type used, implicit or explicit
                ''',
                'null_label',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Global_.MplsInterfaceAttributes.Interface.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_.MplsInterfaceAttributes.Interface.Config',
            False, 
            [
            _MetaInfoClassMember('mpls-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable MPLS forwarding on this interfacek
                ''',
                'mpls_enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to interface name
                ''',
                'name',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Global_.MplsInterfaceAttributes.Interface.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_.MplsInterfaceAttributes.Interface.State',
            False, 
            [
            _MetaInfoClassMember('mpls-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable MPLS forwarding on this interfacek
                ''',
                'mpls_enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to interface name
                ''',
                'name',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Global_.MplsInterfaceAttributes.Interface' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_.MplsInterfaceAttributes.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface name
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Global_.MplsInterfaceAttributes.Interface.Config', 
                [], [], 
                '''                Configuration parameters related to MPLS interfaces:
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Global_.MplsInterfaceAttributes.Interface.State', 
                [], [], 
                '''                State parameters related to TE interfaces
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'interface',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Global_.MplsInterfaceAttributes' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_.MplsInterfaceAttributes',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Global_.MplsInterfaceAttributes.Interface', 
                [], [], 
                '''                List of TE interfaces
                ''',
                'interface',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'mpls-interface-attributes',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Global_' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Global_.Config', 
                [], [], 
                '''                Top level global MPLS configuration
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('mpls-interface-attributes', REFERENCE_CLASS, 'MplsInterfaceAttributes' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Global_.MplsInterfaceAttributes', 
                [], [], 
                '''                Parameters related to MPLS interfaces
                ''',
                'mpls_interface_attributes',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Global_.State', 
                [], [], 
                '''                Top level global MPLS state
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'global',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg_.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg.Srlg_.Config',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cost of the SRLG to the computation
                algorithm
                ''',
                'cost',
                'openconfig-mpls', False),
            _MetaInfoClassMember('flooding-type', REFERENCE_ENUM_CLASS, 'MplsSrlgFloodingTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'MplsSrlgFloodingTypeEnum', 
                [], [], 
                '''                The type of SRLG, either flooded in the IGP or
                statically configured
                ''',
                'flooding_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SRLG group identifier
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                group ID for the SRLG
                ''',
                'value',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg_.State' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg.Srlg_.State',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The cost of the SRLG to the computation
                algorithm
                ''',
                'cost',
                'openconfig-mpls', False),
            _MetaInfoClassMember('flooding-type', REFERENCE_ENUM_CLASS, 'MplsSrlgFloodingTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'MplsSrlgFloodingTypeEnum', 
                [], [], 
                '''                The type of SRLG, either flooded in the IGP or
                statically configured
                ''',
                'flooding_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SRLG group identifier
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                group ID for the SRLG
                ''',
                'value',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.Config',
            False, 
            [
            _MetaInfoClassMember('from-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the a-side of the SRLG link
                ''',
                'from_address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('from-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the a-side of the SRLG link
                        ''',
                        'from_address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('from-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the a-side of the SRLG link
                        ''',
                        'from_address',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('to-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the z-side of the SRLG link
                ''',
                'to_address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('to-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the z-side of the SRLG link
                        ''',
                        'to_address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('to-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the z-side of the SRLG link
                        ''',
                        'to_address',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.State' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.State',
            False, 
            [
            _MetaInfoClassMember('from-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the a-side of the SRLG link
                ''',
                'from_address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('from-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the a-side of the SRLG link
                        ''',
                        'from_address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('from-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the a-side of the SRLG link
                        ''',
                        'from_address',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('to-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the z-side of the SRLG link
                ''',
                'to_address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('to-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the z-side of the SRLG link
                        ''',
                        'to_address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('to-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the z-side of the SRLG link
                        ''',
                        'to_address',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList',
            False, 
            [
            _MetaInfoClassMember('from-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The from address of the link in the SRLG
                ''',
                'from_address',
                'openconfig-mpls', True, [
                    _MetaInfoClassMember('from-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The from address of the link in the SRLG
                        ''',
                        'from_address',
                        'openconfig-mpls', True),
                    _MetaInfoClassMember('from-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The from address of the link in the SRLG
                        ''',
                        'from_address',
                        'openconfig-mpls', True),
                ]),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.Config', 
                [], [], 
                '''                Configuration parameters relating to the
                SRLG members
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.State', 
                [], [], 
                '''                State parameters relating to the SRLG
                members
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'members-list',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers',
            False, 
            [
            _MetaInfoClassMember('members-list', REFERENCE_LIST, 'MembersList' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList', 
                [], [], 
                '''                List of SRLG members, which are expressed
                as IP address endpoints of links contained in the
                SRLG
                ''',
                'members_list',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'static-srlg-members',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg.Srlg_' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg.Srlg_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The SRLG group identifier
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg.Srlg_.Config', 
                [], [], 
                '''                Configuration parameters related to the SRLG
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg.Srlg_.State', 
                [], [], 
                '''                State parameters related to the SRLG
                ''',
                'state',
                'openconfig-mpls', False),
            _MetaInfoClassMember('static-srlg-members', REFERENCE_CLASS, 'StaticSrlgMembers' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers', 
                [], [], 
                '''                SRLG members for static (not flooded) SRLGs 
                ''',
                'static_srlg_members',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'srlg',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.Srlg' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.Srlg',
            False, 
            [
            _MetaInfoClassMember('srlg', REFERENCE_LIST, 'Srlg_' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg.Srlg_', 
                [], [], 
                '''                List of shared risk link groups
                ''',
                'srlg',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'srlg',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdSpecificationEnum' : _MetaInfoEnum('ThresholdSpecificationEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'MIRRORED-UP-DOWN':'MIRRORED_UP_DOWN',
            'SEPARATE-UP-DOWN':'SEPARATE_UP_DOWN',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdTypeEnum' : _MetaInfoEnum('ThresholdTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'DELTA':'DELTA',
            'THRESHOLD-CROSSED':'THRESHOLD_CROSSED',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config',
            False, 
            [
            _MetaInfoClassMember('delta-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The percentage of the maximum-reservable-bandwidth
                considered as the delta that results in an IGP update
                being flooded
                ''',
                'delta_percentage',
                'openconfig-mpls', False),
            _MetaInfoClassMember('down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is decreasing.
                ''',
                'down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-specification', REFERENCE_ENUM_CLASS, 'ThresholdSpecificationEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdSpecificationEnum', 
                [], [], 
                '''                This value specifies whether a single set of threshold
                values should be used for both increasing and decreasing
                bandwidth when determining whether to trigger updated
                bandwidth values to be flooded in the IGP TE extensions.
                MIRRORED-UP-DOWN indicates that a single value (or set of
                values) should be used for both increasing and decreasing
                values, where SEPARATE-UP-DOWN specifies that the increasing
                and decreasing values will be separately specified
                ''',
                'threshold_specification',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_ENUM_CLASS, 'ThresholdTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config.ThresholdTypeEnum', 
                [], [], 
                '''                The type of threshold that should be used to specify the
                values at which bandwidth is flooded. DELTA indicates that
                the local system should flood IGP updates when a change in
                reserved bandwidth >= the specified delta occurs on the
                interface. Where THRESHOLD-CROSSED is specified, the local
                system should trigger an update (and hence flood) the
                reserved bandwidth when the reserved bandwidth changes such
                that it crosses, or becomes equal to one of the threshold
                values
                ''',
                'threshold_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth of the interface) at which bandwidth
                updates are flooded - used both when the bandwidth is
                increasing and decreasing
                ''',
                'up_down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is increasing.
                ''',
                'up_thresholds',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdSpecificationEnum' : _MetaInfoEnum('ThresholdSpecificationEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'MIRRORED-UP-DOWN':'MIRRORED_UP_DOWN',
            'SEPARATE-UP-DOWN':'SEPARATE_UP_DOWN',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdTypeEnum' : _MetaInfoEnum('ThresholdTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'DELTA':'DELTA',
            'THRESHOLD-CROSSED':'THRESHOLD_CROSSED',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State',
            False, 
            [
            _MetaInfoClassMember('delta-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The percentage of the maximum-reservable-bandwidth
                considered as the delta that results in an IGP update
                being flooded
                ''',
                'delta_percentage',
                'openconfig-mpls', False),
            _MetaInfoClassMember('down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is decreasing.
                ''',
                'down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-specification', REFERENCE_ENUM_CLASS, 'ThresholdSpecificationEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdSpecificationEnum', 
                [], [], 
                '''                This value specifies whether a single set of threshold
                values should be used for both increasing and decreasing
                bandwidth when determining whether to trigger updated
                bandwidth values to be flooded in the IGP TE extensions.
                MIRRORED-UP-DOWN indicates that a single value (or set of
                values) should be used for both increasing and decreasing
                values, where SEPARATE-UP-DOWN specifies that the increasing
                and decreasing values will be separately specified
                ''',
                'threshold_specification',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_ENUM_CLASS, 'ThresholdTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State.ThresholdTypeEnum', 
                [], [], 
                '''                The type of threshold that should be used to specify the
                values at which bandwidth is flooded. DELTA indicates that
                the local system should flood IGP updates when a change in
                reserved bandwidth >= the specified delta occurs on the
                interface. Where THRESHOLD-CROSSED is specified, the local
                system should trigger an update (and hence flood) the
                reserved bandwidth when the reserved bandwidth changes such
                that it crosses, or becomes equal to one of the threshold
                values
                ''',
                'threshold_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth of the interface) at which bandwidth
                updates are flooded - used both when the bandwidth is
                increasing and decreasing
                ''',
                'up_down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is increasing.
                ''',
                'up_thresholds',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.IgpFloodingBandwidth' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.IgpFloodingBandwidth',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config', 
                [], [], 
                '''                Configuration parameters for TED
                update threshold 
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State', 
                [], [], 
                '''                State parameters for TED update threshold 
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'igp-flooding-bandwidth',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config',
            False, 
            [
            _MetaInfoClassMember('admin-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name for mpls admin-group
                ''',
                'admin_group_name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('bit-position', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                bit-position value for mpls admin-group. The value
                for the admin group is an integer that represents one
                of the bit positions in the admin-group bitmask. Values
                between 0 and 31 are interpreted as the original limit
                of 32 admin groups. Values >=32 are interpreted as
                extended admin group values as per RFC7308.
                ''',
                'bit_position',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State',
            False, 
            [
            _MetaInfoClassMember('admin-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name for mpls admin-group
                ''',
                'admin_group_name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('bit-position', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                bit-position value for mpls admin-group. The value
                for the admin group is an integer that represents one
                of the bit positions in the admin-group bitmask. Values
                between 0 and 31 are interpreted as the original limit
                of 32 admin groups. Values >=32 are interpreted as
                extended admin group values as per RFC7308.
                ''',
                'bit_position',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup',
            False, 
            [
            _MetaInfoClassMember('admin-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name for mpls admin-group
                ''',
                'admin_group_name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config', 
                [], [], 
                '''                Configurable items for admin-groups
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State', 
                [], [], 
                '''                Operational state for admin-groups
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'admin-group',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.MplsAdminGroups' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.MplsAdminGroups',
            False, 
            [
            _MetaInfoClassMember('admin-group', REFERENCE_LIST, 'AdminGroup' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup', 
                [], [], 
                '''                configuration of value to name mapping
                for mpls affinities/admin-groups
                ''',
                'admin_group',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'mpls-admin-groups',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.TeLspTimers.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.TeLspTimers.Config',
            False, 
            [
            _MetaInfoClassMember('cleanup-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                delay the removal of old te lsp for a specified
                amount of time
                ''',
                'cleanup_delay',
                'openconfig-mpls', False),
            _MetaInfoClassMember('install-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                delay the use of newly installed te lsp for a
                specified amount of time.
                ''',
                'install_delay',
                'openconfig-mpls', False),
            _MetaInfoClassMember('reoptimize-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                frequency of reoptimization of
                a traffic engineered LSP
                ''',
                'reoptimize_timer',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.TeLspTimers.State' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.TeLspTimers.State',
            False, 
            [
            _MetaInfoClassMember('cleanup-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                delay the removal of old te lsp for a specified
                amount of time
                ''',
                'cleanup_delay',
                'openconfig-mpls', False),
            _MetaInfoClassMember('install-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                delay the use of newly installed te lsp for a
                specified amount of time.
                ''',
                'install_delay',
                'openconfig-mpls', False),
            _MetaInfoClassMember('reoptimize-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                frequency of reoptimization of
                a traffic engineered LSP
                ''',
                'reoptimize_timer',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes.TeLspTimers' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes.TeLspTimers',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.TeLspTimers.Config', 
                [], [], 
                '''                Configuration parameters related
                to timers for TE LSPs
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.TeLspTimers.State', 
                [], [], 
                '''                State related to timers for TE LSPs
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'te-lsp-timers',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeGlobalAttributes' : {
        'meta_info' : _MetaInfoClass('Mpls.TeGlobalAttributes',
            False, 
            [
            _MetaInfoClassMember('igp-flooding-bandwidth', REFERENCE_CLASS, 'IgpFloodingBandwidth' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.IgpFloodingBandwidth', 
                [], [], 
                '''                Interface bandwidth change percentages
                that trigger update events into the IGP traffic
                engineering database (TED)
                ''',
                'igp_flooding_bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('mpls-admin-groups', REFERENCE_CLASS, 'MplsAdminGroups' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.MplsAdminGroups', 
                [], [], 
                '''                Top-level container for admin-groups configuration
                and state
                ''',
                'mpls_admin_groups',
                'openconfig-mpls', False),
            _MetaInfoClassMember('srlg', REFERENCE_CLASS, 'Srlg' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.Srlg', 
                [], [], 
                '''                Shared risk link groups attributes
                ''',
                'srlg',
                'openconfig-mpls', False),
            _MetaInfoClassMember('te-lsp-timers', REFERENCE_CLASS, 'TeLspTimers' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes.TeLspTimers', 
                [], [], 
                '''                Definition for delays associated with setup
                and cleanup of TE LSPs
                ''',
                'te_lsp_timers',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'te-global-attributes',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeInterfaceAttributes.Interface.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.TeInterfaceAttributes.Interface.Config',
            False, 
            [
            _MetaInfoClassMember('admin-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of admin groups (by name) on the interface
                ''',
                'admin_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to interface name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('srlg-membership', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named shared risk link groups that the
                interface belongs to.
                ''',
                'srlg_membership',
                'openconfig-mpls', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE specific metric for the link
                ''',
                'te_metric',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeInterfaceAttributes.Interface.State' : {
        'meta_info' : _MetaInfoClass('Mpls.TeInterfaceAttributes.Interface.State',
            False, 
            [
            _MetaInfoClassMember('admin-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of admin groups (by name) on the interface
                ''',
                'admin_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to interface name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('srlg-membership', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named shared risk link groups that the
                interface belongs to.
                ''',
                'srlg_membership',
                'openconfig-mpls', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE specific metric for the link
                ''',
                'te_metric',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdSpecificationEnum' : _MetaInfoEnum('ThresholdSpecificationEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'MIRRORED-UP-DOWN':'MIRRORED_UP_DOWN',
            'SEPARATE-UP-DOWN':'SEPARATE_UP_DOWN',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdTypeEnum' : _MetaInfoEnum('ThresholdTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'DELTA':'DELTA',
            'THRESHOLD-CROSSED':'THRESHOLD_CROSSED',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config',
            False, 
            [
            _MetaInfoClassMember('delta-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The percentage of the maximum-reservable-bandwidth
                considered as the delta that results in an IGP update
                being flooded
                ''',
                'delta_percentage',
                'openconfig-mpls', False),
            _MetaInfoClassMember('down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is decreasing.
                ''',
                'down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-specification', REFERENCE_ENUM_CLASS, 'ThresholdSpecificationEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdSpecificationEnum', 
                [], [], 
                '''                This value specifies whether a single set of threshold
                values should be used for both increasing and decreasing
                bandwidth when determining whether to trigger updated
                bandwidth values to be flooded in the IGP TE extensions.
                MIRRORED-UP-DOWN indicates that a single value (or set of
                values) should be used for both increasing and decreasing
                values, where SEPARATE-UP-DOWN specifies that the increasing
                and decreasing values will be separately specified
                ''',
                'threshold_specification',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_ENUM_CLASS, 'ThresholdTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config.ThresholdTypeEnum', 
                [], [], 
                '''                The type of threshold that should be used to specify the
                values at which bandwidth is flooded. DELTA indicates that
                the local system should flood IGP updates when a change in
                reserved bandwidth >= the specified delta occurs on the
                interface. Where THRESHOLD-CROSSED is specified, the local
                system should trigger an update (and hence flood) the
                reserved bandwidth when the reserved bandwidth changes such
                that it crosses, or becomes equal to one of the threshold
                values
                ''',
                'threshold_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth of the interface) at which bandwidth
                updates are flooded - used both when the bandwidth is
                increasing and decreasing
                ''',
                'up_down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is increasing.
                ''',
                'up_thresholds',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdSpecificationEnum' : _MetaInfoEnum('ThresholdSpecificationEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'MIRRORED-UP-DOWN':'MIRRORED_UP_DOWN',
            'SEPARATE-UP-DOWN':'SEPARATE_UP_DOWN',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdTypeEnum' : _MetaInfoEnum('ThresholdTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'DELTA':'DELTA',
            'THRESHOLD-CROSSED':'THRESHOLD_CROSSED',
        }, 'openconfig-mpls', _yang_ns._namespaces['openconfig-mpls']),
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State' : {
        'meta_info' : _MetaInfoClass('Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State',
            False, 
            [
            _MetaInfoClassMember('delta-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The percentage of the maximum-reservable-bandwidth
                considered as the delta that results in an IGP update
                being flooded
                ''',
                'delta_percentage',
                'openconfig-mpls', False),
            _MetaInfoClassMember('down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is decreasing.
                ''',
                'down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-specification', REFERENCE_ENUM_CLASS, 'ThresholdSpecificationEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdSpecificationEnum', 
                [], [], 
                '''                This value specifies whether a single set of threshold
                values should be used for both increasing and decreasing
                bandwidth when determining whether to trigger updated
                bandwidth values to be flooded in the IGP TE extensions.
                MIRRORED-UP-DOWN indicates that a single value (or set of
                values) should be used for both increasing and decreasing
                values, where SEPARATE-UP-DOWN specifies that the increasing
                and decreasing values will be separately specified
                ''',
                'threshold_specification',
                'openconfig-mpls', False),
            _MetaInfoClassMember('threshold-type', REFERENCE_ENUM_CLASS, 'ThresholdTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State.ThresholdTypeEnum', 
                [], [], 
                '''                The type of threshold that should be used to specify the
                values at which bandwidth is flooded. DELTA indicates that
                the local system should flood IGP updates when a change in
                reserved bandwidth >= the specified delta occurs on the
                interface. Where THRESHOLD-CROSSED is specified, the local
                system should trigger an update (and hence flood) the
                reserved bandwidth when the reserved bandwidth changes such
                that it crosses, or becomes equal to one of the threshold
                values
                ''',
                'threshold_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-down-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth of the interface) at which bandwidth
                updates are flooded - used both when the bandwidth is
                increasing and decreasing
                ''',
                'up_down_thresholds',
                'openconfig-mpls', False),
            _MetaInfoClassMember('up-thresholds', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The thresholds (expressed as a percentage of the maximum
                reservable bandwidth) at which bandwidth updates are to be
                triggered when the bandwidth is increasing.
                ''',
                'up_thresholds',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth' : {
        'meta_info' : _MetaInfoClass('Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config', 
                [], [], 
                '''                Configuration parameters for TED
                update threshold 
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State', 
                [], [], 
                '''                State parameters for TED update threshold 
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'igp-flooding-bandwidth',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeInterfaceAttributes.Interface' : {
        'meta_info' : _MetaInfoClass('Mpls.TeInterfaceAttributes.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The interface name
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.Config', 
                [], [], 
                '''                Configuration parameters related to TE interfaces:
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('igp-flooding-bandwidth', REFERENCE_CLASS, 'IgpFloodingBandwidth' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth', 
                [], [], 
                '''                Interface bandwidth change percentages
                that trigger update events into the IGP traffic
                engineering database (TED)
                ''',
                'igp_flooding_bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface.State', 
                [], [], 
                '''                State parameters related to TE interfaces
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'interface',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.TeInterfaceAttributes' : {
        'meta_info' : _MetaInfoClass('Mpls.TeInterfaceAttributes',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes.Interface', 
                [], [], 
                '''                List of TE interfaces
                ''',
                'interface',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'te-interface-attributes',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Sessions.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Sessions.Config',
            False, 
            [
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'UP':'UP',
            'DOWN':'DOWN',
        }, 'openconfig-mpls-rsvp', _yang_ns._namespaces['openconfig-mpls-rsvp']),
    'Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.TypeEnum' : _MetaInfoEnum('TypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'SOURCE':'SOURCE',
            'TRANSIT':'TRANSIT',
            'DESTINATION':'DESTINATION',
        }, 'openconfig-mpls-rsvp', _yang_ns._namespaces['openconfig-mpls-rsvp']),
    'Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session',
            False, 
            [
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                RSVP source port
                ''',
                'source_port',
                'openconfig-mpls', True),
            _MetaInfoClassMember('destination-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                RSVP source port
                ''',
                'destination_port',
                'openconfig-mpls', True),
            _MetaInfoClassMember('source-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Origin address of RSVP session
                ''',
                'source_address',
                'openconfig-mpls', True, [
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Origin address of RSVP session
                        ''',
                        'source_address',
                        'openconfig-mpls', True),
                    _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Origin address of RSVP session
                        ''',
                        'source_address',
                        'openconfig-mpls', True),
                ]),
            _MetaInfoClassMember('destination-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination address of RSVP session
                ''',
                'destination_address',
                'openconfig-mpls', True, [
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address of RSVP session
                        ''',
                        'destination_address',
                        'openconfig-mpls', True),
                    _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Destination address of RSVP session
                        ''',
                        'destination_address',
                        'openconfig-mpls', True),
                ]),
            _MetaInfoClassMember('associated-lsps', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of label switched paths associated with this RSVP
                session
                ''',
                'associated_lsps',
                'openconfig-mpls', False),
            _MetaInfoClassMember('label-in', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Incoming MPLS label associated with this RSVP session
                ''',
                'label_in',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('label-in', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        Incoming MPLS label associated with this RSVP session
                        ''',
                        'label_in',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('label-in', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        Incoming MPLS label associated with this RSVP session
                        ''',
                        'label_in',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('label-out', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Outgoing MPLS label associated with this RSVP session
                ''',
                'label_out',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('label-out', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        Outgoing MPLS label associated with this RSVP session
                        ''',
                        'label_out',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('label-out', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        Outgoing MPLS label associated with this RSVP session
                        ''',
                        'label_out',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.StatusEnum', 
                [], [], 
                '''                Enumeration of RSVP session states
                ''',
                'status',
                'openconfig-mpls', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Unique identifier of RSVP session
                ''',
                'tunnel_id',
                'openconfig-mpls', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session.TypeEnum', 
                [], [], 
                '''                Enumeration of possible RSVP session types
                ''',
                'type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'session',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Sessions.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Sessions.State',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session', 
                [], [], 
                '''                List of RSVP sessions
                ''',
                'session',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Sessions' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Sessions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Sessions.Config', 
                [], [], 
                '''                Configuration of RSVP sessions on the device
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Sessions.State', 
                [], [], 
                '''                State information relating to RSVP sessions
                on the device
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'sessions',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Neighbors.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Neighbors.Config',
            False, 
            [
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor.NeighborStatusEnum' : _MetaInfoEnum('NeighborStatusEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'UP':'UP',
            'DOWN':'DOWN',
        }, 'openconfig-mpls-rsvp', _yang_ns._namespaces['openconfig-mpls-rsvp']),
    'Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of RSVP neighbor
                ''',
                'address',
                'openconfig-mpls', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of RSVP neighbor
                        ''',
                        'address',
                        'openconfig-mpls', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of RSVP neighbor
                        ''',
                        'address',
                        'openconfig-mpls', True),
                ]),
            _MetaInfoClassMember('detected-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface where RSVP neighbor was detected
                ''',
                'detected_interface',
                'openconfig-mpls', False),
            _MetaInfoClassMember('neighbor-status', REFERENCE_ENUM_CLASS, 'NeighborStatusEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor.NeighborStatusEnum', 
                [], [], 
                '''                Enumuration of possible RSVP neighbor states
                ''',
                'neighbor_status',
                'openconfig-mpls', False),
            _MetaInfoClassMember('refresh-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppport of neighbor for RSVP refresh reduction
                ''',
                'refresh_reduction',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'neighbor',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Neighbors.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Neighbors.State',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor', 
                [], [], 
                '''                List of RSVP neighbors connecting to the device,
                keyed by neighbor address
                ''',
                'neighbor',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Neighbors' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Neighbors',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Neighbors.Config', 
                [], [], 
                '''                Configuration of RSVP neighbor information
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Neighbors.State', 
                [], [], 
                '''                State information relating to RSVP neighbors
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'neighbors',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables graceful restart on the node.
                ''',
                'enable',
                'openconfig-mpls', False),
            _MetaInfoClassMember('recovery-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RSVP state recovery time
                ''',
                'recovery_time',
                'openconfig-mpls', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Graceful restart time (seconds).
                ''',
                'restart_time',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables graceful restart on the node.
                ''',
                'enable',
                'openconfig-mpls', False),
            _MetaInfoClassMember('recovery-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RSVP state recovery time
                ''',
                'recovery_time',
                'openconfig-mpls', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Graceful restart time (seconds).
                ''',
                'restart_time',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config', 
                [], [], 
                '''                Configuration parameters relating to
                graceful-restart
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State', 
                [], [], 
                '''                State information associated with
                RSVP graceful-restart
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'graceful-restart',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables soft preemption on a node.
                ''',
                'enable',
                'openconfig-mpls', False),
            _MetaInfoClassMember('soft-preemption-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Timeout value for soft preemption to revert
                to hard preemption
                ''',
                'soft_preemption_timeout',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables soft preemption on a node.
                ''',
                'enable',
                'openconfig-mpls', False),
            _MetaInfoClassMember('soft-preemption-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Timeout value for soft preemption to revert
                to hard preemption
                ''',
                'soft_preemption_timeout',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config', 
                [], [], 
                '''                Configuration parameters relating to RSVP
                soft preemption support
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State', 
                [], [], 
                '''                State parameters relating to RSVP
                soft preemption support
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'soft-preemption',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config',
            False, 
            [
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '60000')], [], 
                '''                set the interval in ms between RSVP hello
                messages
                ''',
                'hello_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('refresh-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables all RSVP refresh reduction message
                bundling, RSVP message ID, reliable message delivery
                and summary refresh
                ''',
                'refresh_reduction',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State',
            False, 
            [
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '60000')], [], 
                '''                set the interval in ms between RSVP hello
                messages
                ''',
                'hello_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('refresh-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables all RSVP refresh reduction message
                bundling, RSVP message ID, reliable message delivery
                and summary refresh
                ''',
                'refresh_reduction',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.Hellos',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config', 
                [], [], 
                '''                Configuration parameters relating to RSVP
                hellos
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State', 
                [], [], 
                '''                State information associated with RSVP hellos
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'hellos',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters',
            False, 
            [
            _MetaInfoClassMember('in-ack-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP refresh reduction ack
                messages
                ''',
                'in_ack_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-hello-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP hello messages
                ''',
                'in_hello_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-path-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Path Error messages
                ''',
                'in_path_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-path-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Path messages
                ''',
                'in_path_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-path-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Path Tear messages
                ''',
                'in_path_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-reservation-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Resv Error messages
                ''',
                'in_reservation_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-reservation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Resv messages
                ''',
                'in_reservation_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-reservation-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Resv Tear messages
                ''',
                'in_reservation_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-srefresh-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP summary refresh messages
                ''',
                'in_srefresh_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-ack-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP refresh reduction ack messages
                ''',
                'out_ack_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-hello-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP hello messages
                ''',
                'out_hello_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-path-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Path Error messages
                ''',
                'out_path_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-path-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP PATH messages
                ''',
                'out_path_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-path-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Path Tear messages
                ''',
                'out_path_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-reservation-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Resv Error messages
                ''',
                'out_reservation_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-reservation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Resv messages
                ''',
                'out_reservation_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-reservation-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Resv Tear messages
                ''',
                'out_reservation_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-srefresh-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP summary refresh messages
                ''',
                'out_srefresh_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TODO
                ''',
                'path_timeouts',
                'openconfig-mpls', False),
            _MetaInfoClassMember('rate-limited-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                RSVP messages dropped due to rate limiting
                ''',
                'rate_limited_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('reservation-timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                TODO
                ''',
                'reservation_timeouts',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'counters',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_.State',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters', 
                [], [], 
                '''                Platform wide RSVP statistics and counters
                ''',
                'counters',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.Global_' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.Global_',
            False, 
            [
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart', 
                [], [], 
                '''                Operational state and configuration parameters relating to
                graceful-restart for RSVP
                ''',
                'graceful_restart',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hellos', REFERENCE_CLASS, 'Hellos' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.Hellos', 
                [], [], 
                '''                Top level container for RSVP hello parameters
                ''',
                'hellos',
                'openconfig-mpls', False),
            _MetaInfoClassMember('soft-preemption', REFERENCE_CLASS, 'SoftPreemption' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption', 
                [], [], 
                '''                Protocol options relating to RSVP
                soft preemption
                ''',
                'soft_preemption',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_.State', 
                [], [], 
                '''                Platform wide RSVP state, including counters
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'global',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of configured IP interface
                ''',
                'interface_name',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                RSVP priority level for LSPs traversing the interface
                ''',
                'priority',
                'openconfig-mpls', True),
            _MetaInfoClassMember('available-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bandwidth currently available
                ''',
                'available_bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('reserved-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bandwidth currently reserved
                ''',
                'reserved_bandwidth',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'bandwidth',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters',
            False, 
            [
            _MetaInfoClassMember('in-ack-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP refresh reduction ack
                messages
                ''',
                'in_ack_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-hello-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP hello messages
                ''',
                'in_hello_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-path-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Path Error messages
                ''',
                'in_path_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-path-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Path messages
                ''',
                'in_path_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-path-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Path Tear messages
                ''',
                'in_path_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-reservation-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Resv Error messages
                ''',
                'in_reservation_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-reservation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Resv messages
                ''',
                'in_reservation_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-reservation-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP Resv Tear messages
                ''',
                'in_reservation_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('in-srefresh-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of received RSVP summary refresh messages
                ''',
                'in_srefresh_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-ack-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP refresh reduction ack messages
                ''',
                'out_ack_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-hello-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP hello messages
                ''',
                'out_hello_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-path-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Path Error messages
                ''',
                'out_path_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-path-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP PATH messages
                ''',
                'out_path_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-path-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Path Tear messages
                ''',
                'out_path_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-reservation-error-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Resv Error messages
                ''',
                'out_reservation_error_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-reservation-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Resv messages
                ''',
                'out_reservation_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-reservation-tear-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP Resv Tear messages
                ''',
                'out_reservation_tear_messages',
                'openconfig-mpls', False),
            _MetaInfoClassMember('out-srefresh-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of sent RSVP summary refresh messages
                ''',
                'out_srefresh_messages',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'counters',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State',
            False, 
            [
            _MetaInfoClassMember('active-reservation-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of active RSVP reservations
                ''',
                'active_reservation_count',
                'openconfig-mpls', False),
            _MetaInfoClassMember('bandwidth', REFERENCE_LIST, 'Bandwidth' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth', 
                [], [], 
                '''                Available and reserved bandwidth by priority on
                the interface.
                ''',
                'bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters', 
                [], [], 
                '''                Interface specific RSVP statistics and counters
                ''',
                'counters',
                'openconfig-mpls', False),
            _MetaInfoClassMember('highwater-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum bandwidth ever reserved
                ''',
                'highwater_mark',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config',
            False, 
            [
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '60000')], [], 
                '''                set the interval in ms between RSVP hello
                messages
                ''',
                'hello_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('refresh-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables all RSVP refresh reduction message
                bundling, RSVP message ID, reliable message delivery
                and summary refresh
                ''',
                'refresh_reduction',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State',
            False, 
            [
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1000', '60000')], [], 
                '''                set the interval in ms between RSVP hello
                messages
                ''',
                'hello_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('refresh-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables all RSVP refresh reduction message
                bundling, RSVP message ID, reliable message delivery
                and summary refresh
                ''',
                'refresh_reduction',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config', 
                [], [], 
                '''                Configuration parameters relating to RSVP
                hellos
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State', 
                [], [], 
                '''                State information associated with RSVP hellos
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'hellos',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config',
            False, 
            [
            _MetaInfoClassMember('authentication-key', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                authenticate RSVP signaling
                messages
                ''',
                'authentication_key',
                'openconfig-mpls', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables RSVP authentication on the node.
                ''',
                'enable',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State',
            False, 
            [
            _MetaInfoClassMember('authentication-key', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                authenticate RSVP signaling
                messages
                ''',
                'authentication_key',
                'openconfig-mpls', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables RSVP authentication on the node.
                ''',
                'enable',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config', 
                [], [], 
                '''                Configuration parameters relating
                to authentication
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State', 
                [], [], 
                '''                State information associated
                with authentication
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'authentication',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config',
            False, 
            [
            _MetaInfoClassMember('subscription', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                percentage of the interface bandwidth that
                RSVP can reserve
                ''',
                'subscription',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State',
            False, 
            [
            _MetaInfoClassMember('subscription', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                percentage of the interface bandwidth that
                RSVP can reserve
                ''',
                'subscription',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config', 
                [], [], 
                '''                Configuration parameters relating to RSVP
                subscription options
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State', 
                [], [], 
                '''                State parameters relating to RSVP
                subscription options
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'subscription',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config',
            False, 
            [
            _MetaInfoClassMember('bypass-optimize-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                interval between periodic optimization
                of the bypass LSPs
                ''',
                'bypass_optimize_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('link-protection-style-requested', REFERENCE_IDENTITY_CLASS, 'ProtectionTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'ProtectionTypeIdentity', 
                [], [], 
                '''                Style of mpls frr protection desired:
                link, link-node, or unprotected
                ''',
                'link_protection_style_requested',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State',
            False, 
            [
            _MetaInfoClassMember('bypass-optimize-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                interval between periodic optimization
                of the bypass LSPs
                ''',
                'bypass_optimize_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('link-protection-style-requested', REFERENCE_IDENTITY_CLASS, 'ProtectionTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'ProtectionTypeIdentity', 
                [], [], 
                '''                Style of mpls frr protection desired:
                link, link-node, or unprotected
                ''',
                'link_protection_style_requested',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config', 
                [], [], 
                '''                Configuration for link-protection
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State', 
                [], [], 
                '''                State for link-protection
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'protection',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                references a configured IP interface
                ''',
                'interface_name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication', 
                [], [], 
                '''                Configuration and state parameters relating to RSVP
                authentication as per RFC2747
                ''',
                'authentication',
                'openconfig-mpls', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config', 
                [], [], 
                '''                Configuration of per-interface RSVP parameters
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hellos', REFERENCE_CLASS, 'Hellos' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos', 
                [], [], 
                '''                Top level container for RSVP hello parameters
                ''',
                'hellos',
                'openconfig-mpls', False),
            _MetaInfoClassMember('protection', REFERENCE_CLASS, 'Protection' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection', 
                [], [], 
                '''                link-protection (NHOP) related configuration
                ''',
                'protection',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State', 
                [], [], 
                '''                Per-interface RSVP protocol and state information
                ''',
                'state',
                'openconfig-mpls', False),
            _MetaInfoClassMember('subscription', REFERENCE_CLASS, 'Subscription' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription', 
                [], [], 
                '''                Bandwidth percentage reservable by RSVP
                on an interface
                ''',
                'subscription',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'interface',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface', 
                [], [], 
                '''                list of per-interface RSVP configurations
                ''',
                'interface',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'interface-attributes',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.RsvpTe' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.RsvpTe',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Global_', 
                [], [], 
                '''                Platform wide RSVP configuration and state
                ''',
                'global_',
                'openconfig-mpls', False),
            _MetaInfoClassMember('interface-attributes', REFERENCE_CLASS, 'InterfaceAttributes' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes', 
                [], [], 
                '''                Attributes relating to RSVP-TE enabled interfaces
                ''',
                'interface_attributes',
                'openconfig-mpls', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Neighbors', 
                [], [], 
                '''                Configuration and state for RSVP neighbors connecting
                to the device
                ''',
                'neighbors',
                'openconfig-mpls', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe.Sessions', 
                [], [], 
                '''                Configuration and state of RSVP sessions
                ''',
                'sessions',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'rsvp-te',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Srgb.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Srgb.Config',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower value in the block.
                ''',
                'lower_bound',
                'openconfig-mpls', False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Upper value in the block.
                ''',
                'upper_bound',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Srgb.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Srgb.State',
            False, 
            [
            _MetaInfoClassMember('free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of SRGB indexes that have not yet been allocated
                ''',
                'free',
                'openconfig-mpls', False),
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower value in the block.
                ''',
                'lower_bound',
                'openconfig-mpls', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of indexes in the SRGB block
                ''',
                'size',
                'openconfig-mpls', False),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Upper value in the block.
                ''',
                'upper_bound',
                'openconfig-mpls', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of SRGB indexes that are currently allocated
                ''',
                'used',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Srgb' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Srgb',
            False, 
            [
            _MetaInfoClassMember('lower-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lower value in the block.
                ''',
                'lower_bound',
                'openconfig-mpls', True),
            _MetaInfoClassMember('upper-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Upper value in the block.
                ''',
                'upper_bound',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Srgb.Config', 
                [], [], 
                '''                Configuration parameters relating to the Segment Routing
                Global Block (SRGB)
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Srgb.State', 
                [], [], 
                '''                State parameters relating to the Segment Routing Global
                Block (SRGB)
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'srgb',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the interface for which segment routing
                configuration is to be applied.
                ''',
                'interface',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Interfaces.State',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the interface for which segment routing
                configuration is to be applied.
                ''',
                'interface',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config.AdvertiseEnum' : _MetaInfoEnum('AdvertiseEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'PROTECTED':'PROTECTED',
            'UNPROTECTED':'UNPROTECTED',
        }, 'openconfig-mpls-sr', _yang_ns._namespaces['openconfig-mpls-sr']),
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config',
            False, 
            [
            _MetaInfoClassMember('advertise', REFERENCE_LEAFLIST, 'AdvertiseEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config.AdvertiseEnum', 
                [], [], 
                '''                Specifies the type of adjacency SID which should be
                advertised for the specified entity.
                ''',
                'advertise',
                'openconfig-mpls', False),
            _MetaInfoClassMember('groups', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the groups to which this interface belongs.
                Setting a value in this list results in an additional AdjSID
                being advertised, with the S-bit set to 1. The AdjSID is
                assumed to be protected
                ''',
                'groups',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State.AdvertiseEnum' : _MetaInfoEnum('AdvertiseEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'PROTECTED':'PROTECTED',
            'UNPROTECTED':'UNPROTECTED',
        }, 'openconfig-mpls-sr', _yang_ns._namespaces['openconfig-mpls-sr']),
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State',
            False, 
            [
            _MetaInfoClassMember('advertise', REFERENCE_LEAFLIST, 'AdvertiseEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State.AdvertiseEnum', 
                [], [], 
                '''                Specifies the type of adjacency SID which should be
                advertised for the specified entity.
                ''',
                'advertise',
                'openconfig-mpls', False),
            _MetaInfoClassMember('groups', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the groups to which this interface belongs.
                Setting a value in this list results in an additional AdjSID
                being advertised, with the S-bit set to 1. The AdjSID is
                assumed to be protected
                ''',
                'groups',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config', 
                [], [], 
                '''                Configuration parameters for the Adjacency-SIDs
                that are related to this interface
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State', 
                [], [], 
                '''                State parameters for the Adjacency-SIDs that are
                related to this interface
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'adjacency-sid',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the interface for which segment routing
                configuration is to be applied.
                ''',
                'interface',
                'openconfig-mpls', True),
            _MetaInfoClassMember('adjacency-sid', REFERENCE_CLASS, 'AdjacencySid' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid', 
                [], [], 
                '''                Configuration for Adjacency SIDs that are related to
                the specified interface
                ''',
                'adjacency_sid',
                'openconfig-mpls', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config', 
                [], [], 
                '''                Interface configuration parameters for Segment Routing
                relating to the specified interface
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces.State', 
                [], [], 
                '''                State parameters for Segment Routing features relating
                to the specified interface
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'interfaces',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.SegmentRouting',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_LIST, 'Interfaces' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Interfaces', 
                [], [], 
                '''                List of interfaces with associated segment routing
                configuration
                ''',
                'interfaces',
                'openconfig-mpls', False),
            _MetaInfoClassMember('srgb', REFERENCE_LIST, 'Srgb' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting.Srgb', 
                [], [], 
                '''                List of Segment Routing Global Block (SRGB) entries. These
                label blocks are reserved to be allocated as domain-wide
                entries.
                ''',
                'srgb',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'segment-routing',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.Ldp.Timers' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.Ldp.Timers',
            False, 
            [
            ],
            'openconfig-mpls',
            'timers',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols.Ldp' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols.Ldp',
            False, 
            [
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.Ldp.Timers', 
                [], [], 
                '''                LDP timers
                ''',
                'timers',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'ldp',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.SignalingProtocols' : {
        'meta_info' : _MetaInfoClass('Mpls.SignalingProtocols',
            False, 
            [
            _MetaInfoClassMember('ldp', REFERENCE_CLASS, 'Ldp' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.Ldp', 
                [], [], 
                '''                LDP global signaling configuration
                ''',
                'ldp',
                'openconfig-mpls', False),
            _MetaInfoClassMember('rsvp-te', REFERENCE_CLASS, 'RsvpTe' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.RsvpTe', 
                [], [], 
                '''                RSVP-TE global signaling protocol configuration
                ''',
                'rsvp_te',
                'openconfig-mpls', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols.SegmentRouting', 
                [], [], 
                '''                SR global signaling config
                ''',
                'segment_routing',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'signaling-protocols',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A string name that uniquely identifies an explicit
                path
                ''',
                'name',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A string name that uniquely identifies an explicit
                path
                ''',
                'name',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                router hop for the LSP path
                ''',
                'address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        router hop for the LSP path
                        ''',
                        'address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        router hop for the LSP path
                        ''',
                        'address',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'MplsHopTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'MplsHopTypeEnum', 
                [], [], 
                '''                strict or loose hop
                ''',
                'hop_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Index of this explicit route object to express
                the order of hops in the path
                ''',
                'index',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                router hop for the LSP path
                ''',
                'address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        router hop for the LSP path
                        ''',
                        'address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        router hop for the LSP path
                        ''',
                        'address',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('hop-type', REFERENCE_ENUM_CLASS, 'MplsHopTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'MplsHopTypeEnum', 
                [], [], 
                '''                strict or loose hop
                ''',
                'hop_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Index of this explicit route object to express
                the order of hops in the path
                ''',
                'index',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Index of this explicit route object,
                to express the order of hops in path
                ''',
                'index',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config', 
                [], [], 
                '''                Configuration parameters relating to an explicit
                route
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State', 
                [], [], 
                '''                State parameters relating to an explicit route
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'explicit-route-objects',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.NamedExplicitPaths',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A string name that uniquely identifies
                an explicit path
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config', 
                [], [], 
                '''                Configuration parameters relating to named explicit
                paths
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('explicit-route-objects', REFERENCE_LIST, 'ExplicitRouteObjects' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects', 
                [], [], 
                '''                List of explicit route objects
                ''',
                'explicit_route_objects',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State', 
                [], [], 
                '''                Operational state parameters relating to the named
                explicit paths
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'named-explicit-paths',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Config',
            False, 
            [
            _MetaInfoClassMember('admin-status', REFERENCE_IDENTITY_CLASS, 'TunnelAdminStatusIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelAdminStatusIdentity', 
                [], [], 
                '''                TE tunnel administrative state.
                ''',
                'admin_status',
                'openconfig-mpls', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                optional text description for the tunnel
                ''',
                'description',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                preemption priority once the LSP is established,
                lower is higher priority; default 0 indicates other LSPs
                will not preempt the LSPs once established
                ''',
                'hold_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('local-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                locally signficant optional identifier for the
                tunnel; may be a numerical or string value
                ''',
                'local_id',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('local-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        locally signficant optional identifier for the
                        tunnel; may be a numerical or string value
                        ''',
                        'local_id',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('local-id', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        locally signficant optional identifier for the
                        tunnel; may be a numerical or string value
                        ''',
                        'local_id',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSP metric, either explicit or IGP
                ''',
                'metric',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'TeMetricTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'TeMetricTypeEnum', 
                        [], [], 
                        '''                        LSP metric, either explicit or IGP
                        ''',
                        'metric',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        LSP metric, either explicit or IGP
                        ''',
                        'metric',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The tunnel name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specifies a preference for this tunnel.
                A lower number signifies a better preference
                ''',
                'preference',
                'openconfig-mpls', False),
            _MetaInfoClassMember('protection-style-requested', REFERENCE_IDENTITY_CLASS, 'ProtectionTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'ProtectionTypeIdentity', 
                [], [], 
                '''                style of mpls frr protection desired: can be
                link, link-node or unprotected.
                ''',
                'protection_style_requested',
                'openconfig-mpls', False),
            _MetaInfoClassMember('reoptimize-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                frequency of reoptimization of
                a traffic engineered LSP
                ''',
                'reoptimize_timer',
                'openconfig-mpls', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                RSVP-TE preemption priority during LSP setup, lower is
                higher priority; default 7 indicates that LSP will not
                preempt established LSPs during setup
                ''',
                'setup_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('signaling-protocol', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelTypeIdentity', 
                [], [], 
                '''                Signaling protocol used to set up this tunnel
                ''',
                'signaling_protocol',
                'openconfig-mpls', False),
            _MetaInfoClassMember('soft-preemption', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables RSVP soft-preemption on this LSP
                ''',
                'soft_preemption',
                'openconfig-mpls', False),
            _MetaInfoClassMember('source', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RSVP-TE tunnel source address
                ''',
                'source',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RSVP-TE tunnel source address
                        ''',
                        'source',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RSVP-TE tunnel source address
                        ''',
                        'source',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelTypeIdentity', 
                [], [], 
                '''                Tunnel type, p2p or p2mp
                ''',
                'type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes that have been forwarded over the
                label switched path.
                ''',
                'bytes',
                'openconfig-mpls', False),
            _MetaInfoClassMember('current-path-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Indicates the time the LSP switched onto its
                current path. This is reset upon a LSP path
                change.
                ''',
                'current_path_time',
                'openconfig-mpls', False),
            _MetaInfoClassMember('next-reoptimization-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Indicates the next scheduled time the LSP
                will be reoptimized.
                ''',
                'next_reoptimization_time',
                'openconfig-mpls', False),
            _MetaInfoClassMember('online-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Indication of the time the label switched path
                transitioned to an Oper Up or in-service state
                ''',
                'online_time',
                'openconfig-mpls', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of pacets that have been forwarded over the
                label switched path.
                ''',
                'packets',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of path changes for the label switched path
                ''',
                'path_changes',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of state changes for the label switched path
                ''',
                'state_changes',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'counters',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.State',
            False, 
            [
            _MetaInfoClassMember('admin-status', REFERENCE_IDENTITY_CLASS, 'TunnelAdminStatusIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelAdminStatusIdentity', 
                [], [], 
                '''                TE tunnel administrative state.
                ''',
                'admin_status',
                'openconfig-mpls', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters', 
                [], [], 
                '''                State data for MPLS label switched paths. This state
                data is specific to a single label switched path.
                ''',
                'counters',
                'openconfig-mpls', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                optional text description for the tunnel
                ''',
                'description',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                preemption priority once the LSP is established,
                lower is higher priority; default 0 indicates other LSPs
                will not preempt the LSPs once established
                ''',
                'hold_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('local-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                locally signficant optional identifier for the
                tunnel; may be a numerical or string value
                ''',
                'local_id',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('local-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        locally signficant optional identifier for the
                        tunnel; may be a numerical or string value
                        ''',
                        'local_id',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('local-id', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        locally signficant optional identifier for the
                        tunnel; may be a numerical or string value
                        ''',
                        'local_id',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('metric', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSP metric, either explicit or IGP
                ''',
                'metric',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('metric', REFERENCE_ENUM_CLASS, 'TeMetricTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'TeMetricTypeEnum', 
                        [], [], 
                        '''                        LSP metric, either explicit or IGP
                        ''',
                        'metric',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        LSP metric, either explicit or IGP
                        ''',
                        'metric',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The tunnel name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('oper-status', REFERENCE_IDENTITY_CLASS, 'LspOperStatusIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'LspOperStatusIdentity', 
                [], [], 
                '''                The operational status of the TE tunnel
                ''',
                'oper_status',
                'openconfig-mpls', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specifies a preference for this tunnel.
                A lower number signifies a better preference
                ''',
                'preference',
                'openconfig-mpls', False),
            _MetaInfoClassMember('protection-style-requested', REFERENCE_IDENTITY_CLASS, 'ProtectionTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'ProtectionTypeIdentity', 
                [], [], 
                '''                style of mpls frr protection desired: can be
                link, link-node or unprotected.
                ''',
                'protection_style_requested',
                'openconfig-mpls', False),
            _MetaInfoClassMember('reoptimize-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                frequency of reoptimization of
                a traffic engineered LSP
                ''',
                'reoptimize_timer',
                'openconfig-mpls', False),
            _MetaInfoClassMember('role', REFERENCE_IDENTITY_CLASS, 'LspRoleIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'LspRoleIdentity', 
                [], [], 
                '''                The lsp role at the current node, whether it is headend,
                transit or tailend.
                ''',
                'role',
                'openconfig-mpls', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                RSVP-TE preemption priority during LSP setup, lower is
                higher priority; default 7 indicates that LSP will not
                preempt established LSPs during setup
                ''',
                'setup_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('signaling-protocol', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelTypeIdentity', 
                [], [], 
                '''                Signaling protocol used to set up this tunnel
                ''',
                'signaling_protocol',
                'openconfig-mpls', False),
            _MetaInfoClassMember('soft-preemption', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables RSVP soft-preemption on this LSP
                ''',
                'soft_preemption',
                'openconfig-mpls', False),
            _MetaInfoClassMember('source', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                RSVP-TE tunnel source address
                ''',
                'source',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RSVP-TE tunnel source address
                        ''',
                        'source',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('source', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        RSVP-TE tunnel source address
                        ''',
                        'source',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelTypeIdentity', 
                [], [], 
                '''                Tunnel type, p2p or p2mp
                ''',
                'type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config',
            False, 
            [
            _MetaInfoClassMember('set-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                set bandwidth explicitly, e.g., using
                offline calculation
                ''',
                'set_bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('specification-type', REFERENCE_ENUM_CLASS, 'TeBandwidthTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'TeBandwidthTypeEnum', 
                [], [], 
                '''                The method used for settign the bandwidth, either explicitly
                specified or configured
                ''',
                'specification_type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State',
            False, 
            [
            _MetaInfoClassMember('set-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                set bandwidth explicitly, e.g., using
                offline calculation
                ''',
                'set_bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('specification-type', REFERENCE_ENUM_CLASS, 'TeBandwidthTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'TeBandwidthTypeEnum', 
                [], [], 
                '''                The method used for settign the bandwidth, either explicitly
                specified or configured
                ''',
                'specification_type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config',
            False, 
            [
            _MetaInfoClassMember('adjust-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                time in seconds between adjustments to
                LSP bandwidth
                ''',
                'adjust_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('adjust-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                percentage difference between the LSP's
                specified bandwidth and its current bandwidth
                allocation -- if the difference is greater than the
                specified percentage, auto-bandwidth adjustment is
                triggered
                ''',
                'adjust_threshold',
                'openconfig-mpls', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables mpls auto-bandwidth on the
                lsp
                ''',
                'enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('max-bw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                set the maximum bandwidth in Mbps for an
                auto-bandwidth LSP
                ''',
                'max_bw',
                'openconfig-mpls', False),
            _MetaInfoClassMember('min-bw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                set the minimum bandwidth in Mbps for an
                auto-bandwidth LSP
                ''',
                'min_bw',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State',
            False, 
            [
            _MetaInfoClassMember('adjust-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                time in seconds between adjustments to
                LSP bandwidth
                ''',
                'adjust_interval',
                'openconfig-mpls', False),
            _MetaInfoClassMember('adjust-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                percentage difference between the LSP's
                specified bandwidth and its current bandwidth
                allocation -- if the difference is greater than the
                specified percentage, auto-bandwidth adjustment is
                triggered
                ''',
                'adjust_threshold',
                'openconfig-mpls', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables mpls auto-bandwidth on the
                lsp
                ''',
                'enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('max-bw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                set the maximum bandwidth in Mbps for an
                auto-bandwidth LSP
                ''',
                'max_bw',
                'openconfig-mpls', False),
            _MetaInfoClassMember('min-bw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                set the minimum bandwidth in Mbps for an
                auto-bandwidth LSP
                ''',
                'min_bw',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables mpls lsp bandwidth overflow
                adjustment on the lsp
                ''',
                'enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('overflow-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                bandwidth percentage change to trigger
                an overflow event
                ''',
                'overflow_threshold',
                'openconfig-mpls', False),
            _MetaInfoClassMember('trigger-event-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                number of consecutive overflow sample
                events needed to trigger an overflow adjustment
                ''',
                'trigger_event_count',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables mpls lsp bandwidth overflow
                adjustment on the lsp
                ''',
                'enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('overflow-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                bandwidth percentage change to trigger
                an overflow event
                ''',
                'overflow_threshold',
                'openconfig-mpls', False),
            _MetaInfoClassMember('trigger-event-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                number of consecutive overflow sample
                events needed to trigger an overflow adjustment
                ''',
                'trigger_event_count',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config', 
                [], [], 
                '''                Config information for MPLS overflow bandwidth
                adjustment
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State', 
                [], [], 
                '''                Config information for MPLS overflow bandwidth
                adjustment
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'overflow',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables bandwidth underflow
                adjustment on the lsp
                ''',
                'enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('trigger-event-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                number of consecutive underflow sample
                events needed to trigger an underflow adjustment
                ''',
                'trigger_event_count',
                'openconfig-mpls', False),
            _MetaInfoClassMember('underflow-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                bandwidth percentage change to trigger
                and underflow event
                ''',
                'underflow_threshold',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enables bandwidth underflow
                adjustment on the lsp
                ''',
                'enabled',
                'openconfig-mpls', False),
            _MetaInfoClassMember('trigger-event-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                number of consecutive underflow sample
                events needed to trigger an underflow adjustment
                ''',
                'trigger_event_count',
                'openconfig-mpls', False),
            _MetaInfoClassMember('underflow-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                bandwidth percentage change to trigger
                and underflow event
                ''',
                'underflow_threshold',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config', 
                [], [], 
                '''                Config information for MPLS underflow bandwidth
                          adjustment
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State', 
                [], [], 
                '''                State information for MPLS underflow bandwidth
                          adjustment
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'underflow',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config', 
                [], [], 
                '''                Configuration parameters relating to MPLS
                auto-bandwidth on the tunnel.
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('overflow', REFERENCE_CLASS, 'Overflow' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow', 
                [], [], 
                '''                configuration of MPLS overflow bandwidth
                adjustement for the LSP
                ''',
                'overflow',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State', 
                [], [], 
                '''                State parameters relating to MPLS
                auto-bandwidth on the tunnel.
                ''',
                'state',
                'openconfig-mpls', False),
            _MetaInfoClassMember('underflow', REFERENCE_CLASS, 'Underflow' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow', 
                [], [], 
                '''                configuration of MPLS underflow bandwidth
                          adjustement for the LSP
                ''',
                'underflow',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'auto-bandwidth',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth',
            False, 
            [
            _MetaInfoClassMember('auto-bandwidth', REFERENCE_CLASS, 'AutoBandwidth' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth', 
                [], [], 
                '''                Parameters related to auto-bandwidth
                ''',
                'auto_bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config', 
                [], [], 
                '''                Configuration parameters related to bandwidth on TE
                tunnels:
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State', 
                [], [], 
                '''                State parameters related to bandwidth
                configuration of TE tunnels
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'bandwidth',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                P2P tunnel destination address
                ''',
                'destination',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        P2P tunnel destination address
                        ''',
                        'destination',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        P2P tunnel destination address
                        ''',
                        'destination',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State',
            False, 
            [
            _MetaInfoClassMember('destination', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                P2P tunnel destination address
                ''',
                'destination',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        P2P tunnel destination address
                        ''',
                        'destination',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('destination', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        P2P tunnel destination address
                        ''',
                        'destination',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config',
            False, 
            [
            _MetaInfoClassMember('cspf-tiebreaker', REFERENCE_ENUM_CLASS, 'CspfTieBreakingEnum' , 'ydk.models.openconfig.openconfig_mpls', 'CspfTieBreakingEnum', 
                [], [], 
                '''                Determine the tie-breaking method to choose between
                equally desirable paths during CSFP computation
                ''',
                'cspf_tiebreaker',
                'openconfig-mpls', False),
            _MetaInfoClassMember('explicit-path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to a defined path
                ''',
                'explicit_path_name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                preemption priority once the LSP is established,
                lower is higher priority; default 0 indicates other LSPs
                will not preempt the LSPs once established
                ''',
                'hold_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-method', REFERENCE_IDENTITY_CLASS, 'PathComputationMethodIdentity' , 'ydk.models.openconfig.openconfig_mpls', 'PathComputationMethodIdentity', 
                [], [], 
                '''                The method used for computing the path, either
                locally computed, queried from a server or not
                computed at all (explicitly configured).
                ''',
                'path_computation_method',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the external path computation
                server
                ''',
                'path_computation_server',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specifies a preference for this path. The lower the
                number higher the preference
                ''',
                'preference',
                'openconfig-mpls', False),
            _MetaInfoClassMember('retry-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                sets the time between attempts to establish the
                LSP
                ''',
                'retry_timer',
                'openconfig-mpls', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                RSVP-TE preemption priority during LSP setup, lower is
                higher priority; default 7 indicates that LSP will not
                preempt established LSPs during setup
                ''',
                'setup_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('use-cspf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable CSPF for locally computed LSPs
                ''',
                'use_cspf',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State',
            False, 
            [
            _MetaInfoClassMember('cspf-tiebreaker', REFERENCE_ENUM_CLASS, 'CspfTieBreakingEnum' , 'ydk.models.openconfig.openconfig_mpls', 'CspfTieBreakingEnum', 
                [], [], 
                '''                Determine the tie-breaking method to choose between
                equally desirable paths during CSFP computation
                ''',
                'cspf_tiebreaker',
                'openconfig-mpls', False),
            _MetaInfoClassMember('explicit-path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to a defined path
                ''',
                'explicit_path_name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                preemption priority once the LSP is established,
                lower is higher priority; default 0 indicates other LSPs
                will not preempt the LSPs once established
                ''',
                'hold_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-method', REFERENCE_IDENTITY_CLASS, 'PathComputationMethodIdentity' , 'ydk.models.openconfig.openconfig_mpls', 'PathComputationMethodIdentity', 
                [], [], 
                '''                The method used for computing the path, either
                locally computed, queried from a server or not
                computed at all (explicitly configured).
                ''',
                'path_computation_method',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the external path computation
                server
                ''',
                'path_computation_server',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specifies a preference for this path. The lower the
                number higher the preference
                ''',
                'preference',
                'openconfig-mpls', False),
            _MetaInfoClassMember('retry-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                sets the time between attempts to establish the
                LSP
                ''',
                'retry_timer',
                'openconfig-mpls', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                RSVP-TE preemption priority during LSP setup, lower is
                higher priority; default 7 indicates that LSP will not
                preempt established LSPs during setup
                ''',
                'setup_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('use-cspf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable CSPF for locally computed LSPs
                ''',
                'use_cspf',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config',
            False, 
            [
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The priority of the specified secondary path option. Higher
                priority options are less preferable - such that a secondary
                path reference with a priority of 0 is the most preferred
                ''',
                'priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('secondary-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the secondary path that should be utilised
                when the containing primary path option is in use
                ''',
                'secondary_path',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the current active path option that has
                been selected of the candidate secondary paths
                ''',
                'active',
                'openconfig-mpls', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The priority of the specified secondary path option. Higher
                priority options are less preferable - such that a secondary
                path reference with a priority of 0 is the most preferred
                ''',
                'priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('secondary-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the secondary path that should be utilised
                when the containing primary path option is in use
                ''',
                'secondary_path',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath',
            False, 
            [
            _MetaInfoClassMember('secondary-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the secondary path option reference
                which acts as the key of the candidate-secondary-path
                list
                ''',
                'secondary_path',
                'openconfig-mpls', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config', 
                [], [], 
                '''                Configuration parameters relating to the candidate
                secondary path
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State', 
                [], [], 
                '''                Operational state parameters relating to the candidate
                secondary path
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'candidate-secondary-path',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths',
            False, 
            [
            _MetaInfoClassMember('candidate-secondary-path', REFERENCE_LIST, 'CandidateSecondaryPath' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath', 
                [], [], 
                '''                List of secondary paths which may be utilised when the
                current primary path is in use
                ''',
                'candidate_secondary_path',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'candidate-secondary-paths',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config',
            False, 
            [
            _MetaInfoClassMember('exclude-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups to exclude in
                path calculation.
                ''',
                'exclude_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-all-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which all must
                be included
                ''',
                'include_all_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-any-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which one must
                be included
                ''',
                'include_any_group',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State',
            False, 
            [
            _MetaInfoClassMember('exclude-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups to exclude in
                path calculation.
                ''',
                'exclude_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-all-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which all must
                be included
                ''',
                'include_all_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-any-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which one must
                be included
                ''',
                'include_any_group',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config', 
                [], [], 
                '''                Configuration data 
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'admin-groups',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path name
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('admin-groups', REFERENCE_CLASS, 'AdminGroups' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups', 
                [], [], 
                '''                Top-level container for include/exclude constraints for
                link affinities
                ''',
                'admin_groups',
                'openconfig-mpls', False),
            _MetaInfoClassMember('candidate-secondary-paths', REFERENCE_CLASS, 'CandidateSecondaryPaths' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths', 
                [], [], 
                '''                The set of candidate secondary paths which may be used
                for this primary path. When secondary paths are specified
                in the list the path of the secondary LSP in use must be
                restricted to those path options referenced. The
                priority of the secondary paths is specified within the
                list. Higher priority values are less preferred - that is
                to say that a path with priority 0 is the most preferred
                path. In the case that the list is empty, any secondary
                path option may be utilised when the current primary path
                is in use.
                ''',
                'candidate_secondary_paths',
                'openconfig-mpls', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config', 
                [], [], 
                '''                Configuration parameters related to paths
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State', 
                [], [], 
                '''                State parameters related to paths
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'p2p-primary-paths',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config',
            False, 
            [
            _MetaInfoClassMember('cspf-tiebreaker', REFERENCE_ENUM_CLASS, 'CspfTieBreakingEnum' , 'ydk.models.openconfig.openconfig_mpls', 'CspfTieBreakingEnum', 
                [], [], 
                '''                Determine the tie-breaking method to choose between
                equally desirable paths during CSFP computation
                ''',
                'cspf_tiebreaker',
                'openconfig-mpls', False),
            _MetaInfoClassMember('explicit-path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to a defined path
                ''',
                'explicit_path_name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                preemption priority once the LSP is established,
                lower is higher priority; default 0 indicates other LSPs
                will not preempt the LSPs once established
                ''',
                'hold_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-method', REFERENCE_IDENTITY_CLASS, 'PathComputationMethodIdentity' , 'ydk.models.openconfig.openconfig_mpls', 'PathComputationMethodIdentity', 
                [], [], 
                '''                The method used for computing the path, either
                locally computed, queried from a server or not
                computed at all (explicitly configured).
                ''',
                'path_computation_method',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the external path computation
                server
                ''',
                'path_computation_server',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specifies a preference for this path. The lower the
                number higher the preference
                ''',
                'preference',
                'openconfig-mpls', False),
            _MetaInfoClassMember('retry-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                sets the time between attempts to establish the
                LSP
                ''',
                'retry_timer',
                'openconfig-mpls', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                RSVP-TE preemption priority during LSP setup, lower is
                higher priority; default 7 indicates that LSP will not
                preempt established LSPs during setup
                ''',
                'setup_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('use-cspf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable CSPF for locally computed LSPs
                ''',
                'use_cspf',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State',
            False, 
            [
            _MetaInfoClassMember('cspf-tiebreaker', REFERENCE_ENUM_CLASS, 'CspfTieBreakingEnum' , 'ydk.models.openconfig.openconfig_mpls', 'CspfTieBreakingEnum', 
                [], [], 
                '''                Determine the tie-breaking method to choose between
                equally desirable paths during CSFP computation
                ''',
                'cspf_tiebreaker',
                'openconfig-mpls', False),
            _MetaInfoClassMember('explicit-path-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reference to a defined path
                ''',
                'explicit_path_name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('hold-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                preemption priority once the LSP is established,
                lower is higher priority; default 0 indicates other LSPs
                will not preempt the LSPs once established
                ''',
                'hold_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path name
                ''',
                'name',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-method', REFERENCE_IDENTITY_CLASS, 'PathComputationMethodIdentity' , 'ydk.models.openconfig.openconfig_mpls', 'PathComputationMethodIdentity', 
                [], [], 
                '''                The method used for computing the path, either
                locally computed, queried from a server or not
                computed at all (explicitly configured).
                ''',
                'path_computation_method',
                'openconfig-mpls', False),
            _MetaInfoClassMember('path-computation-server', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the external path computation
                server
                ''',
                'path_computation_server',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('path-computation-server', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the external path computation
                        server
                        ''',
                        'path_computation_server',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Specifies a preference for this path. The lower the
                number higher the preference
                ''',
                'preference',
                'openconfig-mpls', False),
            _MetaInfoClassMember('retry-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '600')], [], 
                '''                sets the time between attempts to establish the
                LSP
                ''',
                'retry_timer',
                'openconfig-mpls', False),
            _MetaInfoClassMember('setup-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                RSVP-TE preemption priority during LSP setup, lower is
                higher priority; default 7 indicates that LSP will not
                preempt established LSPs during setup
                ''',
                'setup_priority',
                'openconfig-mpls', False),
            _MetaInfoClassMember('use-cspf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable CSPF for locally computed LSPs
                ''',
                'use_cspf',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config',
            False, 
            [
            _MetaInfoClassMember('exclude-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups to exclude in
                path calculation.
                ''',
                'exclude_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-all-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which all must
                be included
                ''',
                'include_all_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-any-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which one must
                be included
                ''',
                'include_any_group',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State',
            False, 
            [
            _MetaInfoClassMember('exclude-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups to exclude in
                path calculation.
                ''',
                'exclude_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-all-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which all must
                be included
                ''',
                'include_all_group',
                'openconfig-mpls', False),
            _MetaInfoClassMember('include-any-group', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of references to named admin-groups of which one must
                be included
                ''',
                'include_any_group',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config', 
                [], [], 
                '''                Configuration data 
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State', 
                [], [], 
                '''                Operational state data 
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'admin-groups',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Path name
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('admin-groups', REFERENCE_CLASS, 'AdminGroups' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups', 
                [], [], 
                '''                Top-level container for include/exclude constraints for
                link affinities
                ''',
                'admin_groups',
                'openconfig-mpls', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config', 
                [], [], 
                '''                Configuration parameters related to paths
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State', 
                [], [], 
                '''                State parameters related to paths
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'p2p-secondary-paths',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config', 
                [], [], 
                '''                Configuration parameters for P2P LSPs
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('p2p-primary-paths', REFERENCE_LIST, 'P2PPrimaryPaths' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths', 
                [], [], 
                '''                List of p2p primary paths for a tunnel
                ''',
                'p2p_primary_paths',
                'openconfig-mpls', False),
            _MetaInfoClassMember('p2p-secondary-paths', REFERENCE_LIST, 'P2PSecondaryPaths' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths', 
                [], [], 
                '''                List of p2p primary paths for a tunnel
                ''',
                'p2p_secondary_paths',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State', 
                [], [], 
                '''                State parameters for P2P LSPs
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'p2p-tunnel-attributes',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath.Tunnel' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath.Tunnel',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The tunnel name
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'TunnelTypeIdentity' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelTypeIdentity', 
                [], [], 
                '''                The tunnel type, p2p or p2mp.
                ''',
                'type',
                'openconfig-mpls', True),
            _MetaInfoClassMember('bandwidth', REFERENCE_CLASS, 'Bandwidth' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth', 
                [], [], 
                '''                Bandwidth configuration for TE LSPs
                ''',
                'bandwidth',
                'openconfig-mpls', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.Config', 
                [], [], 
                '''                Configuration parameters related to TE tunnels:
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('p2p-tunnel-attributes', REFERENCE_CLASS, 'P2PTunnelAttributes' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes', 
                [], [], 
                '''                Parameters related to LSPs of type P2P
                ''',
                'p2p_tunnel_attributes',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel.State', 
                [], [], 
                '''                State parameters related to TE tunnels
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'tunnel',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.ConstrainedPath' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.ConstrainedPath',
            False, 
            [
            _MetaInfoClassMember('named-explicit-paths', REFERENCE_LIST, 'NamedExplicitPaths' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.NamedExplicitPaths', 
                [], [], 
                '''                A list of explicit paths
                ''',
                'named_explicit_paths',
                'openconfig-mpls', False),
            _MetaInfoClassMember('tunnel', REFERENCE_LIST, 'Tunnel' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath.Tunnel', 
                [], [], 
                '''                List of TE tunnels
                ''',
                'tunnel',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'constrained-path',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp',
            False, 
            [
            _MetaInfoClassMember('fec-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address prefix for packets sharing the same
                forwarding equivalence class for the IGP-based LSP
                ''',
                'fec_address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('fec-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Address prefix for packets sharing the same
                        forwarding equivalence class for the IGP-based LSP
                        ''',
                        'fec_address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('fec-address', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Address prefix for packets sharing the same
                        forwarding equivalence class for the IGP-based LSP
                        ''',
                        'fec_address',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'p2p-lsp',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp',
            False, 
            [
            ],
            'openconfig-mpls',
            'p2mp-lsp',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp',
            False, 
            [
            ],
            'openconfig-mpls',
            'mp2mp-lsp',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.LdpTypeEnum' : _MetaInfoEnum('LdpTypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'BASIC':'BASIC',
            'TARGETED':'TARGETED',
        }, 'openconfig-mpls-ldp', _yang_ns._namespaces['openconfig-mpls-ldp']),
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel',
            False, 
            [
            _MetaInfoClassMember('ldp-type', REFERENCE_ENUM_CLASS, 'LdpTypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.LdpTypeEnum', 
                [], [], 
                '''                specify basic or targeted LDP LSP
                ''',
                'ldp_type',
                'openconfig-mpls', False),
            _MetaInfoClassMember('mp2mp-lsp', REFERENCE_CLASS, 'Mp2MpLsp' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp', 
                [], [], 
                '''                properties of multipoint-to-multipoint tunnels
                ''',
                'mp2mp_lsp',
                'openconfig-mpls', False),
            _MetaInfoClassMember('p2mp-lsp', REFERENCE_CLASS, 'P2MpLsp' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp', 
                [], [], 
                '''                properties of point-to-multipoint tunnels
                ''',
                'p2mp_lsp',
                'openconfig-mpls', False),
            _MetaInfoClassMember('p2p-lsp', REFERENCE_CLASS, 'P2PLsp' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp', 
                [], [], 
                '''                properties of point-to-point tunnels
                ''',
                'p2p_lsp',
                'openconfig-mpls', False),
            _MetaInfoClassMember('tunnel-type', REFERENCE_ENUM_CLASS, 'TunnelTypeEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelTypeEnum', 
                [], [], 
                '''                specifies the type of LSP, e.g., P2P or P2MP
                ''',
                'tunnel_type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'tunnel',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp',
            False, 
            [
            _MetaInfoClassMember('tunnel', REFERENCE_CLASS, 'Tunnel' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel', 
                [], [], 
                '''                contains configuration stanzas for different LSP
                tunnel types (P2P, P2MP, etc.)
                ''',
                'tunnel',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'ldp',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config',
            False, 
            [
            _MetaInfoClassMember('fec-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                FEC that is to be advertised as part of the Prefix-SID
                ''',
                'fec_address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('fec-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        FEC that is to be advertised as part of the Prefix-SID
                        ''',
                        'fec_address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('fec-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        FEC that is to be advertised as part of the Prefix-SID
                        ''',
                        'fec_address',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State',
            False, 
            [
            _MetaInfoClassMember('fec-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                FEC that is to be advertised as part of the Prefix-SID
                ''',
                'fec_address',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('fec-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        FEC that is to be advertised as part of the Prefix-SID
                        ''',
                        'fec_address',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('fec-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        FEC that is to be advertised as part of the Prefix-SID
                        ''',
                        'fec_address',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config.LastHopBehaviorEnum' : _MetaInfoEnum('LastHopBehaviorEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'EXPLICIT-NULL':'EXPLICIT_NULL',
            'UNCHANGED':'UNCHANGED',
            'PHP':'PHP',
        }, 'openconfig-mpls-sr', _yang_ns._namespaces['openconfig-mpls-sr']),
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config.TypeEnum' : _MetaInfoEnum('TypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'INDEX':'INDEX',
            'ABSOLUTE':'ABSOLUTE',
        }, 'openconfig-mpls-sr', _yang_ns._namespaces['openconfig-mpls-sr']),
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config',
            False, 
            [
            _MetaInfoClassMember('last-hop-behavior', REFERENCE_ENUM_CLASS, 'LastHopBehaviorEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config.LastHopBehaviorEnum', 
                [], [], 
                '''                Configuration relating to the LFIB actions for the
                Prefix-SID to be used by the penultimate-hop
                ''',
                'last_hop_behavior',
                'openconfig-mpls', False),
            _MetaInfoClassMember('node-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies that the Prefix-SID is to be treated as a Node-SID
                by setting the N-flag in the advertised Prefix-SID TLV in the
                IGP
                ''',
                'node_flag',
                'openconfig-mpls', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config.TypeEnum', 
                [], [], 
                '''                Specifies how the value of the Prefix-SID should be
                interpreted - whether as an offset to the SRGB, or as an
                absolute value
                ''',
                'type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'config',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State.LastHopBehaviorEnum' : _MetaInfoEnum('LastHopBehaviorEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'EXPLICIT-NULL':'EXPLICIT_NULL',
            'UNCHANGED':'UNCHANGED',
            'PHP':'PHP',
        }, 'openconfig-mpls-sr', _yang_ns._namespaces['openconfig-mpls-sr']),
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State.TypeEnum' : _MetaInfoEnum('TypeEnum', 'ydk.models.openconfig.openconfig_mpls',
        {
            'INDEX':'INDEX',
            'ABSOLUTE':'ABSOLUTE',
        }, 'openconfig-mpls-sr', _yang_ns._namespaces['openconfig-mpls-sr']),
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State',
            False, 
            [
            _MetaInfoClassMember('last-hop-behavior', REFERENCE_ENUM_CLASS, 'LastHopBehaviorEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State.LastHopBehaviorEnum', 
                [], [], 
                '''                Configuration relating to the LFIB actions for the
                Prefix-SID to be used by the penultimate-hop
                ''',
                'last_hop_behavior',
                'openconfig-mpls', False),
            _MetaInfoClassMember('node-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies that the Prefix-SID is to be treated as a Node-SID
                by setting the N-flag in the advertised Prefix-SID TLV in the
                IGP
                ''',
                'node_flag',
                'openconfig-mpls', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TypeEnum' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State.TypeEnum', 
                [], [], 
                '''                Specifies how the value of the Prefix-SID should be
                interpreted - whether as an offset to the SRGB, or as an
                absolute value
                ''',
                'type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'state',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config', 
                [], [], 
                '''                Configuration parameters relating to the Prefix-SID
                used for the originated FEC
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State', 
                [], [], 
                '''                Operational state parameters relating to the
                Prefix-SID used for the originated FEC
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'prefix-sid',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec',
            False, 
            [
            _MetaInfoClassMember('fec-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                FEC that is to be advertised as part of the Prefix-SID
                ''',
                'fec_address',
                'openconfig-mpls', True, [
                    _MetaInfoClassMember('fec-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        FEC that is to be advertised as part of the Prefix-SID
                        ''',
                        'fec_address',
                        'openconfig-mpls', True),
                    _MetaInfoClassMember('fec-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        FEC that is to be advertised as part of the Prefix-SID
                        ''',
                        'fec_address',
                        'openconfig-mpls', True),
                ]),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config', 
                [], [], 
                '''                Configuration parameters relating to the FEC to be
                advertised by SR
                ''',
                'config',
                'openconfig-mpls', False),
            _MetaInfoClassMember('prefix-sid', REFERENCE_CLASS, 'PrefixSid' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid', 
                [], [], 
                '''                Parameters relating to the Prefix-SID
                used for the originated FEC
                ''',
                'prefix_sid',
                'openconfig-mpls', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State', 
                [], [], 
                '''                Operational state relating to a FEC advertised by SR
                ''',
                'state',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'fec',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp',
            False, 
            [
            _MetaInfoClassMember('fec', REFERENCE_LIST, 'Fec' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec', 
                [], [], 
                '''                List of FECs that are to be originated as SR LSPs
                ''',
                'fec',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'p2p-lsp',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel',
            False, 
            [
            _MetaInfoClassMember('p2p-lsp', REFERENCE_CLASS, 'P2PLsp' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp', 
                [], [], 
                '''                properties of point-to-point tunnels
                ''',
                'p2p_lsp',
                'openconfig-mpls', False),
            _MetaInfoClassMember('tunnel-type', REFERENCE_ENUM_CLASS, 'TunnelTypeEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'TunnelTypeEnum', 
                [], [], 
                '''                specifies the type of LSP, e.g., P2P or P2MP
                ''',
                'tunnel_type',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'tunnel',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting',
            False, 
            [
            _MetaInfoClassMember('tunnel', REFERENCE_CLASS, 'Tunnel' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel', 
                [], [], 
                '''                contains configuration stanzas for different LSP
                tunnel types (P2P, P2MP, etc.)
                ''',
                'tunnel',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'segment-routing',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath.PathSetupProtocol',
            False, 
            [
            _MetaInfoClassMember('ldp', REFERENCE_CLASS, 'Ldp' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp', 
                [], [], 
                '''                LDP signaling setup for IGP-congruent LSPs
                ''',
                'ldp',
                'openconfig-mpls', False),
            _MetaInfoClassMember('segment-routing', REFERENCE_CLASS, 'SegmentRouting' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting', 
                [], [], 
                '''                segment routing signaling extensions for
                IGP-confgruent LSPs
                ''',
                'segment_routing',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'path-setup-protocol',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.UnconstrainedPath' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.UnconstrainedPath',
            False, 
            [
            _MetaInfoClassMember('path-setup-protocol', REFERENCE_CLASS, 'PathSetupProtocol' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath.PathSetupProtocol', 
                [], [], 
                '''                select and configure the signaling method for
                 the LSP
                ''',
                'path_setup_protocol',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'unconstrained-path',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress',
            False, 
            [
            _MetaInfoClassMember('incoming-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                label value on the incoming packet
                ''',
                'incoming_label',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        label value on the incoming packet
                        ''',
                        'incoming_label',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('incoming-label', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        label value on the incoming packet
                        ''',
                        'incoming_label',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                next hop IP address for the LSP
                ''',
                'next_hop',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        next hop IP address for the LSP
                        ''',
                        'next_hop',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        next hop IP address for the LSP
                        ''',
                        'next_hop',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('push-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                label value to push at the current hop for the
                LSP
                ''',
                'push_label',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('push-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        label value to push at the current hop for the
                        LSP
                        ''',
                        'push_label',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('push-label', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        label value to push at the current hop for the
                        LSP
                        ''',
                        'push_label',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'ingress',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit',
            False, 
            [
            _MetaInfoClassMember('incoming-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                label value on the incoming packet
                ''',
                'incoming_label',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        label value on the incoming packet
                        ''',
                        'incoming_label',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('incoming-label', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        label value on the incoming packet
                        ''',
                        'incoming_label',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                next hop IP address for the LSP
                ''',
                'next_hop',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        next hop IP address for the LSP
                        ''',
                        'next_hop',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        next hop IP address for the LSP
                        ''',
                        'next_hop',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('push-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                label value to push at the current hop for the
                LSP
                ''',
                'push_label',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('push-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        label value to push at the current hop for the
                        LSP
                        ''',
                        'push_label',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('push-label', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        label value to push at the current hop for the
                        LSP
                        ''',
                        'push_label',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'transit',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress',
            False, 
            [
            _MetaInfoClassMember('incoming-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                label value on the incoming packet
                ''',
                'incoming_label',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('incoming-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        label value on the incoming packet
                        ''',
                        'incoming_label',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('incoming-label', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        label value on the incoming packet
                        ''',
                        'incoming_label',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                next hop IP address for the LSP
                ''',
                'next_hop',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        next hop IP address for the LSP
                        ''',
                        'next_hop',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        next hop IP address for the LSP
                        ''',
                        'next_hop',
                        'openconfig-mpls', False),
                ]),
            _MetaInfoClassMember('push-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                label value to push at the current hop for the
                LSP
                ''',
                'push_label',
                'openconfig-mpls', False, [
                    _MetaInfoClassMember('push-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        label value to push at the current hop for the
                        LSP
                        ''',
                        'push_label',
                        'openconfig-mpls', False),
                    _MetaInfoClassMember('push-label', REFERENCE_ENUM_CLASS, 'MplsLabelEnum' , 'ydk.models.openconfig.openconfig_mpls_types', 'MplsLabelEnum', 
                        [], [], 
                        '''                        label value to push at the current hop for the
                        LSP
                        ''',
                        'push_label',
                        'openconfig-mpls', False),
                ]),
            ],
            'openconfig-mpls',
            'egress',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.StaticLsps.LabelSwitchedPath' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.StaticLsps.LabelSwitchedPath',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name to identify the LSP
                ''',
                'name',
                'openconfig-mpls', True),
            _MetaInfoClassMember('egress', REFERENCE_CLASS, 'Egress' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress', 
                [], [], 
                '''                static LSPs for which the router is a
                egress  node
                ''',
                'egress',
                'openconfig-mpls', False),
            _MetaInfoClassMember('ingress', REFERENCE_CLASS, 'Ingress' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress', 
                [], [], 
                '''                Static LSPs for which the router is an
                ingress node
                ''',
                'ingress',
                'openconfig-mpls', False),
            _MetaInfoClassMember('transit', REFERENCE_CLASS, 'Transit' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit', 
                [], [], 
                '''                static LSPs for which the router is a
                transit node
                ''',
                'transit',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'label-switched-path',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps.StaticLsps' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps.StaticLsps',
            False, 
            [
            _MetaInfoClassMember('label-switched-path', REFERENCE_LIST, 'LabelSwitchedPath' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.StaticLsps.LabelSwitchedPath', 
                [], [], 
                '''                list of defined static LSPs
                ''',
                'label_switched_path',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'static-lsps',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls.Lsps' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps',
            False, 
            [
            _MetaInfoClassMember('constrained-path', REFERENCE_CLASS, 'ConstrainedPath' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.ConstrainedPath', 
                [], [], 
                '''                traffic-engineered LSPs supporting different
                path computation and signaling methods
                ''',
                'constrained_path',
                'openconfig-mpls', False),
            _MetaInfoClassMember('static-lsps', REFERENCE_CLASS, 'StaticLsps' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.StaticLsps', 
                [], [], 
                '''                statically configured LSPs, without dynamic
                signaling
                ''',
                'static_lsps',
                'openconfig-mpls', False),
            _MetaInfoClassMember('unconstrained-path', REFERENCE_CLASS, 'UnconstrainedPath' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps.UnconstrainedPath', 
                [], [], 
                '''                LSPs that use the IGP-determined path, i.e., non
                traffic-engineered, or non constrained-path
                ''',
                'unconstrained_path',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'lsps',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'Mpls' : {
        'meta_info' : _MetaInfoClass('Mpls',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Global_', 
                [], [], 
                '''                general mpls configuration applicable to any
                type of LSP and signaling protocol - label ranges,
                entropy label supportmay be added here
                ''',
                'global_',
                'openconfig-mpls', False),
            _MetaInfoClassMember('lsps', REFERENCE_CLASS, 'Lsps' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.Lsps', 
                [], [], 
                '''                LSP definitions and configuration
                ''',
                'lsps',
                'openconfig-mpls', False),
            _MetaInfoClassMember('signaling-protocols', REFERENCE_CLASS, 'SignalingProtocols' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.SignalingProtocols', 
                [], [], 
                '''                top-level signaling protocol configuration
                ''',
                'signaling_protocols',
                'openconfig-mpls', False),
            _MetaInfoClassMember('te-global-attributes', REFERENCE_CLASS, 'TeGlobalAttributes' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeGlobalAttributes', 
                [], [], 
                '''                traffic-engineering global attributes
                ''',
                'te_global_attributes',
                'openconfig-mpls', False),
            _MetaInfoClassMember('te-interface-attributes', REFERENCE_CLASS, 'TeInterfaceAttributes' , 'ydk.models.openconfig.openconfig_mpls', 'Mpls.TeInterfaceAttributes', 
                [], [], 
                '''                traffic engineering attributes specific
                for interfaces
                ''',
                'te_interface_attributes',
                'openconfig-mpls', False),
            ],
            'openconfig-mpls',
            'mpls',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'LocallyComputedIdentity' : {
        'meta_info' : _MetaInfoClass('LocallyComputedIdentity',
            False, 
            [
            ],
            'openconfig-mpls',
            'locally-computed',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'ExternallyQueriedIdentity' : {
        'meta_info' : _MetaInfoClass('ExternallyQueriedIdentity',
            False, 
            [
            ],
            'openconfig-mpls',
            'externally-queried',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
    'ExplicitlyDefinedIdentity' : {
        'meta_info' : _MetaInfoClass('ExplicitlyDefinedIdentity',
            False, 
            [
            ],
            'openconfig-mpls',
            'explicitly-defined',
            _yang_ns._namespaces['openconfig-mpls'],
        'ydk.models.openconfig.openconfig_mpls'
        ),
    },
}
_meta_table['Mpls.Global_.MplsInterfaceAttributes.Interface.Config']['meta_info'].parent =_meta_table['Mpls.Global_.MplsInterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.Global_.MplsInterfaceAttributes.Interface.State']['meta_info'].parent =_meta_table['Mpls.Global_.MplsInterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.Global_.MplsInterfaceAttributes.Interface']['meta_info'].parent =_meta_table['Mpls.Global_.MplsInterfaceAttributes']['meta_info']
_meta_table['Mpls.Global_.Config']['meta_info'].parent =_meta_table['Mpls.Global_']['meta_info']
_meta_table['Mpls.Global_.State']['meta_info'].parent =_meta_table['Mpls.Global_']['meta_info']
_meta_table['Mpls.Global_.MplsInterfaceAttributes']['meta_info'].parent =_meta_table['Mpls.Global_']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.Config']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList.State']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers.MembersList']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.Config']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.State']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_.StaticSrlgMembers']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg.Srlg_']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.Srlg']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.Config']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth.State']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.Config']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup.State']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups.AdminGroup']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.TeLspTimers.Config']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.TeLspTimers']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.TeLspTimers.State']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes.TeLspTimers']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.Srlg']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.IgpFloodingBandwidth']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.MplsAdminGroups']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes']['meta_info']
_meta_table['Mpls.TeGlobalAttributes.TeLspTimers']['meta_info'].parent =_meta_table['Mpls.TeGlobalAttributes']['meta_info']
_meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.Config']['meta_info'].parent =_meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth']['meta_info']
_meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth.State']['meta_info'].parent =_meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth']['meta_info']
_meta_table['Mpls.TeInterfaceAttributes.Interface.Config']['meta_info'].parent =_meta_table['Mpls.TeInterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.TeInterfaceAttributes.Interface.State']['meta_info'].parent =_meta_table['Mpls.TeInterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.TeInterfaceAttributes.Interface.IgpFloodingBandwidth']['meta_info'].parent =_meta_table['Mpls.TeInterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.TeInterfaceAttributes.Interface']['meta_info'].parent =_meta_table['Mpls.TeInterfaceAttributes']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.State.Session']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.State']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.State.Neighbor']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.State']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.Hellos']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.Hellos.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.Hellos']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.State.Counters']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.State']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.GracefulRestart']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.SoftPreemption']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.Hellos']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Bandwidth']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State.Counters']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Hellos']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Authentication']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Subscription']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface.Protection']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes.Interface']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Sessions']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Neighbors']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.Global_']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe.InterfaceAttributes']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.RsvpTe']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.Config']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.State']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces.AdjacencySid']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Srgb']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting.Interfaces']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.SegmentRouting']['meta_info']
_meta_table['Mpls.SignalingProtocols.Ldp.Timers']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols.Ldp']['meta_info']
_meta_table['Mpls.SignalingProtocols.RsvpTe']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols']['meta_info']
_meta_table['Mpls.SignalingProtocols.SegmentRouting']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols']['meta_info']
_meta_table['Mpls.SignalingProtocols.Ldp']['meta_info'].parent =_meta_table['Mpls.SignalingProtocols']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths.ExplicitRouteObjects']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.State.Counters']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.State']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Overflow']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth.Underflow']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth.AutoBandwidth']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths.CandidateSecondaryPath']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.CandidateSecondaryPaths']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths.AdminGroups']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths.AdminGroups']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PPrimaryPaths']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes.P2PSecondaryPaths']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.State']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.Bandwidth']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel.P2PTunnelAttributes']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.NamedExplicitPaths']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath.Tunnel']['meta_info'].parent =_meta_table['Mpls.Lsps.ConstrainedPath']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2PLsp']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.P2MpLsp']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel.Mp2MpLsp']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp.Tunnel']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid.State']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.Config']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.State']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec.PrefixSid']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp.Fec']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel.P2PLsp']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting.Tunnel']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.Ldp']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol.SegmentRouting']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath.PathSetupProtocol']['meta_info'].parent =_meta_table['Mpls.Lsps.UnconstrainedPath']['meta_info']
_meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath.Ingress']['meta_info'].parent =_meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath']['meta_info']
_meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath.Transit']['meta_info'].parent =_meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath']['meta_info']
_meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath.Egress']['meta_info'].parent =_meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath']['meta_info']
_meta_table['Mpls.Lsps.StaticLsps.LabelSwitchedPath']['meta_info'].parent =_meta_table['Mpls.Lsps.StaticLsps']['meta_info']
_meta_table['Mpls.Lsps.ConstrainedPath']['meta_info'].parent =_meta_table['Mpls.Lsps']['meta_info']
_meta_table['Mpls.Lsps.UnconstrainedPath']['meta_info'].parent =_meta_table['Mpls.Lsps']['meta_info']
_meta_table['Mpls.Lsps.StaticLsps']['meta_info'].parent =_meta_table['Mpls.Lsps']['meta_info']
_meta_table['Mpls.Global_']['meta_info'].parent =_meta_table['Mpls']['meta_info']
_meta_table['Mpls.TeGlobalAttributes']['meta_info'].parent =_meta_table['Mpls']['meta_info']
_meta_table['Mpls.TeInterfaceAttributes']['meta_info'].parent =_meta_table['Mpls']['meta_info']
_meta_table['Mpls.SignalingProtocols']['meta_info'].parent =_meta_table['Mpls']['meta_info']
_meta_table['Mpls.Lsps']['meta_info'].parent =_meta_table['Mpls']['meta_info']
