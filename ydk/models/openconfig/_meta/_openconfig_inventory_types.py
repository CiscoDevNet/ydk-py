


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'OpenconfigSoftwareComponent_Identity' : {
        'meta_info' : _MetaInfoClass('OpenconfigSoftwareComponent_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'openconfig-software-component',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'OpenconfigHardwareComponent_Identity' : {
        'meta_info' : _MetaInfoClass('OpenconfigHardwareComponent_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'openconfig-hardware-component',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Cpu_Identity' : {
        'meta_info' : _MetaInfoClass('Cpu_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'CPU',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Module_Identity' : {
        'meta_info' : _MetaInfoClass('Module_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'MODULE',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Port_Identity' : {
        'meta_info' : _MetaInfoClass('Port_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'PORT',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Linecard_Identity' : {
        'meta_info' : _MetaInfoClass('Linecard_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'LINECARD',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Backplane_Identity' : {
        'meta_info' : _MetaInfoClass('Backplane_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'BACKPLANE',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Chassis_Identity' : {
        'meta_info' : _MetaInfoClass('Chassis_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'CHASSIS',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Fan_Identity' : {
        'meta_info' : _MetaInfoClass('Fan_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'FAN',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'OperatingSystem_Identity' : {
        'meta_info' : _MetaInfoClass('OperatingSystem_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'OPERATING-SYSTEM',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Transceiver_Identity' : {
        'meta_info' : _MetaInfoClass('Transceiver_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'TRANSCEIVER',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'PowerSupply_Identity' : {
        'meta_info' : _MetaInfoClass('PowerSupply_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'POWER-SUPPLY',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'Sensor_Identity' : {
        'meta_info' : _MetaInfoClass('Sensor_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'SENSOR',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
}
