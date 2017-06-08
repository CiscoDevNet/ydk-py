


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ControlPlaneProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ControlPlaneProtocolTypeIdentity',
            False, 
            [
            ],
            'example-network-device',
            'control-plane-protocol-type',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'OamServiceTypeIdentity' : {
        'meta_info' : _MetaInfoClass('OamServiceTypeIdentity',
            False, 
            [
            ],
            'example-network-device',
            'oam-service-type',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'NetworkServiceTypeIdentity' : {
        'meta_info' : _MetaInfoClass('NetworkServiceTypeIdentity',
            False, 
            [
            ],
            'example-network-device',
            'network-service-type',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'MplsLspTypeIdentity' : {
        'meta_info' : _MetaInfoClass('MplsLspTypeIdentity',
            False, 
            [
            ],
            'example-network-device',
            'mpls-lsp-type',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'SystemManagementProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('SystemManagementProtocolTypeIdentity',
            False, 
            [
            ],
            'example-network-device',
            'system-management-protocol-type',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'OamProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('OamProtocolTypeIdentity',
            False, 
            [
            ],
            'example-network-device',
            'oam-protocol-type',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'IetfYangLibrary' : {
        'meta_info' : _MetaInfoClass('IetfYangLibrary',
            False, 
            [
            ],
            'example-network-device',
            'ietf-yang-library',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Interfaces' : {
        'meta_info' : _MetaInfoClass('Interfaces',
            False, 
            [
            ],
            'example-network-device',
            'interfaces',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Hardware' : {
        'meta_info' : _MetaInfoClass('Hardware',
            False, 
            [
            ],
            'example-network-device',
            'hardware',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Qos' : {
        'meta_info' : _MetaInfoClass('Qos',
            False, 
            [
            ],
            'example-network-device',
            'qos',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'SystemManagement.SystemManagementGlobal' : {
        'meta_info' : _MetaInfoClass('SystemManagement.SystemManagementGlobal',
            False, 
            [
            ],
            'example-network-device',
            'system-management-global',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'SystemManagement.SystemManagementProtocol' : {
        'meta_info' : _MetaInfoClass('SystemManagement.SystemManagementProtocol',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'SystemManagementProtocolTypeIdentity' , 'ydk.models.ietf.example_network_device', 'SystemManagementProtocolTypeIdentity', 
                [], [], 
                '''                Syslog, ssh, TACAC+, SNMP, NETCONF, etc.
                ''',
                'type',
                'example-network-device', True),
            ],
            'example-network-device',
            'system-management-protocol',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'SystemManagement' : {
        'meta_info' : _MetaInfoClass('SystemManagement',
            False, 
            [
            _MetaInfoClassMember('system-management-global', REFERENCE_CLASS, 'SystemManagementGlobal' , 'ydk.models.ietf.example_network_device', 'SystemManagement.SystemManagementGlobal', 
                [], [], 
                '''                System management - with reuse of RFC 7317
                ''',
                'system_management_global',
                'example-network-device', False),
            _MetaInfoClassMember('system-management-protocol', REFERENCE_LIST, 'SystemManagementProtocol' , 'ydk.models.ietf.example_network_device', 'SystemManagement.SystemManagementProtocol', 
                [], [], 
                '''                List of system management protocol
                configured for a logical network
                element.
                ''',
                'system_management_protocol',
                'example-network-device', False),
            ],
            'example-network-device',
            'system-management',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'NetworkServices.NetworkService' : {
        'meta_info' : _MetaInfoClass('NetworkServices.NetworkService',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'NetworkServiceTypeIdentity' , 'ydk.models.ietf.example_network_device', 'NetworkServiceTypeIdentity', 
                [], [], 
                '''                The network service type supported within
                a network instance, e.g., NTP server, DNS
                server, DHCP server, etc.
                ''',
                'type',
                'example-network-device', True),
            ],
            'example-network-device',
            'network-service',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'NetworkServices' : {
        'meta_info' : _MetaInfoClass('NetworkServices',
            False, 
            [
            _MetaInfoClassMember('network-service', REFERENCE_LIST, 'NetworkService' , 'ydk.models.ietf.example_network_device', 'NetworkServices.NetworkService', 
                [], [], 
                '''                List of network services configured for a
                network instance.
                ''',
                'network_service',
                'example-network-device', False),
            ],
            'example-network-device',
            'network-services',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'OamProtocols.OamProtocol' : {
        'meta_info' : _MetaInfoClass('OamProtocols.OamProtocol',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'OamProtocolTypeIdentity' , 'ydk.models.ietf.example_network_device', 'OamProtocolTypeIdentity', 
                [], [], 
                '''                The Operations, Administration, and
                Maintenance (OAM) protocol type, e.g., BFD,
                TWAMP, CFM, etc.
                ''',
                'type',
                'example-network-device', True),
            ],
            'example-network-device',
            'oam-protocol',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'OamProtocols' : {
        'meta_info' : _MetaInfoClass('OamProtocols',
            False, 
            [
            _MetaInfoClassMember('oam-protocol', REFERENCE_LIST, 'OamProtocol' , 'ydk.models.ietf.example_network_device', 'OamProtocols.OamProtocol', 
                [], [], 
                '''                List of configured OAM protocols.
                ''',
                'oam_protocol',
                'example-network-device', False),
            ],
            'example-network-device',
            'oam-protocols',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Routing.ControlPlaneProtocol.Policy' : {
        'meta_info' : _MetaInfoClass('Routing.ControlPlaneProtocol.Policy',
            False, 
            [
            ],
            'example-network-device',
            'policy',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Routing.ControlPlaneProtocol' : {
        'meta_info' : _MetaInfoClass('Routing.ControlPlaneProtocol',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'ControlPlaneProtocolTypeIdentity' , 'ydk.models.ietf.example_network_device', 'ControlPlaneProtocolTypeIdentity', 
                [], [], 
                '''                The control plane protocol type, e.g., BGP,
                OSPF IS-IS, etc
                ''',
                'type',
                'example-network-device', True),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.ietf.example_network_device', 'Routing.ControlPlaneProtocol.Policy', 
                [], [], 
                '''                Protocol specific policy,
                reusing [RTG-POLICY]
                ''',
                'policy',
                'example-network-device', False),
            ],
            'example-network-device',
            'control-plane-protocol',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Routing.Rib.Policy' : {
        'meta_info' : _MetaInfoClass('Routing.Rib.Policy',
            False, 
            [
            ],
            'example-network-device',
            'policy',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Routing.Rib' : {
        'meta_info' : _MetaInfoClass('Routing.Rib',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the RIB.
                ''',
                'name',
                'example-network-device', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the RIB
                ''',
                'description',
                'example-network-device', False),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy' , 'ydk.models.ietf.example_network_device', 'Routing.Rib.Policy', 
                [], [], 
                '''                Policy specific to RIB
                ''',
                'policy',
                'example-network-device', False),
            ],
            'example-network-device',
            'rib',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Routing' : {
        'meta_info' : _MetaInfoClass('Routing',
            False, 
            [
            _MetaInfoClassMember('control-plane-protocol', REFERENCE_LIST, 'ControlPlaneProtocol' , 'ydk.models.ietf.example_network_device', 'Routing.ControlPlaneProtocol', 
                [], [], 
                '''                List of control plane protocols configured for
                a network instance.
                ''',
                'control_plane_protocol',
                'example-network-device', False),
            _MetaInfoClassMember('rib', REFERENCE_LIST, 'Rib' , 'ydk.models.ietf.example_network_device', 'Routing.Rib', 
                [], [], 
                '''                Each entry represents a RIB identified by the
                'name' key. All routes in a RIB must belong to the
                same address family.
                
                For each routing instance, an implementation should
                provide one system-controlled default RIB for each
                supported address family.
                ''',
                'rib',
                'example-network-device', False),
            ],
            'example-network-device',
            'routing',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Mpls.Global_' : {
        'meta_info' : _MetaInfoClass('Mpls.Global_',
            False, 
            [
            ],
            'example-network-device',
            'global',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Mpls.Lsps' : {
        'meta_info' : _MetaInfoClass('Mpls.Lsps',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'MplsLspTypeIdentity' , 'ydk.models.ietf.example_network_device', 'MplsLspTypeIdentity', 
                [], [], 
                '''                MPLS and Traffic Engineering protocol LSP types,
                static, LDP/SR (igp-congruent),
                RSVP TE (constrained-paths) , etc.
                ''',
                'type',
                'example-network-device', True),
            ],
            'example-network-device',
            'lsps',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'Mpls' : {
        'meta_info' : _MetaInfoClass('Mpls',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.ietf.example_network_device', 'Mpls.Global_', 
                [], [], 
                '''                Global MPLS configuration
                ''',
                'global_',
                'example-network-device', False),
            _MetaInfoClassMember('lsps', REFERENCE_LIST, 'Lsps' , 'ydk.models.ietf.example_network_device', 'Mpls.Lsps', 
                [], [], 
                '''                List of LSP types.
                ''',
                'lsps',
                'example-network-device', False),
            ],
            'example-network-device',
            'mpls',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'IeeeDot1Q' : {
        'meta_info' : _MetaInfoClass('IeeeDot1Q',
            False, 
            [
            ],
            'example-network-device',
            'ieee-dot1Q',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'IetfAcl' : {
        'meta_info' : _MetaInfoClass('IetfAcl',
            False, 
            [
            ],
            'example-network-device',
            'ietf-acl',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'IetfKeyChain' : {
        'meta_info' : _MetaInfoClass('IetfKeyChain',
            False, 
            [
            ],
            'example-network-device',
            'ietf-key-chain',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'LogicalNetworkElement' : {
        'meta_info' : _MetaInfoClass('LogicalNetworkElement',
            False, 
            [
            ],
            'example-network-device',
            'logical-network-element',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
    'NetworkInstance' : {
        'meta_info' : _MetaInfoClass('NetworkInstance',
            False, 
            [
            ],
            'example-network-device',
            'network-instance',
            _yang_ns._namespaces['example-network-device'],
        'ydk.models.ietf.example_network_device'
        ),
    },
}
_meta_table['SystemManagement.SystemManagementGlobal']['meta_info'].parent =_meta_table['SystemManagement']['meta_info']
_meta_table['SystemManagement.SystemManagementProtocol']['meta_info'].parent =_meta_table['SystemManagement']['meta_info']
_meta_table['NetworkServices.NetworkService']['meta_info'].parent =_meta_table['NetworkServices']['meta_info']
_meta_table['OamProtocols.OamProtocol']['meta_info'].parent =_meta_table['OamProtocols']['meta_info']
_meta_table['Routing.ControlPlaneProtocol.Policy']['meta_info'].parent =_meta_table['Routing.ControlPlaneProtocol']['meta_info']
_meta_table['Routing.Rib.Policy']['meta_info'].parent =_meta_table['Routing.Rib']['meta_info']
_meta_table['Routing.ControlPlaneProtocol']['meta_info'].parent =_meta_table['Routing']['meta_info']
_meta_table['Routing.Rib']['meta_info'].parent =_meta_table['Routing']['meta_info']
_meta_table['Mpls.Global_']['meta_info'].parent =_meta_table['Mpls']['meta_info']
_meta_table['Mpls.Lsps']['meta_info'].parent =_meta_table['Mpls']['meta_info']
