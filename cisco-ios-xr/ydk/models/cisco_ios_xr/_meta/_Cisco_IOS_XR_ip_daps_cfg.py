


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('start-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Start address of the range
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-daps-cfg', True, [
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Start address of the range
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Start address of the range
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                ]),
            _MetaInfoClassMember('blocked', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Blocked flag
                ''',
                'blocked',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                End Address of the range
                ''',
                'end_address',
                'Cisco-IOS-XR-ip-daps-cfg', False, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        End Address of the range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        End Address of the range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange', 
                [], [], 
                '''                None
                ''',
                'address_range',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude',
            False, 
            [
            _MetaInfoClassMember('start-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First Address in IPv6 exclude range
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-daps-cfg', True, [
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        First Address in IPv6 exclude range
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                    _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        First Address in IPv6 exclude range
                        ''',
                        'start_address',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                ]),
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Last address in exclude Range
                ''',
                'end_address',
                'Cisco-IOS-XR-ip-daps-cfg', False, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last address in exclude Range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last address in exclude Range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'exclude',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes',
            False, 
            [
            _MetaInfoClassMember('exclude', REFERENCE_LIST, 'Exclude' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude', 
                [], [], 
                '''                None
                ''',
                'exclude',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'excludes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark',
            False, 
            [
            _MetaInfoClassMember('high-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Specify numerical value as percentage
                ''',
                'high_mark',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('low-mark', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Specify numerical value as percentage
                ''',
                'low_mark',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'utilization-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange',
            False, 
            [
            _MetaInfoClassMember('start-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                First prefix of range
                ''',
                'start_prefix',
                'Cisco-IOS-XR-ip-daps-cfg', True, [
                    _MetaInfoClassMember('start-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        First prefix of range
                        ''',
                        'start_prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                    _MetaInfoClassMember('start-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        First prefix of range
                        ''',
                        'start_prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                ]),
            _MetaInfoClassMember('blocked', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Blocked flag
                ''',
                'blocked',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('end-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Last prefix of range
                ''',
                'end_prefix',
                'Cisco-IOS-XR-ip-daps-cfg', False, [
                    _MetaInfoClassMember('end-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last prefix of range
                        ''',
                        'end_prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                    _MetaInfoClassMember('end-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last prefix of range
                        ''',
                        'end_prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'prefix-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges',
            False, 
            [
            _MetaInfoClassMember('prefix-range', REFERENCE_LIST, 'PrefixRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange', 
                [], [], 
                '''                None
                ''',
                'prefix_range',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'prefix-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                None
                ''',
                'prefix',
                'Cisco-IOS-XR-ip-daps-cfg', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        None
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        None
                        ''',
                        'prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                ]),
            _MetaInfoClassMember('blocked', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Blocked flag
                ''',
                'blocked',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Prefix length for the IPv6 Prefix
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'network',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_LIST, 'Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network', 
                [], [], 
                '''                None
                ''',
                'network',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'networks',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool',
            False, 
            [
            _MetaInfoClassMember('ipv6-pool-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Enter the IPv6 Pool name
                ''',
                'ipv6_pool_name',
                'Cisco-IOS-XR-ip-daps-cfg', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges', 
                [], [], 
                '''                Specify address range for allocation
                ''',
                'address_ranges',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('excludes', REFERENCE_CLASS, 'Excludes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes', 
                [], [], 
                '''                Exclude IPv6 addresses / prefixes
                ''',
                'excludes',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('networks', REFERENCE_CLASS, 'Networks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks', 
                [], [], 
                '''                Specify network for allocation
                ''',
                'networks',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('1', '128')], [], 
                '''                Enter the prefix-length for the Pool
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('prefix-ranges', REFERENCE_CLASS, 'PrefixRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges', 
                [], [], 
                '''                Specify prefix range for allocation
                ''',
                'prefix_ranges',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('utilization-mark', REFERENCE_CLASS, 'UtilizationMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark', 
                [], [], 
                '''                Specify utilization mark
                ''',
                'utilization_mark',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6.Pools' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6.Pools',
            False, 
            [
            _MetaInfoClassMember('pool', REFERENCE_LIST, 'Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool', 
                [], [], 
                '''                Enter the IPv6 Pool name
                ''',
                'pool',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv6' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv6',
            False, 
            [
            _MetaInfoClassMember('pools', REFERENCE_CLASS, 'Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6.Pools', 
                [], [], 
                '''                IPv6 Pool Name
                ''',
                'pools',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange',
            False, 
            [
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Specify first address of the range
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-daps-cfg', True),
            _MetaInfoClassMember('blocked', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Blocked flag
                ''',
                'blocked',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Last address of the range
                ''',
                'end_address',
                'Cisco-IOS-XR-ip-daps-cfg', False, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last address of the range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last address of the range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'address-range',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges',
            False, 
            [
            _MetaInfoClassMember('address-range', REFERENCE_LIST, 'AddressRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange', 
                [], [], 
                '''                Specify first address in range
                ''',
                'address_range',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'address-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude',
            False, 
            [
            _MetaInfoClassMember('start-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                First address in exclude range
                ''',
                'start_address',
                'Cisco-IOS-XR-ip-daps-cfg', True),
            _MetaInfoClassMember('end-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Last address in excluded range
                ''',
                'end_address',
                'Cisco-IOS-XR-ip-daps-cfg', False, [
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last address in excluded range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                    _MetaInfoClassMember('end-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Last address in excluded range
                        ''',
                        'end_address',
                        'Cisco-IOS-XR-ip-daps-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'exclude',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes',
            False, 
            [
            _MetaInfoClassMember('exclude', REFERENCE_LIST, 'Exclude' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude', 
                [], [], 
                '''                First address in range
                ''',
                'exclude',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'excludes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark',
            False, 
            [
            _MetaInfoClassMember('high', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Specify numerical value as percentage
                ''',
                'high',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('low', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Specify numerical value as percentage
                ''',
                'low',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'utilization-mark',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network',
            False, 
            [
            _MetaInfoClassMember('ipv4-prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                None
                ''',
                'ipv4_prefix',
                'Cisco-IOS-XR-ip-daps-cfg', True, [
                    _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        None
                        ''',
                        'ipv4_prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                    _MetaInfoClassMember('ipv4-prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        None
                        ''',
                        'ipv4_prefix',
                        'Cisco-IOS-XR-ip-daps-cfg', True),
                ]),
            _MetaInfoClassMember('blocked', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Blocked flag
                ''',
                'blocked',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('default-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Default Gateway for IPv4 subnet
                ''',
                'default_router',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Subnet Length for IPv4 subnet
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'network',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_LIST, 'Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network', 
                [], [], 
                '''                Network Prefix
                ''',
                'network',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'networks',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool',
            False, 
            [
            _MetaInfoClassMember('pool-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Enter the IPv4 Pool name
                ''',
                'pool_name',
                'Cisco-IOS-XR-ip-daps-cfg', True),
            _MetaInfoClassMember('address-ranges', REFERENCE_CLASS, 'AddressRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges', 
                [], [], 
                '''                address range for allocation
                ''',
                'address_ranges',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('excludes', REFERENCE_CLASS, 'Excludes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes', 
                [], [], 
                '''                Exclude addresses
                ''',
                'excludes',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('networks', REFERENCE_CLASS, 'Networks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks', 
                [], [], 
                '''                Specify network for allocation
                ''',
                'networks',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('utilization-mark', REFERENCE_CLASS, 'UtilizationMark' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark', 
                [], [], 
                '''                Specify utilization mark
                ''',
                'utilization_mark',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'pool',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4.Pools' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4.Pools',
            False, 
            [
            _MetaInfoClassMember('pool', REFERENCE_LIST, 'Pool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool', 
                [], [], 
                '''                IPv4 Pool name
                ''',
                'pool',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'pools',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf.Ipv4' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf.Ipv4',
            False, 
            [
            _MetaInfoClassMember('pools', REFERENCE_CLASS, 'Pools' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4.Pools', 
                [], [], 
                '''                IPv4 Pool Table
                ''',
                'pools',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                none
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-daps-cfg', True),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv4', 
                [], [], 
                '''                Enter IPv4 specific configuration
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf.Ipv6', 
                [], [], 
                '''                Enter IPv6 specific mode
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService.Vrfs' : {
        'meta_info' : _MetaInfoClass('AddressPoolService.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs.Vrf', 
                [], [], 
                '''                Specify VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
    'AddressPoolService' : {
        'meta_info' : _MetaInfoClass('AddressPoolService',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg', 'AddressPoolService.Vrfs', 
                [], [], 
                '''                Enter VRF specific config mode
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-daps-cfg', False),
            ],
            'Cisco-IOS-XR-ip-daps-cfg',
            'address-pool-service',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-daps-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_daps_cfg'
        ),
    },
}
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes.Exclude']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges.PrefixRange']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks.Network']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.AddressRanges']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Excludes']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.UtilizationMark']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.PrefixRanges']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool.Networks']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools.Pool']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6.Pools']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges.AddressRange']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes.Exclude']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks.Network']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.AddressRanges']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Excludes']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.UtilizationMark']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool.Networks']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools.Pool']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4.Pools']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv6']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf.Ipv4']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs.Vrf']['meta_info']
_meta_table['AddressPoolService.Vrfs.Vrf']['meta_info'].parent =_meta_table['AddressPoolService.Vrfs']['meta_info']
_meta_table['AddressPoolService.Vrfs']['meta_info'].parent =_meta_table['AddressPoolService']['meta_info']
