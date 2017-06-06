


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CcbptpolicysourcetypeEnum' : _MetaInfoEnum('CcbptpolicysourcetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB',
        {
            'ciscoCbQos':'ciscoCbQos',
            'ciscoCbpBase':'ciscoCbpBase',
        }, 'CISCO-CBP-TARGET-TC-MIB', _yang_ns._namespaces['CISCO-CBP-TARGET-TC-MIB']),
    'CcbpttargettypeEnum' : _MetaInfoEnum('CcbpttargettypeEnum', 'ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB',
        {
            'genIf':'genIf',
            'atmPvc':'atmPvc',
            'frDlci':'frDlci',
            'entity':'entity',
            'fwZone':'fwZone',
            'fwZonePair':'fwZonePair',
            'aaaSession':'aaaSession',
        }, 'CISCO-CBP-TARGET-TC-MIB', _yang_ns._namespaces['CISCO-CBP-TARGET-TC-MIB']),
    'CcbpttargetdirectionEnum' : _MetaInfoEnum('CcbpttargetdirectionEnum', 'ydk.models.cisco_ios_xe.CISCO_CBP_TARGET_TC_MIB',
        {
            'undirected':'undirected',
            'input':'input',
            'output':'output',
            'inOut':'inOut',
        }, 'CISCO-CBP-TARGET-TC-MIB', _yang_ns._namespaces['CISCO-CBP-TARGET-TC-MIB']),
}
