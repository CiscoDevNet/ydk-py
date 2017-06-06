


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EntityoperstateEnum' : _MetaInfoEnum('EntityoperstateEnum', 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB',
        {
            'unknown':'unknown',
            'disabled':'disabled',
            'enabled':'enabled',
            'testing':'testing',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
    'EntityusagestateEnum' : _MetaInfoEnum('EntityusagestateEnum', 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB',
        {
            'unknown':'unknown',
            'idle':'idle',
            'active':'active',
            'busy':'busy',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
    'EntityadminstateEnum' : _MetaInfoEnum('EntityadminstateEnum', 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB',
        {
            'unknown':'unknown',
            'locked':'locked',
            'shuttingDown':'shuttingDown',
            'unlocked':'unlocked',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
    'EntitystandbystatusEnum' : _MetaInfoEnum('EntitystandbystatusEnum', 'ydk.models.cisco_ios_xe.ENTITY_STATE_TC_MIB',
        {
            'unknown':'unknown',
            'hotStandby':'hotStandby',
            'coldStandby':'coldStandby',
            'providingService':'providingService',
        }, 'ENTITY-STATE-TC-MIB', _yang_ns._namespaces['ENTITY-STATE-TC-MIB']),
}
