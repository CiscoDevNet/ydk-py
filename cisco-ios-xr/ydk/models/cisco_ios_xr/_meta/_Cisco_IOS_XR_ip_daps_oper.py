


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpAddrEnum' : _MetaInfoEnum('IpAddrEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ip-daps-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper']),
    'DapsClientEnum' : _MetaInfoEnum('DapsClientEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper',
        {
            'none':'none',
            'ppp':'ppp',
            'dhcp':'dhcp',
            'dhcpv6':'dhcpv6',
            'ipv6nd':'ipv6nd',
        }, 'Cisco-IOS-XR-ip-daps-oper', _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper']),
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'IpAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddrEnum', 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'start-address-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'IpAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddrEnum', 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'end-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'IpAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddrEnum', 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'default-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('start-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP Address
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-daps-oper', True, [
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-ip-daps-oper', True),
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP Address
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-ip-daps-oper', True),
                ]),
            _MetaInfoClassMember('allocated-addresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of addresses allocated
                ''',
                'allocated_addresses',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('default-router', REFERENCE_CLASS, 'DefaultRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter', 
                [], [], 
                '''                Default router
                ''',
                'default_router',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('end-address', REFERENCE_CLASS, 'EndAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress', 
                [], [], 
                '''                Range end
                ''',
                'end_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('excluded-addresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of addresses excluded
                ''',
                'excluded_addresses',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('free-addresses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of addresses free
                ''',
                'free_addresses',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('network-blocked-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Is network blocked
                ''',
                'network_blocked_status',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('network-blocked-status-trp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Is network blocked trap send
                ''',
                'network_blocked_status_trp',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-scope', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pool scope
                ''',
                'pool_scope',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('start-address-xr', REFERENCE_CLASS, 'StartAddressXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr', 
                [], [], 
                '''                Range start
                ''',
                'start_address_xr',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange', 
                [], [], 
                '''                Start Address of the Range
                ''',
                'address_range',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold',
            False, 
            [
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold in percentage
                ''',
                'threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('time-last-crossed', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last time at which threshold crossed in DDD MMM
                DD HH:MM:SS YYYY format eg: Tue Apr 11 21:30:47
                2011
                ''',
                'time_last_crossed',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('triggers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Triggers
                ''',
                'triggers',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'high-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold',
            False, 
            [
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Threshold in percentage
                ''',
                'threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('time-last-crossed', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last time at which threshold crossed in DDD MMM
                DD HH:MM:SS YYYY format eg: Tue Apr 11 21:30:47
                2011
                ''',
                'time_last_crossed',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('triggers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Triggers
                ''',
                'triggers',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'low-threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations',
            False, 
            [
            _MetaInfoClassMember('excluded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excluded allocations
                ''',
                'excluded',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free allocations
                ''',
                'free',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('high-threshold', REFERENCE_CLASS, 'HighThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold', 
                [], [], 
                '''                High threshold data
                ''',
                'high_threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('low-threshold', REFERENCE_CLASS, 'LowThreshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold', 
                [], [], 
                '''                Low threshold data
                ''',
                'low_threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total allocations
                ''',
                'total',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used allocations
                ''',
                'used',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('utilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current utilization in percentage
                ''',
                'utilization',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'pool-allocations',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'IpAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddrEnum', 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'start-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'IpAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddrEnum', 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'end-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange',
            False, 
            [
            _MetaInfoClassMember('end-address', REFERENCE_CLASS, 'EndAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress', 
                [], [], 
                '''                Range end
                ''',
                'end_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('excluded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excluded allocations
                ''',
                'excluded',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free allocations
                ''',
                'free',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('start-address', REFERENCE_CLASS, 'StartAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress', 
                [], [], 
                '''                Range start
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used allocations
                ''',
                'used',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'IpAddrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'IpAddrEnum', 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address', 
                [], [], 
                '''                Client address
                ''',
                'address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('client-type', REFERENCE_ENUM_CLASS, 'DapsClientEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'DapsClientEnum', 
                [], [], 
                '''                Client type
                ''',
                'client_type',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'in-use-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange', 
                [], [], 
                '''                Address ranges
                ''',
                'address_range',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('in-use-address', REFERENCE_LIST, 'InUseAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress', 
                [], [], 
                '''                In-use addresses
                ''',
                'in_use_address',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-allocations', REFERENCE_CLASS, 'PoolAllocations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations', 
                [], [], 
                '''                Pool allocations
                ''',
                'pool_allocations',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'allocated-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool.Configuration' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool.Configuration',
            False, 
            [
            _MetaInfoClassMember('current-utilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Current utilization
                ''',
                'current_utilization',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('high-utilization-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                High utilization mark
                ''',
                'high_utilization_mark',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('low-utilization-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Low utilization mark
                ''',
                'low_utilization_mark',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Pool ID for MIBS
                ''',
                'pool_id',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'pool_prefix_length',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-scope', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pool Scope
                ''',
                'pool_scope',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('utilization-high-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times High utilization threshold was
                crossed
                ''',
                'utilization_high_count',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('utilization-low-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of times Low utilization threshold was
                crossed
                ''',
                'utilization_low_count',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools.Pool' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools.Pool',
            False, 
            [
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ip-daps-oper', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges', 
                [], [], 
                '''                Summary info for pool
                ''',
                'address_ranges',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('allocated-addresses', REFERENCE_CLASS, 'AllocatedAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses', 
                [], [], 
                '''                Detailed info for the Pool
                ''',
                'allocated_addresses',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('configuration', REFERENCE_CLASS, 'Configuration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool.Configuration', 
                [], [], 
                '''                Configuration info for pool
                ''',
                'configuration',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Pools' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Pools',
            False, 
            [
            _MetaInfoClassMember('pool', REFERENCE_LIST, 'Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools.Pool', 
                [], [], 
                '''                Pool data by pool name
                ''',
                'pool',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.TotalUtilization' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.TotalUtilization',
            False, 
            [
            _MetaInfoClassMember('current-total-utilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Current utilization
                ''',
                'current_total_utilization',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total-utilization-high-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                High utilization mark
                ''',
                'total_utilization_high_mark',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total-utilization-low-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Low utilization mark
                ''',
                'total_utilization_low_mark',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'total-utilization',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary',
            False, 
            [
            _MetaInfoClassMember('excluded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excluded allocations
                ''',
                'excluded',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free allocations
                ''',
                'free',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('high-utilization-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                High utilization threshold in percentage
                ''',
                'high_utilization_threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('low-utilization-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Low utilization threshold in percentage
                ''',
                'low_utilization_threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total allocations
                ''',
                'total',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used allocations
                ''',
                'used',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('utilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Current utilization in percentage
                ''',
                'utilization',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'allocation-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools',
            False, 
            [
            _MetaInfoClassMember('excluded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excluded allocations
                ''',
                'excluded',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free allocations
                ''',
                'free',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total allocations
                ''',
                'total',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used allocations
                ''',
                'used',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4',
            False, 
            [
            _MetaInfoClassMember('allocation-summary', REFERENCE_CLASS, 'AllocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary', 
                [], [], 
                '''                Allocation summary
                ''',
                'allocation_summary',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pools', REFERENCE_LIST, 'Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools', 
                [], [], 
                '''                Pools data
                ''',
                'pools',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary',
            False, 
            [
            _MetaInfoClassMember('excluded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excluded allocations
                ''',
                'excluded',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free allocations
                ''',
                'free',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('high-utilization-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                High utilization threshold in percentage
                ''',
                'high_utilization_threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('low-utilization-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Low utilization threshold in percentage
                ''',
                'low_utilization_threshold',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total allocations
                ''',
                'total',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used allocations
                ''',
                'used',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('utilization', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Current utilization in percentage
                ''',
                'utilization',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'allocation-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools',
            False, 
            [
            _MetaInfoClassMember('excluded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excluded allocations
                ''',
                'excluded',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('free', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free allocations
                ''',
                'free',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total allocations
                ''',
                'total',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('used', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used allocations
                ''',
                'used',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6',
            False, 
            [
            _MetaInfoClassMember('allocation-summary', REFERENCE_CLASS, 'AllocationSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary', 
                [], [], 
                '''                Allocation summary
                ''',
                'allocation_summary',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('pools', REFERENCE_LIST, 'Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools', 
                [], [], 
                '''                Pools data
                ''',
                'pools',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-daps-oper', True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4', 
                [], [], 
                '''                IPv4 pool VRF data
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6', 
                [], [], 
                '''                IPv6 Pool VRF data
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node.Vrfs' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs.Vrf', 
                [], [], 
                '''                VRF level Pool information
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-daps-oper', True),
            _MetaInfoClassMember('pools', REFERENCE_CLASS, 'Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Pools', 
                [], [], 
                '''                List of IPv4/IPv6 pool data
                ''',
                'pools',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('total-utilization', REFERENCE_CLASS, 'TotalUtilization' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.TotalUtilization', 
                [], [], 
                '''                Show total utilization for pool
                ''',
                'total_utilization',
                'Cisco-IOS-XR-ip-daps-oper', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node.Vrfs', 
                [], [], 
                '''                Pool VRF data
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService.Nodes' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes.Node', 
                [], [], 
                '''                Location. For eg., 0/1/CPU0
                ''',
                'node',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
    'AddressPoolService' : {
        'meta_info' : _MetaInfoClass('AddressPoolService',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper', 'AddressPoolService.Nodes', 
                [], [], 
                '''                Pool operational data for a particular location
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-daps-oper', False),
            ],
            'Cisco-IOS-XR-ip-daps-oper',
            'address-pool-service',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_oper'
        ),
    },
}
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr.Address']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress.Address']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter.Address']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.StartAddressXr']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.EndAddress']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange.DefaultRouter']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.HighThreshold']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations.LowThreshold']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress.Address']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress.Address']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.StartAddress']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange.EndAddress']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address.Address_']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress.Address']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.PoolAllocations']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.AddressRange']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses.InUseAddress']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AddressRanges']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.AllocatedAddresses']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool.Configuration']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools.Pool']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Pools']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.AllocationSummary']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4.Pools']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.AllocationSummary']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6.Pools']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv4']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf.Ipv6']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs.Vrf']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node.Vrfs']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Pools']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.TotalUtilization']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node']['meta_info']
_meta_table['AddressPoolService.Nodes.Node.Vrfs']['meta_info'].parent =_meta_table['AddressPoolService.Nodes.Node']['meta_info']
_meta_table['AddressPoolService.Nodes.Node']['meta_info'].parent =_meta_table['AddressPoolService.Nodes']['meta_info']
_meta_table['AddressPoolService.Nodes']['meta_info'].parent =_meta_table['AddressPoolService']['meta_info']
