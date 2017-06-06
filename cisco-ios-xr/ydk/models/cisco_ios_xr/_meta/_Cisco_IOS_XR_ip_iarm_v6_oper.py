


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address',
            False, 
            [
            _MetaInfoClassMember('afi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('is-prefix-sid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is prefix_sid valid - valid only for IPV6
                addresses
                ''',
                'is_prefix_sid',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('is-primary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is address primary - valid only for IPv4
                addresses
                ''',
                'is_primary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('is-tentative', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is address valid/tentative - valid only for IPV6
                addresses
                ''',
                'is_tentative',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('producer', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Producer Name
                ''',
                'producer',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route Tag of the address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('address-xr', REFERENCE_CLASS, 'AddressXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr', 
                [], [], 
                '''                Address info
                ''',
                'address_xr',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('handle', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'handle',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Prefix Length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('referenced-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Referenced Interface - only valid for an
                unnumbered interface
                ''',
                'referenced_interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'network',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf.Networks' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Networks',
            False, 
            [
            _MetaInfoClassMember('network', REFERENCE_LIST, 'Network' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network', 
                [], [], 
                '''                An IPv6 Address in IPv6 ARM
                ''',
                'network',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'networks',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_',
            False, 
            [
            _MetaInfoClassMember('afi', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                AFI
                ''',
                'afi',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV4 Address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPV6 Address
                ''',
                'ipv6_address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_', 
                [], [], 
                '''                Address
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('is-prefix-sid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is prefix_sid valid - valid only for IPV6
                addresses
                ''',
                'is_prefix_sid',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('is-primary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is address primary - valid only for IPv4
                addresses
                ''',
                'is_primary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('is-tentative', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is address valid/tentative - valid only for IPV6
                addresses
                ''',
                'is_tentative',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('producer', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Producer Name
                ''',
                'producer',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route Tag of the address
                ''',
                'route_tag',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', True),
            _MetaInfoClassMember('address', REFERENCE_LIST, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address', 
                [], [], 
                '''                Address info
                ''',
                'address',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('referenced-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Referenced Interface - only valid for an
                unnumbered interface
                ''',
                'referenced_interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface', 
                [], [], 
                '''                An IPv6 address in IPv6 ARM
                ''',
                'interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces', 
                [], [], 
                '''                IPv6 ARM address database information by
                interface
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('networks', REFERENCE_CLASS, 'Networks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf.Networks', 
                [], [], 
                '''                IPv6 ARM address database information by
                network
                ''',
                'networks',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs.Vrf', 
                [], [], 
                '''                IPv6 ARM address database information in a VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Addresses' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Addresses',
            False, 
            [
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses.Vrfs', 
                [], [], 
                '''                IPv6 ARM address database information per VRF
                ''',
                'vrfs',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.Summary' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.Summary',
            False, 
            [
            _MetaInfoClassMember('address-conflict-count', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number of address conflicts
                ''',
                'address_conflict_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('db-master-version', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-ARM DB master version
                ''',
                'db_master_version',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('producer-count', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number of producers
                ''',
                'producer_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('unnumbered-conflict-count', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number of unnumbered interface conflicts
                ''',
                'unnumbered_conflict_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('vrf-count', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number of known VRFs
                ''',
                'vrf_count',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.VrfSummaries.VrfSummary' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.VrfSummaries.VrfSummary',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ip-iarm-v6-oper', True),
            _MetaInfoClassMember('vrf-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF ID
                ''',
                'vrf_id',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('vrf-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF Name
                ''',
                'vrf_name_xr',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm.VrfSummaries' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm.VrfSummaries',
            False, 
            [
            _MetaInfoClassMember('vrf-summary', REFERENCE_LIST, 'VrfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.VrfSummaries.VrfSummary', 
                [], [], 
                '''                IPv6 ARM VRF summary information
                ''',
                'vrf_summary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'vrf-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
    'Ipv6Arm' : {
        'meta_info' : _MetaInfoClass('Ipv6Arm',
            False, 
            [
            _MetaInfoClassMember('addresses', REFERENCE_CLASS, 'Addresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Addresses', 
                [], [], 
                '''                IPv6 ARM address database information
                ''',
                'addresses',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('multicast-host-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Default multicast host interface
                ''',
                'multicast_host_interface',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.Summary', 
                [], [], 
                '''                IPv6 ARM summary information
                ''',
                'summary',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            _MetaInfoClassMember('vrf-summaries', REFERENCE_CLASS, 'VrfSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper', 'Ipv6Arm.VrfSummaries', 
                [], [], 
                '''                IPv6 ARM VRFs summary information
                ''',
                'vrf_summaries',
                'Cisco-IOS-XR-ip-iarm-v6-oper', False),
            ],
            'Cisco-IOS-XR-ip-iarm-v6-oper',
            'ipv6arm',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-iarm-v6-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_iarm_v6_oper'
        ),
    },
}
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr.Address']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network.AddressXr']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Networks.Network']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Networks']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address.Address_']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface.Address']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces.Interface']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Networks']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf.Interfaces']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses.Vrfs']['meta_info']
_meta_table['Ipv6Arm.Addresses.Vrfs']['meta_info'].parent =_meta_table['Ipv6Arm.Addresses']['meta_info']
_meta_table['Ipv6Arm.VrfSummaries.VrfSummary']['meta_info'].parent =_meta_table['Ipv6Arm.VrfSummaries']['meta_info']
_meta_table['Ipv6Arm.Addresses']['meta_info'].parent =_meta_table['Ipv6Arm']['meta_info']
_meta_table['Ipv6Arm.Summary']['meta_info'].parent =_meta_table['Ipv6Arm']['meta_info']
_meta_table['Ipv6Arm.VrfSummaries']['meta_info'].parent =_meta_table['Ipv6Arm']['meta_info']
