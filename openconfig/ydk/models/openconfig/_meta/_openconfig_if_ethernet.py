


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EthernetSpeedIdentity' : {
        'meta_info' : _MetaInfoClass('EthernetSpeedIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'ethernet-speed',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_40GbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_40GbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_40Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_10MbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_10MbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_10Mb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_25GbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_25GbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_25Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_1GbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_1GbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_1Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_UnknownIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_UnknownIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_UNKNOWN',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_10GbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_10GbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_10Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_100GbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_100GbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_100Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_100MbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_100MbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_100Mb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
    'Speed_50GbIdentity' : {
        'meta_info' : _MetaInfoClass('Speed_50GbIdentity',
            False, 
            [
            ],
            'openconfig-if-ethernet',
            'SPEED_50Gb',
            _yang_ns._namespaces['openconfig-if-ethernet'],
        'ydk.models.openconfig.openconfig_if_ethernet'
        ),
    },
}
