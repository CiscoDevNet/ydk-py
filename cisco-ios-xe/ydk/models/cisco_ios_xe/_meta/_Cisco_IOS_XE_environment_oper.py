


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SensorUnitsTypeEnum' : _MetaInfoEnum('SensorUnitsTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper',
        {
            'Watts':'Watts',
            'Celsius':'Celsius',
            'milliVolts':'milliVolts',
            'Amperes':'Amperes',
            'Volts-DC':'Volts_DC',
            'Volts-AC':'Volts_AC',
            'milliAmperes':'milliAmperes',
        }, 'Cisco-IOS-XE-environment-oper', _yang_ns._namespaces['Cisco-IOS-XE-environment-oper']),
    'EnvironmentSensors.EnvironmentSensor' : {
        'meta_info' : _MetaInfoClass('EnvironmentSensors.EnvironmentSensor',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the sensor component.
                This includes all physical components of the chasis - 
                both fixed and pluggable.
                ''',
                'name',
                'Cisco-IOS-XE-environment-oper', True),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the location where this slot is present.
                ''',
                'location',
                'Cisco-IOS-XE-environment-oper', True),
            _MetaInfoClassMember('current-reading', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Numerical value of current sensor reading in sensor-units.
                ''',
                'current_reading',
                'Cisco-IOS-XE-environment-oper', False),
            _MetaInfoClassMember('sensor-units', REFERENCE_ENUM_CLASS, 'SensorUnitsTypeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper', 'SensorUnitsTypeEnum', 
                [], [], 
                '''                Units corresponding to current-reading value.
                ''',
                'sensor_units',
                'Cisco-IOS-XE-environment-oper', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A description of current state of the sensor.
                ''',
                'state',
                'Cisco-IOS-XE-environment-oper', False),
            ],
            'Cisco-IOS-XE-environment-oper',
            'environment-sensor',
            _yang_ns._namespaces['Cisco-IOS-XE-environment-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper'
        ),
    },
    'EnvironmentSensors' : {
        'meta_info' : _MetaInfoClass('EnvironmentSensors',
            False, 
            [
            _MetaInfoClassMember('environment-sensor', REFERENCE_LIST, 'EnvironmentSensor' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper', 'EnvironmentSensors.EnvironmentSensor', 
                [], [], 
                '''                The list of components on the device chasis.
                ''',
                'environment_sensor',
                'Cisco-IOS-XE-environment-oper', False),
            ],
            'Cisco-IOS-XE-environment-oper',
            'environment-sensors',
            _yang_ns._namespaces['Cisco-IOS-XE-environment-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_environment_oper'
        ),
    },
}
_meta_table['EnvironmentSensors.EnvironmentSensor']['meta_info'].parent =_meta_table['EnvironmentSensors']['meta_info']
