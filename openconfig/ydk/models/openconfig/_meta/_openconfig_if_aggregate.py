


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AggregationTypeEnum' : _MetaInfoEnum('AggregationTypeEnum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'LACP':'LACP',
            'STATIC':'STATIC',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpActivityTypeEnum' : _MetaInfoEnum('LacpActivityTypeEnum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'ACTIVE':'ACTIVE',
            'PASSIVE':'PASSIVE',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpSynchronizationTypeEnum' : _MetaInfoEnum('LacpSynchronizationTypeEnum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'IN_SYNC':'IN_SYNC',
            'OUT_SYNC':'OUT_SYNC',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpTimeoutTypeEnum' : _MetaInfoEnum('LacpTimeoutTypeEnum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'LONG':'LONG',
            'SHORT':'SHORT',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
    'LacpPeriodTypeEnum' : _MetaInfoEnum('LacpPeriodTypeEnum', 'ydk.models.openconfig.openconfig_if_aggregate',
        {
            'FAST':'FAST',
            'SLOW':'SLOW',
        }, 'openconfig-if-aggregate', _yang_ns._namespaces['openconfig-if-aggregate']),
}
