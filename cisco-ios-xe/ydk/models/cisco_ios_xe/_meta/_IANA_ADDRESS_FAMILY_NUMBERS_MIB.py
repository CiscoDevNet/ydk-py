


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AddressfamilynumbersEnum' : _MetaInfoEnum('AddressfamilynumbersEnum', 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB',
        {
            'other':'other',
            'ipV4':'ipV4',
            'ipV6':'ipV6',
            'nsap':'nsap',
            'hdlc':'hdlc',
            'bbn1822':'bbn1822',
            'all802':'all802',
            'e163':'e163',
            'e164':'e164',
            'f69':'f69',
            'x121':'x121',
            'ipx':'ipx',
            'appletalk':'appletalk',
            'decnetIV':'decnetIV',
            'banyanVines':'banyanVines',
            'e164withNsap':'e164withNsap',
            'dns':'dns',
            'distinguishedname':'distinguishedname',
            'asnumber':'asnumber',
            'xtpoveripv4':'xtpoveripv4',
            'xtpoveripv6':'xtpoveripv6',
            'xtpnativemodextp':'xtpnativemodextp',
            'reserved':'reserved',
        }, 'IANA-ADDRESS-FAMILY-NUMBERS-MIB', _yang_ns._namespaces['IANA-ADDRESS-FAMILY-NUMBERS-MIB']),
}
