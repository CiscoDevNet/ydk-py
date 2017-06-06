


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CbpexecutionstrategyEnum' : _MetaInfoEnum('CbpexecutionstrategyEnum', 'ydk.models.cisco_ios_xe.CISCO_CBP_TC_MIB',
        {
            'other':'other',
            'doUntilSuccess':'doUntilSuccess',
            'doUntilFailure':'doUntilFailure',
            'doAll':'doAll',
        }, 'CISCO-CBP-TC-MIB', _yang_ns._namespaces['CISCO-CBP-TC-MIB']),
}
