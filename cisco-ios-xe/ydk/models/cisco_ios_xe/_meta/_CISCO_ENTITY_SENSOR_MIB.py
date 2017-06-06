


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SensordatatypeEnum' : _MetaInfoEnum('SensordatatypeEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB',
        {
            'other':'other',
            'unknown':'unknown',
            'voltsAC':'voltsAC',
            'voltsDC':'voltsDC',
            'amperes':'amperes',
            'watts':'watts',
            'hertz':'hertz',
            'celsius':'celsius',
            'percentRH':'percentRH',
            'rpm':'rpm',
            'cmm':'cmm',
            'truthvalue':'truthvalue',
            'specialEnum':'specialEnum',
            'dBm':'dBm',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensorthresholdrelationEnum' : _MetaInfoEnum('SensorthresholdrelationEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB',
        {
            'lessThan':'lessThan',
            'lessOrEqual':'lessOrEqual',
            'greaterThan':'greaterThan',
            'greaterOrEqual':'greaterOrEqual',
            'equalTo':'equalTo',
            'notEqualTo':'notEqualTo',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensordatascaleEnum' : _MetaInfoEnum('SensordatascaleEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB',
        {
            'yocto':'yocto',
            'zepto':'zepto',
            'atto':'atto',
            'femto':'femto',
            'pico':'pico',
            'nano':'nano',
            'micro':'micro',
            'milli':'milli',
            'units':'units',
            'kilo':'kilo',
            'mega':'mega',
            'giga':'giga',
            'tera':'tera',
            'exa':'exa',
            'peta':'peta',
            'zetta':'zetta',
            'yotta':'yotta',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensorthresholdseverityEnum' : _MetaInfoEnum('SensorthresholdseverityEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB',
        {
            'other':'other',
            'minor':'minor',
            'major':'major',
            'critical':'critical',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'SensorstatusEnum' : _MetaInfoEnum('SensorstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB',
        {
            'ok':'ok',
            'unavailable':'unavailable',
            'nonoperational':'nonoperational',
        }, 'CISCO-ENTITY-SENSOR-MIB', _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB']),
    'CiscoEntitySensorMib.Entsensorglobalobjects' : {
        'meta_info' : _MetaInfoClass('CiscoEntitySensorMib.Entsensorglobalobjects',
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-SENSOR-MIB', True),
            _MetaInfoClassMember('entSensorMeasuredEntity', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
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
                [('-8', '9')], [], 
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
            _MetaInfoClassMember('entSensorScale', REFERENCE_ENUM_CLASS, 'SensordatascaleEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'SensordatascaleEnum', 
                [], [], 
                '''                This variable indicates the exponent to apply
                to sensor values reported by entSensorValue.
                
                This variable is set by the agent at start-up
                and the value does not change during operation.
                ''',
                'entsensorscale',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorStatus', REFERENCE_ENUM_CLASS, 'SensorstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'SensorstatusEnum', 
                [], [], 
                '''                This variable indicates the present operational status
                of the sensor.
                ''',
                'entsensorstatus',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorType', REFERENCE_ENUM_CLASS, 'SensordatatypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'SensordatatypeEnum', 
                [], [], 
                '''                This variable indicates the type of data
                reported by the entSensorValue.
                
                This variable is set by the agent at start-up
                and the value does not change during operation.
                ''',
                'entsensortype',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorValue', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1073741823')], [], 
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
                [('0', '4294967295')], [], 
                '''                This variable indicates the age of the value reported by
                entSensorValue
                ''',
                'entsensorvaluetimestamp',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorValueUpdateRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '999999999')], [], 
                '''                This variable indicates the rate that the agent
                updates entSensorValue.
                ''',
                'entsensorvalueupdaterate',
                'CISCO-ENTITY-SENSOR-MIB', False),
            ],
            'CISCO-ENTITY-SENSOR-MIB',
            'entSensorValueEntry',
            _yang_ns._namespaces['CISCO-ENTITY-SENSOR-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CiscoEntitySensorMib.Entsensorvaluetable' : {
        'meta_info' : _MetaInfoClass('CiscoEntitySensorMib.Entsensorvaluetable',
            False, 
            [
            _MetaInfoClassMember('entSensorValueEntry', REFERENCE_LIST, 'Entsensorvalueentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-SENSOR-MIB', True),
            _MetaInfoClassMember('entSensorThresholdIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '99999999')], [], 
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
            _MetaInfoClassMember('entSensorThresholdRelation', REFERENCE_ENUM_CLASS, 'SensorthresholdrelationEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'SensorthresholdrelationEnum', 
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
            _MetaInfoClassMember('entSensorThresholdSeverity', REFERENCE_ENUM_CLASS, 'SensorthresholdseverityEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'SensorthresholdseverityEnum', 
                [], [], 
                '''                This variable indicates the severity of this threshold.
                ''',
                'entsensorthresholdseverity',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorThresholdValue', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1073741823')], [], 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CiscoEntitySensorMib.Entsensorthresholdtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntitySensorMib.Entsensorthresholdtable',
            False, 
            [
            _MetaInfoClassMember('entSensorThresholdEntry', REFERENCE_LIST, 'Entsensorthresholdentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
    'CiscoEntitySensorMib' : {
        'meta_info' : _MetaInfoClass('CiscoEntitySensorMib',
            False, 
            [
            _MetaInfoClassMember('entSensorGlobalObjects', REFERENCE_CLASS, 'Entsensorglobalobjects' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'CiscoEntitySensorMib.Entsensorglobalobjects', 
                [], [], 
                '''                ''',
                'entsensorglobalobjects',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorThresholdTable', REFERENCE_CLASS, 'Entsensorthresholdtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'CiscoEntitySensorMib.Entsensorthresholdtable', 
                [], [], 
                '''                This table lists the threshold severity, relation, and
                comparison value, for a sensor listed in the Entity-MIB 
                entPhysicalTable.
                ''',
                'entsensorthresholdtable',
                'CISCO-ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entSensorValueTable', REFERENCE_CLASS, 'Entsensorvaluetable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB', 'CiscoEntitySensorMib.Entsensorvaluetable', 
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
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB'
        ),
    },
}
_meta_table['CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry']['meta_info'].parent =_meta_table['CiscoEntitySensorMib.Entsensorvaluetable']['meta_info']
_meta_table['CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry']['meta_info'].parent =_meta_table['CiscoEntitySensorMib.Entsensorthresholdtable']['meta_info']
_meta_table['CiscoEntitySensorMib.Entsensorglobalobjects']['meta_info'].parent =_meta_table['CiscoEntitySensorMib']['meta_info']
_meta_table['CiscoEntitySensorMib.Entsensorvaluetable']['meta_info'].parent =_meta_table['CiscoEntitySensorMib']['meta_info']
_meta_table['CiscoEntitySensorMib.Entsensorthresholdtable']['meta_info'].parent =_meta_table['CiscoEntitySensorMib']['meta_info']
