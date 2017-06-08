


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'TrafficSelectorFormatIdentity' : {
        'meta_info' : _MetaInfoClass('TrafficSelectorFormatIdentity',
            False, 
            [
            ],
            'ietf-traffic-selector-types',
            'traffic-selector-format',
            _yang_ns._namespaces['ietf-traffic-selector-types'],
        'ydk.models.ietf.ietf_traffic_selector_types'
        ),
    },
    'Ipv4BinarySelectorFormatIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4BinarySelectorFormatIdentity',
            False, 
            [
            ],
            'ietf-traffic-selector-types',
            'ipv4-binary-selector-format',
            _yang_ns._namespaces['ietf-traffic-selector-types'],
        'ydk.models.ietf.ietf_traffic_selector_types'
        ),
    },
    'Ipv6BinarySelectorFormatIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6BinarySelectorFormatIdentity',
            False, 
            [
            ],
            'ietf-traffic-selector-types',
            'ipv6-binary-selector-format',
            _yang_ns._namespaces['ietf-traffic-selector-types'],
        'ydk.models.ietf.ietf_traffic_selector_types'
        ),
    },
}
