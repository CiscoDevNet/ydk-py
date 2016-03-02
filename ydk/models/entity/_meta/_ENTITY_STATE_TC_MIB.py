


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'EntityStandbyStatus_Enum' : _MetaInfoEnum('EntityStandbyStatus_Enum', 'ydk.models.entity.ENTITY_STATE_TC_MIB',
        {
            'unknown':'UNKNOWN',
            'hotStandby':'HOTSTANDBY',
            'coldStandby':'COLDSTANDBY',
            'providingService':'PROVIDINGSERVICE',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
    'EntityOperState_Enum' : _MetaInfoEnum('EntityOperState_Enum', 'ydk.models.entity.ENTITY_STATE_TC_MIB',
        {
            'unknown':'UNKNOWN',
            'disabled':'DISABLED',
            'enabled':'ENABLED',
            'testing':'TESTING',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
    'EntityAdminState_Enum' : _MetaInfoEnum('EntityAdminState_Enum', 'ydk.models.entity.ENTITY_STATE_TC_MIB',
        {
            'unknown':'UNKNOWN',
            'locked':'LOCKED',
            'shuttingDown':'SHUTTINGDOWN',
            'unlocked':'UNLOCKED',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
    'EntityUsageState_Enum' : _MetaInfoEnum('EntityUsageState_Enum', 'ydk.models.entity.ENTITY_STATE_TC_MIB',
        {
            'unknown':'UNKNOWN',
            'idle':'IDLE',
            'active':'ACTIVE',
            'busy':'BUSY',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
}
