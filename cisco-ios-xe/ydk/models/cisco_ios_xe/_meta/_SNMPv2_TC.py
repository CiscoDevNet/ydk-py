


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RowstatusEnum' : _MetaInfoEnum('RowstatusEnum', 'ydk.models.cisco_ios_xe.SNMPv2_TC',
        {
            'active':'active',
            'notInService':'notInService',
            'notReady':'notReady',
            'createAndGo':'createAndGo',
            'createAndWait':'createAndWait',
            'destroy':'destroy',
        }, 'SNMPv2-TC', _yang_ns._namespaces['SNMPv2-TC']),
    'TruthvalueEnum' : _MetaInfoEnum('TruthvalueEnum', 'ydk.models.cisco_ios_xe.SNMPv2_TC',
        {
            'true':'true',
            'false':'false',
        }, 'SNMPv2-TC', _yang_ns._namespaces['SNMPv2-TC']),
    'StoragetypeEnum' : _MetaInfoEnum('StoragetypeEnum', 'ydk.models.cisco_ios_xe.SNMPv2_TC',
        {
            'other':'other',
            'volatile':'volatile',
            'nonVolatile':'nonVolatile',
            'permanent':'permanent',
            'readOnly':'readOnly',
        }, 'SNMPv2-TC', _yang_ns._namespaces['SNMPv2-TC']),
}
