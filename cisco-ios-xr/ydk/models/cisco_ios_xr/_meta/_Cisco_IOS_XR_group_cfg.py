


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Groups.Group' : {
        'meta_info' : _MetaInfoClass('Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Group name
                ''',
                'group_name',
                'Cisco-IOS-XR-group-cfg', True),
            ],
            'Cisco-IOS-XR-group-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-group-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg'
        ),
    },
    'Groups' : {
        'meta_info' : _MetaInfoClass('Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg', 'Groups.Group', 
                [], [], 
                '''                Group config definition
                ''',
                'group',
                'Cisco-IOS-XR-group-cfg', False),
            ],
            'Cisco-IOS-XR-group-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-group-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg'
        ),
    },
    'ApplyGroups' : {
        'meta_info' : _MetaInfoClass('ApplyGroups',
            False, 
            [
            _MetaInfoClassMember('apply-group', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                apply-group name
                ''',
                'apply_group',
                'Cisco-IOS-XR-group-cfg', False),
            ],
            'Cisco-IOS-XR-group-cfg',
            'apply-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-group-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_group_cfg'
        ),
    },
}
_meta_table['Groups.Group']['meta_info'].parent =_meta_table['Groups']['meta_info']
