


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RipIdentity' : {
        'meta_info' : _MetaInfoClass('RipIdentity',
            False, 
            [
            ],
            'cisco-routing-ext',
            'rip',
            _yang_ns._namespaces['cisco-routing-ext'],
        'ydk.models.cisco_ios_xe.cisco_routing_ext'
        ),
    },
    'BgpIdentity' : {
        'meta_info' : _MetaInfoClass('BgpIdentity',
            False, 
            [
            ],
            'cisco-routing-ext',
            'bgp',
            _yang_ns._namespaces['cisco-routing-ext'],
        'ydk.models.cisco_ios_xe.cisco_routing_ext'
        ),
    },
    'IsIsIdentity' : {
        'meta_info' : _MetaInfoClass('IsIsIdentity',
            False, 
            [
            ],
            'cisco-routing-ext',
            'is-is',
            _yang_ns._namespaces['cisco-routing-ext'],
        'ydk.models.cisco_ios_xe.cisco_routing_ext'
        ),
    },
    'EigrpIdentity' : {
        'meta_info' : _MetaInfoClass('EigrpIdentity',
            False, 
            [
            ],
            'cisco-routing-ext',
            'eigrp',
            _yang_ns._namespaces['cisco-routing-ext'],
        'ydk.models.cisco_ios_xe.cisco_routing_ext'
        ),
    },
    'MobileIdentity' : {
        'meta_info' : _MetaInfoClass('MobileIdentity',
            False, 
            [
            ],
            'cisco-routing-ext',
            'mobile',
            _yang_ns._namespaces['cisco-routing-ext'],
        'ydk.models.cisco_ios_xe.cisco_routing_ext'
        ),
    },
}
