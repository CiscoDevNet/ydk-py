


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'http-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'tftp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'netconf-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'xr-xml',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'ssh-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'snmp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'telnet-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'all-protocols',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-lib-mpp-cfg', True),
            _MetaInfoClassMember('all-protocols', REFERENCE_CLASS, 'AllProtocols' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols', 
                [], [], 
                '''                Configure all protocols on this interface
                ''',
                'all_protocols',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('http-protocol', REFERENCE_CLASS, 'HttpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol', 
                [], [], 
                '''                Configure HTTP on this interface
                ''',
                'http_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('netconf-protocol', REFERENCE_CLASS, 'NetconfProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol', 
                [], [], 
                '''                Configure NETCONF protocol and peer addresses
                ''',
                'netconf_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('snmp-protocol', REFERENCE_CLASS, 'SnmpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol', 
                [], [], 
                '''                Configure SNMP for this interface
                ''',
                'snmp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('ssh-protocol', REFERENCE_CLASS, 'SshProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol', 
                [], [], 
                '''                Configure SSH protocol and peer addresses
                ''',
                'ssh_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('telnet-protocol', REFERENCE_CLASS, 'TelnetProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol', 
                [], [], 
                '''                Configure Telnet for this interface
                ''',
                'telnet_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('tftp-protocol', REFERENCE_CLASS, 'TftpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol', 
                [], [], 
                '''                Configure TFTP on this interface
                ''',
                'tftp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('xr-xml', REFERENCE_CLASS, 'XrXml' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml', 
                [], [], 
                '''                Configure XML and peer addresses
                ''',
                'xr_xml',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface', 
                [], [], 
                '''                Specific interface
                ''',
                'interface',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'http-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'tftp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'netconf-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'xr-xml',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'ssh-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'snmp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'telnet-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'all-protocols',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces',
            False, 
            [
            _MetaInfoClassMember('all-protocols', REFERENCE_CLASS, 'AllProtocols' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols', 
                [], [], 
                '''                Configure all protocols on this interface
                ''',
                'all_protocols',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('http-protocol', REFERENCE_CLASS, 'HttpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol', 
                [], [], 
                '''                Configure HTTP on this interface
                ''',
                'http_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('netconf-protocol', REFERENCE_CLASS, 'NetconfProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol', 
                [], [], 
                '''                Configure NETCONF protocol and peer addresses
                ''',
                'netconf_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('snmp-protocol', REFERENCE_CLASS, 'SnmpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol', 
                [], [], 
                '''                Configure SNMP for this interface
                ''',
                'snmp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('ssh-protocol', REFERENCE_CLASS, 'SshProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol', 
                [], [], 
                '''                Configure SSH protocol and peer addresses
                ''',
                'ssh_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('telnet-protocol', REFERENCE_CLASS, 'TelnetProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol', 
                [], [], 
                '''                Configure Telnet for this interface
                ''',
                'telnet_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('tftp-protocol', REFERENCE_CLASS, 'TftpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol', 
                [], [], 
                '''                Configure TFTP on this interface
                ''',
                'tftp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('xr-xml', REFERENCE_CLASS, 'XrXml' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml', 
                [], [], 
                '''                Configure XML and peer addresses
                ''',
                'xr_xml',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'all-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection',
            False, 
            [
            _MetaInfoClassMember('all-interfaces', REFERENCE_CLASS, 'AllInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces', 
                [], [], 
                '''                Configure all Inband interfaces
                ''',
                'all_interfaces',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces', 
                [], [], 
                '''                Configure a specific interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'interface-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Outband' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Outband',
            False, 
            [
            _MetaInfoClassMember('interface-selection', REFERENCE_CLASS, 'InterfaceSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection', 
                [], [], 
                '''                Configure interfaces
                ''',
                'interface_selection',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('outband-vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure outband VRF
                ''',
                'outband_vrf',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'outband',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'http-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'tftp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'netconf-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'xr-xml',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'ssh-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'snmp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'telnet-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'all-protocols',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-lib-mpp-cfg', True),
            _MetaInfoClassMember('all-protocols', REFERENCE_CLASS, 'AllProtocols' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols', 
                [], [], 
                '''                Configure all protocols on this interface
                ''',
                'all_protocols',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('http-protocol', REFERENCE_CLASS, 'HttpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol', 
                [], [], 
                '''                Configure HTTP on this interface
                ''',
                'http_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('netconf-protocol', REFERENCE_CLASS, 'NetconfProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol', 
                [], [], 
                '''                Configure NETCONF protocol and peer addresses
                ''',
                'netconf_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('snmp-protocol', REFERENCE_CLASS, 'SnmpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol', 
                [], [], 
                '''                Configure SNMP for this interface
                ''',
                'snmp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('ssh-protocol', REFERENCE_CLASS, 'SshProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol', 
                [], [], 
                '''                Configure SSH protocol and peer addresses
                ''',
                'ssh_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('telnet-protocol', REFERENCE_CLASS, 'TelnetProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol', 
                [], [], 
                '''                Configure Telnet for this interface
                ''',
                'telnet_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('tftp-protocol', REFERENCE_CLASS, 'TftpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol', 
                [], [], 
                '''                Configure TFTP on this interface
                ''',
                'tftp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('xr-xml', REFERENCE_CLASS, 'XrXml' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml', 
                [], [], 
                '''                Configure XML and peer addresses
                ''',
                'xr_xml',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface', 
                [], [], 
                '''                Specific interface
                ''',
                'interface',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'http-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'tftp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'netconf-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'xr-xml',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'ssh-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'snmp-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'telnet-protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix
                ''',
                'address',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        prefix
                        ''',
                        'address',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer', 
                [], [], 
                '''                Configure peer on the interface
                ''',
                'peer',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix',
            False, 
            [
            _MetaInfoClassMember('address-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                prefix/length
                ''',
                'address_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', True, [
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                    _MetaInfoClassMember('address-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        prefix/length
                        ''',
                        'address_prefix',
                        'Cisco-IOS-XR-lib-mpp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes',
            False, 
            [
            _MetaInfoClassMember('peer-prefix', REFERENCE_LIST, 'PeerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix', 
                [], [], 
                '''                Peer address (with prefix)
                ''',
                'peer_prefix',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6',
            False, 
            [
            _MetaInfoClassMember('peer-prefixes', REFERENCE_CLASS, 'PeerPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes', 
                [], [], 
                '''                Configure peer addresses with prefix
                ''',
                'peer_prefixes',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peers',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass',
            False, 
            [
            _MetaInfoClassMember('peer-all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only takes 'True'
                ''',
                'peer_all',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v4', REFERENCE_CLASS, 'PeerV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4', 
                [], [], 
                '''                Configure v4 peer addresses
                ''',
                'peer_v4',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('peer-v6', REFERENCE_CLASS, 'PeerV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6', 
                [], [], 
                '''                Configure v6 peer addresses
                ''',
                'peer_v6',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'peer-class',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols',
            False, 
            [
            _MetaInfoClassMember('peer-class', REFERENCE_CLASS, 'PeerClass' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass', 
                [], [], 
                '''                Configure peer addresses
                ''',
                'peer_class',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'all-protocols',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces',
            False, 
            [
            _MetaInfoClassMember('all-protocols', REFERENCE_CLASS, 'AllProtocols' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols', 
                [], [], 
                '''                Configure all protocols on this interface
                ''',
                'all_protocols',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('http-protocol', REFERENCE_CLASS, 'HttpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol', 
                [], [], 
                '''                Configure HTTP on this interface
                ''',
                'http_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('netconf-protocol', REFERENCE_CLASS, 'NetconfProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol', 
                [], [], 
                '''                Configure NETCONF protocol and peer addresses
                ''',
                'netconf_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('snmp-protocol', REFERENCE_CLASS, 'SnmpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol', 
                [], [], 
                '''                Configure SNMP for this interface
                ''',
                'snmp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('ssh-protocol', REFERENCE_CLASS, 'SshProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol', 
                [], [], 
                '''                Configure SSH protocol and peer addresses
                ''',
                'ssh_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('telnet-protocol', REFERENCE_CLASS, 'TelnetProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol', 
                [], [], 
                '''                Configure Telnet for this interface
                ''',
                'telnet_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('tftp-protocol', REFERENCE_CLASS, 'TftpProtocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol', 
                [], [], 
                '''                Configure TFTP on this interface
                ''',
                'tftp_protocol',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('xr-xml', REFERENCE_CLASS, 'XrXml' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml', 
                [], [], 
                '''                Configure XML and peer addresses
                ''',
                'xr_xml',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'all-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection',
            False, 
            [
            _MetaInfoClassMember('all-interfaces', REFERENCE_CLASS, 'AllInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces', 
                [], [], 
                '''                Configure all Inband interfaces
                ''',
                'all_interfaces',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces', 
                [], [], 
                '''                Configure a specific interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'interface-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection.Inband' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection.Inband',
            False, 
            [
            _MetaInfoClassMember('interface-selection', REFERENCE_CLASS, 'InterfaceSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection', 
                [], [], 
                '''                Configure interfaces
                ''',
                'interface_selection',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'inband',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane.ManagementPlaneProtection' : {
        'meta_info' : _MetaInfoClass('ControlPlane.ManagementPlaneProtection',
            False, 
            [
            _MetaInfoClassMember('inband', REFERENCE_CLASS, 'Inband' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Inband', 
                [], [], 
                '''                Inband Configuration
                ''',
                'inband',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            _MetaInfoClassMember('outband', REFERENCE_CLASS, 'Outband' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection.Outband', 
                [], [], 
                '''                Outband Configuration
                ''',
                'outband',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'management-plane-protection',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
    'ControlPlane' : {
        'meta_info' : _MetaInfoClass('ControlPlane',
            False, 
            [
            _MetaInfoClassMember('management-plane-protection', REFERENCE_CLASS, 'ManagementPlaneProtection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg', 'ControlPlane.ManagementPlaneProtection', 
                [], [], 
                '''                Configure management plane protection
                ''',
                'management_plane_protection',
                'Cisco-IOS-XR-lib-mpp-cfg', False),
            ],
            'Cisco-IOS-XR-lib-mpp-cfg',
            'control-plane',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_cfg'
        ),
    },
}
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.HttpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TftpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.NetconfProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.XrXml']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SshProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.SnmpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.TelnetProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface.AllProtocols']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces.Interface']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.HttpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TftpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.NetconfProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.XrXml']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SshProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.SnmpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.TelnetProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces.AllProtocols']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.Interfaces']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection.AllInterfaces']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband.InterfaceSelection']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Outband']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.HttpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TftpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.NetconfProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.XrXml']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SshProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.SnmpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.TelnetProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface.AllProtocols']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces.Interface']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers.Peer']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes.PeerPrefix']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.Peers']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6.PeerPrefixes']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV4']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass.PeerV6']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols.PeerClass']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.HttpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TftpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.NetconfProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.XrXml']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SshProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.SnmpProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.TelnetProtocol']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces.AllProtocols']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.Interfaces']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection.AllInterfaces']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband.InterfaceSelection']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection.Inband']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Outband']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection.Inband']['meta_info'].parent =_meta_table['ControlPlane.ManagementPlaneProtection']['meta_info']
_meta_table['ControlPlane.ManagementPlaneProtection']['meta_info'].parent =_meta_table['ControlPlane']['meta_info']
