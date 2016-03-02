


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'TruthValue_Enum' : _MetaInfoEnum('TruthValue_Enum', 'ydk.models.snmpv2.SNMPv2_TC',
        {
            'true':'TRUE',
            'false':'FALSE',
        }, 'SNMPv2-TC', _yang_ns._namespaces['SNMPv2-TC']),
    'StorageType_Enum' : _MetaInfoEnum('StorageType_Enum', 'ydk.models.snmpv2.SNMPv2_TC',
        {
            'other':'OTHER',
            'volatile':'VOLATILE',
            'nonVolatile':'NONVOLATILE',
            'permanent':'PERMANENT',
            'readOnly':'READONLY',
        }, 'SNMPv2-TC', _yang_ns._namespaces['SNMPv2-TC']),
    'RowStatus_Enum' : _MetaInfoEnum('RowStatus_Enum', 'ydk.models.snmpv2.SNMPv2_TC',
        {
            'active':'ACTIVE',
            'notInService':'NOTINSERVICE',
            'notReady':'NOTREADY',
            'createAndGo':'CREATEANDGO',
            'createAndWait':'CREATEANDWAIT',
            'destroy':'DESTROY',
        }, 'SNMPv2-TC', _yang_ns._namespaces['SNMPv2-TC']),
}
