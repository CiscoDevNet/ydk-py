


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpAddressOriginEnum' : _MetaInfoEnum('IpAddressOriginEnum', 'ydk.models.openconfig.openconfig_if_ip',
        {
            'OTHER':'OTHER',
            'STATIC':'STATIC',
            'DHCP':'DHCP',
            'LINK_LAYER':'LINK_LAYER',
            'RANDOM':'RANDOM',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
    'NeighborOriginEnum' : _MetaInfoEnum('NeighborOriginEnum', 'ydk.models.openconfig.openconfig_if_ip',
        {
            'OTHER':'OTHER',
            'STATIC':'STATIC',
            'DYNAMIC':'DYNAMIC',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
}
