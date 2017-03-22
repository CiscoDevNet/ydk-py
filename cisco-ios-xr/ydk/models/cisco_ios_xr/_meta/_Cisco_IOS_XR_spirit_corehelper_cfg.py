


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Exception.File' : {
        'meta_info' : _MetaInfoClass('Exception.File',
            False, 
            [
            _MetaInfoClassMember('choice1', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Preference of the dump location
                ''',
                'choice1',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            _MetaInfoClassMember('choice2', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Preference of the dump location
                ''',
                'choice2',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            _MetaInfoClassMember('choice3', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Preference of the dump location
                ''',
                'choice3',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            ],
            'Cisco-IOS-XR-spirit-corehelper-cfg',
            'file',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-corehelper-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg'
        ),
    },
    'Exception' : {
        'meta_info' : _MetaInfoClass('Exception',
            False, 
            [
            _MetaInfoClassMember('file', REFERENCE_CLASS, 'File' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg', 'Exception.File', 
                [], [], 
                '''                Container for the order of preference
                ''',
                'file',
                'Cisco-IOS-XR-spirit-corehelper-cfg', False),
            ],
            'Cisco-IOS-XR-spirit-corehelper-cfg',
            'exception',
            _yang_ns._namespaces['Cisco-IOS-XR-spirit-corehelper-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_spirit_corehelper_cfg'
        ),
    },
}
_meta_table['Exception.File']['meta_info'].parent =_meta_table['Exception']['meta_info']
