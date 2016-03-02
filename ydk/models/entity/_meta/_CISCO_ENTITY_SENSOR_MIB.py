


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'SensorThresholdSeverity_Enum' : _MetaInfoEnum('SensorThresholdSeverity_Enum', 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB',
        {
            'other':'OTHER',
            'minor':'MINOR',
            'major':'MAJOR',
            'critical':'CRITICAL',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensorStatus_Enum' : _MetaInfoEnum('SensorStatus_Enum', 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB',
        {
            'ok':'OK',
            'unavailable':'UNAVAILABLE',
            'nonoperational':'NONOPERATIONAL',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensorDataType_Enum' : _MetaInfoEnum('SensorDataType_Enum', 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB',
        {
            'other':'OTHER',
            'unknown':'UNKNOWN',
            'voltsAC':'VOLTSAC',
            'voltsDC':'VOLTSDC',
            'amperes':'AMPERES',
            'watts':'WATTS',
            'hertz':'HERTZ',
            'celsius':'CELSIUS',
            'percentRH':'PERCENTRH',
            'rpm':'RPM',
            'cmm':'CMM',
            'truthvalue':'TRUTHVALUE',
            'specialEnum':'SPECIALENUM',
            'dBm':'DBM',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensorThresholdRelation_Enum' : _MetaInfoEnum('SensorThresholdRelation_Enum', 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB',
        {
            'lessThan':'LESSTHAN',
            'lessOrEqual':'LESSOREQUAL',
            'greaterThan':'GREATERTHAN',
            'greaterOrEqual':'GREATEROREQUAL',
            'equalTo':'EQUALTO',
            'notEqualTo':'NOTEQUALTO',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensorDataScale_Enum' : _MetaInfoEnum('SensorDataScale_Enum', 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB',
        {
            'yocto':'YOCTO',
            'zepto':'ZEPTO',
            'atto':'ATTO',
            'femto':'FEMTO',
            'pico':'PICO',
            'nano':'NANO',
            'micro':'MICRO',
            'milli':'MILLI',
            'units':'UNITS',
            'kilo':'KILO',
            'mega':'MEGA',
            'giga':'GIGA',
            'tera':'TERA',
            'exa':'EXA',
            'peta':'PETA',
            'zetta':'ZETTA',
            'yotta':'YOTTA',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'CISCOENTITYSENSORMIB.EntSensorGlobalObjects' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYSENSORMIB.EntSensorGlobalObjects',
            False, 
            [
            _MetaInfoClassMember('entSensorThreshNotifGlobalEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable enables the generation of
                entSensorThresholdNotification globally
                on the device. If this object value is
                'false', then no entSensorThresholdNotification
                will be generated on this device. If this object
                value is 'true', then whether a 
                entSensorThresholdNotification for a threshold will
                be generated or not depends on the instance value of
                entSensorThresholdNotificationEnable for that
                threshold.
                ''',
                'entsensorthreshnotifglobalenable',
                'CISCO-ENTITY-SENSOR-MIB', False),
            ],
            'CISCO-ENTITY-SENSOR-MIB',
            'entSensorGlobalObjects',
            _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB'],
        'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-SENSOR-MIB', True),
            _MetaInfoClassMember('entSensorThresholdIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 99999999)], [], 
                '''                An index that uniquely identifies an entry
                in the entSensorThresholdTable. This index
                permits the same sensor to have several 
                different thresholds.
                ''',
                'entsensorthresholdindex',
                'CISCO-ENTITY-SENSOR-MIB', True),
            _MetaInfoClassMember('entSensorThresholdEvaluation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable indicates the result of the most
                recent evaluation of the threshold.  If the threshold
                condition is true, entSensorThresholdEvaluation 
                is true(1).  If the threshold condition is false, 
                entSensorThresholdEvaluation is false(2).
                
                Thresholds are evaluated at the rate indicated by 
                entSensorValueUpdateRate.
                ''',
                'entsensorthresholdevaluation',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorThresholdNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable controls generation of
                entSensorThresholdNotification for this threshold.
                
                When this variable is 'true', generation of 
                entSensorThresholdNotification is enabled for this
                threshold. When this variable is 'false', 
                generation of entSensorThresholdNotification is
                disabled for this threshold.
                ''',
                'entsensorthresholdnotificationenable',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorThresholdRelation', REFERENCE_ENUM_CLASS, 'SensorThresholdRelation_Enum' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'SensorThresholdRelation_Enum', 
                [], [], 
                '''                This variable indicates the relation between sensor value
                (entSensorValue) and threshold value (entSensorThresholdValue), 
                required to trigger the alarm.  when evaluating the relation, 
                entSensorValue is on the left of entSensorThresholdRelation, 
                entSensorThresholdValue is on the right. 
                
                in pseudo-code, the evaluation-alarm mechanism is:
                
                ...
                if (entSensorStatus == ok) then
                    if (evaluate(entSensorValue, entSensorThresholdRelation,  
                        entSensorThresholdValue)) 
                    then
                        if (entSensorThresholdNotificationEnable == true)) 
                        then
                            raise_alarm(sensor's entPhysicalIndex);
                        endif
                    endif
                endif
                ...
                ''',
                'entsensorthresholdrelation',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorThresholdSeverity', REFERENCE_ENUM_CLASS, 'SensorThresholdSeverity_Enum' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'SensorThresholdSeverity_Enum', 
                [], [], 
                '''                This variable indicates the severity of this threshold.
                ''',
                'entsensorthresholdseverity',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorThresholdValue', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                This variable indicates the value of the threshold.
                
                To correctly display or interpret this variable's value, 
                you must also know entSensorType, entSensorScale, and 
                entSensorPrecision.
                
                However, you can directly compare entSensorValue 
                with the threshold values given in entSensorThresholdTable 
                without any semantic knowledge.
                ''',
                'entsensorthresholdvalue',
                'CISCO-ENTITY-SENSOR-MIB', False),
            ],
            'CISCO-ENTITY-SENSOR-MIB',
            'entSensorThresholdEntry',
            _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB'],
        'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CISCOENTITYSENSORMIB.EntSensorThresholdTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYSENSORMIB.EntSensorThresholdTable',
            False, 
            [
            _MetaInfoClassMember('entSensorThresholdEntry', REFERENCE_LIST, 'EntSensorThresholdEntry' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry', 
                [], [], 
                '''                An entSensorThresholdTable entry describes the
                thresholds for a sensor: the threshold severity,
                the threshold value, the relation, and the 
                evaluation of the threshold.
                
                Only entities of type sensor(8) are listed in this table.
                Only pre-configured thresholds are listed in this table.
                
                Users can create sensor-value monitoring instruments
                in different ways, such as RMON alarms, Expression-MIB, etc.
                
                Entries are created by the agent at system startup and
                FRU insertion.  Entries are deleted by the agent at
                FRU removal.
                ''',
                'entsensorthresholdentry',
                'CISCO-ENTITY-SENSOR-MIB', False),
            ],
            'CISCO-ENTITY-SENSOR-MIB',
            'entSensorThresholdTable',
            _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB'],
        'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-SENSOR-MIB', True),
            _MetaInfoClassMember('entSensorMeasuredEntity', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object identifies the physical entity for which the
                sensor is taking measurements.  For example, for a sensor
                measuring the voltage output of a power-supply, this object
                would be the entPhysicalIndex of that power-supply; for a sensor
                measuring the temperature inside one chassis of a multi-chassis
                system, this object would be the enPhysicalIndex of that
                chassis.
                
                This object has a value of zero when the physical entity
                for which the sensor is taking measurements can not be
                represented by any one row in the entPhysicalTable, or that
                there is no such physical entity.
                ''',
                'entsensormeasuredentity',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorPrecision', ATTRIBUTE, 'int' , None, None, 
                [(-8, 9)], [], 
                '''                This variable indicates the number of decimal
                places of precision in fixed-point
                sensor values reported by entSensorValue.
                
                This variable is set to 0 when entSensorType
                is not a fixed-point type: e.g.'percentRH(9)', 
                'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.
                
                This variable is set by the agent at start-up
                and the value does not change during operation.
                ''',
                'entsensorprecision',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorScale', REFERENCE_ENUM_CLASS, 'SensorDataScale_Enum' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'SensorDataScale_Enum', 
                [], [], 
                '''                This variable indicates the exponent to apply
                to sensor values reported by entSensorValue.
                
                This variable is set by the agent at start-up
                and the value does not change during operation.
                ''',
                'entsensorscale',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorStatus', REFERENCE_ENUM_CLASS, 'SensorStatus_Enum' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'SensorStatus_Enum', 
                [], [], 
                '''                This variable indicates the present operational status
                of the sensor.
                ''',
                'entsensorstatus',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorType', REFERENCE_ENUM_CLASS, 'SensorDataType_Enum' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'SensorDataType_Enum', 
                [], [], 
                '''                This variable indicates the type of data
                reported by the entSensorValue.
                
                This variable is set by the agent at start-up
                and the value does not change during operation.
                ''',
                'entsensortype',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorValue', ATTRIBUTE, 'int' , None, None, 
                [(-1000000000, 1000000000)], [], 
                '''                This variable reports the most recent measurement seen
                by the sensor.
                
                To correctly display or interpret this variable's value, 
                you must also know entSensorType, entSensorScale, and 
                entSensorPrecision.
                
                However, you can compare entSensorValue with the threshold
                values given in entSensorThresholdTable without any semantic
                knowledge.
                ''',
                'entsensorvalue',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorValueTimeStamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This variable indicates the age of the value reported by
                entSensorValue
                ''',
                'entsensorvaluetimestamp',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorValueUpdateRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 999999999)], [], 
                '''                This variable indicates the rate that the agent
                updates entSensorValue.
                ''',
                'entsensorvalueupdaterate',
                'CISCO-ENTITY-SENSOR-MIB', False),
            ],
            'CISCO-ENTITY-SENSOR-MIB',
            'entSensorValueEntry',
            _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB'],
        'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CISCOENTITYSENSORMIB.EntSensorValueTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYSENSORMIB.EntSensorValueTable',
            False, 
            [
            _MetaInfoClassMember('entSensorValueEntry', REFERENCE_LIST, 'EntSensorValueEntry' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry', 
                [], [], 
                '''                An entSensorValueTable entry describes the
                present reading of a sensor, the measurement units
                and scale, and sensor operational status.
                ''',
                'entsensorvalueentry',
                'CISCO-ENTITY-SENSOR-MIB', False),
            ],
            'CISCO-ENTITY-SENSOR-MIB',
            'entSensorValueTable',
            _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB'],
        'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CISCOENTITYSENSORMIB' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYSENSORMIB',
            False, 
            [
            _MetaInfoClassMember('entSensorGlobalObjects', REFERENCE_CLASS, 'EntSensorGlobalObjects' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'CISCOENTITYSENSORMIB.EntSensorGlobalObjects', 
                [], [], 
                '''                ''',
                'entsensorglobalobjects',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorThresholdTable', REFERENCE_CLASS, 'EntSensorThresholdTable' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'CISCOENTITYSENSORMIB.EntSensorThresholdTable', 
                [], [], 
                '''                This table lists the threshold severity, relation, and
                comparison value, for a sensor listed in the Entity-MIB 
                entPhysicalTable.
                ''',
                'entsensorthresholdtable',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorValueTable', REFERENCE_CLASS, 'EntSensorValueTable' , 'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB', 'CISCOENTITYSENSORMIB.EntSensorValueTable', 
                [], [], 
                '''                This table lists the type, scale, and present value
                of a sensor listed in the Entity-MIB entPhysicalTable.
                ''',
                'entsensorvaluetable',
                'CISCO-ENTITY-SENSOR-MIB', False),
            ],
            'CISCO-ENTITY-SENSOR-MIB',
            'CISCO-ENTITY-SENSOR-MIB',
            _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB'],
        'ydk.models.entity.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
}
_meta_table['CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry']['meta_info'].parent =_meta_table['CISCOENTITYSENSORMIB.EntSensorThresholdTable']['meta_info']
_meta_table['CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry']['meta_info'].parent =_meta_table['CISCOENTITYSENSORMIB.EntSensorValueTable']['meta_info']
_meta_table['CISCOENTITYSENSORMIB.EntSensorGlobalObjects']['meta_info'].parent =_meta_table['CISCOENTITYSENSORMIB']['meta_info']
_meta_table['CISCOENTITYSENSORMIB.EntSensorThresholdTable']['meta_info'].parent =_meta_table['CISCOENTITYSENSORMIB']['meta_info']
_meta_table['CISCOENTITYSENSORMIB.EntSensorValueTable']['meta_info'].parent =_meta_table['CISCOENTITYSENSORMIB']['meta_info']
