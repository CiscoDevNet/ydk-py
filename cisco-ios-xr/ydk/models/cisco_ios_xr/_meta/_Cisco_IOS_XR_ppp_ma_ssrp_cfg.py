


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ssrp.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Ssrp.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the profile
                ''',
                'name',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', True),
            _MetaInfoClassMember('max-hops', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                This specifies the maximum number of hops for
                packets on the SSO channel
                ''',
                'max_hops',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            _MetaInfoClassMember('peer-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                This specifies the remote end's IPv4-address
                for the SSO channel
                ''',
                'peer_ipv4_address',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-ssrp-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-ssrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg'
        ),
    },
    'Ssrp.Profiles' : {
        'meta_info' : _MetaInfoClass('Ssrp.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg', 'Ssrp.Profiles.Profile', 
                [], [], 
                '''                SSRP Profile configuration
                ''',
                'profile',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-ssrp-cfg',
            'profiles',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-ssrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg'
        ),
    },
    'Ssrp' : {
        'meta_info' : _MetaInfoClass('Ssrp',
            False, 
            [
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg', 'Ssrp.Profiles', 
                [], [], 
                '''                Table of SSRP Profiles
                ''',
                'profiles',
                'Cisco-IOS-XR-ppp-ma-ssrp-cfg', False),
            ],
            'Cisco-IOS-XR-ppp-ma-ssrp-cfg',
            'ssrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ppp-ma-ssrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ppp_ma_ssrp_cfg'
        ),
    },
}
_meta_table['Ssrp.Profiles.Profile']['meta_info'].parent =_meta_table['Ssrp.Profiles']['meta_info']
_meta_table['Ssrp.Profiles']['meta_info'].parent =_meta_table['Ssrp']['meta_info']
