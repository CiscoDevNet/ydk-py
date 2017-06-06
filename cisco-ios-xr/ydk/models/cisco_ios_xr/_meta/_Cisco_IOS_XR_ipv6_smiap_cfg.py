


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ipv6Virtual.Vrfs.Vrf.Address' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual.Vrfs.Vrf.Address',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPv6 address prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-smiap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg'
        ),
    },
    'Ipv6Virtual.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-smiap-cfg', True),
            _MetaInfoClassMember('address', REFERENCE_CLASS, 'Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg', 'Ipv6Virtual.Vrfs.Vrf.Address', 
                [], [], 
                '''                IPv6 address and mask
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-smiap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg'
        ),
    },
    'Ipv6Virtual.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg', 'Ipv6Virtual.Vrfs.Vrf', 
                [], [], 
                '''                A VRF for a virtual IPv6 address.  Specify
                'default' for VRF default
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-smiap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg'
        ),
    },
    'Ipv6Virtual' : {
        'meta_info' : _MetaInfoClass('Ipv6Virtual',
            False, 
            [
            _MetaInfoClassMember('use-as-source-address', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable use as default source address on sourced
                packets
                ''',
                'use_as_source_address',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg', 'Ipv6Virtual.Vrfs', 
                [], [], 
                '''                VRFs for the virtual IPv6 addresses
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-smiap-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-smiap-cfg',
            'ipv6-virtual',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-smiap-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_smiap_cfg'
        ),
    },
}
_meta_table['Ipv6Virtual.Vrfs.Vrf.Address']['meta_info'].parent =_meta_table['Ipv6Virtual.Vrfs.Vrf']['meta_info']
_meta_table['Ipv6Virtual.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ipv6Virtual.Vrfs']['meta_info']
_meta_table['Ipv6Virtual.Vrfs']['meta_info'].parent =_meta_table['Ipv6Virtual']['meta_info']
