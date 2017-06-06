


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CpwvctypeEnum' : _MetaInfoEnum('CpwvctypeEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB',
        {
            'other':'other',
            'frameRelay':'frameRelay',
            'atmAal5Vcc':'atmAal5Vcc',
            'atmTransparent':'atmTransparent',
            'ethernetVLAN':'ethernetVLAN',
            'ethernet':'ethernet',
            'hdlc':'hdlc',
            'ppp':'ppp',
            'cep':'cep',
            'atmVccCell':'atmVccCell',
            'atmVpcCell':'atmVpcCell',
            'ethernetVPLS':'ethernetVPLS',
            'e1Satop':'e1Satop',
            't1Satop':'t1Satop',
            'e3Satop':'e3Satop',
            't3Satop':'t3Satop',
            'basicCesPsn':'basicCesPsn',
            'basicTdmIp':'basicTdmIp',
            'tdmCasCesPsn':'tdmCasCesPsn',
            'tdmCasTdmIp':'tdmCasTdmIp',
        }, 'CISCO-IETF-PW-TC-MIB', _yang_ns._namespaces['CISCO-IETF-PW-TC-MIB']),
    'CpwoperstatusEnum' : _MetaInfoEnum('CpwoperstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_IETF_PW_TC_MIB',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
            'unknown':'unknown',
            'dormant':'dormant',
            'notPresent':'notPresent',
            'lowerLayerDown':'lowerLayerDown',
        }, 'CISCO-IETF-PW-TC-MIB', _yang_ns._namespaces['CISCO-IETF-PW-TC-MIB']),
}
