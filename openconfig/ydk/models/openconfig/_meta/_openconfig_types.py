


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Address_FamilyIdentity' : {
        'meta_info' : _MetaInfoClass('Address_FamilyIdentity',
            False, 
            [
            ],
            'openconfig-types',
            'ADDRESS_FAMILY',
            _yang_ns._namespaces['openconfig-types'],
        'ydk.models.openconfig.openconfig_types'
        ),
    },
    'Ipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6Identity',
            False, 
            [
            ],
            'openconfig-types',
            'IPV6',
            _yang_ns._namespaces['openconfig-types'],
        'ydk.models.openconfig.openconfig_types'
        ),
    },
    'Ipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4Identity',
            False, 
            [
            ],
            'openconfig-types',
            'IPV4',
            _yang_ns._namespaces['openconfig-types'],
        'ydk.models.openconfig.openconfig_types'
        ),
    },
}
