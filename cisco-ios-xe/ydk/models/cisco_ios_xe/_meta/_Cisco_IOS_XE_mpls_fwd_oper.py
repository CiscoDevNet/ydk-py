


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId' : {
        'meta_info' : _MetaInfoClass('MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId',
            False, 
            [
            _MetaInfoClassMember('global', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'global_',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('node', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'node',
                'Cisco-IOS-XE-mpls-fwd-oper', False, [
                    _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'node',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                    _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'node',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-fwd-oper',
            'src-id',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper'
        ),
    },
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId' : {
        'meta_info' : _MetaInfoClass('MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId',
            False, 
            [
            _MetaInfoClassMember('global', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'global_',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('node', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'node',
                'Cisco-IOS-XE-mpls-fwd-oper', False, [
                    _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'node',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                    _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'node',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-fwd-oper',
            'dst-id',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper'
        ),
    },
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp' : {
        'meta_info' : _MetaInfoClass('MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp',
            False, 
            [
            _MetaInfoClassMember('dst-id', REFERENCE_CLASS, 'DstId' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId', 
                [], [], 
                '''                ''',
                'dst_id',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('src-id', REFERENCE_CLASS, 'SrcId' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId', 
                [], [], 
                '''                ''',
                'src_id',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('tunnel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'tunnel',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            ],
            'Cisco-IOS-XE-mpls-fwd-oper',
            'tunnel-tp',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper'
        ),
    },
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TypeEnum' : _MetaInfoEnum('TypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper',
        {
            'ip':'ip',
            'tunnel':'tunnel',
            'nh-id':'nh_id',
            'l2ckt':'l2ckt',
            'ip-vrf':'ip_vrf',
            'none':'none',
            'tunnel-tp':'tunnel_tp',
        }, 'Cisco-IOS-XE-mpls-fwd-oper', _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper']),
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo' : {
        'meta_info' : _MetaInfoClass('MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'Cisco-IOS-XE-mpls-fwd-oper', False, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                ]),
            _MetaInfoClassMember('l2ckt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'l2ckt_id',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'mask',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('nh-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'nh_id',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'tunnel_id',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('tunnel-tp', REFERENCE_CLASS, 'TunnelTp' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp', 
                [], [], 
                '''                ''',
                'tunnel_tp',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TypeEnum', 
                [], [], 
                '''                The type of connection represented by this label
                ''',
                'type',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'vrf_id',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            ],
            'Cisco-IOS-XE-mpls-fwd-oper',
            'connection-info',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper'
        ),
    },
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.NextHopEnum' : _MetaInfoEnum('NextHopEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper',
        {
            'point2point':'point2point',
        }, 'Cisco-IOS-XE-mpls-fwd-oper', _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper']),
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingInterfaceEnum' : _MetaInfoEnum('OutgoingInterfaceEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper',
        {
            'drop':'drop',
            'punt':'punt',
            'aggregate':'aggregate',
            'exception':'exception',
            'none':'none',
        }, 'Cisco-IOS-XE-mpls-fwd-oper', _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper']),
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingLabelEnum' : _MetaInfoEnum('OutgoingLabelEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper',
        {
            'no-label':'no_label',
            'pop-label':'pop_label',
            'aggregate':'aggregate',
            'explicit-null':'explicit_null',
            'illegal':'illegal',
        }, 'Cisco-IOS-XE-mpls-fwd-oper', _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper']),
    'MplsForwardingTable.LocalLabelEntry.ForwardingInfo' : {
        'meta_info' : _MetaInfoClass('MplsForwardingTable.LocalLabelEntry.ForwardingInfo',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The name of the outgoing interface.
                Example possible values are 1.none, 2.drop, 3.<tunnel-name>,
                4.<interface-name>, 5.aggregate/<vrf-name> etc.
                ''',
                'outgoing_interface',
                'Cisco-IOS-XE-mpls-fwd-oper', True, [
                    _MetaInfoClassMember('outgoing-interface', REFERENCE_ENUM_CLASS, 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingInterfaceEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingInterfaceEnum', 
                        [], [], 
                        '''                        The name of the outgoing interface.
                        Example possible values are 1.none, 2.drop, 3.<tunnel-name>,
                        4.<interface-name>, 5.aggregate/<vrf-name> etc.
                        ''',
                        'outgoing_interface',
                        'Cisco-IOS-XE-mpls-fwd-oper', True),
                    _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        The name of the outgoing interface.
                        Example possible values are 1.none, 2.drop, 3.<tunnel-name>,
                        4.<interface-name>, 5.aggregate/<vrf-name> etc.
                        ''',
                        'outgoing_interface',
                        'Cisco-IOS-XE-mpls-fwd-oper', True),
                ]),
            _MetaInfoClassMember('connection-info', REFERENCE_CLASS, 'ConnectionInfo' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo', 
                [], [], 
                '''                The Prefix or tunnel-id info corresponding to this label.
                Ex: 1) for l2ckt, a number tunnel-id value.
                2) for ipv4, a prefix with [V] tag (113.113.113.113/32[V]).
                3) for TE, a pefix with [T] tag (113.113.113.113/32[T])
                ''',
                'connection_info',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('label-switched-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of bytes switched using this label.
                ''',
                'label_switched_bytes',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Next hop information.
                Example possible values are
                1.point2point,
                2.<ip-address>
                ''',
                'next_hop',
                'Cisco-IOS-XE-mpls-fwd-oper', False, [
                    _MetaInfoClassMember('next-hop', REFERENCE_ENUM_CLASS, 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.NextHopEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.NextHopEnum', 
                        [], [], 
                        '''                        Next hop information.
                        Example possible values are
                        1.point2point,
                        2.<ip-address>
                        ''',
                        'next_hop',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                    _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Next hop information.
                        Example possible values are
                        1.point2point,
                        2.<ip-address>
                        ''',
                        'next_hop',
                        'Cisco-IOS-XE-mpls-fwd-oper', False, [
                            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Next hop information.
                                Example possible values are
                                1.point2point,
                                2.<ip-address>
                                ''',
                                'next_hop',
                                'Cisco-IOS-XE-mpls-fwd-oper', False),
                            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Next hop information.
                                Example possible values are
                                1.point2point,
                                2.<ip-address>
                                ''',
                                'next_hop',
                                'Cisco-IOS-XE-mpls-fwd-oper', False),
                        ]),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                        '''                        Next hop information.
                        Example possible values are
                        1.point2point,
                        2.<ip-address>
                        ''',
                        'next_hop',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                ]),
            _MetaInfoClassMember('outgoing-label', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Value of outgoing-label if exists or
                the type of non-present label.
                ''',
                'outgoing_label',
                'Cisco-IOS-XE-mpls-fwd-oper', False, [
                    _MetaInfoClassMember('outgoing-label', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Value of outgoing-label if exists or
                        the type of non-present label.
                        ''',
                        'outgoing_label',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                    _MetaInfoClassMember('outgoing-label', REFERENCE_ENUM_CLASS, 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingLabelEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo.OutgoingLabelEnum', 
                        [], [], 
                        '''                        Value of outgoing-label if exists or
                        the type of non-present label.
                        ''',
                        'outgoing_label',
                        'Cisco-IOS-XE-mpls-fwd-oper', False),
                ]),
            ],
            'Cisco-IOS-XE-mpls-fwd-oper',
            'forwarding-info',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper'
        ),
    },
    'MplsForwardingTable.LocalLabelEntry' : {
        'meta_info' : _MetaInfoClass('MplsForwardingTable.LocalLabelEntry',
            False, 
            [
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value of local-label.
                ''',
                'local_label',
                'Cisco-IOS-XE-mpls-fwd-oper', True),
            _MetaInfoClassMember('forwarding-info', REFERENCE_LIST, 'ForwardingInfo' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry.ForwardingInfo', 
                [], [], 
                '''                ''',
                'forwarding_info',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            ],
            'Cisco-IOS-XE-mpls-fwd-oper',
            'local-label-entry',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper'
        ),
    },
    'MplsForwardingTable' : {
        'meta_info' : _MetaInfoClass('MplsForwardingTable',
            False, 
            [
            _MetaInfoClassMember('local-label-entry', REFERENCE_LIST, 'LocalLabelEntry' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper', 'MplsForwardingTable.LocalLabelEntry', 
                [], [], 
                '''                The list of MPLS forwarding table entries.
                ''',
                'local_label_entry',
                'Cisco-IOS-XE-mpls-fwd-oper', False),
            ],
            'Cisco-IOS-XE-mpls-fwd-oper',
            'mpls-forwarding-table',
            _yang_ns._namespaces['Cisco-IOS-XE-mpls-fwd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_mpls_fwd_oper'
        ),
    },
}
_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.SrcId']['meta_info'].parent =_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp']['meta_info']
_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp.DstId']['meta_info'].parent =_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp']['meta_info']
_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo.TunnelTp']['meta_info'].parent =_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo']['meta_info']
_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo.ConnectionInfo']['meta_info'].parent =_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo']['meta_info']
_meta_table['MplsForwardingTable.LocalLabelEntry.ForwardingInfo']['meta_info'].parent =_meta_table['MplsForwardingTable.LocalLabelEntry']['meta_info']
_meta_table['MplsForwardingTable.LocalLabelEntry']['meta_info'].parent =_meta_table['MplsForwardingTable']['meta_info']
