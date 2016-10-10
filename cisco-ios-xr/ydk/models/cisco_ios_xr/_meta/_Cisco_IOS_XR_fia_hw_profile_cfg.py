


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'HwModuleProfileConfig.Profile.Tcams.Tcam' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.Tcams.Tcam',
            False, 
            [
            _MetaInfoClassMember('address-type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                none
                ''',
                'address_type',
                'Cisco-IOS-XR-fia-hw-profile-cfg', True),
            _MetaInfoClassMember('communication-type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                none
                ''',
                'communication_type',
                'Cisco-IOS-XR-fia-hw-profile-cfg', True),
            _MetaInfoClassMember('table-type', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                none
                ''',
                'table_type',
                'Cisco-IOS-XR-fia-hw-profile-cfg', True),
            _MetaInfoClassMember('percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                curve out percentage of TCAM table entries
                ''',
                'percent',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'tcam',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile.Tcams' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile.Tcams',
            False, 
            [
            _MetaInfoClassMember('tcam', REFERENCE_LIST, 'Tcam' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.Tcams.Tcam', 
                [], [], 
                '''                In the tcam fib table, denotes the address
                type ipv4 or ipv6 and whether unicast or
                multicast
                ''',
                'tcam',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'tcams',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig.Profile' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig.Profile',
            False, 
            [
            _MetaInfoClassMember('tcams', REFERENCE_CLASS, 'Tcams' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile.Tcams', 
                [], [], 
                '''                Configure profile for TCAM LC cards
                ''',
                'tcams',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'profile',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
    'HwModuleProfileConfig' : {
        'meta_info' : _MetaInfoClass('HwModuleProfileConfig',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_CLASS, 'Profile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg', 'HwModuleProfileConfig.Profile', 
                [], [], 
                '''                Configure profile.
                ''',
                'profile',
                'Cisco-IOS-XR-fia-hw-profile-cfg', False),
            ],
            'Cisco-IOS-XR-fia-hw-profile-cfg',
            'hw-module-profile-config',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-hw-profile-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_hw_profile_cfg'
        ),
    },
}
_meta_table['HwModuleProfileConfig.Profile.Tcams.Tcam']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile.Tcams']['meta_info']
_meta_table['HwModuleProfileConfig.Profile.Tcams']['meta_info'].parent =_meta_table['HwModuleProfileConfig.Profile']['meta_info']
_meta_table['HwModuleProfileConfig.Profile']['meta_info'].parent =_meta_table['HwModuleProfileConfig']['meta_info']
