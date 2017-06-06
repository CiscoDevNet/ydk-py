


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HoptypeEnum' : _MetaInfoEnum('HoptypeEnum', 'ydk.models.cisco_ios_xe.common_mpls_static',
        {
            'PRIMARY':'PRIMARY',
            'BACKUP':'BACKUP',
        }, 'common-mpls-static', _yang_ns._namespaces['common-mpls-static']),
    'NexthopResolutionTypeIdentity' : {
        'meta_info' : _MetaInfoClass('NexthopResolutionTypeIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'nexthop-resolution-type',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'LspTypeIdentity' : {
        'meta_info' : _MetaInfoClass('LspTypeIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'lsp-type',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The interface index
                ''',
                'if_index',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address of the nexthop
                ''',
                'ipv4_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of the nexthop
                ''',
                'ipv6_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the nexthop
                ''',
                'mac_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('out-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface
                ''',
                'out_interface_name',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop-type',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop
                ''',
                'index',
                'common-mpls-static', True),
            _MetaInfoClassMember('next-hop-type', REFERENCE_CLASS, 'NextHopType' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType', 
                [], [], 
                '''                Next-hop
                ''',
                'next_hop_type',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            _MetaInfoClassMember('protected-by', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop that protects this nexthop
                ''',
                'protected_by',
                'common-mpls-static', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'HoptypeEnum' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'HoptypeEnum', 
                [], [], 
                '''                The forwarding path's hoptype
                ''',
                'type',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path',
            False, 
            [
            _MetaInfoClassMember('auto-protect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables automatic protection if true
                ''',
                'auto_protect',
                'common-mpls-static', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop', 
                [], [], 
                '''                next-hops list
                ''',
                'next_hop',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'path',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the VRF
                ''',
                'vrf_name',
                'common-mpls-static', True),
            _MetaInfoClassMember('in-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the local label
                ''',
                'in_label',
                'common-mpls-static', True, [
                    _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        Value of the local label
                        ''',
                        'in_label',
                        'common-mpls-static', True),
                    _MetaInfoClassMember('in-label', REFERENCE_ENUM_CLASS, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        Value of the local label
                        ''',
                        'in_label',
                        'common-mpls-static', True),
                ]),
            _MetaInfoClassMember('path', REFERENCE_CLASS, 'Path' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path', 
                [], [], 
                '''                Fowarding path
                ''',
                'path',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'in-label-lsp',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.InLabelLsps' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.InLabelLsps',
            False, 
            [
            _MetaInfoClassMember('in-label-lsp', REFERENCE_LIST, 'InLabelLsp' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp', 
                [], [], 
                '''                Non-ingress MPLS Static LSPs,
                keyed on the incoming label
                ''',
                'in_label_lsp',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'in-label-lsps',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The interface index
                ''',
                'if_index',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address of the nexthop
                ''',
                'ipv4_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of the nexthop
                ''',
                'ipv6_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the nexthop
                ''',
                'mac_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('out-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface
                ''',
                'out_interface_name',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop-type',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop
                ''',
                'index',
                'common-mpls-static', True),
            _MetaInfoClassMember('next-hop-type', REFERENCE_CLASS, 'NextHopType' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType', 
                [], [], 
                '''                Next-hop
                ''',
                'next_hop_type',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            _MetaInfoClassMember('protected-by', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop that protects this nexthop
                ''',
                'protected_by',
                'common-mpls-static', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'HoptypeEnum' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'HoptypeEnum', 
                [], [], 
                '''                The forwarding path's hoptype
                ''',
                'type',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path',
            False, 
            [
            _MetaInfoClassMember('auto-protect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables automatic protection if true
                ''',
                'auto_protect',
                'common-mpls-static', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop', 
                [], [], 
                '''                next-hops list
                ''',
                'next_hop',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'path',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the VRF
                ''',
                'vrf_name',
                'common-mpls-static', True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                IPv6 prefix of packets that will ingress on this LSP
                ''',
                'prefix',
                'common-mpls-static', True),
            _MetaInfoClassMember('in-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the local label. Optional for ingress
                ''',
                'in_label',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        Value of the local label. Optional for ingress
                        ''',
                        'in_label',
                        'common-mpls-static', False),
                    _MetaInfoClassMember('in-label', REFERENCE_ENUM_CLASS, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        Value of the local label. Optional for ingress
                        ''',
                        'in_label',
                        'common-mpls-static', False),
                ]),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the LSP
                ''',
                'name',
                'common-mpls-static', False),
            _MetaInfoClassMember('path', REFERENCE_CLASS, 'Path' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path', 
                [], [], 
                '''                Fowarding path
                ''',
                'path',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'ipv6-ingress-lsp',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv6IngressLsps' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv6IngressLsps',
            False, 
            [
            _MetaInfoClassMember('ipv6-ingress-lsp', REFERENCE_LIST, 'Ipv6IngressLsp' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp', 
                [], [], 
                '''                MPLS Static IPv6 Label Switched Path
                Configuration at Ingress
                ''',
                'ipv6_ingress_lsp',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'ipv6-ingress-lsps',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The interface index
                ''',
                'if_index',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address of the nexthop
                ''',
                'ipv4_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of the nexthop
                ''',
                'ipv6_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the nexthop
                ''',
                'mac_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('out-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface
                ''',
                'out_interface_name',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop-type',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop
                ''',
                'index',
                'common-mpls-static', True),
            _MetaInfoClassMember('next-hop-type', REFERENCE_CLASS, 'NextHopType' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType', 
                [], [], 
                '''                Next-hop
                ''',
                'next_hop_type',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            _MetaInfoClassMember('protected-by', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop that protects this nexthop
                ''',
                'protected_by',
                'common-mpls-static', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'HoptypeEnum' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'HoptypeEnum', 
                [], [], 
                '''                The forwarding path's hoptype
                ''',
                'type',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path',
            False, 
            [
            _MetaInfoClassMember('auto-protect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables automatic protection if true
                ''',
                'auto_protect',
                'common-mpls-static', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop', 
                [], [], 
                '''                next-hops list
                ''',
                'next_hop',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'path',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the VRF
                ''',
                'vrf_name',
                'common-mpls-static', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the LSP
                ''',
                'name',
                'common-mpls-static', True),
            _MetaInfoClassMember('in-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the local label
                ''',
                'in_label',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        Value of the local label
                        ''',
                        'in_label',
                        'common-mpls-static', False),
                    _MetaInfoClassMember('in-label', REFERENCE_ENUM_CLASS, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        Value of the local label
                        ''',
                        'in_label',
                        'common-mpls-static', False),
                ]),
            _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                ipv4 prefix
                ''',
                'ipv4_prefix',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                ipv6 prefix
                ''',
                'ipv6_prefix',
                'common-mpls-static', False),
            _MetaInfoClassMember('lsp-type', REFERENCE_IDENTITY_CLASS, 'LspTypeIdentity' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'LspTypeIdentity', 
                [], [], 
                '''                lsp type
                ''',
                'lsp_type',
                'common-mpls-static', False),
            _MetaInfoClassMember('path', REFERENCE_CLASS, 'Path' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path', 
                [], [], 
                '''                Fowarding path
                ''',
                'path',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'named-lsp',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.NamedLsps' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.NamedLsps',
            False, 
            [
            _MetaInfoClassMember('named-lsp', REFERENCE_LIST, 'NamedLsp' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp', 
                [], [], 
                '''                MPLS Static Label Switched Path Configuration.
                The LSPs in this list are referenced by a string name.
                The LSPs may be ingress/egress/crossconnect,
                may have v4/v6 prefixes and may be associated with any
                VRF. The other specialized lists above are for
                implemetations that are keyed on prefixes or in-labels
                instead of the LSP name.
                ''',
                'named_lsp',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'named-lsps',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'name',
                'common-mpls-static', True),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Enabled boolean
                ''',
                'enabled',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'interface',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Interfaces' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Interfaces.Interface', 
                [], [], 
                '''                List of interfaces that can be enabled under
                mpls static
                ''',
                'interface',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'interfaces',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The interface index
                ''',
                'if_index',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address of the nexthop
                ''',
                'ipv4_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of the nexthop
                ''',
                'ipv6_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the nexthop
                ''',
                'mac_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('out-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface
                ''',
                'out_interface_name',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop-type',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop
                ''',
                'index',
                'common-mpls-static', True),
            _MetaInfoClassMember('next-hop-type', REFERENCE_CLASS, 'NextHopType' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType', 
                [], [], 
                '''                Next-hop
                ''',
                'next_hop_type',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            _MetaInfoClassMember('protected-by', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop that protects this nexthop
                ''',
                'protected_by',
                'common-mpls-static', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'HoptypeEnum' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'HoptypeEnum', 
                [], [], 
                '''                The forwarding path's hoptype
                ''',
                'type',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path',
            False, 
            [
            _MetaInfoClassMember('auto-protect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables automatic protection if true
                ''',
                'auto_protect',
                'common-mpls-static', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop', 
                [], [], 
                '''                next-hops list
                ''',
                'next_hop',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'path',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the VRF
                ''',
                'vrf_name',
                'common-mpls-static', True),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                IPv4 prefix of packets that will ingress on this LSP
                ''',
                'prefix',
                'common-mpls-static', True),
            _MetaInfoClassMember('in-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the local label. Optional for ingress
                ''',
                'in_label',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('in-label', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        Value of the local label. Optional for ingress
                        ''',
                        'in_label',
                        'common-mpls-static', False),
                    _MetaInfoClassMember('in-label', REFERENCE_ENUM_CLASS, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        Value of the local label. Optional for ingress
                        ''',
                        'in_label',
                        'common-mpls-static', False),
                ]),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the LSP
                ''',
                'name',
                'common-mpls-static', False),
            _MetaInfoClassMember('path', REFERENCE_CLASS, 'Path' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path', 
                [], [], 
                '''                Fowarding path
                ''',
                'path',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'ipv4-ingress-lsp',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg.Ipv4IngressLsps' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg.Ipv4IngressLsps',
            False, 
            [
            _MetaInfoClassMember('ipv4-ingress-lsp', REFERENCE_LIST, 'Ipv4IngressLsp' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp', 
                [], [], 
                '''                MPLS Static IPv4 Label Switched
                Path Configuration at Ingress
                ''',
                'ipv4_ingress_lsp',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'ipv4-ingress-lsps',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticCfg' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticCfg',
            False, 
            [
            _MetaInfoClassMember('in-label-lsps', REFERENCE_CLASS, 'InLabelLsps' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.InLabelLsps', 
                [], [], 
                '''                The LSPs indexed by in-label
                ''',
                'in_label_lsps',
                'common-mpls-static', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Interfaces', 
                [], [], 
                '''                The list of interfaces configured with mpls
                ''',
                'interfaces',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv4-ingress-lsps', REFERENCE_CLASS, 'Ipv4IngressLsps' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv4IngressLsps', 
                [], [], 
                '''                The LSPs indexed by ipv4 prefix
                ''',
                'ipv4_ingress_lsps',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv6-ingress-lsps', REFERENCE_CLASS, 'Ipv6IngressLsps' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.Ipv6IngressLsps', 
                [], [], 
                '''                The LSPs indexed by ipv6 prefix
                ''',
                'ipv6_ingress_lsps',
                'common-mpls-static', False),
            _MetaInfoClassMember('named-lsps', REFERENCE_CLASS, 'NamedLsps' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg.NamedLsps', 
                [], [], 
                '''                The LSPs indexed by name
                ''',
                'named_lsps',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'mpls-static-cfg',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for byte count
                ''',
                'bytes',
                'common-mpls-static', False),
            _MetaInfoClassMember('dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for dropped-bytes
                ''',
                'dropped_bytes',
                'common-mpls-static', False),
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for dropped-packets
                ''',
                'dropped_packets',
                'common-mpls-static', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for packet count
                ''',
                'packets',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'stats',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats',
            False, 
            [
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats', 
                [], [], 
                '''                Statistics
                ''',
                'stats',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'ingress-stats',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for byte count
                ''',
                'bytes',
                'common-mpls-static', False),
            _MetaInfoClassMember('dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for dropped-bytes
                ''',
                'dropped_bytes',
                'common-mpls-static', False),
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for dropped-packets
                ''',
                'dropped_packets',
                'common-mpls-static', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for packet count
                ''',
                'packets',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'stats',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats',
            False, 
            [
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats', 
                [], [], 
                '''                Statistics
                ''',
                'stats',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'egress-stats',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The interface index
                ''',
                'if_index',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address of the nexthop
                ''',
                'ipv4_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 Address of the nexthop
                ''',
                'ipv6_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the nexthop
                ''',
                'mac_address',
                'common-mpls-static', False),
            _MetaInfoClassMember('out-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface
                ''',
                'out_interface_name',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop-type',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'swap',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack',
            False, 
            [
            _MetaInfoClassMember('label-stack', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First label in the list is the top of the stack
                ''',
                'label_stack',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                    _MetaInfoClassMember('label-stack', REFERENCE_LEAFLIST, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        First label in the list is the top of the stack
                        ''',
                        'label_stack',
                        'common-mpls-static', False, min_elements=1),
                ], min_elements=1),
            ],
            'common-mpls-static',
            'stack',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push',
            False, 
            [
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack', 
                [], [], 
                '''                The label stack
                ''',
                'stack',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'push',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations',
            False, 
            [
            _MetaInfoClassMember('pop-and-forward', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Pop the incoming label and forward
                ''',
                'pop_and_forward',
                'common-mpls-static', False),
            _MetaInfoClassMember('preserve', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                preserve incoming label stack
                ''',
                'preserve',
                'common-mpls-static', False),
            _MetaInfoClassMember('push', REFERENCE_CLASS, 'Push' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'push',
                'common-mpls-static', False),
            _MetaInfoClassMember('swap', REFERENCE_CLASS, 'Swap' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap', 
                [], [], 
                '''                Push outgoing label stack
                ''',
                'swap',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'operations',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for byte count
                ''',
                'bytes',
                'common-mpls-static', False),
            _MetaInfoClassMember('dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for dropped-bytes
                ''',
                'dropped_bytes',
                'common-mpls-static', False),
            _MetaInfoClassMember('dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for dropped-packets
                ''',
                'dropped_packets',
                'common-mpls-static', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                stats for packet count
                ''',
                'packets',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'stats',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats',
            False, 
            [
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats', 
                [], [], 
                '''                Statistics
                ''',
                'stats',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'nexthop-stats',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop
                ''',
                'index',
                'common-mpls-static', True),
            _MetaInfoClassMember('next-hop-type', REFERENCE_CLASS, 'NextHopType' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType', 
                [], [], 
                '''                Next-hop
                ''',
                'next_hop_type',
                'common-mpls-static', False),
            _MetaInfoClassMember('nexthop-stats', REFERENCE_CLASS, 'NexthopStats' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats', 
                [], [], 
                '''                lsp stats
                ''',
                'nexthop_stats',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            _MetaInfoClassMember('origin', REFERENCE_IDENTITY_CLASS, 'NexthopResolutionTypeIdentity' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'NexthopResolutionTypeIdentity', 
                [], [], 
                '''                The origin of this nexthop
                ''',
                'origin',
                'common-mpls-static', False),
            _MetaInfoClassMember('protected-by', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of the nexthop that protects this nexthop
                ''',
                'protected_by',
                'common-mpls-static', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'HoptypeEnum' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'HoptypeEnum', 
                [], [], 
                '''                The forwarding path's hoptype
                ''',
                'type',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'next-hop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path',
            False, 
            [
            _MetaInfoClassMember('auto-protect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables automatic protection if true
                ''',
                'auto_protect',
                'common-mpls-static', False),
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop', 
                [], [], 
                '''                next-hops list
                ''',
                'next_hop',
                'common-mpls-static', False),
            _MetaInfoClassMember('operations', REFERENCE_CLASS, 'Operations' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations', 
                [], [], 
                '''                The incoming label processing
                ''',
                'operations',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'path',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the VRF
                ''',
                'vrf_name',
                'common-mpls-static', True),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP v4/v6 prefix
                ''',
                'prefix',
                'common-mpls-static', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        IP v4/v6 prefix
                        ''',
                        'prefix',
                        'common-mpls-static', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        IP v4/v6 prefix
                        ''',
                        'prefix',
                        'common-mpls-static', True),
                ]),
            _MetaInfoClassMember('egress-stats', REFERENCE_CLASS, 'EgressStats' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats', 
                [], [], 
                '''                egress stats
                ''',
                'egress_stats',
                'common-mpls-static', False),
            _MetaInfoClassMember('in-label-value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of the local label
                ''',
                'in_label_value',
                'common-mpls-static', False, [
                    _MetaInfoClassMember('in-label-value', ATTRIBUTE, 'int' , None, None, 
                        [('16', '1048575')], [], 
                        '''                        Value of the local label
                        ''',
                        'in_label_value',
                        'common-mpls-static', False),
                    _MetaInfoClassMember('in-label-value', REFERENCE_ENUM_CLASS, 'IetfMplsLabelEnum' , 'ydk.models.cisco_ios_xe.common_mpls_types', 'IetfMplsLabelEnum', 
                        [], [], 
                        '''                        Value of the local label
                        ''',
                        'in_label_value',
                        'common-mpls-static', False),
                ]),
            _MetaInfoClassMember('ingress-stats', REFERENCE_CLASS, 'IngressStats' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats', 
                [], [], 
                '''                ingress stats
                ''',
                'ingress_stats',
                'common-mpls-static', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the LSP
                ''',
                'name',
                'common-mpls-static', False),
            _MetaInfoClassMember('path', REFERENCE_CLASS, 'Path' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path', 
                [], [], 
                '''                Fowarding path
                ''',
                'path',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'label-switched-path',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState.LabelSwitchedPaths' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState.LabelSwitchedPaths',
            False, 
            [
            _MetaInfoClassMember('label-switched-path', REFERENCE_LIST, 'LabelSwitchedPath' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath', 
                [], [], 
                '''                MPLS LSPs list
                ''',
                'label_switched_path',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'label-switched-paths',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic.MplsStaticState' : {
        'meta_info' : _MetaInfoClass('MplsStatic.MplsStaticState',
            False, 
            [
            _MetaInfoClassMember('label-switched-paths', REFERENCE_CLASS, 'LabelSwitchedPaths' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState.LabelSwitchedPaths', 
                [], [], 
                '''                MPLS Static Label Switched Paths
                ''',
                'label_switched_paths',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'mpls-static-state',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'MplsStatic' : {
        'meta_info' : _MetaInfoClass('MplsStatic',
            False, 
            [
            _MetaInfoClassMember('mpls-static-cfg', REFERENCE_CLASS, 'MplsStaticCfg' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticCfg', 
                [], [], 
                '''                MPLS Static configuration commands
                ''',
                'mpls_static_cfg',
                'common-mpls-static', False),
            _MetaInfoClassMember('mpls-static-state', REFERENCE_CLASS, 'MplsStaticState' , 'ydk.models.cisco_ios_xe.common_mpls_static', 'MplsStatic.MplsStaticState', 
                [], [], 
                '''                MPLS static operational data
                ''',
                'mpls_static_state',
                'common-mpls-static', False),
            ],
            'common-mpls-static',
            'mpls-static',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'BgpRouteNexthopIdentity' : {
        'meta_info' : _MetaInfoClass('BgpRouteNexthopIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'bgp-route-nexthop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'LspVrfIdentity' : {
        'meta_info' : _MetaInfoClass('LspVrfIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'lsp-vrf',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'LspIpv4Identity' : {
        'meta_info' : _MetaInfoClass('LspIpv4Identity',
            False, 
            [
            ],
            'common-mpls-static',
            'lsp-IPv4',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'StaticNexthopIdentity' : {
        'meta_info' : _MetaInfoClass('StaticNexthopIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'static-nexthop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'IsisRouteNexthopIdentity' : {
        'meta_info' : _MetaInfoClass('IsisRouteNexthopIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'isis-route-nexthop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'LspIdentity' : {
        'meta_info' : _MetaInfoClass('LspIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'lsp',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'OspfRouteNexthopIdentity' : {
        'meta_info' : _MetaInfoClass('OspfRouteNexthopIdentity',
            False, 
            [
            ],
            'common-mpls-static',
            'ospf-route-nexthop',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
    'LspIpv6Identity' : {
        'meta_info' : _MetaInfoClass('LspIpv6Identity',
            False, 
            [
            ],
            'common-mpls-static',
            'lsp-IPv6',
            _yang_ns._namespaces['common-mpls-static'],
        'ydk.models.cisco_ios_xe.common_mpls_static'
        ),
    },
}
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.NextHopType']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path.NextHop']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp.Path']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps.InLabelLsp']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.NextHopType']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path.NextHop']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp.Path']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps.Ipv6IngressLsp']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.NextHopType']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path.NextHop']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp.Path']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps.NamedLsp']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.NamedLsps']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Interfaces.Interface']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Interfaces']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.NextHopType']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path.NextHop']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp.Path']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps.Ipv4IngressLsp']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.InLabelLsps']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv6IngressLsps']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.NamedLsps']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Interfaces']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg.Ipv4IngressLsps']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticCfg']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats.Stats']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats.Stats']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push.Stack']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Swap']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations.Push']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats.Stats']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NextHopType']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop.NexthopStats']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.Operations']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path.NextHop']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.IngressStats']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.EgressStats']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath.Path']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths.LabelSwitchedPath']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths']['meta_info']
_meta_table['MplsStatic.MplsStaticState.LabelSwitchedPaths']['meta_info'].parent =_meta_table['MplsStatic.MplsStaticState']['meta_info']
_meta_table['MplsStatic.MplsStaticCfg']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
_meta_table['MplsStatic.MplsStaticState']['meta_info'].parent =_meta_table['MplsStatic']['meta_info']
