""" CISCO_ENTITY_SENSOR_MIB 

The CISCO\-ENTITY\-SENSOR\-MIB is used to monitor
the values of sensors in the Entity\-MIB (RFC 2037) 
entPhysicalTable.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class SensorDataScale_Enum(Enum):
    """
    SensorDataScale_Enum

    International System of Units (SI) prefixes.

    """

    YOCTO = 1

    ZEPTO = 2

    ATTO = 3

    FEMTO = 4

    PICO = 5

    NANO = 6

    MICRO = 7

    MILLI = 8

    UNITS = 9

    KILO = 10

    MEGA = 11

    GIGA = 12

    TERA = 13

    EXA = 14

    PETA = 15

    ZETTA = 16

    YOTTA = 17


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorDataScale_Enum']


class SensorDataType_Enum(Enum):
    """
    SensorDataType_Enum

    sensor measurement data types.  valid values are\:
    other(1)\:        a measure other than those listed below
    unknown(2)\:      unknown measurement, or 
                     arbitrary, relative numbers    
    voltsAC(3)\:      electric potential
    voltsDC(4)\:      electric potential
    amperes(5)\:      electric current
    watts(6)\:        power
    hertz(7)\:        frequency
    celsius(8)\:      temperature
    percentRH(9)\:    percent relative humidity
    rpm(10)\:         shaft revolutions per minute
    cmm(11),\:        cubic meters per minute (airflow)
    truthvalue(12)\:  value takes { true(1), false(2) }
    specialEnum(13)\: value takes user defined enumerated values
    dBm(14)\:         dB relative to 1mW of power

    """

    OTHER = 1

    UNKNOWN = 2

    VOLTSAC = 3

    VOLTSDC = 4

    AMPERES = 5

    WATTS = 6

    HERTZ = 7

    CELSIUS = 8

    PERCENTRH = 9

    RPM = 10

    CMM = 11

    TRUTHVALUE = 12

    SPECIALENUM = 13

    DBM = 14


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorDataType_Enum']


class SensorStatus_Enum(Enum):
    """
    SensorStatus_Enum

    Indicates the operational status of the sensor.
    
    ok(1) means the agent can read the sensor 
    value.
    
    unavailable(2) means that the agent presently 
    can not report the sensor value.
    
    nonoperational(3) means that the agent believes
    the sensor is broken.  The sensor could have a 
    hard failure (disconnected wire), or a soft failure
    such as out\-of\-range, jittery, or wildly fluctuating
    readings.

    """

    OK = 1

    UNAVAILABLE = 2

    NONOPERATIONAL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorStatus_Enum']


class SensorThresholdRelation_Enum(Enum):
    """
    SensorThresholdRelation_Enum

    sensor threshold relational operator types.  valid values are\:
    
    lessThan(1)\:        if the sensor value is less than
                        the threshold value
    lessOrEqual(2)\:     if the sensor value is less than or equal to
                        the threshold value
    greaterThan(3)\:     if the sensor value is greater than 
                        the threshold value
    greaterOrEqual(4)\:  if the sensor value is greater than or equal
                        to the threshold value
    equalTo(5)\:         if the sensor value is equal to
                        the threshold value
    notEqualTo(6)\:      if the sensor value is not equal to
                        the threshold value

    """

    LESSTHAN = 1

    LESSOREQUAL = 2

    GREATERTHAN = 3

    GREATEROREQUAL = 4

    EQUALTO = 5

    NOTEQUALTO = 6


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorThresholdRelation_Enum']


class SensorThresholdSeverity_Enum(Enum):
    """
    SensorThresholdSeverity_Enum

    sensor threshold severity.  Valid values are\:
    
    other(1)    \: a severity other than those listed below.
    minor(10)   \: Minor Problem threshold.
    major(20)   \: Major Problem threshold.
    critical(30)\: Critical problem threshold. A system might shut
                  down the sensor associated FRU automatically if
                  the sensor value reach the critical problem
                  threshold.

    """

    OTHER = 1

    MINOR = 10

    MAJOR = 20

    CRITICAL = 30


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorThresholdSeverity_Enum']



class CISCOENTITYSENSORMIB(object):
    """
    
    
    .. attribute:: entsensorglobalobjects
    
    	
    	**type**\: :py:class:`EntSensorGlobalObjects <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.EntSensorGlobalObjects>`
    
    .. attribute:: entsensorthresholdtable
    
    	This table lists the threshold severity, relation, and comparison value, for a sensor listed in the Entity\-MIB  entPhysicalTable
    	**type**\: :py:class:`EntSensorThresholdTable <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.EntSensorThresholdTable>`
    
    .. attribute:: entsensorvaluetable
    
    	This table lists the type, scale, and present value of a sensor listed in the Entity\-MIB entPhysicalTable
    	**type**\: :py:class:`EntSensorValueTable <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.EntSensorValueTable>`
    
    

    """

    _prefix = 'cisco-entity'
    _revision = '2015-01-15'

    def __init__(self):
        self.entsensorglobalobjects = CISCOENTITYSENSORMIB.EntSensorGlobalObjects()
        self.entsensorglobalobjects.parent = self
        self.entsensorthresholdtable = CISCOENTITYSENSORMIB.EntSensorThresholdTable()
        self.entsensorthresholdtable.parent = self
        self.entsensorvaluetable = CISCOENTITYSENSORMIB.EntSensorValueTable()
        self.entsensorvaluetable.parent = self


    class EntSensorGlobalObjects(object):
        """
        
        
        .. attribute:: entsensorthreshnotifglobalenable
        
        	This variable enables the generation of entSensorThresholdNotification globally on the device. If this object value is 'false', then no entSensorThresholdNotification will be generated on this device. If this object value is 'true', then whether a  entSensorThresholdNotification for a threshold will be generated or not depends on the instance value of entSensorThresholdNotificationEnable for that threshold
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2015-01-15'

        def __init__(self):
            self.parent = None
            self.entsensorthreshnotifglobalenable = None

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorGlobalObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.entsensorthreshnotifglobalenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
            return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorGlobalObjects']['meta_info']


    class EntSensorThresholdTable(object):
        """
        This table lists the threshold severity, relation, and
        comparison value, for a sensor listed in the Entity\-MIB 
        entPhysicalTable.
        
        .. attribute:: entsensorthresholdentry
        
        	An entSensorThresholdTable entry describes the thresholds for a sensor\: the threshold severity, the threshold value, the relation, and the  evaluation of the threshold.  Only entities of type sensor(8) are listed in this table. Only pre\-configured thresholds are listed in this table.  Users can create sensor\-value monitoring instruments in different ways, such as RMON alarms, Expression\-MIB, etc.  Entries are created by the agent at system startup and FRU insertion.  Entries are deleted by the agent at FRU removal
        	**type**\: list of :py:class:`EntSensorThresholdEntry <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2015-01-15'

        def __init__(self):
            self.parent = None
            self.entsensorthresholdentry = YList()
            self.entsensorthresholdentry.parent = self
            self.entsensorthresholdentry.name = 'entsensorthresholdentry'


        class EntSensorThresholdEntry(object):
            """
            An entSensorThresholdTable entry describes the
            thresholds for a sensor\: the threshold severity,
            the threshold value, the relation, and the 
            evaluation of the threshold.
            
            Only entities of type sensor(8) are listed in this table.
            Only pre\-configured thresholds are listed in this table.
            
            Users can create sensor\-value monitoring instruments
            in different ways, such as RMON alarms, Expression\-MIB, etc.
            
            Entries are created by the agent at system startup and
            FRU insertion.  Entries are deleted by the agent at
            FRU removal.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entsensorthresholdindex
            
            	An index that uniquely identifies an entry in the entSensorThresholdTable. This index permits the same sensor to have several  different thresholds
            	**type**\: int
            
            	**range:** 1..99999999
            
            .. attribute:: entsensorthresholdevaluation
            
            	This variable indicates the result of the most recent evaluation of the threshold.  If the threshold condition is true, entSensorThresholdEvaluation  is true(1).  If the threshold condition is false,  entSensorThresholdEvaluation is false(2).  Thresholds are evaluated at the rate indicated by  entSensorValueUpdateRate
            	**type**\: bool
            
            .. attribute:: entsensorthresholdnotificationenable
            
            	This variable controls generation of entSensorThresholdNotification for this threshold.  When this variable is 'true', generation of  entSensorThresholdNotification is enabled for this threshold. When this variable is 'false',  generation of entSensorThresholdNotification is disabled for this threshold
            	**type**\: bool
            
            .. attribute:: entsensorthresholdrelation
            
            	This variable indicates the relation between sensor value (entSensorValue) and threshold value (entSensorThresholdValue),  required to trigger the alarm.  when evaluating the relation,  entSensorValue is on the left of entSensorThresholdRelation,  entSensorThresholdValue is on the right.   in pseudo\-code, the evaluation\-alarm mechanism is\:  ... if (entSensorStatus == ok) then     if (evaluate(entSensorValue, entSensorThresholdRelation,           entSensorThresholdValue))      then         if (entSensorThresholdNotificationEnable == true))          then             raise\_alarm(sensor's entPhysicalIndex);         endif     endif endif ..
            	**type**\: :py:class:`SensorThresholdRelation_Enum <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.SensorThresholdRelation_Enum>`
            
            .. attribute:: entsensorthresholdseverity
            
            	This variable indicates the severity of this threshold
            	**type**\: :py:class:`SensorThresholdSeverity_Enum <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.SensorThresholdSeverity_Enum>`
            
            .. attribute:: entsensorthresholdvalue
            
            	This variable indicates the value of the threshold.  To correctly display or interpret this variable's value,  you must also know entSensorType, entSensorScale, and  entSensorPrecision.  However, you can directly compare entSensorValue  with the threshold values given in entSensorThresholdTable  without any semantic knowledge
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2015-01-15'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.entsensorthresholdindex = None
                self.entsensorthresholdevaluation = None
                self.entsensorthresholdnotificationenable = None
                self.entsensorthresholdrelation = None
                self.entsensorthresholdseverity = None
                self.entsensorthresholdvalue = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')
                if self.entsensorthresholdindex is None:
                    raise YPYDataValidationError('Key property entsensorthresholdindex is None')

                return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorThresholdTable/CISCO-ENTITY-SENSOR-MIB:entSensorThresholdEntry[CISCO-ENTITY-SENSOR-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENTITY-SENSOR-MIB:entSensorThresholdIndex = ' + str(self.entsensorthresholdindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.entsensorthresholdindex is not None:
                    return True

                if self.entsensorthresholdevaluation is not None:
                    return True

                if self.entsensorthresholdnotificationenable is not None:
                    return True

                if self.entsensorthresholdrelation is not None:
                    return True

                if self.entsensorthresholdseverity is not None:
                    return True

                if self.entsensorthresholdvalue is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
                return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorThresholdTable.EntSensorThresholdEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorThresholdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.entsensorthresholdentry is not None:
                for child_ref in self.entsensorthresholdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
            return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorThresholdTable']['meta_info']


    class EntSensorValueTable(object):
        """
        This table lists the type, scale, and present value
        of a sensor listed in the Entity\-MIB entPhysicalTable.
        
        .. attribute:: entsensorvalueentry
        
        	An entSensorValueTable entry describes the present reading of a sensor, the measurement units and scale, and sensor operational status
        	**type**\: list of :py:class:`EntSensorValueEntry <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2015-01-15'

        def __init__(self):
            self.parent = None
            self.entsensorvalueentry = YList()
            self.entsensorvalueentry.parent = self
            self.entsensorvalueentry.name = 'entsensorvalueentry'


        class EntSensorValueEntry(object):
            """
            An entSensorValueTable entry describes the
            present reading of a sensor, the measurement units
            and scale, and sensor operational status.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entsensormeasuredentity
            
            	This object identifies the physical entity for which the sensor is taking measurements.  For example, for a sensor measuring the voltage output of a power\-supply, this object would be the entPhysicalIndex of that power\-supply; for a sensor measuring the temperature inside one chassis of a multi\-chassis system, this object would be the enPhysicalIndex of that chassis.  This object has a value of zero when the physical entity for which the sensor is taking measurements can not be represented by any one row in the entPhysicalTable, or that there is no such physical entity
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: entsensorprecision
            
            	This variable indicates the number of decimal places of precision in fixed\-point sensor values reported by entSensorValue.  This variable is set to 0 when entSensorType is not a fixed\-point type\: e.g.'percentRH(9)',  'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\: int
            
            	**range:** \-8..9
            
            .. attribute:: entsensorscale
            
            	This variable indicates the exponent to apply to sensor values reported by entSensorValue.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\: :py:class:`SensorDataScale_Enum <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.SensorDataScale_Enum>`
            
            .. attribute:: entsensorstatus
            
            	This variable indicates the present operational status of the sensor
            	**type**\: :py:class:`SensorStatus_Enum <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.SensorStatus_Enum>`
            
            .. attribute:: entsensortype
            
            	This variable indicates the type of data reported by the entSensorValue.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\: :py:class:`SensorDataType_Enum <ydk.models.entity.CISCO_ENTITY_SENSOR_MIB.SensorDataType_Enum>`
            
            .. attribute:: entsensorvalue
            
            	This variable reports the most recent measurement seen by the sensor.  To correctly display or interpret this variable's value,  you must also know entSensorType, entSensorScale, and  entSensorPrecision.  However, you can compare entSensorValue with the threshold values given in entSensorThresholdTable without any semantic knowledge
            	**type**\: int
            
            	**range:** \-1000000000..1000000000
            
            .. attribute:: entsensorvaluetimestamp
            
            	This variable indicates the age of the value reported by entSensorValue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: entsensorvalueupdaterate
            
            	This variable indicates the rate that the agent updates entSensorValue
            	**type**\: int
            
            	**range:** 0..999999999
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2015-01-15'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.entsensormeasuredentity = None
                self.entsensorprecision = None
                self.entsensorscale = None
                self.entsensorstatus = None
                self.entsensortype = None
                self.entsensorvalue = None
                self.entsensorvaluetimestamp = None
                self.entsensorvalueupdaterate = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorValueTable/CISCO-ENTITY-SENSOR-MIB:entSensorValueEntry[CISCO-ENTITY-SENSOR-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.entsensormeasuredentity is not None:
                    return True

                if self.entsensorprecision is not None:
                    return True

                if self.entsensorscale is not None:
                    return True

                if self.entsensorstatus is not None:
                    return True

                if self.entsensortype is not None:
                    return True

                if self.entsensorvalue is not None:
                    return True

                if self.entsensorvaluetimestamp is not None:
                    return True

                if self.entsensorvalueupdaterate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
                return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorValueTable.EntSensorValueEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorValueTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.entsensorvalueentry is not None:
                for child_ref in self.entsensorvalueentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
            return meta._meta_table['CISCOENTITYSENSORMIB.EntSensorValueTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.entsensorglobalobjects is not None and self.entsensorglobalobjects._has_data():
            return True

        if self.entsensorglobalobjects is not None and self.entsensorglobalobjects.is_presence():
            return True

        if self.entsensorthresholdtable is not None and self.entsensorthresholdtable._has_data():
            return True

        if self.entsensorthresholdtable is not None and self.entsensorthresholdtable.is_presence():
            return True

        if self.entsensorvaluetable is not None and self.entsensorvaluetable._has_data():
            return True

        if self.entsensorvaluetable is not None and self.entsensorvaluetable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['CISCOENTITYSENSORMIB']['meta_info']


