


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'AddressPoolTypeEnum' : _MetaInfoEnum('AddressPoolTypeEnum', 'ydk.models.ietf.ietf_address_pool',
        {
            'usergateway':'usergateway',
            'import-route':'import_route',
        }, 'ietf-address-pool', _yang_ns._namespaces['ietf-address-pool']),
    'InstanceTypeEnum' : _MetaInfoEnum('InstanceTypeEnum', 'ydk.models.ietf.ietf_address_pool',
        {
            'pppoe':'pppoe',
            'dhcp':'dhcp',
            'vpn':'vpn',
            'ds-lite':'ds_lite',
            'lw4over6':'lw4over6',
            'map':'map',
            'cgn':'cgn',
            'xlat':'xlat',
            'other':'other',
        }, 'ietf-address-pool', _yang_ns._namespaces['ietf-address-pool']),
    'AddressPools.AddressPool.AddressPoolService' : {
        'meta_info' : _MetaInfoClass('AddressPools.AddressPool.AddressPoolService',
            False, 
            [
            _MetaInfoClassMember('service-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A service name: e.g., any, voip, iptv, internet, etc.
                ''',
                'service_name',
                'ietf-address-pool', True),
            ],
            'ietf-address-pool',
            'address-pool-service',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPools.AddressPool.AddressPoolEntries.Ipv4AddressRange' : {
        'meta_info' : _MetaInfoClass('AddressPools.AddressPool.AddressPoolEntries.Ipv4AddressRange',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-range-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of IPv4 address range.
                ''',
                'ipv4_address_range_name',
                'ietf-address-pool', True),
            _MetaInfoClassMember('gwnetmask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                The netmask for usergateway.
                ''',
                'gwnetmask',
                'ietf-address-pool', False),
            _MetaInfoClassMember('instance', REFERENCE_ENUM_CLASS, 'InstanceTypeEnum' , 'ydk.models.ietf.ietf_address_pool', 'InstanceTypeEnum', 
                [], [], 
                '''                The instance of the address pool.
                ''',
                'instance',
                'ietf-address-pool', False),
            _MetaInfoClassMember('ip-lower-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The lower IPv4 address of the address range.
                ''',
                'ip_lower_address',
                'ietf-address-pool', False),
            _MetaInfoClassMember('ip-upper-address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The upper IPv4 address of the address range.
                ''',
                'ip_upper_address',
                'ietf-address-pool', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The lifetime for the address pool. '0' means
                withdrawal.
                ''',
                'lifetime',
                'ietf-address-pool', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AddressPoolTypeEnum' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolTypeEnum', 
                [], [], 
                '''                The type of the address pool.
                ''',
                'type',
                'ietf-address-pool', False),
            _MetaInfoClassMember('usergateway', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                It only exists when address pool are used for
                user addressing.
                ''',
                'usergateway',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'ipv4-address-range',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPools.AddressPool.AddressPoolEntries.Ipv6Prefix' : {
        'meta_info' : _MetaInfoClass('AddressPools.AddressPool.AddressPoolEntries.Ipv6Prefix',
            False, 
            [
            _MetaInfoClassMember('ipv6-prefix-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of IPv6 prefix.
                ''',
                'ipv6_prefix_name',
                'ietf-address-pool', True),
            _MetaInfoClassMember('instance', REFERENCE_ENUM_CLASS, 'InstanceTypeEnum' , 'ydk.models.ietf.ietf_address_pool', 'InstanceTypeEnum', 
                [], [], 
                '''                The instance of the address pool.
                ''',
                'instance',
                'ietf-address-pool', False),
            _MetaInfoClassMember('ipv6-prefix', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                The IPv6 prefix.
                ''',
                'ipv6_prefix',
                'ietf-address-pool', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The lifetime for the address pool. '0' means
                withdrawal.
                ''',
                'lifetime',
                'ietf-address-pool', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'AddressPoolTypeEnum' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolTypeEnum', 
                [], [], 
                '''                The type of the address pool.
                ''',
                'type',
                'ietf-address-pool', False),
            _MetaInfoClassMember('usergateway', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                It only exists when address pool are used for
                user addressing.
                ''',
                'usergateway',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'ipv6-prefix',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPools.AddressPool.AddressPoolEntries' : {
        'meta_info' : _MetaInfoClass('AddressPools.AddressPool.AddressPoolEntries',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-range', REFERENCE_LIST, 'Ipv4AddressRange' , 'ydk.models.ietf.ietf_address_pool', 'AddressPools.AddressPool.AddressPoolEntries.Ipv4AddressRange', 
                [], [], 
                '''                IPv4 Address range.
                ''',
                'ipv4_address_range',
                'ietf-address-pool', False),
            _MetaInfoClassMember('ipv6-prefix', REFERENCE_LIST, 'Ipv6Prefix' , 'ydk.models.ietf.ietf_address_pool', 'AddressPools.AddressPool.AddressPoolEntries.Ipv6Prefix', 
                [], [], 
                '''                IPv6 prefix.
                ''',
                'ipv6_prefix',
                'ietf-address-pool', False),
            _MetaInfoClassMember('warning-threshold-v4', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The threshold of the ipv4 address pool.
                ''',
                'warning_threshold_v4',
                'ietf-address-pool', False),
            _MetaInfoClassMember('warning-threshold-v6', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The threshold of the ipv6 address pool.
                ''',
                'warning_threshold_v6',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'address-pool-entries',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPools.AddressPool' : {
        'meta_info' : _MetaInfoClass('AddressPools.AddressPool',
            False, 
            [
            _MetaInfoClassMember('address-pool-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of address pool
                ''',
                'address_pool_name',
                'ietf-address-pool', True),
            _MetaInfoClassMember('address-pool-entries', REFERENCE_CLASS, 'AddressPoolEntries' , 'ydk.models.ietf.ietf_address_pool', 'AddressPools.AddressPool.AddressPoolEntries', 
                [], [], 
                '''                The address-pool-entries container contains
                a list of address-ranges and associated attributes.
                ''',
                'address_pool_entries',
                'ietf-address-pool', False),
            _MetaInfoClassMember('address-pool-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Address Pool id
                ''',
                'address_pool_id',
                'ietf-address-pool', False),
            _MetaInfoClassMember('address-pool-service', REFERENCE_LIST, 'AddressPoolService' , 'ydk.models.ietf.ietf_address_pool', 'AddressPools.AddressPool.AddressPoolService', 
                [], [], 
                '''                The services that can use these pool.
                ''',
                'address_pool_service',
                'ietf-address-pool', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The identifier of device that using address pool
                ''',
                'device_id',
                'ietf-address-pool', False),
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The domain name
                ''',
                'domain_name',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'address-pool',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPools' : {
        'meta_info' : _MetaInfoClass('AddressPools',
            False, 
            [
            _MetaInfoClassMember('address-pool', REFERENCE_LIST, 'AddressPool' , 'ydk.models.ietf.ietf_address_pool', 'AddressPools.AddressPool', 
                [], [], 
                '''                An Address Pool is an ordered list of
                Address Pool Entries (APE). Each Access Pool Entry has a
                list of address ranges and its associated lifetime.
                ''',
                'address_pool',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'address-pools',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPoolStatus.AddressPool.AddressPoolService' : {
        'meta_info' : _MetaInfoClass('AddressPoolStatus.AddressPool.AddressPoolService',
            False, 
            [
            _MetaInfoClassMember('service-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A service name: e.g., any, voip, iptv, internet, etc.
                ''',
                'service_name',
                'ietf-address-pool', True),
            ],
            'ietf-address-pool',
            'address-pool-service',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv4AddressRange' : {
        'meta_info' : _MetaInfoClass('AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv4AddressRange',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-range-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of IPv4 address range.
                ''',
                'ipv4_address_range_name',
                'ietf-address-pool', True),
            _MetaInfoClassMember('average-address-usage-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The average usage rate of the address range.
                ''',
                'average_address_usage_ratio',
                'ietf-address-pool', False),
            _MetaInfoClassMember('peak-address-usage-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The peak usage rate of the address range.
                ''',
                'peak_address_usage_ratio',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'ipv4-address-range',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv6Prefix' : {
        'meta_info' : _MetaInfoClass('AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv6Prefix',
            False, 
            [
            _MetaInfoClassMember('ipv6-prefix-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of IPv6 prefix.
                ''',
                'ipv6_prefix_name',
                'ietf-address-pool', True),
            _MetaInfoClassMember('average-prefix-usage-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The average usage rate of the prefix.
                ''',
                'average_prefix_usage_ratio',
                'ietf-address-pool', False),
            _MetaInfoClassMember('peak-prefix-usage-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The peak usage rate of the prefix.
                ''',
                'peak_prefix_usage_ratio',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'ipv6-prefix',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPoolStatus.AddressPool.AddressPoolEntries.PortRange' : {
        'meta_info' : _MetaInfoClass('AddressPoolStatus.AddressPool.AddressPoolEntries.PortRange',
            False, 
            [
            _MetaInfoClassMember('port-range-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of port range.
                ''',
                'port_range_name',
                'ietf-address-pool', True),
            _MetaInfoClassMember('average-address-usage-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The average usage rate of the port range.
                ''',
                'average_address_usage_ratio',
                'ietf-address-pool', False),
            _MetaInfoClassMember('peak-address-usage-ratio', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                The peak usage rate of the port range.
                ''',
                'peak_address_usage_ratio',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'port-range',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPoolStatus.AddressPool.AddressPoolEntries' : {
        'meta_info' : _MetaInfoClass('AddressPoolStatus.AddressPool.AddressPoolEntries',
            False, 
            [
            _MetaInfoClassMember('ipv4-address-range', REFERENCE_LIST, 'Ipv4AddressRange' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv4AddressRange', 
                [], [], 
                '''                IPv4 Address range.
                ''',
                'ipv4_address_range',
                'ietf-address-pool', False),
            _MetaInfoClassMember('ipv6-prefix', REFERENCE_LIST, 'Ipv6Prefix' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv6Prefix', 
                [], [], 
                '''                IPv6 prefix.
                ''',
                'ipv6_prefix',
                'ietf-address-pool', False),
            _MetaInfoClassMember('port-range', REFERENCE_LIST, 'PortRange' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolStatus.AddressPool.AddressPoolEntries.PortRange', 
                [], [], 
                '''                port range.
                ''',
                'port_range',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'address-pool-entries',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPoolStatus.AddressPool.StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.ietf.ietf_address_pool',
        {
            'active':'active',
            'idle':'idle',
        }, 'ietf-address-pool', _yang_ns._namespaces['ietf-address-pool']),
    'AddressPoolStatus.AddressPool' : {
        'meta_info' : _MetaInfoClass('AddressPoolStatus.AddressPool',
            False, 
            [
            _MetaInfoClassMember('address-pool-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of address pool
                ''',
                'address_pool_name',
                'ietf-address-pool', True),
            _MetaInfoClassMember('address-pool-entries', REFERENCE_CLASS, 'AddressPoolEntries' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolStatus.AddressPool.AddressPoolEntries', 
                [], [], 
                '''                The address-pool-entries container contains
                a list of address-ranges and associated attributes.
                ''',
                'address_pool_entries',
                'ietf-address-pool', False),
            _MetaInfoClassMember('address-pool-service', REFERENCE_LIST, 'AddressPoolService' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolStatus.AddressPool.AddressPoolService', 
                [], [], 
                '''                The services that can use these pool.
                ''',
                'address_pool_service',
                'ietf-address-pool', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolStatus.AddressPool.StatusEnum', 
                [], [], 
                '''                The status of address pool
                ''',
                'status',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'address-pool',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
    'AddressPoolStatus' : {
        'meta_info' : _MetaInfoClass('AddressPoolStatus',
            False, 
            [
            _MetaInfoClassMember('address-pool', REFERENCE_LIST, 'AddressPool' , 'ydk.models.ietf.ietf_address_pool', 'AddressPoolStatus.AddressPool', 
                [], [], 
                '''                An Address Pool is an ordered list of
                Address Pool Entries (APE). Each Access Pool Entry has a
                list of address ranges and its associated lifetime. 
                ''',
                'address_pool',
                'ietf-address-pool', False),
            ],
            'ietf-address-pool',
            'address-pool-status',
            _yang_ns._namespaces['ietf-address-pool'],
        'ydk.models.ietf.ietf_address_pool'
        ),
    },
}
_meta_table['AddressPools.AddressPool.AddressPoolEntries.Ipv4AddressRange']['meta_info'].parent =_meta_table['AddressPools.AddressPool.AddressPoolEntries']['meta_info']
_meta_table['AddressPools.AddressPool.AddressPoolEntries.Ipv6Prefix']['meta_info'].parent =_meta_table['AddressPools.AddressPool.AddressPoolEntries']['meta_info']
_meta_table['AddressPools.AddressPool.AddressPoolService']['meta_info'].parent =_meta_table['AddressPools.AddressPool']['meta_info']
_meta_table['AddressPools.AddressPool.AddressPoolEntries']['meta_info'].parent =_meta_table['AddressPools.AddressPool']['meta_info']
_meta_table['AddressPools.AddressPool']['meta_info'].parent =_meta_table['AddressPools']['meta_info']
_meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv4AddressRange']['meta_info'].parent =_meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries']['meta_info']
_meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries.Ipv6Prefix']['meta_info'].parent =_meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries']['meta_info']
_meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries.PortRange']['meta_info'].parent =_meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries']['meta_info']
_meta_table['AddressPoolStatus.AddressPool.AddressPoolService']['meta_info'].parent =_meta_table['AddressPoolStatus.AddressPool']['meta_info']
_meta_table['AddressPoolStatus.AddressPool.AddressPoolEntries']['meta_info'].parent =_meta_table['AddressPoolStatus.AddressPool']['meta_info']
_meta_table['AddressPoolStatus.AddressPool']['meta_info'].parent =_meta_table['AddressPoolStatus']['meta_info']
