


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LldpL3AddrProtocolEnum' : _MetaInfoEnum('LldpL3AddrProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ethernet-lldp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper']),
    'Lldp.GlobalLldp.LldpInfo' : {
        'meta_info' : _MetaInfoClass('Lldp.GlobalLldp.LldpInfo',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Length  of time  (in sec)                       
                that receiver must keep this                    
                packet
                ''',
                'hold_time',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('re-init', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Delay (in sec) for LLDP                         
                initialization on any                           
                interface
                ''',
                're_init',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate at which LLDP packets                      
                are sent (in sec)
                ''',
                'timer',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.GlobalLldp' : {
        'meta_info' : _MetaInfoClass('Lldp.GlobalLldp',
            False, 
            [
            _MetaInfoClassMember('lldp-info', REFERENCE_CLASS, 'LldpInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.GlobalLldp.LldpInfo', 
                [], [], 
                '''                The LLDP Global Information of this box
                ''',
                'lldp_info',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'global-lldp',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'LldpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('if-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface num
                ''',
                'if_num',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ma-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MA sub type
                ''',
                'ma_subtype',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('lldp-addr-entry', REFERENCE_LIST, 'LldpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry', 
                [], [], 
                '''                lldp addr entry
                ''',
                'lldp_addr_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail',
            False, 
            [
            _MetaInfoClassMember('auto-negotiation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Auto Negotiation
                ''',
                'auto_negotiation',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('media-attachment-unit-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Media Attachment Unit type
                ''',
                'media_attachment_unit_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('network-addresses', REFERENCE_CLASS, 'NetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses', 
                [], [], 
                '''                Management Addresses
                ''',
                'network_addresses',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('physical-media-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Physical media capabilities
                ''',
                'physical_media_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port Description
                ''',
                'port_description',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vlan ID
                ''',
                'port_vlan_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Capabilities
                ''',
                'system_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Description
                ''',
                'system_description',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Name
                ''',
                'system_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time remaining
                ''',
                'time_remaining',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry',
            False, 
            [
            _MetaInfoClassMember('tlv-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Unknown TLV type
                ''',
                'tlv_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Unknown TLV payload
                ''',
                'tlv_value',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-unknown-tlv-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList',
            False, 
            [
            _MetaInfoClassMember('lldp-unknown-tlv-entry', REFERENCE_LIST, 'LldpUnknownTlvEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry', 
                [], [], 
                '''                lldp unknown tlv entry
                ''',
                'lldp_unknown_tlv_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'unknown-tlv-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Organizationally Unique Identifier
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-info-indes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lldpRemOrgDefInfoIndex
                ''',
                'tlv_info_indes',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Org Def TLV subtype
                ''',
                'tlv_subtype',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Org Def TLV payload
                ''',
                'tlv_value',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-org-def-tlv-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList',
            False, 
            [
            _MetaInfoClassMember('lldp-org-def-tlv-entry', REFERENCE_LIST, 'LldpOrgDefTlvEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry', 
                [], [], 
                '''                lldp org def tlv entry
                ''',
                'lldp_org_def_tlv_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'org-def-tlv-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib',
            False, 
            [
            _MetaInfoClassMember('chassis-id-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Chassis ID length
                ''',
                'chassis_id_len',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('chassis-id-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Chassis ID sub type
                ''',
                'chassis_id_sub_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('combined-capabilities', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Supported and combined cpabilities
                ''',
                'combined_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('org-def-tlv-list', REFERENCE_CLASS, 'OrgDefTlvList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList', 
                [], [], 
                '''                Org Def TLV list
                ''',
                'org_def_tlv_list',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port ID length
                ''',
                'port_id_len',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID sub type
                ''',
                'port_id_sub_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lldpRemIndex
                ''',
                'rem_index',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-local-port-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LldpPortNumber
                ''',
                'rem_local_port_num',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-time-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TimeFilter
                ''',
                'rem_time_mark',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('unknown-tlv-list', REFERENCE_CLASS, 'UnknownTlvList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList', 
                [], [], 
                '''                Unknown TLV list
                ''',
                'unknown_tlv_list',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'mib',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis id
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail', 
                [], [], 
                '''                Detailed neighbor info
                ''',
                'detail',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('header-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version number
                ''',
                'header_version',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('mib', REFERENCE_CLASS, 'Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib', 
                [], [], 
                '''                MIB nieghbor info
                ''',
                'mib',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('platform', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Platform type
                ''',
                'platform',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-detail', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id_detail',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('receiving-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface the neighbor entry was received on 
                ''',
                'receiving_interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('receiving-parent-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface the neighbor entry was
                received on 
                ''',
                'receiving_parent_interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices.Device' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices.Device',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The neighboring device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('lldp-neighbor', REFERENCE_LIST, 'LldpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor', 
                [], [], 
                '''                lldp neighbor
                ''',
                'lldp_neighbor',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'device',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Devices' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Devices',
            False, 
            [
            _MetaInfoClassMember('device', REFERENCE_LIST, 'Device' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices.Device', 
                [], [], 
                '''                Detailed information about a LLDP neighbor
                entry
                ''',
                'device',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'devices',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'LldpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('if-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface num
                ''',
                'if_num',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ma-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MA sub type
                ''',
                'ma_subtype',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('lldp-addr-entry', REFERENCE_LIST, 'LldpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry', 
                [], [], 
                '''                lldp addr entry
                ''',
                'lldp_addr_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_',
            False, 
            [
            _MetaInfoClassMember('auto-negotiation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Auto Negotiation
                ''',
                'auto_negotiation',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('media-attachment-unit-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Media Attachment Unit type
                ''',
                'media_attachment_unit_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('network-addresses', REFERENCE_CLASS, 'NetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses', 
                [], [], 
                '''                Management Addresses
                ''',
                'network_addresses',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('physical-media-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Physical media capabilities
                ''',
                'physical_media_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port Description
                ''',
                'port_description',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vlan ID
                ''',
                'port_vlan_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Capabilities
                ''',
                'system_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Description
                ''',
                'system_description',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Name
                ''',
                'system_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time remaining
                ''',
                'time_remaining',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry',
            False, 
            [
            _MetaInfoClassMember('tlv-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Unknown TLV type
                ''',
                'tlv_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Unknown TLV payload
                ''',
                'tlv_value',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-unknown-tlv-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList',
            False, 
            [
            _MetaInfoClassMember('lldp-unknown-tlv-entry', REFERENCE_LIST, 'LldpUnknownTlvEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry', 
                [], [], 
                '''                lldp unknown tlv entry
                ''',
                'lldp_unknown_tlv_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'unknown-tlv-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Organizationally Unique Identifier
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-info-indes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lldpRemOrgDefInfoIndex
                ''',
                'tlv_info_indes',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Org Def TLV subtype
                ''',
                'tlv_subtype',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Org Def TLV payload
                ''',
                'tlv_value',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-org-def-tlv-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList',
            False, 
            [
            _MetaInfoClassMember('lldp-org-def-tlv-entry', REFERENCE_LIST, 'LldpOrgDefTlvEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry', 
                [], [], 
                '''                lldp org def tlv entry
                ''',
                'lldp_org_def_tlv_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'org-def-tlv-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib',
            False, 
            [
            _MetaInfoClassMember('chassis-id-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Chassis ID length
                ''',
                'chassis_id_len',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('chassis-id-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Chassis ID sub type
                ''',
                'chassis_id_sub_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('combined-capabilities', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Supported and combined cpabilities
                ''',
                'combined_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('org-def-tlv-list', REFERENCE_CLASS, 'OrgDefTlvList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList', 
                [], [], 
                '''                Org Def TLV list
                ''',
                'org_def_tlv_list',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port ID length
                ''',
                'port_id_len',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID sub type
                ''',
                'port_id_sub_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lldpRemIndex
                ''',
                'rem_index',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-local-port-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LldpPortNumber
                ''',
                'rem_local_port_num',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-time-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TimeFilter
                ''',
                'rem_time_mark',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('unknown-tlv-list', REFERENCE_CLASS, 'UnknownTlvList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList', 
                [], [], 
                '''                Unknown TLV list
                ''',
                'unknown_tlv_list',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'mib',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis id
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_', 
                [], [], 
                '''                Detailed neighbor info
                ''',
                'detail',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('header-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version number
                ''',
                'header_version',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('mib', REFERENCE_CLASS, 'Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib', 
                [], [], 
                '''                MIB nieghbor info
                ''',
                'mib',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('platform', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Platform type
                ''',
                'platform',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-detail', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id_detail',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('receiving-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface the neighbor entry was received on 
                ''',
                'receiving_interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('receiving-parent-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface the neighbor entry was
                received on 
                ''',
                'receiving_parent_interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details.Detail' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details.Detail',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The neighboring device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('lldp-neighbor', REFERENCE_LIST, 'LldpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor', 
                [], [], 
                '''                lldp neighbor
                ''',
                'lldp_neighbor',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Details' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Details',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_LIST, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details.Detail', 
                [], [], 
                '''                Detailed information about a LLDP neighbor
                entry
                ''',
                'detail',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'details',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'LldpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('if-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface num
                ''',
                'if_num',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ma-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MA sub type
                ''',
                'ma_subtype',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('lldp-addr-entry', REFERENCE_LIST, 'LldpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry', 
                [], [], 
                '''                lldp addr entry
                ''',
                'lldp_addr_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail',
            False, 
            [
            _MetaInfoClassMember('auto-negotiation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Auto Negotiation
                ''',
                'auto_negotiation',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('media-attachment-unit-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Media Attachment Unit type
                ''',
                'media_attachment_unit_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('network-addresses', REFERENCE_CLASS, 'NetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses', 
                [], [], 
                '''                Management Addresses
                ''',
                'network_addresses',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('physical-media-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Physical media capabilities
                ''',
                'physical_media_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port Description
                ''',
                'port_description',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vlan ID
                ''',
                'port_vlan_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Capabilities
                ''',
                'system_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Description
                ''',
                'system_description',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                System Name
                ''',
                'system_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('time-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time remaining
                ''',
                'time_remaining',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry',
            False, 
            [
            _MetaInfoClassMember('tlv-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Unknown TLV type
                ''',
                'tlv_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Unknown TLV payload
                ''',
                'tlv_value',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-unknown-tlv-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList',
            False, 
            [
            _MetaInfoClassMember('lldp-unknown-tlv-entry', REFERENCE_LIST, 'LldpUnknownTlvEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry', 
                [], [], 
                '''                lldp unknown tlv entry
                ''',
                'lldp_unknown_tlv_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'unknown-tlv-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry',
            False, 
            [
            _MetaInfoClassMember('oui', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Organizationally Unique Identifier
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-info-indes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lldpRemOrgDefInfoIndex
                ''',
                'tlv_info_indes',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Org Def TLV subtype
                ''',
                'tlv_subtype',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tlv-value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Org Def TLV payload
                ''',
                'tlv_value',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-org-def-tlv-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList',
            False, 
            [
            _MetaInfoClassMember('lldp-org-def-tlv-entry', REFERENCE_LIST, 'LldpOrgDefTlvEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry', 
                [], [], 
                '''                lldp org def tlv entry
                ''',
                'lldp_org_def_tlv_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'org-def-tlv-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib',
            False, 
            [
            _MetaInfoClassMember('chassis-id-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Chassis ID length
                ''',
                'chassis_id_len',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('chassis-id-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Chassis ID sub type
                ''',
                'chassis_id_sub_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('combined-capabilities', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Supported and combined cpabilities
                ''',
                'combined_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('org-def-tlv-list', REFERENCE_CLASS, 'OrgDefTlvList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList', 
                [], [], 
                '''                Org Def TLV list
                ''',
                'org_def_tlv_list',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port ID length
                ''',
                'port_id_len',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID sub type
                ''',
                'port_id_sub_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                lldpRemIndex
                ''',
                'rem_index',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-local-port-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LldpPortNumber
                ''',
                'rem_local_port_num',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rem-time-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TimeFilter
                ''',
                'rem_time_mark',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('unknown-tlv-list', REFERENCE_CLASS, 'UnknownTlvList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList', 
                [], [], 
                '''                Unknown TLV list
                ''',
                'unknown_tlv_list',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'mib',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Chassis id
                ''',
                'chassis_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail', 
                [], [], 
                '''                Detailed neighbor info
                ''',
                'detail',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('enabled-capabilities', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Enabled Capabilities
                ''',
                'enabled_capabilities',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('header-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Version number
                ''',
                'header_version',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remaining hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('mib', REFERENCE_CLASS, 'Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib', 
                [], [], 
                '''                MIB nieghbor info
                ''',
                'mib',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('platform', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Platform type
                ''',
                'platform',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-detail', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id_detail',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('receiving-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface the neighbor entry was received on 
                ''',
                'receiving_interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('receiving-parent-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface the neighbor entry was
                received on 
                ''',
                'receiving_parent_interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries.Summary' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries.Summary',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The neighboring device identifier
                ''',
                'device_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('lldp-neighbor', REFERENCE_LIST, 'LldpNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor', 
                [], [], 
                '''                lldp neighbor
                ''',
                'lldp_neighbor',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors.Summaries' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors.Summaries',
            False, 
            [
            _MetaInfoClassMember('summary', REFERENCE_LIST, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries.Summary', 
                [], [], 
                '''                Brief information about a LLDP neighbor
                entry
                ''',
                'summary',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Neighbors' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Neighbors',
            False, 
            [
            _MetaInfoClassMember('details', REFERENCE_CLASS, 'Details' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Details', 
                [], [], 
                '''                The detailed LLDP neighbor table
                ''',
                'details',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('devices', REFERENCE_CLASS, 'Devices' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Devices', 
                [], [], 
                '''                The detailed LLDP neighbor table on this
                device
                ''',
                'devices',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('summaries', REFERENCE_CLASS, 'Summaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors.Summaries', 
                [], [], 
                '''                The LLDP neighbor summary table
                ''',
                'summaries',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address',
            False, 
            [
            _MetaInfoClassMember('address-type', REFERENCE_ENUM_CLASS, 'LldpL3AddrProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'LldpL3AddrProtocolEnum', 
                [], [], 
                '''                AddressType
                ''',
                'address_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address', 
                [], [], 
                '''                Network layer address
                ''',
                'address',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('if-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface num
                ''',
                'if_num',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('ma-subtype', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MA sub type
                ''',
                'ma_subtype',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp-addr-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses',
            False, 
            [
            _MetaInfoClassMember('lldp-addr-entry', REFERENCE_LIST, 'LldpAddrEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry', 
                [], [], 
                '''                lldp addr entry
                ''',
                'lldp_addr_entry',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'local-network-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', True),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ifIndex
                ''',
                'if_index',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('local-network-addresses', REFERENCE_CLASS, 'LocalNetworkAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses', 
                [], [], 
                '''                Local Management Addresses
                ''',
                'local_network_addresses',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port Description
                ''',
                'port_description',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Outgoing port identifier
                ''',
                'port_id',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('port-id-sub-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Port ID sub type
                ''',
                'port_id_sub_type',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rx-enabled', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                RX Enabled
                ''',
                'rx_enabled',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('rx-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RX State
                ''',
                'rx_state',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tx-enabled', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TX Enabled
                ''',
                'tx_enabled',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('tx-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TX State
                ''',
                'tx_state',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Operational data for an interface on which
                LLDP is running
                ''',
                'interface',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node.Statistics' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node.Statistics',
            False, 
            [
            _MetaInfoClassMember('aged-out-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Aged out entries
                ''',
                'aged_out_entries',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('bad-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bad packet received and dropped
                ''',
                'bad_packets',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('discarded-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded packets
                ''',
                'discarded_packets',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('discarded-tl-vs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discarded TLVs
                ''',
                'discarded_tl_vs',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('encapsulation-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmission errors
                ''',
                'encapsulation_errors',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('out-of-memory-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Out-of-memory conditions
                ''',
                'out_of_memory_errors',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('queue-overflow-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Queue overflows
                ''',
                'queue_overflow_errors',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('received-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Received packets
                ''',
                'received_packets',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('table-overflow-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Table overflows
                ''',
                'table_overflow_errors',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('transmitted-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmitted packets
                ''',
                'transmitted_packets',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('unrecognized-tl-vs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unrecognized TLVs
                ''',
                'unrecognized_tl_vs',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The identifier for the node
                ''',
                'node_name',
                'Cisco-IOS-XR-ethernet-lldp-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Interfaces', 
                [], [], 
                '''                The table of interfaces on which LLDP is
                running on this node
                ''',
                'interfaces',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Neighbors', 
                [], [], 
                '''                The LLDP neighbor tables on this node
                ''',
                'neighbors',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node.Statistics', 
                [], [], 
                '''                The LLDP traffic statistics for this node
                ''',
                'statistics',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp.Nodes' : {
        'meta_info' : _MetaInfoClass('Lldp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes.Node', 
                [], [], 
                '''                The LLDP operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
    'Lldp' : {
        'meta_info' : _MetaInfoClass('Lldp',
            False, 
            [
            _MetaInfoClassMember('global-lldp', REFERENCE_CLASS, 'GlobalLldp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.GlobalLldp', 
                [], [], 
                '''                Global LLDP data
                ''',
                'global_lldp',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper', 'Lldp.Nodes', 
                [], [], 
                '''                Per node LLDP operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ethernet-lldp-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-lldp-oper',
            'lldp',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-lldp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_lldp_oper'
        ),
    },
}
_meta_table['Lldp.GlobalLldp.LldpInfo']['meta_info'].parent =_meta_table['Lldp.GlobalLldp']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail.NetworkAddresses']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.UnknownTlvList']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib.OrgDefTlvList']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Detail']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor.Mib']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device.LldpNeighbor']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices.Device']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Devices']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry.Address']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses.LldpAddrEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_.NetworkAddresses']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.UnknownTlvList']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib.OrgDefTlvList']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Detail_']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor.Mib']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail.LldpNeighbor']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details.Detail']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Details']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry.Address']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses.LldpAddrEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail.NetworkAddresses']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList.LldpUnknownTlvEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList.LldpOrgDefTlvEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.UnknownTlvList']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib.OrgDefTlvList']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Detail']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor.Mib']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary.LldpNeighbor']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries.Summary']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors.Summaries']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Devices']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Details']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors.Summaries']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Neighbors']['meta_info']
_meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry.Address']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry']['meta_info']
_meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses.LldpAddrEntry']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses']['meta_info']
_meta_table['Lldp.Nodes.Node.Interfaces.Interface.LocalNetworkAddresses']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Lldp.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Lldp.Nodes.Node.Interfaces']['meta_info']
_meta_table['Lldp.Nodes.Node.Neighbors']['meta_info'].parent =_meta_table['Lldp.Nodes.Node']['meta_info']
_meta_table['Lldp.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Lldp.Nodes.Node']['meta_info']
_meta_table['Lldp.Nodes.Node.Statistics']['meta_info'].parent =_meta_table['Lldp.Nodes.Node']['meta_info']
_meta_table['Lldp.Nodes.Node']['meta_info'].parent =_meta_table['Lldp.Nodes']['meta_info']
_meta_table['Lldp.GlobalLldp']['meta_info'].parent =_meta_table['Lldp']['meta_info']
_meta_table['Lldp.Nodes']['meta_info'].parent =_meta_table['Lldp']['meta_info']
