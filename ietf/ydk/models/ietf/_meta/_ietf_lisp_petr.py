


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PetrIdentity' : {
        'meta_info' : _MetaInfoClass('PetrIdentity',
            False, 
            [
            ],
            'ietf-lisp-petr',
            'petr',
            _yang_ns._namespaces['ietf-lisp-petr'],
        'ydk.models.ietf.ietf_lisp_petr'
        ),
    },
}
