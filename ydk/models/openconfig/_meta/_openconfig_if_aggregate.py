


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AggregationType_Enum' : _MetaInfoEnum('AggregationType_Enum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'LACP':'LACP',
            'STATIC':'STATIC',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpTimeoutType_Enum' : _MetaInfoEnum('LacpTimeoutType_Enum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'LONG':'LONG',
            'SHORT':'SHORT',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpPeriodType_Enum' : _MetaInfoEnum('LacpPeriodType_Enum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'FAST':'FAST',
            'SLOW':'SLOW',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpActivityType_Enum' : _MetaInfoEnum('LacpActivityType_Enum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'ACTIVE':'ACTIVE',
            'PASSIVE':'PASSIVE',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpSynchronizationType_Enum' : _MetaInfoEnum('LacpSynchronizationType_Enum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'IN_SYNC':'IN_SYNC',
            'OUT_SYNC':'OUT_SYNC',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
}
