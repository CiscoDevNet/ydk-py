""" CISCO_ENTITY_SENSOR_MIB 

The CISCO\-ENTITY\-SENSOR\-MIB is used to monitor
the values of sensors in the Entity\-MIB (RFC 2037) 
entPhysicalTable.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class SensordatascaleEnum(Enum):
    """
    SensordatascaleEnum

    International System of Units (SI) prefixes.

    .. data:: yocto = 1

    .. data:: zepto = 2

    .. data:: atto = 3

    .. data:: femto = 4

    .. data:: pico = 5

    .. data:: nano = 6

    .. data:: micro = 7

    .. data:: milli = 8

    .. data:: units = 9

    .. data:: kilo = 10

    .. data:: mega = 11

    .. data:: giga = 12

    .. data:: tera = 13

    .. data:: exa = 14

    .. data:: peta = 15

    .. data:: zetta = 16

    .. data:: yotta = 17

    """

    yocto = 1

    zepto = 2

    atto = 3

    femto = 4

    pico = 5

    nano = 6

    micro = 7

    milli = 8

    units = 9

    kilo = 10

    mega = 11

    giga = 12

    tera = 13

    exa = 14

    peta = 15

    zetta = 16

    yotta = 17


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensordatascaleEnum']


class SensordatatypeEnum(Enum):
    """
    SensordatatypeEnum

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

    .. data:: other = 1

    .. data:: unknown = 2

    .. data:: voltsAC = 3

    .. data:: voltsDC = 4

    .. data:: amperes = 5

    .. data:: watts = 6

    .. data:: hertz = 7

    .. data:: celsius = 8

    .. data:: percentRH = 9

    .. data:: rpm = 10

    .. data:: cmm = 11

    .. data:: truthvalue = 12

    .. data:: specialEnum = 13

    .. data:: dBm = 14

    """

    other = 1

    unknown = 2

    voltsAC = 3

    voltsDC = 4

    amperes = 5

    watts = 6

    hertz = 7

    celsius = 8

    percentRH = 9

    rpm = 10

    cmm = 11

    truthvalue = 12

    specialEnum = 13

    dBm = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensordatatypeEnum']


class SensorstatusEnum(Enum):
    """
    SensorstatusEnum

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

    .. data:: ok = 1

    .. data:: unavailable = 2

    .. data:: nonoperational = 3

    """

    ok = 1

    unavailable = 2

    nonoperational = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorstatusEnum']


class SensorthresholdrelationEnum(Enum):
    """
    SensorthresholdrelationEnum

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

    .. data:: lessThan = 1

    .. data:: lessOrEqual = 2

    .. data:: greaterThan = 3

    .. data:: greaterOrEqual = 4

    .. data:: equalTo = 5

    .. data:: notEqualTo = 6

    """

    lessThan = 1

    lessOrEqual = 2

    greaterThan = 3

    greaterOrEqual = 4

    equalTo = 5

    notEqualTo = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorthresholdrelationEnum']


class SensorthresholdseverityEnum(Enum):
    """
    SensorthresholdseverityEnum

    sensor threshold severity.  Valid values are\:

    other(1)    \: a severity other than those listed below.

    minor(10)   \: Minor Problem threshold.

    major(20)   \: Major Problem threshold.

    critical(30)\: Critical problem threshold. A system might shut

                  down the sensor associated FRU automatically if

                  the sensor value reach the critical problem

                  threshold.

    .. data:: other = 1

    .. data:: minor = 10

    .. data:: major = 20

    .. data:: critical = 30

    """

    other = 1

    minor = 10

    major = 20

    critical = 30


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['SensorthresholdseverityEnum']



class CiscoEntitySensorMib(object):
    """
    
    
    .. attribute:: entsensorglobalobjects
    
    	
    	**type**\:   :py:class:`Entsensorglobalobjects <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CiscoEntitySensorMib.Entsensorglobalobjects>`
    
    .. attribute:: entsensorthresholdtable
    
    	This table lists the threshold severity, relation, and comparison value, for a sensor listed in the Entity\-MIB  entPhysicalTable
    	**type**\:   :py:class:`Entsensorthresholdtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CiscoEntitySensorMib.Entsensorthresholdtable>`
    
    .. attribute:: entsensorvaluetable
    
    	This table lists the type, scale, and present value of a sensor listed in the Entity\-MIB entPhysicalTable
    	**type**\:   :py:class:`Entsensorvaluetable <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CiscoEntitySensorMib.Entsensorvaluetable>`
    
    

    """

    _prefix = 'CISCO-ENTITY-SENSOR-MIB'
    _revision = '2015-01-15'

    def __init__(self):
        self.entsensorglobalobjects = CiscoEntitySensorMib.Entsensorglobalobjects()
        self.entsensorglobalobjects.parent = self
        self.entsensorthresholdtable = CiscoEntitySensorMib.Entsensorthresholdtable()
        self.entsensorthresholdtable.parent = self
        self.entsensorvaluetable = CiscoEntitySensorMib.Entsensorvaluetable()
        self.entsensorvaluetable.parent = self


    class Entsensorglobalobjects(object):
        """
        
        
        .. attribute:: entsensorthreshnotifglobalenable
        
        	This variable enables the generation of entSensorThresholdNotification globally on the device. If this object value is 'false', then no entSensorThresholdNotification will be generated on this device. If this object value is 'true', then whether a  entSensorThresholdNotification for a threshold will be generated or not depends on the instance value of entSensorThresholdNotificationEnable for that threshold
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-ENTITY-SENSOR-MIB'
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
            if self.entsensorthreshnotifglobalenable is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
            return meta._meta_table['CiscoEntitySensorMib.Entsensorglobalobjects']['meta_info']


    class Entsensorvaluetable(object):
        """
        This table lists the type, scale, and present value
        of a sensor listed in the Entity\-MIB entPhysicalTable.
        
        .. attribute:: entsensorvalueentry
        
        	An entSensorValueTable entry describes the present reading of a sensor, the measurement units and scale, and sensor operational status
        	**type**\: list of    :py:class:`Entsensorvalueentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-SENSOR-MIB'
        _revision = '2015-01-15'

        def __init__(self):
            self.parent = None
            self.entsensorvalueentry = YList()
            self.entsensorvalueentry.parent = self
            self.entsensorvalueentry.name = 'entsensorvalueentry'


        class Entsensorvalueentry(object):
            """
            An entSensorValueTable entry describes the
            present reading of a sensor, the measurement units
            and scale, and sensor operational status.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entsensormeasuredentity
            
            	This object identifies the physical entity for which the sensor is taking measurements.  For example, for a sensor measuring the voltage output of a power\-supply, this object would be the entPhysicalIndex of that power\-supply; for a sensor measuring the temperature inside one chassis of a multi\-chassis system, this object would be the enPhysicalIndex of that chassis.  This object has a value of zero when the physical entity for which the sensor is taking measurements can not be represented by any one row in the entPhysicalTable, or that there is no such physical entity
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: entsensorprecision
            
            	This variable indicates the number of decimal places of precision in fixed\-point sensor values reported by entSensorValue.  This variable is set to 0 when entSensorType is not a fixed\-point type\: e.g.'percentRH(9)',  'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\:  int
            
            	**range:** \-8..9
            
            .. attribute:: entsensorscale
            
            	This variable indicates the exponent to apply to sensor values reported by entSensorValue.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\:   :py:class:`SensordatascaleEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensordatascaleEnum>`
            
            .. attribute:: entsensorstatus
            
            	This variable indicates the present operational status of the sensor
            	**type**\:   :py:class:`SensorstatusEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorstatusEnum>`
            
            .. attribute:: entsensortype
            
            	This variable indicates the type of data reported by the entSensorValue.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\:   :py:class:`SensordatatypeEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensordatatypeEnum>`
            
            .. attribute:: entsensorvalue
            
            	This variable reports the most recent measurement seen by the sensor.  To correctly display or interpret this variable's value,  you must also know entSensorType, entSensorScale, and  entSensorPrecision.  However, you can compare entSensorValue with the threshold values given in entSensorThresholdTable without any semantic knowledge
            	**type**\:  int
            
            	**range:** \-1000000000..1073741823
            
            .. attribute:: entsensorvaluetimestamp
            
            	This variable indicates the age of the value reported by entSensorValue
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: entsensorvalueupdaterate
            
            	This variable indicates the rate that the agent updates entSensorValue
            	**type**\:  int
            
            	**range:** 0..999999999
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-ENTITY-SENSOR-MIB'
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
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorValueTable/CISCO-ENTITY-SENSOR-MIB:entSensorValueEntry[CISCO-ENTITY-SENSOR-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
                return meta._meta_table['CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorValueTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.entsensorvalueentry is not None:
                for child_ref in self.entsensorvalueentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
            return meta._meta_table['CiscoEntitySensorMib.Entsensorvaluetable']['meta_info']


    class Entsensorthresholdtable(object):
        """
        This table lists the threshold severity, relation, and
        comparison value, for a sensor listed in the Entity\-MIB 
        entPhysicalTable.
        
        .. attribute:: entsensorthresholdentry
        
        	An entSensorThresholdTable entry describes the thresholds for a sensor\: the threshold severity, the threshold value, the relation, and the  evaluation of the threshold.  Only entities of type sensor(8) are listed in this table. Only pre\-configured thresholds are listed in this table.  Users can create sensor\-value monitoring instruments in different ways, such as RMON alarms, Expression\-MIB, etc.  Entries are created by the agent at system startup and FRU insertion.  Entries are deleted by the agent at FRU removal
        	**type**\: list of    :py:class:`Entsensorthresholdentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-SENSOR-MIB'
        _revision = '2015-01-15'

        def __init__(self):
            self.parent = None
            self.entsensorthresholdentry = YList()
            self.entsensorthresholdentry.parent = self
            self.entsensorthresholdentry.name = 'entsensorthresholdentry'


        class Entsensorthresholdentry(object):
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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entsensorthresholdindex  <key>
            
            	An index that uniquely identifies an entry in the entSensorThresholdTable. This index permits the same sensor to have several  different thresholds
            	**type**\:  int
            
            	**range:** 1..99999999
            
            .. attribute:: entsensorthresholdevaluation
            
            	This variable indicates the result of the most recent evaluation of the threshold.  If the threshold condition is true, entSensorThresholdEvaluation  is true(1).  If the threshold condition is false,  entSensorThresholdEvaluation is false(2).  Thresholds are evaluated at the rate indicated by  entSensorValueUpdateRate
            	**type**\:  bool
            
            .. attribute:: entsensorthresholdnotificationenable
            
            	This variable controls generation of entSensorThresholdNotification for this threshold.  When this variable is 'true', generation of  entSensorThresholdNotification is enabled for this threshold. When this variable is 'false',  generation of entSensorThresholdNotification is disabled for this threshold
            	**type**\:  bool
            
            .. attribute:: entsensorthresholdrelation
            
            	This variable indicates the relation between sensor value (entSensorValue) and threshold value (entSensorThresholdValue),  required to trigger the alarm.  when evaluating the relation,  entSensorValue is on the left of entSensorThresholdRelation,  entSensorThresholdValue is on the right.   in pseudo\-code, the evaluation\-alarm mechanism is\:  ... if (entSensorStatus == ok) then     if (evaluate(entSensorValue, entSensorThresholdRelation,           entSensorThresholdValue))      then         if (entSensorThresholdNotificationEnable == true))          then             raise\_alarm(sensor's entPhysicalIndex);         endif     endif endif ..
            	**type**\:   :py:class:`SensorthresholdrelationEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorthresholdrelationEnum>`
            
            .. attribute:: entsensorthresholdseverity
            
            	This variable indicates the severity of this threshold
            	**type**\:   :py:class:`SensorthresholdseverityEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorthresholdseverityEnum>`
            
            .. attribute:: entsensorthresholdvalue
            
            	This variable indicates the value of the threshold.  To correctly display or interpret this variable's value,  you must also know entSensorType, entSensorScale, and  entSensorPrecision.  However, you can directly compare entSensorValue  with the threshold values given in entSensorThresholdTable  without any semantic knowledge
            	**type**\:  int
            
            	**range:** \-1000000000..1073741823
            
            

            """

            _prefix = 'CISCO-ENTITY-SENSOR-MIB'
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
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.entsensorthresholdindex is None:
                    raise YPYModelError('Key property entsensorthresholdindex is None')

                return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorThresholdTable/CISCO-ENTITY-SENSOR-MIB:entSensorThresholdEntry[CISCO-ENTITY-SENSOR-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENTITY-SENSOR-MIB:entSensorThresholdIndex = ' + str(self.entsensorthresholdindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
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

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
                return meta._meta_table['CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/CISCO-ENTITY-SENSOR-MIB:entSensorThresholdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.entsensorthresholdentry is not None:
                for child_ref in self.entsensorthresholdentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
            return meta._meta_table['CiscoEntitySensorMib.Entsensorthresholdtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.entsensorglobalobjects is not None and self.entsensorglobalobjects._has_data():
            return True

        if self.entsensorthresholdtable is not None and self.entsensorthresholdtable._has_data():
            return True

        if self.entsensorvaluetable is not None and self.entsensorvaluetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_SENSOR_MIB as meta
        return meta._meta_table['CiscoEntitySensorMib']['meta_info']


