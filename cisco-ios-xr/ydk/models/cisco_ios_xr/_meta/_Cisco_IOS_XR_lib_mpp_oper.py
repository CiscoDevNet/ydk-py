


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MppAllowEnum' : _MetaInfoEnum('MppAllowEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper',
        {
            'ssh':'ssh',
            'telnet':'telnet',
            'snmp':'snmp',
            'tftp':'tftp',
            'http':'http',
            'xr-xml':'xr_xml',
            'netconf':'netconf',
            'all':'all',
        }, 'Cisco-IOS-XR-lib-mpp-oper', _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper']),
    'MppAfIdBaseIdentity' : {
        'meta_info' : _MetaInfoClass('MppAfIdBaseIdentity',
            False, 
            [
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'Mpp-af-id-base',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Outband.Vrf' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outband VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'MppAfIdBaseIdentity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAfIdBaseIdentity', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'peer-address',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol',
            False, 
            [
            _MetaInfoClassMember('allow', REFERENCE_ENUM_CLASS, 'MppAllowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAllowEnum', 
                [], [], 
                '''                MPP allow
                ''',
                'allow',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('is-all-peers-allowed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, all peers are allowed
                ''',
                'is_all_peers_allowed',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('peer-address', REFERENCE_LIST, 'PeerAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress', 
                [], [], 
                '''                List of peer addresses
                ''',
                'peer_address',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name, specify 'all' for all
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-lib-mpp-oper', True),
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol', 
                [], [], 
                '''                MPP Interface protocols
                ''',
                'protocol',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Outband.Interfaces' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces.Interface', 
                [], [], 
                '''                MPP interface information
                ''',
                'interface',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Outband' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Outband',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Interfaces', 
                [], [], 
                '''                List of inband/outband interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('vrf', REFERENCE_CLASS, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband.Vrf', 
                [], [], 
                '''                Outband VRF information
                ''',
                'vrf',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'outband',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_IDENTITY_CLASS, 'MppAfIdBaseIdentity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAfIdBaseIdentity', 
                [], [], 
                '''                AFName
                ''',
                'af_name',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'peer-address',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol',
            False, 
            [
            _MetaInfoClassMember('allow', REFERENCE_ENUM_CLASS, 'MppAllowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'MppAllowEnum', 
                [], [], 
                '''                MPP allow
                ''',
                'allow',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('is-all-peers-allowed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, all peers are allowed
                ''',
                'is_all_peers_allowed',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('peer-address', REFERENCE_LIST, 'PeerAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress', 
                [], [], 
                '''                List of peer addresses
                ''',
                'peer_address',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'protocol',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name, specify 'all' for all
                interfaces
                ''',
                'interface_name',
                'Cisco-IOS-XR-lib-mpp-oper', True),
            _MetaInfoClassMember('protocol', REFERENCE_LIST, 'Protocol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol', 
                [], [], 
                '''                MPP Interface protocols
                ''',
                'protocol',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Inband.Interfaces' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces.Interface', 
                [], [], 
                '''                MPP interface information
                ''',
                'interface',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection.Inband' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection.Inband',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband.Interfaces', 
                [], [], 
                '''                List of inband/outband interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'inband',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'ManagementPlaneProtection' : {
        'meta_info' : _MetaInfoClass('ManagementPlaneProtection',
            False, 
            [
            _MetaInfoClassMember('inband', REFERENCE_CLASS, 'Inband' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Inband', 
                [], [], 
                '''                Management Plane Protection (MPP) inband
                interface data
                ''',
                'inband',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            _MetaInfoClassMember('outband', REFERENCE_CLASS, 'Outband' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper', 'ManagementPlaneProtection.Outband', 
                [], [], 
                '''                Management Plane Protection (MPP) outband
                interface data
                ''',
                'outband',
                'Cisco-IOS-XR-lib-mpp-oper', False),
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'management-plane-protection',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'Ipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4Identity',
            False, 
            [
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
    'Ipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6Identity',
            False, 
            [
            ],
            'Cisco-IOS-XR-lib-mpp-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-lib-mpp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_mpp_oper'
        ),
    },
}
_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol.PeerAddress']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface.Protocol']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Interfaces.Interface']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband.Interfaces']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Vrf']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband']['meta_info']
_meta_table['ManagementPlaneProtection.Outband.Interfaces']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Outband']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol.PeerAddress']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface.Protocol']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces.Interface']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband.Interfaces']['meta_info']
_meta_table['ManagementPlaneProtection.Inband.Interfaces']['meta_info'].parent =_meta_table['ManagementPlaneProtection.Inband']['meta_info']
_meta_table['ManagementPlaneProtection.Outband']['meta_info'].parent =_meta_table['ManagementPlaneProtection']['meta_info']
_meta_table['ManagementPlaneProtection.Inband']['meta_info'].parent =_meta_table['ManagementPlaneProtection']['meta_info']
