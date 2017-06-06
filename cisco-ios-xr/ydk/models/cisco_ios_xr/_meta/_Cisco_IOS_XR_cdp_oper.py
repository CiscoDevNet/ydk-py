


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CdpL3AddrProtocolEnum' : _MetaInfoEnum('CdpL3AddrProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-cdp-oper', _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper']),
    'CdpDuplexEnum' : _MetaInfoEnum('CdpDuplexEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper',
        {
            'cdp-dplx-none':'cdp_dplx_none',
            'cdp-dplx-half':'cdp_dplx_half',
            'cdp-dplx-full':'cdp_dplx_full',
        }, 'Cisco-IOS-XR-cdp-oper', _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper']),
    'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'CdpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('cdp-addr-entry', REFERENCE_LIST, 'CdpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry', 
                [], [], 
                '''                cdp addr entry
                ''',
                'cdp_addr_entry',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry',
            False, 
            [
            _MetaInfoClassMember('hello-message', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Protocol Hello msg
                ''',
                'hello_message',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-prot-hello-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList',
            False, 
            [
            _MetaInfoClassMember('cdp-prot-hello-entry', REFERENCE_LIST, 'CdpProtHelloEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry', 
                [], [], 
                '''                cdp prot hello entry
                ''',
                'cdp_prot_hello_entry',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'protocol-hello-list',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_',
            False, 
            [
            _MetaInfoClassMember('duplex', REFERENCE_ENUM_CLASS, 'CdpDuplexEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpDuplexEnum', 
                [], [], 
                '''                Duplex setting
                ''',
                'duplex',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Native VLAN
                ''',
                'native_vlan',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('network-addresses', REFERENCE_CLASS, 'NetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses', 
                [], [], 
                '''                List of network addresses 
                ''',
                'network_addresses',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('protocol-hello-list', REFERENCE_CLASS, 'ProtocolHelloList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList', 
                [], [], 
                '''                List of protocol hello entries
                ''',
                'protocol_hello_list',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SysName
                ''',
                'system_name',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version TLV
                ''',
                'version',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('vtp-domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VTP domain
                ''',
                'vtp_domain',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor',
            False, 
            [
            _MetaInfoClassMember('capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capabilities
                ''',
                'capabilities',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_', 
                [], [], 
                '''                Detailed neighbor info
                ''',
                'detail',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('header-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version number
                ''',
                'header_version',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('platform', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Platform type
                ''',
                'platform',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('receiving-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface the neighbor entry was received on 
                ''',
                'receiving_interface_name',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details.Detail' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details.Detail',
            False, 
            [
            _MetaInfoClassMember('cdp-neighbor', REFERENCE_LIST, 'CdpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor', 
                [], [], 
                '''                cdp neighbor
                ''',
                'cdp_neighbor',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The neighboring device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Details' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Details',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_LIST, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details.Detail', 
                [], [], 
                '''                Detailed information about a CDP neighbor
                entry
                ''',
                'detail',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'CdpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('cdp-addr-entry', REFERENCE_LIST, 'CdpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry', 
                [], [], 
                '''                cdp addr entry
                ''',
                'cdp_addr_entry',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry',
            False, 
            [
            _MetaInfoClassMember('hello-message', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Protocol Hello msg
                ''',
                'hello_message',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-prot-hello-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList',
            False, 
            [
            _MetaInfoClassMember('cdp-prot-hello-entry', REFERENCE_LIST, 'CdpProtHelloEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry', 
                [], [], 
                '''                cdp prot hello entry
                ''',
                'cdp_prot_hello_entry',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'protocol-hello-list',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail',
            False, 
            [
            _MetaInfoClassMember('duplex', REFERENCE_ENUM_CLASS, 'CdpDuplexEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpDuplexEnum', 
                [], [], 
                '''                Duplex setting
                ''',
                'duplex',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Native VLAN
                ''',
                'native_vlan',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('network-addresses', REFERENCE_CLASS, 'NetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses', 
                [], [], 
                '''                List of network addresses 
                ''',
                'network_addresses',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('protocol-hello-list', REFERENCE_CLASS, 'ProtocolHelloList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList', 
                [], [], 
                '''                List of protocol hello entries
                ''',
                'protocol_hello_list',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SysName
                ''',
                'system_name',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version TLV
                ''',
                'version',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('vtp-domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VTP domain
                ''',
                'vtp_domain',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor',
            False, 
            [
            _MetaInfoClassMember('capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capabilities
                ''',
                'capabilities',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail', 
                [], [], 
                '''                Detailed neighbor info
                ''',
                'detail',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('header-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version number
                ''',
                'header_version',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('platform', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Platform type
                ''',
                'platform',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('receiving-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface the neighbor entry was received on 
                ''',
                'receiving_interface_name',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices.Device' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices.Device',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The neighboring device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-cdp-oper', True),
            _MetaInfoClassMember('cdp-neighbor', REFERENCE_LIST, 'CdpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor', 
                [], [], 
                '''                cdp neighbor
                ''',
                'cdp_neighbor',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'device',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Devices' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Devices',
            False, 
            [
            _MetaInfoClassMember('device', REFERENCE_LIST, 'Device' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices.Device', 
                [], [], 
                '''                Detailed information about a CDP neighbor
                entry
                ''',
                'device',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'devices',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'CdpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('cdp-addr-entry', REFERENCE_LIST, 'CdpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry', 
                [], [], 
                '''                cdp addr entry
                ''',
                'cdp_addr_entry',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry',
            False, 
            [
            _MetaInfoClassMember('hello-message', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Protocol Hello msg
                ''',
                'hello_message',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-prot-hello-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList',
            False, 
            [
            _MetaInfoClassMember('cdp-prot-hello-entry', REFERENCE_LIST, 'CdpProtHelloEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry', 
                [], [], 
                '''                cdp prot hello entry
                ''',
                'cdp_prot_hello_entry',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'protocol-hello-list',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail',
            False, 
            [
            _MetaInfoClassMember('duplex', REFERENCE_ENUM_CLASS, 'CdpDuplexEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'CdpDuplexEnum', 
                [], [], 
                '''                Duplex setting
                ''',
                'duplex',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Native VLAN
                ''',
                'native_vlan',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('network-addresses', REFERENCE_CLASS, 'NetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses', 
                [], [], 
                '''                List of network addresses 
                ''',
                'network_addresses',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('protocol-hello-list', REFERENCE_CLASS, 'ProtocolHelloList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList', 
                [], [], 
                '''                List of protocol hello entries
                ''',
                'protocol_hello_list',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SysName
                ''',
                'system_name',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version TLV
                ''',
                'version',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('vtp-domain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VTP domain
                ''',
                'vtp_domain',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor',
            False, 
            [
            _MetaInfoClassMember('capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capabilities
                ''',
                'capabilities',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail', 
                [], [], 
                '''                Detailed neighbor info
                ''',
                'detail',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('header-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version number
                ''',
                'header_version',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('platform', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Platform type
                ''',
                'platform',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('receiving-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface the neighbor entry was received on 
                ''',
                'receiving_interface_name',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries.Summary' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries.Summary',
            False, 
            [
            _MetaInfoClassMember('cdp-neighbor', REFERENCE_LIST, 'CdpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor', 
                [], [], 
                '''                cdp neighbor
                ''',
                'cdp_neighbor',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The neighboring device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors.Summaries' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors.Summaries',
            False, 
            [
            _MetaInfoClassMember('summary', REFERENCE_LIST, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries.Summary', 
                [], [], 
                '''                Brief information about a CDP neighbor entry
                ''',
                'summary',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Neighbors' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Neighbors',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Details', 
                [], [], 
                '''                The detailed CDP neighbor table
                ''',
                'details',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('devices', REFERENCE_CLASS, 'Devices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Devices', 
                [], [], 
                '''                The detailed CDP neighbor table
                ''',
                'devices',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('summaries', REFERENCE_CLASS, 'Summaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors.Summaries', 
                [], [], 
                '''                The CDP neighbor summary table
                ''',
                'summaries',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('bad-packet-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad packet received and dropped
                ''',
                'bad_packet_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('checksum-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Checksum errors
                ''',
                'checksum_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('encapsulation-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmission errors
                ''',
                'encapsulation_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('header-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Header syntax errors
                ''',
                'header_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('header-version-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Can't handle receive version
                ''',
                'header_version_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('open-file-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cannot open file
                ''',
                'open_file_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('out-of-memory-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory conditions
                ''',
                'out_of_memory_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('received-packets-v1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received v1 packets
                ''',
                'received_packets_v1',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('received-packets-v2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received v2 packets
                ''',
                'received_packets_v2',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('transmitted-packets-v1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmitted v1 packets
                ''',
                'transmitted_packets_v1',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('transmitted-packets-v2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmitted v2 packets
                ''',
                'transmitted_packets_v2',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('truncated-packet-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Truncated messages
                ''',
                'truncated_packet_errors',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-cdp-oper', True),
            _MetaInfoClassMember('basecaps-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface basecaps state
                ''',
                'basecaps_state',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('cdp-protocol-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CDP protocol state
                ''',
                'cdp_protocol_state',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('interface-encaps', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface encapsulation
                ''',
                'interface_encaps',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_handle',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Operational data for an interface on which
                CDP is running
                ''',
                'interface',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The identifier for the node
                ''',
                'node_name',
                'Cisco-IOS-XR-cdp-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Interfaces', 
                [], [], 
                '''                The table of interfaces on which CDP is
                running on this node
                ''',
                'interfaces',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Neighbors', 
                [], [], 
                '''                The CDP neighbor tables on this node
                ''',
                'neighbors',
                'Cisco-IOS-XR-cdp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node.Statistics', 
                [], [], 
                '''                The CDP traffic statistics for this node
                ''',
                'statistics',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp.Nodes' : {
        'meta_info' : _MetaInfoClass('Cdp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes.Node', 
                [], [], 
                '''                The CDP operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
    'Cdp' : {
        'meta_info' : _MetaInfoClass('Cdp',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper', 'Cdp.Nodes', 
                [], [], 
                '''                Per node CDP operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-cdp-oper', False),
            ],
            'Cisco-IOS-XR-cdp-oper',
            'cdp',
            _yang_ns._namespaces['Cisco-IOS-XR-cdp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cdp_oper'
        ),
    },
}
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry.Address']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses.CdpAddrEntry']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList.CdpProtHelloEntry']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.NetworkAddresses']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_.ProtocolHelloList']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor.Detail_']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail.CdpNeighbor']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details.Detail']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Details']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.NetworkAddresses']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail.ProtocolHelloList']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor.Detail']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device.CdpNeighbor']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices.Device']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Devices']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry.Address']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses.CdpAddrEntry']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList.CdpProtHelloEntry']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.NetworkAddresses']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail.ProtocolHelloList']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor.Detail']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary.CdpNeighbor']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries.Summary']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors.Summaries']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Details']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Devices']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors.Summaries']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Neighbors']['meta_info']
_meta_table['Cdp.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Cdp.Nodes.Node.Interfaces']['meta_info']
_meta_table['Cdp.Nodes.Node.Neighbors']['meta_info'].parent =_meta_table['Cdp.Nodes.Node']['meta_info']
_meta_table['Cdp.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Cdp.Nodes.Node']['meta_info']
_meta_table['Cdp.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Cdp.Nodes.Node']['meta_info']
_meta_table['Cdp.Nodes.Node']['meta_info'].parent =_meta_table['Cdp.Nodes']['meta_info']
_meta_table['Cdp.Nodes']['meta_info'].parent =_meta_table['Cdp']['meta_info']
