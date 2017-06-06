


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IetfMplsLabelEnum' : _MetaInfoEnum('IetfMplsLabelEnum', 'ydk.models.cisco_ios_xe.common_mpls_types',
        {
            'v4-explicit-null':'v4_explicit_null',
            'v6-explicit-null':'v6_explicit_null',
            'implicit-null':'implicit_null',
        }, 'common-mpls-types', _yang_ns._namespaces['common-mpls-types']),
}
