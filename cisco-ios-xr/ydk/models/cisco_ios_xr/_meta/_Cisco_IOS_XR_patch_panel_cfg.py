


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PatchPanel' : {
        'meta_info' : _MetaInfoClass('PatchPanel',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable patch-panel service
                ''',
                'enable',
                'Cisco-IOS-XR-patch-panel-cfg', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address for patch-panel
                ''',
                'ipv4',
                'Cisco-IOS-XR-patch-panel-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Password name to be used for Authentication with
                Patch-Panel
                ''',
                'password',
                'Cisco-IOS-XR-patch-panel-cfg', False),
            _MetaInfoClassMember('user-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                User name to be used for Authentication with
                Patch-Panel
                ''',
                'user_name',
                'Cisco-IOS-XR-patch-panel-cfg', False),
            ],
            'Cisco-IOS-XR-patch-panel-cfg',
            'patch-panel',
            _yang_ns._namespaces['Cisco-IOS-XR-patch-panel-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_patch_panel_cfg'
        ),
    },
}
