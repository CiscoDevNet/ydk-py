


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ArpResolutionHistoryStatusEnum' : _MetaInfoEnum('ArpResolutionHistoryStatusEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper',
        {
            'status-none':'STATUS_NONE',
            'status-resolution-request':'STATUS_RESOLUTION_REQUEST',
            'status-resolved-reply':'STATUS_RESOLVED_REPLY',
            'status-resolved-grat-arp':'STATUS_RESOLVED_GRAT_ARP',
            'status-resolved-request':'STATUS_RESOLVED_REQUEST',
            'status-resolved-lc-sync':'STATUS_RESOLVED_LC_SYNC',
            'status-resolved-lc-sync-purge-delay':'STATUS_RESOLVED_LC_SYNC_PURGE_DELAY',
            'status-resolved-client':'STATUS_RESOLVED_CLIENT',
            'status-removed-client':'STATUS_REMOVED_CLIENT',
            'status-already-resolved':'STATUS_ALREADY_RESOLVED',
            'status-failed':'STATUS_FAILED',
            'status-dropped-interface-down':'STATUS_DROPPED_INTERFACE_DOWN',
            'status-dropped-broadcast-disabled':'STATUS_DROPPED_BROADCAST_DISABLED',
            'status-dropped-interface-unavailable':'STATUS_DROPPED_INTERFACE_UNAVAILABLE',
            'status-dropped-bad-subnet':'STATUS_DROPPED_BAD_SUBNET',
            'status-dropped-dynamic-learning-disabled':'STATUS_DROPPED_DYNAMIC_LEARNING_DISABLED',
            'status-dropped-out-of-subnet-disabled':'STATUS_DROPPED_OUT_OF_SUBNET_DISABLED',
            'status-removed-client-sweep':'STATUS_REMOVED_CLIENT_SWEEP',
            'status-added-client':'STATUS_ADDED_CLIENT',
            'status-added-v1':'STATUS_ADDED_V1',
            'status-removed-v1':'STATUS_REMOVED_V1',
            'status-resolved-peer-sync':'STATUS_RESOLVED_PEER_SYNC',
        }, 'Cisco-IOS-XR-ipv4-arp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper']),
    'IpArpBagEncapEnum' : _MetaInfoEnum('IpArpBagEncapEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper',
        {
            'none':'NONE',
            'arpa':'ARPA',
            'snap':'SNAP',
            'ieee802-1q':'IEEE802_1Q',
            'srp':'SRP',
            'srpa':'SRPA',
            'srpb':'SRPB',
        }, 'Cisco-IOS-XR-ipv4-arp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper']),
    'ArpGmpBagEncapEnum' : _MetaInfoEnum('ArpGmpBagEncapEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper',
        {
            'none':'NONE',
            'arpa':'ARPA',
            'snap':'SNAP',
            'ieee802-1q':'IEEE802_1Q',
            'srp':'SRP',
            'srpa':'SRPA',
            'srpb':'SRPB',
        }, 'Cisco-IOS-XR-ipv4-arp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper']),
    'IpArpBagMediaEnum' : _MetaInfoEnum('IpArpBagMediaEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper',
        {
            'media-arpa':'MEDIA_ARPA',
            'media-srp':'MEDIA_SRP',
            'media-unknown':'MEDIA_UNKNOWN',
        }, 'Cisco-IOS-XR-ipv4-arp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper']),
    'ArpGmpBagEntryEnum' : _MetaInfoEnum('ArpGmpBagEntryEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper',
        {
            'null':'NULL',
            'static':'STATIC',
            'alias':'ALIAS',
        }, 'Cisco-IOS-XR-ipv4-arp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper']),
    'IpArpBagStateEnum' : _MetaInfoEnum('IpArpBagStateEnum', 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper',
        {
            'state-none':'STATE_NONE',
            'state-interface':'STATE_INTERFACE',
            'state-standby':'STATE_STANDBY',
            'state-static':'STATE_STATIC',
            'state-alias':'STATE_ALIAS',
            'state-mobile':'STATE_MOBILE',
            'state-incomplete':'STATE_INCOMPLETE',
            'state-deleted':'STATE_DELETED',
            'state-dynamic':'STATE_DYNAMIC',
            'state-probe':'STATE_PROBE',
            'state-purge-delayed':'STATE_PURGE_DELAYED',
            'state-dhcp':'STATE_DHCP',
            'state-vxlan':'STATE_VXLAN',
            'state-sat':'STATE_SAT',
            'state-r-sync':'STATE_R_SYNC',
            'state-max':'STATE_MAX',
        }, 'Cisco-IOS-XR-ipv4-arp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper']),
    'ArpGmp.VrfInfos.VrfInfo' : {
        'meta_info' : _MetaInfoClass('ArpGmp.VrfInfos.VrfInfo',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name for the default VRF use 'default'
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('vrf-id-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                VRF ID
                ''',
                'vrf_id_number',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                IPv4 unicast table ID
                ''',
                'table_id',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('rsi-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                RSI registration handle
                ''',
                'rsi_handle',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('rsi-handle-high', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                RSI registration handle (top 32-bits)
                ''',
                'rsi_handle_high',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'vrf-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.VrfInfos' : {
        'meta_info' : _MetaInfoClass('ArpGmp.VrfInfos',
            False, 
            [
            _MetaInfoClassMember('vrf-info', REFERENCE_LIST, 'VrfInfo' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.VrfInfos.VrfInfo', 
                [], [], 
                '''                VRF related ARP-GMP operational data
                ''',
                'vrf_info',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'vrf-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configured ARP-GMP IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('hardware-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Hardware address 
                ''',
                'hardware_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'ArpGmpBagEncapEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEncapEnum', 
                [], [], 
                '''                Encap type
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('entry-type', REFERENCE_ENUM_CLASS, 'ArpGmpBagEntryEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEntryEnum', 
                [], [], 
                '''                Entry type static/alias
                ''',
                'entry_type',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'configured-ip-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses',
            False, 
            [
            _MetaInfoClassMember('configured-ip-address', REFERENCE_LIST, 'ConfiguredIpAddress' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress', 
                [], [], 
                '''                ARP-GMP configured IP address information
                ''',
                'configured_ip_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'configured-ip-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf.Routes.Route' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 32)], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('prefix-length-xr', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                IP address length
                ''',
                'prefix_length_xr',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name (first element of InterfaceNames
                array)
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('interface-name', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface names
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf.Routes' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf.Routes.Route', 
                [], [], 
                '''                ARP GMP route information
                ''',
                'route',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('hardware-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Hardware address 
                ''',
                'hardware_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'ArpGmpBagEncapEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEncapEnum', 
                [], [], 
                '''                Encap type
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('entry-type', REFERENCE_ENUM_CLASS, 'ArpGmpBagEntryEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmpBagEntryEnum', 
                [], [], 
                '''                Entry type static/alias
                ''',
                'entry_type',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'associated-configuration-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configured ARP-GMP IP
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('associated-configuration-entry', REFERENCE_CLASS, 'AssociatedConfigurationEntry' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry', 
                [], [], 
                '''                Associated configuration entry
                ''',
                'associated_configuration_entry',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('interface-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name_xr',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('reference-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Route reference count
                ''',
                'reference_count',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'interface-configured-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps',
            False, 
            [
            _MetaInfoClassMember('interface-configured-ip', REFERENCE_LIST, 'InterfaceConfiguredIp' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp', 
                [], [], 
                '''                ARP GMP interface and associated configured
                IP data
                ''',
                'interface_configured_ip',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'interface-configured-ips',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name for the default VRF use 'default'
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('configured-ip-addresses', REFERENCE_CLASS, 'ConfiguredIpAddresses' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses', 
                [], [], 
                '''                Table of ARP-GMP configured IP addresses
                information
                ''',
                'configured_ip_addresses',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf.Routes', 
                [], [], 
                '''                Table of ARP GMP route information
                ''',
                'routes',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('interface-configured-ips', REFERENCE_CLASS, 'InterfaceConfiguredIps' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps', 
                [], [], 
                '''                Table of ARP GMP interface and associated
                configured IP data
                ''',
                'interface_configured_ips',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp.Vrfs' : {
        'meta_info' : _MetaInfoClass('ArpGmp.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs.Vrf', 
                [], [], 
                '''                Per VRF ARP-GMP operational data
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'ArpGmp' : {
        'meta_info' : _MetaInfoClass('ArpGmp',
            False, 
            [
            _MetaInfoClassMember('vrf-infos', REFERENCE_CLASS, 'VrfInfos' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.VrfInfos', 
                [], [], 
                '''                Table of VRF related ARP-GMP operational data
                ''',
                'vrf_infos',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpGmp.Vrfs', 
                [], [], 
                '''                Table of per VRF ARP-GMP operational data
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'arp-gmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry',
            False, 
            [
            _MetaInfoClassMember('nsec-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Timestamp for entry in nanoseconds since Epoch,
                i.e. since 00:00:00 UTC, January 1, 1970
                ''',
                'nsec_timestamp',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('idb-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'idb_interface_name',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ArpResolutionHistoryStatusEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpResolutionHistoryStatusEnum', 
                [], [], 
                '''                Resolution status
                ''',
                'status',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Resolving Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('entry-state', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ARP entry state
                ''',
                'entry_state',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-request-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Resolution Request count
                ''',
                'resolution_request_count',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'arp-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.ResolutionHistoryDynamic' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.ResolutionHistoryDynamic',
            False, 
            [
            _MetaInfoClassMember('arp-entry', REFERENCE_LIST, 'ArpEntry' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry', 
                [], [], 
                '''                Resolution history array
                ''',
                'arp_entry',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'resolution-history-dynamic',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.TrafficVrfs.TrafficVrf' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.TrafficVrfs.TrafficVrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('requests-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP requests received
                ''',
                'requests_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('replies-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP replies received
                ''',
                'replies_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('requests-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP requests sent
                ''',
                'requests_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP replies sent
                ''',
                'replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('proxy-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Proxy ARP replies sent
                ''',
                'proxy_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('local-proxy-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Local Proxy ARP replies sent
                ''',
                'local_proxy_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('gratuitous-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Gratuituous ARP replies sent
                ''',
                'gratuitous_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-requests-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP resolution requests received
                ''',
                'resolution_requests_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-replies-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP resolution replies received
                ''',
                'resolution_replies_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-requests-dropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                total ARP resolution requests dropped
                ''',
                'resolution_requests_dropped',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('out-of-memory-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total errors for out of memory
                ''',
                'out_of_memory_errors',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('no-buffer-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total errors for no buffer
                ''',
                'no_buffer_errors',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('total-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP entries in the cache
                ''',
                'total_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('dynamic-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total dynamic entries in the cache
                ''',
                'dynamic_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('static-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total static entries in the cache
                ''',
                'static_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('alias-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total alias entries in the cache
                ''',
                'alias_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('interface-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total interface entries in the cache
                ''',
                'interface_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('standby-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total standby entries in the cache
                ''',
                'standby_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('dhcp-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total DHCP entries in the cache
                ''',
                'dhcp_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('vxlan-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total VXLAN entries in the cache
                ''',
                'vxlan_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ip-packets-dropped-node', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ip packets droped on this node
                ''',
                'ip_packets_dropped_node',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('arp-packet-node-out-of-subnet', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP packets on node due to out of subnet
                ''',
                'arp_packet_node_out_of_subnet',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ip-packets-dropped-interface', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ip packets droped on this interface
                ''',
                'ip_packets_dropped_interface',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('arp-packet-interface-out-of-subnet', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total arp packets on interface due to out of
                subnet
                ''',
                'arp_packet_interface_out_of_subnet',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('idb-structures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total idb structures on this node
                ''',
                'idb_structures',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'traffic-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.TrafficVrfs' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.TrafficVrfs',
            False, 
            [
            _MetaInfoClassMember('traffic-vrf', REFERENCE_LIST, 'TrafficVrf' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.TrafficVrfs.TrafficVrf', 
                [], [], 
                '''                Per VRF traffic data
                ''',
                'traffic_vrf',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'traffic-vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.TrafficNode' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.TrafficNode',
            False, 
            [
            _MetaInfoClassMember('requests-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP requests received
                ''',
                'requests_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('replies-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP replies received
                ''',
                'replies_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('requests-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP requests sent
                ''',
                'requests_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP replies sent
                ''',
                'replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('proxy-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Proxy ARP replies sent
                ''',
                'proxy_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('local-proxy-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Local Proxy ARP replies sent
                ''',
                'local_proxy_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('gratuitous-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Gratuituous ARP replies sent
                ''',
                'gratuitous_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-requests-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP resolution requests received
                ''',
                'resolution_requests_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-replies-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP resolution replies received
                ''',
                'resolution_replies_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-requests-dropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                total ARP resolution requests dropped
                ''',
                'resolution_requests_dropped',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('out-of-memory-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total errors for out of memory
                ''',
                'out_of_memory_errors',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('no-buffer-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total errors for no buffer
                ''',
                'no_buffer_errors',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('total-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP entries in the cache
                ''',
                'total_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('dynamic-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total dynamic entries in the cache
                ''',
                'dynamic_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('static-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total static entries in the cache
                ''',
                'static_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('alias-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total alias entries in the cache
                ''',
                'alias_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('interface-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total interface entries in the cache
                ''',
                'interface_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('standby-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total standby entries in the cache
                ''',
                'standby_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('dhcp-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total DHCP entries in the cache
                ''',
                'dhcp_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('vxlan-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total VXLAN entries in the cache
                ''',
                'vxlan_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ip-packets-dropped-node', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ip packets droped on this node
                ''',
                'ip_packets_dropped_node',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('arp-packet-node-out-of-subnet', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP packets on node due to out of subnet
                ''',
                'arp_packet_node_out_of_subnet',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ip-packets-dropped-interface', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ip packets droped on this interface
                ''',
                'ip_packets_dropped_interface',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('arp-packet-interface-out-of-subnet', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total arp packets on interface due to out of
                subnet
                ''',
                'arp_packet_interface_out_of_subnet',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('idb-structures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total idb structures on this node
                ''',
                'idb_structures',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'traffic-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry',
            False, 
            [
            _MetaInfoClassMember('nsec-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Timestamp for entry in nanoseconds since Epoch,
                i.e. since 00:00:00 UTC, January 1, 1970
                ''',
                'nsec_timestamp',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('idb-interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'idb_interface_name',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'ArpResolutionHistoryStatusEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'ArpResolutionHistoryStatusEnum', 
                [], [], 
                '''                Resolution status
                ''',
                'status',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('client-id', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Resolving Client ID
                ''',
                'client_id',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('entry-state', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ARP entry state
                ''',
                'entry_state',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-request-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Resolution Request count
                ''',
                'resolution_request_count',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'arp-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.ResolutionHistoryClient' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.ResolutionHistoryClient',
            False, 
            [
            _MetaInfoClassMember('arp-entry', REFERENCE_LIST, 'ArpEntry' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry', 
                [], [], 
                '''                Resolution history array
                ''',
                'arp_entry',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'resolution-history-client',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.Entries.Entry' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.Entries.Entry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP Address of ARP entry
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('media-type', REFERENCE_ENUM_CLASS, 'IpArpBagMediaEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'IpArpBagMediaEnum', 
                [], [], 
                '''                Media type for this entry
                ''',
                'media_type',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IpArpBagStateEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'IpArpBagStateEnum', 
                [], [], 
                '''                State of this entry
                ''',
                'state',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Age of this entry
                ''',
                'age',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'IpArpBagEncapEnum' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'IpArpBagEncapEnum', 
                [], [], 
                '''                Source encapsulation type
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('hardware-length', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Source hardware length
                ''',
                'hardware_length',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('hardware-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Hardware address
                ''',
                'hardware_address',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.Entries' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.Entries',
            False, 
            [
            _MetaInfoClassMember('entry', REFERENCE_LIST, 'Entry' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.Entries.Entry', 
                [], [], 
                '''                ARP entry
                ''',
                'entry',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'entries',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.TrafficInterfaces.TrafficInterface' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.TrafficInterfaces.TrafficInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('requests-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP requests received
                ''',
                'requests_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('replies-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP replies received
                ''',
                'replies_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('requests-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP requests sent
                ''',
                'requests_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP replies sent
                ''',
                'replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('proxy-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Proxy ARP replies sent
                ''',
                'proxy_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('local-proxy-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Local Proxy ARP replies sent
                ''',
                'local_proxy_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('gratuitous-replies-sent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total Gratuituous ARP replies sent
                ''',
                'gratuitous_replies_sent',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-requests-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP resolution requests received
                ''',
                'resolution_requests_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-replies-received', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP resolution replies received
                ''',
                'resolution_replies_received',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-requests-dropped', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                total ARP resolution requests dropped
                ''',
                'resolution_requests_dropped',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('out-of-memory-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total errors for out of memory
                ''',
                'out_of_memory_errors',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('no-buffer-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total errors for no buffer
                ''',
                'no_buffer_errors',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('total-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP entries in the cache
                ''',
                'total_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('dynamic-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total dynamic entries in the cache
                ''',
                'dynamic_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('static-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total static entries in the cache
                ''',
                'static_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('alias-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total alias entries in the cache
                ''',
                'alias_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('interface-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total interface entries in the cache
                ''',
                'interface_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('standby-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total standby entries in the cache
                ''',
                'standby_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('dhcp-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total DHCP entries in the cache
                ''',
                'dhcp_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('vxlan-entries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total VXLAN entries in the cache
                ''',
                'vxlan_entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ip-packets-dropped-node', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ip packets droped on this node
                ''',
                'ip_packets_dropped_node',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('arp-packet-node-out-of-subnet', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ARP packets on node due to out of subnet
                ''',
                'arp_packet_node_out_of_subnet',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('ip-packets-dropped-interface', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total ip packets droped on this interface
                ''',
                'ip_packets_dropped_interface',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('arp-packet-interface-out-of-subnet', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total arp packets on interface due to out of
                subnet
                ''',
                'arp_packet_interface_out_of_subnet',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('idb-structures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total idb structures on this node
                ''',
                'idb_structures',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'traffic-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node.TrafficInterfaces' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node.TrafficInterfaces',
            False, 
            [
            _MetaInfoClassMember('traffic-interface', REFERENCE_LIST, 'TrafficInterface' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.TrafficInterfaces.TrafficInterface', 
                [], [], 
                '''                Per interface traffic data
                ''',
                'traffic_interface',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'traffic-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ipv4-arp-oper', True),
            _MetaInfoClassMember('resolution-history-dynamic', REFERENCE_CLASS, 'ResolutionHistoryDynamic' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.ResolutionHistoryDynamic', 
                [], [], 
                '''                Per node dynamically-resolved ARP resolution
                history data
                ''',
                'resolution_history_dynamic',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('traffic-vrfs', REFERENCE_CLASS, 'TrafficVrfs' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.TrafficVrfs', 
                [], [], 
                '''                ARP Traffic information per VRF
                ''',
                'traffic_vrfs',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('traffic-node', REFERENCE_CLASS, 'TrafficNode' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.TrafficNode', 
                [], [], 
                '''                Per node ARP Traffic data
                ''',
                'traffic_node',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('resolution-history-client', REFERENCE_CLASS, 'ResolutionHistoryClient' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.ResolutionHistoryClient', 
                [], [], 
                '''                Per node client-installed ARP resolution
                history data
                ''',
                'resolution_history_client',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('entries', REFERENCE_CLASS, 'Entries' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.Entries', 
                [], [], 
                '''                Table of ARP entries
                ''',
                'entries',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            _MetaInfoClassMember('traffic-interfaces', REFERENCE_CLASS, 'TrafficInterfaces' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node.TrafficInterfaces', 
                [], [], 
                '''                ARP Traffic information per interface
                ''',
                'traffic_interfaces',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp.Nodes' : {
        'meta_info' : _MetaInfoClass('Arp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes.Node', 
                [], [], 
                '''                Per-node ARP operational data
                ''',
                'node',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
    'Arp' : {
        'meta_info' : _MetaInfoClass('Arp',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper', 'Arp.Nodes', 
                [], [], 
                '''                Table of per-node ARP operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ipv4-arp-oper', False),
            ],
            'Cisco-IOS-XR-ipv4-arp-oper',
            'arp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-arp-oper'],
        'ydk.models.ipv4.Cisco_IOS_XR_ipv4_arp_oper'
        ),
    },
}
_meta_table['ArpGmp.VrfInfos.VrfInfo']['meta_info'].parent =_meta_table['ArpGmp.VrfInfos']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses.ConfiguredIpAddress']['meta_info'].parent =_meta_table['ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf.Routes.Route']['meta_info'].parent =_meta_table['ArpGmp.Vrfs.Vrf.Routes']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp.AssociatedConfigurationEntry']['meta_info'].parent =_meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps.InterfaceConfiguredIp']['meta_info'].parent =_meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf.ConfiguredIpAddresses']['meta_info'].parent =_meta_table['ArpGmp.Vrfs.Vrf']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf.Routes']['meta_info'].parent =_meta_table['ArpGmp.Vrfs.Vrf']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf.InterfaceConfiguredIps']['meta_info'].parent =_meta_table['ArpGmp.Vrfs.Vrf']['meta_info']
_meta_table['ArpGmp.Vrfs.Vrf']['meta_info'].parent =_meta_table['ArpGmp.Vrfs']['meta_info']
_meta_table['ArpGmp.VrfInfos']['meta_info'].parent =_meta_table['ArpGmp']['meta_info']
_meta_table['ArpGmp.Vrfs']['meta_info'].parent =_meta_table['ArpGmp']['meta_info']
_meta_table['Arp.Nodes.Node.ResolutionHistoryDynamic.ArpEntry']['meta_info'].parent =_meta_table['Arp.Nodes.Node.ResolutionHistoryDynamic']['meta_info']
_meta_table['Arp.Nodes.Node.TrafficVrfs.TrafficVrf']['meta_info'].parent =_meta_table['Arp.Nodes.Node.TrafficVrfs']['meta_info']
_meta_table['Arp.Nodes.Node.ResolutionHistoryClient.ArpEntry']['meta_info'].parent =_meta_table['Arp.Nodes.Node.ResolutionHistoryClient']['meta_info']
_meta_table['Arp.Nodes.Node.Entries.Entry']['meta_info'].parent =_meta_table['Arp.Nodes.Node.Entries']['meta_info']
_meta_table['Arp.Nodes.Node.TrafficInterfaces.TrafficInterface']['meta_info'].parent =_meta_table['Arp.Nodes.Node.TrafficInterfaces']['meta_info']
_meta_table['Arp.Nodes.Node.ResolutionHistoryDynamic']['meta_info'].parent =_meta_table['Arp.Nodes.Node']['meta_info']
_meta_table['Arp.Nodes.Node.TrafficVrfs']['meta_info'].parent =_meta_table['Arp.Nodes.Node']['meta_info']
_meta_table['Arp.Nodes.Node.TrafficNode']['meta_info'].parent =_meta_table['Arp.Nodes.Node']['meta_info']
_meta_table['Arp.Nodes.Node.ResolutionHistoryClient']['meta_info'].parent =_meta_table['Arp.Nodes.Node']['meta_info']
_meta_table['Arp.Nodes.Node.Entries']['meta_info'].parent =_meta_table['Arp.Nodes.Node']['meta_info']
_meta_table['Arp.Nodes.Node.TrafficInterfaces']['meta_info'].parent =_meta_table['Arp.Nodes.Node']['meta_info']
_meta_table['Arp.Nodes.Node']['meta_info'].parent =_meta_table['Arp.Nodes']['meta_info']
_meta_table['Arp.Nodes']['meta_info'].parent =_meta_table['Arp']['meta_info']
