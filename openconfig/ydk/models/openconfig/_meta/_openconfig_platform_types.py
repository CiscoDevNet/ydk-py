


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Openconfig_Hardware_ComponentIdentity' : {
        'meta_info' : _MetaInfoClass('Openconfig_Hardware_ComponentIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'OPENCONFIG_HARDWARE_COMPONENT',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'Openconfig_Software_ComponentIdentity' : {
        'meta_info' : _MetaInfoClass('Openconfig_Software_ComponentIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'OPENCONFIG_SOFTWARE_COMPONENT',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'CpuIdentity' : {
        'meta_info' : _MetaInfoClass('CpuIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'CPU',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'SensorIdentity' : {
        'meta_info' : _MetaInfoClass('SensorIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'SENSOR',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'ModuleIdentity' : {
        'meta_info' : _MetaInfoClass('ModuleIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'MODULE',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'TransceiverIdentity' : {
        'meta_info' : _MetaInfoClass('TransceiverIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'TRANSCEIVER',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'FanIdentity' : {
        'meta_info' : _MetaInfoClass('FanIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'FAN',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'Operating_SystemIdentity' : {
        'meta_info' : _MetaInfoClass('Operating_SystemIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'OPERATING_SYSTEM',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'Power_SupplyIdentity' : {
        'meta_info' : _MetaInfoClass('Power_SupplyIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'POWER_SUPPLY',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'BackplaneIdentity' : {
        'meta_info' : _MetaInfoClass('BackplaneIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'BACKPLANE',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'LinecardIdentity' : {
        'meta_info' : _MetaInfoClass('LinecardIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'LINECARD',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'ChassisIdentity' : {
        'meta_info' : _MetaInfoClass('ChassisIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'CHASSIS',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
    'PortIdentity' : {
        'meta_info' : _MetaInfoClass('PortIdentity',
            False, 
            [
            ],
            'openconfig-platform-types',
            'PORT',
            _yang_ns._namespaces['openconfig-platform-types'],
        'ydk.models.openconfig.openconfig_platform_types'
        ),
    },
}
