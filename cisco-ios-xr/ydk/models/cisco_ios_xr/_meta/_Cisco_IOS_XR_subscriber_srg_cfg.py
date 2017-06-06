


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SrgAddrFamilyEnum' : _MetaInfoEnum('SrgAddrFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-subscriber-srg-cfg', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg']),
    'SubscriberRedundancyGroupRoleEnum' : _MetaInfoEnum('SubscriberRedundancyGroupRoleEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg',
        {
            'master':'master',
            'slave':'slave',
        }, 'Cisco-IOS-XR-subscriber-srg-cfg', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg']),
    'SubscriberRedundancyGroupSlaveModeEnum' : _MetaInfoEnum('SubscriberRedundancyGroupSlaveModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg',
        {
            'warm':'warm',
            'hot':'hot',
        }, 'Cisco-IOS-XR-subscriber-srg-cfg', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg']),
    'SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-srg-cfg', True),
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface Id for the interface
                ''',
                'interface_id',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface', 
                [], [], 
                '''                Interface for this Group
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-srg-cfg', True),
            _MetaInfoClassMember('sub-interface-range-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Sub Interface Start Range
                ''',
                'sub_interface_range_start',
                'Cisco-IOS-XR-subscriber-srg-cfg', True),
            _MetaInfoClassMember('sub-interface-range-end', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Sub Interface End Range
                ''',
                'sub_interface_range_end',
                'Cisco-IOS-XR-subscriber-srg-cfg', True),
            _MetaInfoClassMember('interface-id-range-end', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface ID End Range
                ''',
                'interface_id_range_end',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('interface-id-range-start', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface ID Start Range
                ''',
                'interface_id_range_start',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'interface-range',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges',
            False, 
            [
            _MetaInfoClassMember('interface-range', REFERENCE_LIST, 'InterfaceRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange', 
                [], [], 
                '''                Interface for this Group
                ''',
                'interface_range',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'interface-ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.InterfaceList' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.InterfaceList',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable List of Interfaces for this Group.
                Deletion of this object also causes deletion
                of all associated objects under InterfaceList
                .
                ''',
                'enable',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('interface-ranges', REFERENCE_CLASS, 'InterfaceRanges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges', 
                [], [], 
                '''                Table of InterfaceRange
                ''',
                'interface_ranges',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces', 
                [], [], 
                '''                Table of Interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'interface-list',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.Peer.Ipaddress' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.Peer.Ipaddress',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'SrgAddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SrgAddrFamilyEnum', 
                [], [], 
                '''                Type of IPv4/IPv6 address
                ''',
                'address_family',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('prefix-string', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4/IPv6 address
                ''',
                'prefix_string',
                'Cisco-IOS-XR-subscriber-srg-cfg', False, [
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/IPv6 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/IPv6 address
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'ipaddress',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.Peer' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.Peer',
            False, 
            [
            _MetaInfoClassMember('ipaddress', REFERENCE_CLASS, 'Ipaddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.Peer.Ipaddress', 
                [], [], 
                '''                IPv4 or IPv6 Address of SRG Peer
                ''',
                'ipaddress',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('route-add-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set Route add disable
                ''',
                'route_add_disable',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.RevertiveTimer' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.RevertiveTimer',
            False, 
            [
            _MetaInfoClassMember('max-value', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Value of MAX Revertive Timer
                ''',
                'max_value',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Value of revertive time in minutes
                ''',
                'value',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'revertive-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.VirtualMac' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.VirtualMac',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Virtual MAC Address for this Group
                ''',
                'address',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Virtual MAC Address for this Group
                ''',
                'disable',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'virtual-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Route' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Route',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'SrgAddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SrgAddrFamilyEnum', 
                [], [], 
                '''                Type of IPv4 address with prefix-length
                ''',
                'address_family',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('prefix-string', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 address with prefix-length
                ''',
                'prefix_string',
                'Cisco-IOS-XR-subscriber-srg-cfg', False, [
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address with prefix-length
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 address with prefix-length
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                ]),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag value
                ''',
                'value',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'ipv4-route',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoute' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoute',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'SrgAddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SrgAddrFamilyEnum', 
                [], [], 
                '''                Type of IPv6 address with prefix-length
                ''',
                'address_family',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('prefix-string', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address with prefix-length
                ''',
                'prefix_string',
                'Cisco-IOS-XR-subscriber-srg-cfg', False, [
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address with prefix-length
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address with prefix-length
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                ]),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag value
                ''',
                'value',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'ipv6na-route',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoute' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoute',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_ENUM_CLASS, 'SrgAddrFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SrgAddrFamilyEnum', 
                [], [], 
                '''                Type of IPv6 address with prefix-length
                ''',
                'address_family',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Prefix of the IP Address
                ''',
                'prefix_length',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('prefix-string', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv6 address with prefix-length
                ''',
                'prefix_string',
                'Cisco-IOS-XR-subscriber-srg-cfg', False, [
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address with prefix-length
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                    _MetaInfoClassMember('prefix-string', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv6 address with prefix-length
                        ''',
                        'prefix_string',
                        'Cisco-IOS-XR-subscriber-srg-cfg', False),
                ]),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag value
                ''',
                'value',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'ipv6pd-route',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route',
            False, 
            [
            _MetaInfoClassMember('ipv6na-route', REFERENCE_CLASS, 'Ipv6NaRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoute', 
                [], [], 
                '''                None
                ''',
                'ipv6na_route',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('ipv6pd-route', REFERENCE_CLASS, 'Ipv6PdRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoute', 
                [], [], 
                '''                None
                ''',
                'ipv6pd_route',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'ipv6-route',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group.StateControlRoute' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group.StateControlRoute',
            False, 
            [
            _MetaInfoClassMember('ipv4-route', REFERENCE_CLASS, 'Ipv4Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Route', 
                [], [], 
                '''                None
                ''',
                'ipv4_route',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('ipv6-route', REFERENCE_CLASS, 'Ipv6Route' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route', 
                [], [], 
                '''                None
                ''',
                'ipv6_route',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'state-control-route',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups.Group' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '500')], [], 
                '''                Group ID
                ''',
                'group_id',
                'Cisco-IOS-XR-subscriber-srg-cfg', True),
            _MetaInfoClassMember('access-tracking-object', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Access Tracking Object for this Group
                ''',
                'access_tracking_object',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('core-tracking-object', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Core Tracking Object for this Group
                ''',
                'core_tracking_object',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description for this Group
                ''',
                'description',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('disable-tracking-object', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Tracking Object for this Group
                ''',
                'disable_tracking_object',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Redundancy Group configuration.
                Deletion of this object also causes deletion
                of all associated objects under Group.
                ''',
                'enable',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('enable-fast-switchover', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable fast switchover for this Group
                ''',
                'enable_fast_switchover',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Set hold time (in Minutes)
                ''',
                'hold_timer',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('interface-list', REFERENCE_CLASS, 'InterfaceList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.InterfaceList', 
                [], [], 
                '''                List of Interfaces for this Group
                ''',
                'interface_list',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('l2tp-source-ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Enter an IP address
                ''',
                'l2tp_source_ip_address',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('peer', REFERENCE_CLASS, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.Peer', 
                [], [], 
                '''                None
                ''',
                'peer',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SubscriberRedundancyGroupRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupRoleEnum', 
                [], [], 
                '''                Set preferred role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('redundancy-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable
                ''',
                'redundancy_disable',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('revertive-timer', REFERENCE_CLASS, 'RevertiveTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.RevertiveTimer', 
                [], [], 
                '''                None
                ''',
                'revertive_timer',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SubscriberRedundancyGroupSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupSlaveModeEnum', 
                [], [], 
                '''                Set Slave Mode
                ''',
                'slave_mode',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('state-control-route', REFERENCE_CLASS, 'StateControlRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.StateControlRoute', 
                [], [], 
                '''                None
                ''',
                'state_control_route',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('virtual-mac', REFERENCE_CLASS, 'VirtualMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group.VirtualMac', 
                [], [], 
                '''                Virtual MAC Address for this Group
                ''',
                'virtual_mac',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.Groups' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups.Group', 
                [], [], 
                '''                Redundancy Group configuration
                ''',
                'group',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy.RevertiveTimer' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy.RevertiveTimer',
            False, 
            [
            _MetaInfoClassMember('max-value', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Value of MAX Revertive Timer
                ''',
                'max_value',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Value of revertive time in minutes
                ''',
                'value',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'revertive-timer',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
    'SubscriberRedundancy' : {
        'meta_info' : _MetaInfoClass('SubscriberRedundancy',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Subscriber Redundancy configuration.
                Deletion of this object also causes deletion of
                all associated objects under
                SubscriberRedundancy.
                ''',
                'enable',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.Groups', 
                [], [], 
                '''                Table of Group
                ''',
                'groups',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Set hold time (in Minutes)
                ''',
                'hold_timer',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('preferred-role', REFERENCE_ENUM_CLASS, 'SubscriberRedundancyGroupRoleEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupRoleEnum', 
                [], [], 
                '''                Set preferred role
                ''',
                'preferred_role',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('redundancy-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable
                ''',
                'redundancy_disable',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('revertive-timer', REFERENCE_CLASS, 'RevertiveTimer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancy.RevertiveTimer', 
                [], [], 
                '''                None
                ''',
                'revertive_timer',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('slave-mode', REFERENCE_ENUM_CLASS, 'SubscriberRedundancyGroupSlaveModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg', 'SubscriberRedundancyGroupSlaveModeEnum', 
                [], [], 
                '''                Set slave
                ''',
                'slave_mode',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Source Interface for Redundancy Peer
                Communication
                ''',
                'source_interface',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            _MetaInfoClassMember('virtual-mac-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Virtual MAC Prefix for Subscriber Redundancy
                ''',
                'virtual_mac_prefix',
                'Cisco-IOS-XR-subscriber-srg-cfg', False),
            ],
            'Cisco-IOS-XR-subscriber-srg-cfg',
            'subscriber-redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-srg-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_srg_cfg'
        ),
    },
}
_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces.Interface']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges.InterfaceRange']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.Interfaces']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList.InterfaceRanges']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.Peer.Ipaddress']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.Peer']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6NaRoute']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route.Ipv6PdRoute']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv4Route']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute.Ipv6Route']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.InterfaceList']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.Peer']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.RevertiveTimer']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.VirtualMac']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group.StateControlRoute']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups.Group']['meta_info']
_meta_table['SubscriberRedundancy.Groups.Group']['meta_info'].parent =_meta_table['SubscriberRedundancy.Groups']['meta_info']
_meta_table['SubscriberRedundancy.Groups']['meta_info'].parent =_meta_table['SubscriberRedundancy']['meta_info']
_meta_table['SubscriberRedundancy.RevertiveTimer']['meta_info'].parent =_meta_table['SubscriberRedundancy']['meta_info']
