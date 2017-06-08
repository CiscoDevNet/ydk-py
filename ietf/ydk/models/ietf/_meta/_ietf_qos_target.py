


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'DirectionIdentity' : {
        'meta_info' : _MetaInfoClass('DirectionIdentity',
            False, 
            [
            ],
            'ietf-qos-target',
            'direction',
            _yang_ns._namespaces['ietf-qos-target'],
        'ydk.models.ietf.ietf_qos_target'
        ),
    },
    'InboundIdentity' : {
        'meta_info' : _MetaInfoClass('InboundIdentity',
            False, 
            [
            ],
            'ietf-qos-target',
            'inbound',
            _yang_ns._namespaces['ietf-qos-target'],
        'ydk.models.ietf.ietf_qos_target'
        ),
    },
    'OutboundIdentity' : {
        'meta_info' : _MetaInfoClass('OutboundIdentity',
            False, 
            [
            ],
            'ietf-qos-target',
            'outbound',
            _yang_ns._namespaces['ietf-qos-target'],
        'ydk.models.ietf.ietf_qos_target'
        ),
    },
}
