


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the usergroup
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', True),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'usergroup-under-username',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-admin-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg'
        ),
    },
    'Aaa.Usernames.Username.UsergroupUnderUsernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username.UsergroupUnderUsernames',
            False, 
            [
            _MetaInfoClassMember('usergroup-under-username', REFERENCE_LIST, 'UsergroupUnderUsername' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername', 
                [], [], 
                '''                Name of the usergroup
                ''',
                'usergroup_under_username',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'usergroup-under-usernames',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-admin-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg'
        ),
    },
    'Aaa.Usernames.Username' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames.Username',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Username
                ''',
                'name',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', True),
            _MetaInfoClassMember('secret', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify the secret for the admin user
                ''',
                'secret',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            _MetaInfoClassMember('usergroup-under-usernames', REFERENCE_CLASS, 'UsergroupUnderUsernames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames.Username.UsergroupUnderUsernames', 
                [], [], 
                '''                Specify the usergroup to which this admin user
                belongs
                ''',
                'usergroup_under_usernames',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'username',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-admin-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg'
        ),
    },
    'Aaa.Usernames' : {
        'meta_info' : _MetaInfoClass('Aaa.Usernames',
            False, 
            [
            _MetaInfoClassMember('username', REFERENCE_LIST, 'Username' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames.Username', 
                [], [], 
                '''                Admin Username
                ''',
                'username',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'usernames',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-admin-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg'
        ),
    },
    'Aaa' : {
        'meta_info' : _MetaInfoClass('Aaa',
            False, 
            [
            _MetaInfoClassMember('usernames', REFERENCE_CLASS, 'Usernames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg', 'Aaa.Usernames', 
                [], [], 
                '''                Configure local username
                ''',
                'usernames',
                'Cisco-IOS-XR-aaa-locald-admin-cfg', False),
            ],
            'Cisco-IOS-XR-aaa-locald-admin-cfg',
            'aaa',
            _yang_ns._namespaces['Cisco-IOS-XR-aaa-locald-admin-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_locald_admin_cfg'
        ),
    },
}
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames.UsergroupUnderUsername']['meta_info'].parent =_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info']
_meta_table['Aaa.Usernames.Username.UsergroupUnderUsernames']['meta_info'].parent =_meta_table['Aaa.Usernames.Username']['meta_info']
_meta_table['Aaa.Usernames.Username']['meta_info'].parent =_meta_table['Aaa.Usernames']['meta_info']
_meta_table['Aaa.Usernames']['meta_info'].parent =_meta_table['Aaa']['meta_info']
