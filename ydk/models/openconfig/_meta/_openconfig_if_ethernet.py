


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'EthernetSpeed_Identity' : {
        'meta_info' : _MetaInfoClass('EthernetSpeed_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'ethernet-speed',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_40Gb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_40Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_40Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_100Mb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_100Mb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_100Mb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_Unknown_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_Unknown_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_UNKNOWN',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_100Gb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_100Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_100Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_50Gb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_50Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_50Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_25Gb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_25Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_25Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_1Gb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_1Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_1Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_10Gb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_10Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_10Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_10Mb_Identity' : {
        'meta_info' : _MetaInfoClass('Speed_10Mb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_10Mb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
}
