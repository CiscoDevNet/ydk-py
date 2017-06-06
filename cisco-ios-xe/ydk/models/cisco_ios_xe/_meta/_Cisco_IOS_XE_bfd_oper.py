


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BfdRemoteStateTypeEnum' : _MetaInfoEnum('BfdRemoteStateTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper',
        {
            'up':'up',
            'down':'down',
            'init':'init',
            'admindown':'admindown',
            'invalid':'invalid',
        }, 'Cisco-IOS-XE-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper']),
    'BfdOperSessionTypeEnum' : _MetaInfoEnum('BfdOperSessionTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'vccv':'vccv',
            'mpls-tp':'mpls_tp',
            'ipv4-multihop':'ipv4_multihop',
            'ipv6-multihop':'ipv6_multihop',
        }, 'Cisco-IOS-XE-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper']),
    'BfdStateTypeEnum' : _MetaInfoEnum('BfdStateTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper',
        {
            'admindown':'admindown',
            'down':'down',
            'fail':'fail',
            'init':'init',
            'up':'up',
            'invalid':'invalid',
        }, 'Cisco-IOS-XE-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper']),
    'BfdLspTypeEnum' : _MetaInfoEnum('BfdLspTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper',
        {
            'working':'working',
            'protect':'protect',
            'unknown':'unknown',
        }, 'Cisco-IOS-XE-bfd-oper', _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper']),
    'BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XE-bfd-oper', True),
            _MetaInfoClassMember('lsp-type', REFERENCE_ENUM_CLASS, 'BfdLspTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdLspTypeEnum', 
                [], [], 
                '''                ''',
                'lsp_type',
                'Cisco-IOS-XE-bfd-oper', True),
            _MetaInfoClassMember('ld', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local-discriminator
                ''',
                'ld',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('rd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote-discriminator
                ''',
                'rd',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('remote-state', REFERENCE_ENUM_CLASS, 'BfdRemoteStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdRemoteStateTypeEnum', 
                [], [], 
                '''                 Remote Heard. RH state of BFD version '0' 
                 is also mapped to up/down. 
                ''',
                'remote_state',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdStateTypeEnum', 
                [], [], 
                '''                BFD state
                ''',
                'state',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-tunnel-path',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdTunnelPaths' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdTunnelPaths',
            False, 
            [
            _MetaInfoClassMember('bfd-tunnel-path', REFERENCE_LIST, 'BfdTunnelPath' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath', 
                [], [], 
                '''                Tunnel Path
                ''',
                'bfd_tunnel_path',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-tunnel-paths',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdCircuits.BfdCircuit' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdCircuits.BfdCircuit',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XE-bfd-oper', True),
            _MetaInfoClassMember('vcid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'vcid',
                'Cisco-IOS-XE-bfd-oper', True),
            _MetaInfoClassMember('ld', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local-discriminator
                ''',
                'ld',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('rd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote-discriminator
                ''',
                'rd',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('remote-state', REFERENCE_ENUM_CLASS, 'BfdRemoteStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdRemoteStateTypeEnum', 
                [], [], 
                '''                 Remote Heard. RH state of BFD version '0' 
                 is also mapped to up/down. 
                ''',
                'remote_state',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdStateTypeEnum', 
                [], [], 
                '''                BFD state
                ''',
                'state',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-circuit',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdCircuits' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdCircuits',
            False, 
            [
            _MetaInfoClassMember('bfd-circuit', REFERENCE_LIST, 'BfdCircuit' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdCircuits.BfdCircuit', 
                [], [], 
                '''                BFD circuit
                ''',
                'bfd_circuit',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-circuits',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdNbrs.BfdNbr' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdNbrs.BfdNbr',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'Cisco-IOS-XE-bfd-oper', True, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-bfd-oper', True),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-bfd-oper', True),
                ]),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XE-bfd-oper', True),
            _MetaInfoClassMember('ld', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local-discriminator
                ''',
                'ld',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('rd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote-discriminator
                ''',
                'rd',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('remote-state', REFERENCE_ENUM_CLASS, 'BfdRemoteStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdRemoteStateTypeEnum', 
                [], [], 
                '''                 Remote Heard. RH state of BFD version '0' 
                 is also mapped to up/down. 
                ''',
                'remote_state',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdStateTypeEnum', 
                [], [], 
                '''                BFD state
                ''',
                'state',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-nbr',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdNbrs' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdNbrs',
            False, 
            [
            _MetaInfoClassMember('bfd-nbr', REFERENCE_LIST, 'BfdNbr' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdNbrs.BfdNbr', 
                [], [], 
                '''                This is for directly connected neighbor case
                ''',
                'bfd_nbr',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-nbrs',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'Cisco-IOS-XE-bfd-oper', True, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-bfd-oper', True),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-bfd-oper', True),
                ]),
            _MetaInfoClassMember('ld', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local-discriminator
                ''',
                'ld',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('rd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote-discriminator
                ''',
                'rd',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('remote-state', REFERENCE_ENUM_CLASS, 'BfdRemoteStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdRemoteStateTypeEnum', 
                [], [], 
                '''                 Remote Heard. RH state of BFD version '0' 
                 is also mapped to up/down. 
                ''',
                'remote_state',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdStateTypeEnum', 
                [], [], 
                '''                BFD state
                ''',
                'state',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-mhop-nbr',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdMhopNbrs' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdMhopNbrs',
            False, 
            [
            _MetaInfoClassMember('bfd-mhop-nbr', REFERENCE_LIST, 'BfdMhopNbr' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr', 
                [], [], 
                '''                This is for multi hop neighbor scenario 
                for global VRF (no VRF).
                ''',
                'bfd_mhop_nbr',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-mhop-nbrs',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                ''',
                'ip',
                'Cisco-IOS-XE-bfd-oper', True, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-bfd-oper', True),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        ''',
                        'ip',
                        'Cisco-IOS-XE-bfd-oper', True),
                ]),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'vrf',
                'Cisco-IOS-XE-bfd-oper', True),
            _MetaInfoClassMember('ld', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                local-discriminator
                ''',
                'ld',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('rd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                remote-discriminator
                ''',
                'rd',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('remote-state', REFERENCE_ENUM_CLASS, 'BfdRemoteStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdRemoteStateTypeEnum', 
                [], [], 
                '''                 Remote Heard. RH state of BFD version '0' 
                 is also mapped to up/down. 
                ''',
                'remote_state',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'BfdStateTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdStateTypeEnum', 
                [], [], 
                '''                BFD state
                ''',
                'state',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-mhop-vrf-nbr',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session.BfdMhopVrfNbrs' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session.BfdMhopVrfNbrs',
            False, 
            [
            _MetaInfoClassMember('bfd-mhop-vrf-nbr', REFERENCE_LIST, 'BfdMhopVrfNbr' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr', 
                [], [], 
                '''                This is for multi hop neighbor scenario 
                for non-global VRF.
                ''',
                'bfd_mhop_vrf_nbr',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-mhop-vrf-nbrs',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BfdOperSessionTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdOperSessionTypeEnum', 
                [], [], 
                '''                Session type
                ''',
                'type',
                'Cisco-IOS-XE-bfd-oper', True),
            _MetaInfoClassMember('bfd-circuits', REFERENCE_CLASS, 'BfdCircuits' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdCircuits', 
                [], [], 
                '''                ''',
                'bfd_circuits',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('bfd-mhop-nbrs', REFERENCE_CLASS, 'BfdMhopNbrs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdMhopNbrs', 
                [], [], 
                '''                ''',
                'bfd_mhop_nbrs',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('bfd-mhop-vrf-nbrs', REFERENCE_CLASS, 'BfdMhopVrfNbrs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdMhopVrfNbrs', 
                [], [], 
                '''                ''',
                'bfd_mhop_vrf_nbrs',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('bfd-nbrs', REFERENCE_CLASS, 'BfdNbrs' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdNbrs', 
                [], [], 
                '''                ''',
                'bfd_nbrs',
                'Cisco-IOS-XE-bfd-oper', False),
            _MetaInfoClassMember('bfd-tunnel-paths', REFERENCE_CLASS, 'BfdTunnelPaths' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session.BfdTunnelPaths', 
                [], [], 
                '''                ''',
                'bfd_tunnel_paths',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState.Sessions' : {
        'meta_info' : _MetaInfoClass('BfdState.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions.Session', 
                [], [], 
                '''                ''',
                'session',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
    'BfdState' : {
        'meta_info' : _MetaInfoClass('BfdState',
            False, 
            [
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper', 'BfdState.Sessions', 
                [], [], 
                '''                ''',
                'sessions',
                'Cisco-IOS-XE-bfd-oper', False),
            ],
            'Cisco-IOS-XE-bfd-oper',
            'bfd-state',
            _yang_ns._namespaces['Cisco-IOS-XE-bfd-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_bfd_oper'
        ),
    },
}
_meta_table['BfdState.Sessions.Session.BfdTunnelPaths.BfdTunnelPath']['meta_info'].parent =_meta_table['BfdState.Sessions.Session.BfdTunnelPaths']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdCircuits.BfdCircuit']['meta_info'].parent =_meta_table['BfdState.Sessions.Session.BfdCircuits']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdNbrs.BfdNbr']['meta_info'].parent =_meta_table['BfdState.Sessions.Session.BfdNbrs']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdMhopNbrs.BfdMhopNbr']['meta_info'].parent =_meta_table['BfdState.Sessions.Session.BfdMhopNbrs']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdMhopVrfNbrs.BfdMhopVrfNbr']['meta_info'].parent =_meta_table['BfdState.Sessions.Session.BfdMhopVrfNbrs']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdTunnelPaths']['meta_info'].parent =_meta_table['BfdState.Sessions.Session']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdCircuits']['meta_info'].parent =_meta_table['BfdState.Sessions.Session']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdNbrs']['meta_info'].parent =_meta_table['BfdState.Sessions.Session']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdMhopNbrs']['meta_info'].parent =_meta_table['BfdState.Sessions.Session']['meta_info']
_meta_table['BfdState.Sessions.Session.BfdMhopVrfNbrs']['meta_info'].parent =_meta_table['BfdState.Sessions.Session']['meta_info']
_meta_table['BfdState.Sessions.Session']['meta_info'].parent =_meta_table['BfdState.Sessions']['meta_info']
_meta_table['BfdState.Sessions']['meta_info'].parent =_meta_table['BfdState']['meta_info']
