


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator',
            False, 
            [
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Remote Discriminator Value
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', True),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'remote-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address' : {
        'meta_info' : _MetaInfoClass('Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                 IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ip-sbfd-cfg', True),
            _MetaInfoClassMember('remote-discriminator', REFERENCE_LIST, 'RemoteDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator', 
                [], [], 
                '''                Remote Discriminator value
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.RemoteTarget.Ipv4Addresses' : {
        'meta_info' : _MetaInfoClass('Sbfd.RemoteTarget.Ipv4Addresses',
            False, 
            [
            _MetaInfoClassMember('ipv4-address', REFERENCE_LIST, 'Ipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address', 
                [], [], 
                '''                IP Address Value for RemoteDiscriminatorTable
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'ipv4-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator',
            False, 
            [
            _MetaInfoClassMember('remote-discriminator', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Remote Discriminator Value
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', True),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'remote-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address' : {
        'meta_info' : _MetaInfoClass('Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                 IPv6 adddress
                ''',
                'address',
                'Cisco-IOS-XR-ip-sbfd-cfg', True),
            _MetaInfoClassMember('remote-discriminator', REFERENCE_LIST, 'RemoteDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator', 
                [], [], 
                '''                Remote Discriminator value
                ''',
                'remote_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'ipv6-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.RemoteTarget.Ipv6Addresses' : {
        'meta_info' : _MetaInfoClass('Sbfd.RemoteTarget.Ipv6Addresses',
            False, 
            [
            _MetaInfoClassMember('ipv6-address', REFERENCE_LIST, 'Ipv6Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address', 
                [], [], 
                '''                IP Address Value for RemoteDiscriminatorTable
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'ipv6-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.RemoteTarget' : {
        'meta_info' : _MetaInfoClass('Sbfd.RemoteTarget',
            False, 
            [
            _MetaInfoClassMember('ipv4-addresses', REFERENCE_CLASS, 'Ipv4Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.RemoteTarget.Ipv4Addresses', 
                [], [], 
                '''                ipv4 address as target
                ''',
                'ipv4_addresses',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            _MetaInfoClassMember('ipv6-addresses', REFERENCE_CLASS, 'Ipv6Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.RemoteTarget.Ipv6Addresses', 
                [], [], 
                '''                ipv6 address as target
                ''',
                'ipv6_addresses',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'remote-target',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-sbfd-cfg', True),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'intf-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.IntfDiscriminators' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.IntfDiscriminators',
            False, 
            [
            _MetaInfoClassMember('intf-discriminator', REFERENCE_LIST, 'IntfDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator', 
                [], [], 
                '''                interface address as discriminator
                ''',
                'intf_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'intf-discriminators',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator',
            False, 
            [
            _MetaInfoClassMember('discriminator', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                Dynamic discriminator value
                ''',
                'discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', True),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'dynamic-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.DynamicDiscriminators' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.DynamicDiscriminators',
            False, 
            [
            _MetaInfoClassMember('dynamic-discriminator', REFERENCE_LIST, 'DynamicDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator', 
                [], [], 
                '''                Local discriminator value
                ''',
                'dynamic_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'dynamic-discriminators',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                 IPv4 address
                ''',
                'address',
                'Cisco-IOS-XR-ip-sbfd-cfg', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                         IPv4 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ip-sbfd-cfg', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                         IPv4 address
                        ''',
                        'address',
                        'Cisco-IOS-XR-ip-sbfd-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'ipv4-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.Ipv4Discriminators' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.Ipv4Discriminators',
            False, 
            [
            _MetaInfoClassMember('ipv4-discriminator', REFERENCE_LIST, 'Ipv4Discriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator', 
                [], [], 
                '''                ipv4 address as discriminator
                ''',
                'ipv4_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'ipv4-discriminators',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator',
            False, 
            [
            _MetaInfoClassMember('discriminator', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Local discriminator value
                ''',
                'discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', True),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'val32-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator.Val32Discriminators' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator.Val32Discriminators',
            False, 
            [
            _MetaInfoClassMember('val32-discriminator', REFERENCE_LIST, 'Val32Discriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator', 
                [], [], 
                '''                Local discriminator value
                ''',
                'val32_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'val32-discriminators',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd.LocalDiscriminator' : {
        'meta_info' : _MetaInfoClass('Sbfd.LocalDiscriminator',
            False, 
            [
            _MetaInfoClassMember('dynamic-discriminators', REFERENCE_CLASS, 'DynamicDiscriminators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.DynamicDiscriminators', 
                [], [], 
                '''                Configure local discriminator dynamically
                ''',
                'dynamic_discriminators',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            _MetaInfoClassMember('intf-discriminators', REFERENCE_CLASS, 'IntfDiscriminators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.IntfDiscriminators', 
                [], [], 
                '''                Configure local discriminator from interface
                address
                ''',
                'intf_discriminators',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            _MetaInfoClassMember('ipv4-discriminators', REFERENCE_CLASS, 'Ipv4Discriminators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.Ipv4Discriminators', 
                [], [], 
                '''                Configure local discriminator as an ipv4
                address
                ''',
                'ipv4_discriminators',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            _MetaInfoClassMember('val32-discriminators', REFERENCE_CLASS, 'Val32Discriminators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator.Val32Discriminators', 
                [], [], 
                '''                Configure local discriminator as an integer
                ''',
                'val32_discriminators',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'local-discriminator',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
    'Sbfd' : {
        'meta_info' : _MetaInfoClass('Sbfd',
            False, 
            [
            _MetaInfoClassMember('local-discriminator', REFERENCE_CLASS, 'LocalDiscriminator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.LocalDiscriminator', 
                [], [], 
                '''                Configure local discriminator
                ''',
                'local_discriminator',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            _MetaInfoClassMember('remote-target', REFERENCE_CLASS, 'RemoteTarget' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg', 'Sbfd.RemoteTarget', 
                [], [], 
                '''                configure remote target
                ''',
                'remote_target',
                'Cisco-IOS-XR-ip-sbfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-sbfd-cfg',
            'sbfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-sbfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_sbfd_cfg'
        ),
    },
}
_meta_table['Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address.RemoteDiscriminator']['meta_info'].parent =_meta_table['Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address']['meta_info']
_meta_table['Sbfd.RemoteTarget.Ipv4Addresses.Ipv4Address']['meta_info'].parent =_meta_table['Sbfd.RemoteTarget.Ipv4Addresses']['meta_info']
_meta_table['Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address.RemoteDiscriminator']['meta_info'].parent =_meta_table['Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address']['meta_info']
_meta_table['Sbfd.RemoteTarget.Ipv6Addresses.Ipv6Address']['meta_info'].parent =_meta_table['Sbfd.RemoteTarget.Ipv6Addresses']['meta_info']
_meta_table['Sbfd.RemoteTarget.Ipv4Addresses']['meta_info'].parent =_meta_table['Sbfd.RemoteTarget']['meta_info']
_meta_table['Sbfd.RemoteTarget.Ipv6Addresses']['meta_info'].parent =_meta_table['Sbfd.RemoteTarget']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.IntfDiscriminators.IntfDiscriminator']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator.IntfDiscriminators']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.DynamicDiscriminators.DynamicDiscriminator']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator.DynamicDiscriminators']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.Ipv4Discriminators.Ipv4Discriminator']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator.Ipv4Discriminators']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.Val32Discriminators.Val32Discriminator']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator.Val32Discriminators']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.IntfDiscriminators']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.DynamicDiscriminators']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.Ipv4Discriminators']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator']['meta_info']
_meta_table['Sbfd.LocalDiscriminator.Val32Discriminators']['meta_info'].parent =_meta_table['Sbfd.LocalDiscriminator']['meta_info']
_meta_table['Sbfd.RemoteTarget']['meta_info'].parent =_meta_table['Sbfd']['meta_info']
_meta_table['Sbfd.LocalDiscriminator']['meta_info'].parent =_meta_table['Sbfd']['meta_info']
