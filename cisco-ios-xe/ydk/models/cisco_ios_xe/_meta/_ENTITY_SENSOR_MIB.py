


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EntitysensordatatypeEnum' : _MetaInfoEnum('EntitysensordatatypeEnum', 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB',
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
        }, 'ENTITY-SENSOR-MIB', _yang_ns._namespaces['ENTITY-SENSOR-MIB']),
    'EntitysensorstatusEnum' : _MetaInfoEnum('EntitysensorstatusEnum', 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB',
        {
            'ok':'ok',
            'unavailable':'unavailable',
            'nonoperational':'nonoperational',
        }, 'ENTITY-SENSOR-MIB', _yang_ns._namespaces['ENTITY-SENSOR-MIB']),
    'EntitysensordatascaleEnum' : _MetaInfoEnum('EntitysensordatascaleEnum', 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB',
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
        }, 'ENTITY-SENSOR-MIB', _yang_ns._namespaces['ENTITY-SENSOR-MIB']),
    'EntitySensorMib.Entphysensortable.Entphysensorentry' : {
        'meta_info' : _MetaInfoClass('EntitySensorMib.Entphysensortable.Entphysensorentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'ENTITY-SENSOR-MIB', True),
            _MetaInfoClassMember('entPhySensorOperStatus', REFERENCE_ENUM_CLASS, 'EntitysensorstatusEnum' , 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB', 'EntitysensorstatusEnum', 
                [], [], 
                '''                The operational status of the sensor.
                ''',
                'entphysensoroperstatus',
                'ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entPhySensorPrecision', ATTRIBUTE, 'int' , None, None, 
                [('-8', '9')], [], 
                '''                The number of decimal places of precision in fixed-point
                sensor values returned by the associated entPhySensorValue
                object.
                
                This object SHOULD be set to '0' when the associated
                entPhySensorType value is not a fixed-point type: e.g.,
                'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.
                
                This object SHOULD be set by the agent during entry
                creation, and the value SHOULD NOT change during operation.
                ''',
                'entphysensorprecision',
                'ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entPhySensorScale', REFERENCE_ENUM_CLASS, 'EntitysensordatascaleEnum' , 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB', 'EntitysensordatascaleEnum', 
                [], [], 
                '''                The exponent to apply to values returned by the associated
                entPhySensorValue object.
                
                This object SHOULD be set by the agent during entry
                creation, and the value SHOULD NOT change during operation.
                ''',
                'entphysensorscale',
                'ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entPhySensorType', REFERENCE_ENUM_CLASS, 'EntitysensordatatypeEnum' , 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB', 'EntitysensordatatypeEnum', 
                [], [], 
                '''                The type of data returned by the associated
                entPhySensorValue object.
                
                This object SHOULD be set by the agent during entry
                creation, and the value SHOULD NOT change during operation.
                ''',
                'entphysensortype',
                'ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entPhySensorUnitsDisplay', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual description of the data units that should be used
                in the display of entPhySensorValue.
                ''',
                'entphysensorunitsdisplay',
                'ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entPhySensorValue', ATTRIBUTE, 'int' , None, None, 
                [('-1000000000', '1073741823')], [], 
                '''                The most recent measurement obtained by the agent for this
                sensor.
                
                To correctly interpret the value of this object, the
                associated entPhySensorType, entPhySensorScale, and
                entPhySensorPrecision objects must also be examined.
                ''',
                'entphysensorvalue',
                'ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entPhySensorValueTimeStamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time the status and/or value
                of this sensor was last obtained by the agent.
                ''',
                'entphysensorvaluetimestamp',
                'ENTITY-SENSOR-MIB', False),
            _MetaInfoClassMember('entPhySensorValueUpdateRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An indication of the frequency that the agent updates the
                associated entPhySensorValue object, representing in
                milliseconds.
                
                The value zero indicates:
                
                    - the sensor value is updated on demand (e.g.,
                      when polled by the agent for a get-request),
                    - the sensor value is updated when the sensor
                      value changes (event-driven),
                    - the agent does not know the update rate.
                ''',
                'entphysensorvalueupdaterate',
                'ENTITY-SENSOR-MIB', False),
            ],
            'ENTITY-SENSOR-MIB',
            'entPhySensorEntry',
            _yang_ns._namespaces['ENTITY-SENSOR-MIB'],
        'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB'
        ),
    },
    'EntitySensorMib.Entphysensortable' : {
        'meta_info' : _MetaInfoClass('EntitySensorMib.Entphysensortable',
            False, 
            [
            _MetaInfoClassMember('entPhySensorEntry', REFERENCE_LIST, 'Entphysensorentry' , 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB', 'EntitySensorMib.Entphysensortable.Entphysensorentry', 
                [], [], 
                '''                Information about a particular physical sensor.
                
                An entry in this table describes the present reading of a
                sensor, the measurement units and scale, and sensor
                operational status.
                
                Entries are created in this table by the agent.  An entry
                for each physical sensor SHOULD be created at the same time
                as the associated entPhysicalEntry.  An entry SHOULD be
                destroyed if the associated entPhysicalEntry is destroyed.
                ''',
                'entphysensorentry',
                'ENTITY-SENSOR-MIB', False),
            ],
            'ENTITY-SENSOR-MIB',
            'entPhySensorTable',
            _yang_ns._namespaces['ENTITY-SENSOR-MIB'],
        'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB'
        ),
    },
    'EntitySensorMib' : {
        'meta_info' : _MetaInfoClass('EntitySensorMib',
            False, 
            [
            _MetaInfoClassMember('entPhySensorTable', REFERENCE_CLASS, 'Entphysensortable' , 'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB', 'EntitySensorMib.Entphysensortable', 
                [], [], 
                '''                This table contains one row per physical sensor represented
                by an associated row in the entPhysicalTable.
                ''',
                'entphysensortable',
                'ENTITY-SENSOR-MIB', False),
            ],
            'ENTITY-SENSOR-MIB',
            'ENTITY-SENSOR-MIB',
            _yang_ns._namespaces['ENTITY-SENSOR-MIB'],
        'ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB'
        ),
    },
}
_meta_table['EntitySensorMib.Entphysensortable.Entphysensorentry']['meta_info'].parent =_meta_table['EntitySensorMib.Entphysensortable']['meta_info']
_meta_table['EntitySensorMib.Entphysensortable']['meta_info'].parent =_meta_table['EntitySensorMib']['meta_info']
