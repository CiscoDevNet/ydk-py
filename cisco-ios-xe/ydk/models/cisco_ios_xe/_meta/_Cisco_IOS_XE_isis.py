


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IsisRoutesLevelTypeEnum' : _MetaInfoEnum('IsisRoutesLevelTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_isis',
        {
            'level-1':'level_1',
            'level-1-2':'level_1_2',
            'level-2':'level_2',
        }, 'Cisco-IOS-XE-isis', _yang_ns._namespaces['Cisco-IOS-XE-isis']),
    'IsisLevelTypeEnum' : _MetaInfoEnum('IsisLevelTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_isis',
        {
            'level-1':'level_1',
            'level-1-2':'level_1_2',
            'level-2':'level_2',
        }, 'Cisco-IOS-XE-isis', _yang_ns._namespaces['Cisco-IOS-XE-isis']),
    'AuthenticationLevelTypeEnum' : _MetaInfoEnum('AuthenticationLevelTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_isis',
        {
            'level-1':'level_1',
            'level-2':'level_2',
        }, 'Cisco-IOS-XE-isis', _yang_ns._namespaces['Cisco-IOS-XE-isis']),
}
