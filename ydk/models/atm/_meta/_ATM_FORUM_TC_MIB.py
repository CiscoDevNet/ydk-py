


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TruthValue_Enum' : _MetaInfoEnum('TruthValue_Enum', 'ydk.models.atm.ATM_FORUM_TC_MIB',
        {
            'true':'TRUE',
            'false':'FALSE',
        }, 'ATM-FORUM-TC-MIB', _yang_ns._namespaces['ATM-FORUM-TC-MIB']),
    'AtmServiceCategory_Enum' : _MetaInfoEnum('AtmServiceCategory_Enum', 'ydk.models.atm.ATM_FORUM_TC_MIB',
        {
            'other':'OTHER',
            'cbr':'CBR',
            'rtVbr':'RTVBR',
            'nrtVbr':'NRTVBR',
            'abr':'ABR',
            'ubr':'UBR',
        }, 'ATM-FORUM-TC-MIB', _yang_ns._namespaces['ATM-FORUM-TC-MIB']),
}
