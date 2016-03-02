


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'OamCCVcState_Enum' : _MetaInfoEnum('OamCCVcState_Enum', 'ydk.models.atm.CISCO_ATM_EXT_MIB',
        {
            'verified':'VERIFIED',
            'aisrdi':'AISRDI',
            'notManaged':'NOTMANAGED',
        }, 'CISCO-ATM-EXT-MIB', _yang_ns._namespaces['CISCO-ATM-EXT-MIB']),
    'OamCCStatus_Enum' : _MetaInfoEnum('OamCCStatus_Enum', 'ydk.models.atm.CISCO_ATM_EXT_MIB',
        {
            'ready':'READY',
            'waitActiveResponse':'WAITACTIVERESPONSE',
            'waitActiveConfirm':'WAITACTIVECONFIRM',
            'active':'ACTIVE',
            'waitDeactiveConfirm':'WAITDEACTIVECONFIRM',
        }, 'CISCO-ATM-EXT-MIB', _yang_ns._namespaces['CISCO-ATM-EXT-MIB']),
}
