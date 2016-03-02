


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'AddressFamilyNumbers_Enum' : _MetaInfoEnum('AddressFamilyNumbers_Enum', 'ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB',
        {
            'other':'OTHER',
            'ipV4':'IPV4',
            'ipV6':'IPV6',
            'nsap':'NSAP',
            'hdlc':'HDLC',
            'bbn1822':'BBN1822',
            'all802':'ALL802',
            'e163':'E163',
            'e164':'E164',
            'f69':'F69',
            'x121':'X121',
            'ipx':'IPX',
            'appletalk':'APPLETALK',
            'decnetIV':'DECNETIV',
            'banyanVines':'BANYANVINES',
            'e164withNsap':'E164WITHNSAP',
            'dns':'DNS',
            'distinguishedname':'DISTINGUISHEDNAME',
            'asnumber':'ASNUMBER',
            'xtpoveripv4':'XTPOVERIPV4',
            'xtpoveripv6':'XTPOVERIPV6',
            'xtpnativemodextp':'XTPNATIVEMODEXTP',
            'reserved':'RESERVED',
        }, 'IANA-ADDRESS-FAMILY-NUMBERS-MIB', _yang_ns._namespaces['IANA-ADDRESS-FAMILY-NUMBERS-MIB']),
}
