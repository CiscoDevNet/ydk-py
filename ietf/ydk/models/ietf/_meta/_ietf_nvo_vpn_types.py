


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'VpntunneltypeEnum' : _MetaInfoEnum('VpntunneltypeEnum', 'ydk.models.ietf.ietf_nvo_vpn_types',
        {
            'NOP':'NOP',
            'MPLS':'MPLS',
            'MPLS-TP':'MPLS_TP',
        }, 'ietf-nvo-vpn-types', _yang_ns._namespaces['ietf-nvo-vpn-types']),
    'ProtectionroleEnum' : _MetaInfoEnum('ProtectionroleEnum', 'ydk.models.ietf.ietf_nvo_vpn_types',
        {
            'NOP':'NOP',
            'MAIN':'MAIN',
        }, 'ietf-nvo-vpn-types', _yang_ns._namespaces['ietf-nvo-vpn-types']),
    'ServicetypeEnum' : _MetaInfoEnum('ServicetypeEnum', 'ydk.models.ietf.ietf_nvo_vpn_types',
        {
            'l3vpn':'l3vpn',
            'l2vpn':'l2vpn',
        }, 'ietf-nvo-vpn-types', _yang_ns._namespaces['ietf-nvo-vpn-types']),
}
