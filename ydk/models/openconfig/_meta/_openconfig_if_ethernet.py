


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
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
    'SPEED_100Gb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_100Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_100Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_100Mb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_100Mb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_100Mb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_10Gb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_10Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_10Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_10Mb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_10Mb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_10Mb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_1Gb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_1Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_1Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_25Gb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_25Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_25Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_40Gb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_40Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_40Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_50Gb_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_50Gb_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_50Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'SPEED_UNKNOWN_Identity' : {
        'meta_info' : _MetaInfoClass('SPEED_UNKNOWN_Identity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_UNKNOWN',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
}
