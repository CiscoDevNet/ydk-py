


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LldpL3AddrProtocolEnum' : _MetaInfoEnum('LldpL3AddrProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper']),
    'LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis id
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('port-id-detail', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id_detail',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('recv-intf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Receive Interface
                ''',
                'recv_intf',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Name
                ''',
                'system_name',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'lldp-neighbor-brief-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.LldpNeighborBrief.Neighbours' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.LldpNeighborBrief.Neighbours',
            False, 
            [
            _MetaInfoClassMember('lldp-neighbor-brief-entry', REFERENCE_LIST, 'LldpNeighborBriefEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry', 
                [], [], 
                '''                lldp neighbor brief entry
                ''',
                'lldp_neighbor_brief_entry',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'neighbours',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.LldpNeighborBrief' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.LldpNeighborBrief',
            False, 
            [
            _MetaInfoClassMember('neighbours', REFERENCE_CLASS, 'Neighbours' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.LldpNeighborBrief.Neighbours', 
                [], [], 
                '''                List of LLDP neighbors
                ''',
                'neighbours',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('number-of-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of active neighbors entries
                ''',
                'number_of_entries',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'lldp-neighbor-brief',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'LldpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('if-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface num
                ''',
                'if_num',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('ma-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MA sub type
                ''',
                'ma_subtype',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'lldp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('lldp-addr-entry', REFERENCE_LIST, 'LldpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry', 
                [], [], 
                '''                lldp addr entry
                ''',
                'lldp_addr_entry',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.EthernetControllerNames.EthernetControllerName' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.EthernetControllerNames.EthernetControllerName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', True),
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis id
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('drop-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LLDP Packet Drop Enabled
                ''',
                'drop_enabled',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('lldp-neighbor', ATTRIBUTE, 'str' , None, None, 
                [(0, 40)], [], 
                '''                LldpNeighbor
                ''',
                'lldp_neighbor',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('network-addresses', REFERENCE_CLASS, 'NetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses', 
                [], [], 
                '''                Management Addresses
                ''',
                'network_addresses',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('port-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port Description
                ''',
                'port_description',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('port-id-detail', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id_detail',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('rx-lldp-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Received LLDP Packets count
                ''',
                'rx_lldp_pkts',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('source-mac', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Mac address of the neighbor
                ''',
                'source_mac',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('system-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Capabilities
                ''',
                'system_capabilities',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('system-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Description
                ''',
                'system_description',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Name
                ''',
                'system_name',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'ethernet-controller-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData.EthernetControllerNames' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData.EthernetControllerNames',
            False, 
            [
            _MetaInfoClassMember('ethernet-controller-name', REFERENCE_LIST, 'EthernetControllerName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.EthernetControllerNames.EthernetControllerName', 
                [], [], 
                '''                port Name
                ''',
                'ethernet_controller_name',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'ethernet-controller-names',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
    'LldpSnoopData' : {
        'meta_info' : _MetaInfoClass('LldpSnoopData',
            False, 
            [
            _MetaInfoClassMember('ethernet-controller-names', REFERENCE_CLASS, 'EthernetControllerNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.EthernetControllerNames', 
                [], [], 
                '''                Ethernet controller snoop data
                ''',
                'ethernet_controller_names',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            _MetaInfoClassMember('lldp-neighbor-brief', REFERENCE_CLASS, 'LldpNeighborBrief' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper', 'LldpSnoopData.LldpNeighborBrief', 
                [], [], 
                '''                NCS1K LLDP Neighbor brief info
                ''',
                'lldp_neighbor_brief',
                'Cisco-IOS-XR-ncs1k-mxp-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-lldp-oper',
            'lldp-snoop-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_lldp_oper'
        ),
    },
}
_meta_table['LldpSnoopData.LldpNeighborBrief.Neighbours.LldpNeighborBriefEntry']['meta_info'].parent =_meta_table['LldpSnoopData.LldpNeighborBrief.Neighbours']['meta_info']
_meta_table['LldpSnoopData.LldpNeighborBrief.Neighbours']['meta_info'].parent =_meta_table['LldpSnoopData.LldpNeighborBrief']['meta_info']
_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry.Address']['meta_info'].parent =_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry']['meta_info']
_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses.LldpAddrEntry']['meta_info'].parent =_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses']['meta_info']
_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName.NetworkAddresses']['meta_info'].parent =_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName']['meta_info']
_meta_table['LldpSnoopData.EthernetControllerNames.EthernetControllerName']['meta_info'].parent =_meta_table['LldpSnoopData.EthernetControllerNames']['meta_info']
_meta_table['LldpSnoopData.LldpNeighborBrief']['meta_info'].parent =_meta_table['LldpSnoopData']['meta_info']
_meta_table['LldpSnoopData.EthernetControllerNames']['meta_info'].parent =_meta_table['LldpSnoopData']['meta_info']
