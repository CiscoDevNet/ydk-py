


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'NeighborOrigin_Enum' : _MetaInfoEnum('NeighborOrigin_Enum', 'ydk.models.openconfig.openconfig_if_ip',
        {
            'OTHER':'OTHER',
            'STATIC':'STATIC',
            'DYNAMIC':'DYNAMIC',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
    'IpAddressOrigin_Enum' : _MetaInfoEnum('IpAddressOrigin_Enum', 'ydk.models.openconfig.openconfig_if_ip',
        {
            'OTHER':'OTHER',
            'STATIC':'STATIC',
            'DHCP':'DHCP',
            'LINK_LAYER':'LINK_LAYER',
            'RANDOM':'RANDOM',
        }, 'openconfig-if-ip', _yang_ns._namespaces['openconfig-if-ip']),
}
