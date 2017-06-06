


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AtmservicecategoryEnum' : _MetaInfoEnum('AtmservicecategoryEnum', 'ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB',
        {
            'other':'other',
            'cbr':'cbr',
            'rtVbr':'rtVbr',
            'nrtVbr':'nrtVbr',
            'abr':'abr',
            'ubr':'ubr',
        }, 'ATM-FORUM-TC-MIB', _yang_ns._namespaces['ATM-FORUM-TC-MIB']),
    'TruthvalueEnum' : _MetaInfoEnum('TruthvalueEnum', 'ydk.models.cisco_ios_xe.ATM_FORUM_TC_MIB',
        {
            'true':'true',
            'false':'false',
        }, 'ATM-FORUM-TC-MIB', _yang_ns._namespaces['ATM-FORUM-TC-MIB']),
}
