


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EthIfSpeedIdentity' : {
        'meta_info' : _MetaInfoClass('EthIfSpeedIdentity',
            False, 
            [
            ],
            'cisco-ethernet',
            'eth-if-speed',
            _yang_ns._namespaces['cisco-ethernet'],
        'ydk.models.cisco_ios_xe.cisco_ethernet'
        ),
    },
    'EthIfSpeed10GbIdentity' : {
        'meta_info' : _MetaInfoClass('EthIfSpeed10GbIdentity',
            False, 
            [
            ],
            'cisco-ethernet',
            'eth-if-speed-10gb',
            _yang_ns._namespaces['cisco-ethernet'],
        'ydk.models.cisco_ios_xe.cisco_ethernet'
        ),
    },
    'EthIfSpeed100GbIdentity' : {
        'meta_info' : _MetaInfoClass('EthIfSpeed100GbIdentity',
            False, 
            [
            ],
            'cisco-ethernet',
            'eth-if-speed-100gb',
            _yang_ns._namespaces['cisco-ethernet'],
        'ydk.models.cisco_ios_xe.cisco_ethernet'
        ),
    },
    'EthIfSpeed10MbIdentity' : {
        'meta_info' : _MetaInfoClass('EthIfSpeed10MbIdentity',
            False, 
            [
            ],
            'cisco-ethernet',
            'eth-if-speed-10mb',
            _yang_ns._namespaces['cisco-ethernet'],
        'ydk.models.cisco_ios_xe.cisco_ethernet'
        ),
    },
    'EthIfSpeed100MbIdentity' : {
        'meta_info' : _MetaInfoClass('EthIfSpeed100MbIdentity',
            False, 
            [
            ],
            'cisco-ethernet',
            'eth-if-speed-100mb',
            _yang_ns._namespaces['cisco-ethernet'],
        'ydk.models.cisco_ios_xe.cisco_ethernet'
        ),
    },
    'EthIfSpeed40GbIdentity' : {
        'meta_info' : _MetaInfoClass('EthIfSpeed40GbIdentity',
            False, 
            [
            ],
            'cisco-ethernet',
            'eth-if-speed-40gb',
            _yang_ns._namespaces['cisco-ethernet'],
        'ydk.models.cisco_ios_xe.cisco_ethernet'
        ),
    },
    'EthIfSpeed1GbIdentity' : {
        'meta_info' : _MetaInfoClass('EthIfSpeed1GbIdentity',
            False, 
            [
            ],
            'cisco-ethernet',
            'eth-if-speed-1gb',
            _yang_ns._namespaces['cisco-ethernet'],
        'ydk.models.cisco_ios_xe.cisco_ethernet'
        ),
    },
}
