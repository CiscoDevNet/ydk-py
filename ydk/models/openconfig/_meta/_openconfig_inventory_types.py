


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
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
    'BACKPLANE_Identity' : {
        'meta_info' : _MetaInfoClass('BACKPLANE_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'BACKPLANE',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'CHASSIS_Identity' : {
        'meta_info' : _MetaInfoClass('CHASSIS_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'CHASSIS',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'CPU_Identity' : {
        'meta_info' : _MetaInfoClass('CPU_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'CPU',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'FAN_Identity' : {
        'meta_info' : _MetaInfoClass('FAN_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'FAN',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'LINECARD_Identity' : {
        'meta_info' : _MetaInfoClass('LINECARD_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'LINECARD',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'MODULE_Identity' : {
        'meta_info' : _MetaInfoClass('MODULE_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'MODULE',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'OPERATINGSYSTEM_Identity' : {
        'meta_info' : _MetaInfoClass('OPERATINGSYSTEM_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'OPERATING-SYSTEM',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'PORT_Identity' : {
        'meta_info' : _MetaInfoClass('PORT_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'PORT',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'POWERSUPPLY_Identity' : {
        'meta_info' : _MetaInfoClass('POWERSUPPLY_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'POWER-SUPPLY',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'SENSOR_Identity' : {
        'meta_info' : _MetaInfoClass('SENSOR_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'SENSOR',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
    'TRANSCEIVER_Identity' : {
        'meta_info' : _MetaInfoClass('TRANSCEIVER_Identity',
            False, 
            [
            ],
            'openconfig-inventory-types',
            'TRANSCEIVER',
            _yang_ns._namespaces['openconfig-inventory-types'],
        'ydk.models.openconfig.openconfig_inventory_types'
        ),
    },
}
