


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DynamictemplatetargettypeEnum' : _MetaInfoEnum('DynamictemplatetargettypeEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB',
        {
            'other':'other',
            'interface':'interface',
        }, 'CISCO-DYNAMIC-TEMPLATE-TC-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-TC-MIB']),
    'DynamictemplatetypeEnum' : _MetaInfoEnum('DynamictemplatetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_DYNAMIC_TEMPLATE_TC_MIB',
        {
            'other':'other',
            'derived':'derived',
            'ppp':'ppp',
            'ethernet':'ethernet',
            'ipSubscriber':'ipSubscriber',
            'service':'service',
        }, 'CISCO-DYNAMIC-TEMPLATE-TC-MIB', _yang_ns._namespaces['CISCO-DYNAMIC-TEMPLATE-TC-MIB']),
}
