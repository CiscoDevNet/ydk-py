


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'OpenconfigSoftwareComponentIdentity' : {
        'meta_info' : _MetaInfoClass('OpenconfigSoftwareComponentIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'openconfig-software-component',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'OpenconfigHardwareComponentIdentity' : {
        'meta_info' : _MetaInfoClass('OpenconfigHardwareComponentIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'openconfig-hardware-component',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'TransceiverIdentity' : {
        'meta_info' : _MetaInfoClass('TransceiverIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'TRANSCEIVER',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'LinecardIdentity' : {
        'meta_info' : _MetaInfoClass('LinecardIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'LINECARD',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'PowerSupplyIdentity' : {
        'meta_info' : _MetaInfoClass('PowerSupplyIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'POWER-SUPPLY',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'CpuIdentity' : {
        'meta_info' : _MetaInfoClass('CpuIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'CPU',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'ModuleIdentity' : {
        'meta_info' : _MetaInfoClass('ModuleIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'MODULE',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'BackplaneIdentity' : {
        'meta_info' : _MetaInfoClass('BackplaneIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'BACKPLANE',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'ChassisIdentity' : {
        'meta_info' : _MetaInfoClass('ChassisIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'CHASSIS',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'FanIdentity' : {
        'meta_info' : _MetaInfoClass('FanIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'FAN',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'OperatingSystemIdentity' : {
        'meta_info' : _MetaInfoClass('OperatingSystemIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'OPERATING-SYSTEM',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'SensorIdentity' : {
        'meta_info' : _MetaInfoClass('SensorIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'SENSOR',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'PortIdentity' : {
        'meta_info' : _MetaInfoClass('PortIdentity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'PORT',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
}
