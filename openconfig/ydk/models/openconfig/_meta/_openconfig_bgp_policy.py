


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BgpNextHopTypeEnum' : _MetaInfoEnum('BgpNextHopTypeEnum', 'ydk.models.openconfig.openconfig_bgp_policy',
        {
            'SELF':'SELF',
        }, 'openconfig-bgp-policy', _yang_ns._namespaces['openconfig-bgp-policy']),
    'BgpSetCommunityOptionTypeEnum' : _MetaInfoEnum('BgpSetCommunityOptionTypeEnum', 'ydk.models.openconfig.openconfig_bgp_policy',
        {
            'ADD':'ADD',
            'REMOVE':'REMOVE',
            'REPLACE':'REPLACE',
        }, 'openconfig-bgp-policy', _yang_ns._namespaces['openconfig-bgp-policy']),
    'BgpSetMedTypeEnum' : _MetaInfoEnum('BgpSetMedTypeEnum', 'ydk.models.openconfig.openconfig_bgp_policy',
        {
            'IGP':'IGP',
        }, 'openconfig-bgp-policy', _yang_ns._namespaces['openconfig-bgp-policy']),
}
