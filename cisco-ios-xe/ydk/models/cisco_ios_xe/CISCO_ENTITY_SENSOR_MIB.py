""" CISCO_ENTITY_SENSOR_MIB 

The CISCO\-ENTITY\-SENSOR\-MIB is used to monitor
the values of sensors in the Entity\-MIB (RFC 2037) 
entPhysicalTable.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class SensorDataScale(Enum):
    """
    SensorDataScale (Enum Class)

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

    yocto = Enum.YLeaf(1, "yocto")

    zepto = Enum.YLeaf(2, "zepto")

    atto = Enum.YLeaf(3, "atto")

    femto = Enum.YLeaf(4, "femto")

    pico = Enum.YLeaf(5, "pico")

    nano = Enum.YLeaf(6, "nano")

    micro = Enum.YLeaf(7, "micro")

    milli = Enum.YLeaf(8, "milli")

    units = Enum.YLeaf(9, "units")

    kilo = Enum.YLeaf(10, "kilo")

    mega = Enum.YLeaf(11, "mega")

    giga = Enum.YLeaf(12, "giga")

    tera = Enum.YLeaf(13, "tera")

    exa = Enum.YLeaf(14, "exa")

    peta = Enum.YLeaf(15, "peta")

    zetta = Enum.YLeaf(16, "zetta")

    yotta = Enum.YLeaf(17, "yotta")


class SensorDataType(Enum):
    """
    SensorDataType (Enum Class)

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

    other = Enum.YLeaf(1, "other")

    unknown = Enum.YLeaf(2, "unknown")

    voltsAC = Enum.YLeaf(3, "voltsAC")

    voltsDC = Enum.YLeaf(4, "voltsDC")

    amperes = Enum.YLeaf(5, "amperes")

    watts = Enum.YLeaf(6, "watts")

    hertz = Enum.YLeaf(7, "hertz")

    celsius = Enum.YLeaf(8, "celsius")

    percentRH = Enum.YLeaf(9, "percentRH")

    rpm = Enum.YLeaf(10, "rpm")

    cmm = Enum.YLeaf(11, "cmm")

    truthvalue = Enum.YLeaf(12, "truthvalue")

    specialEnum = Enum.YLeaf(13, "specialEnum")

    dBm = Enum.YLeaf(14, "dBm")


class SensorStatus(Enum):
    """
    SensorStatus (Enum Class)

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

    ok = Enum.YLeaf(1, "ok")

    unavailable = Enum.YLeaf(2, "unavailable")

    nonoperational = Enum.YLeaf(3, "nonoperational")


class SensorThresholdRelation(Enum):
    """
    SensorThresholdRelation (Enum Class)

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

    lessThan = Enum.YLeaf(1, "lessThan")

    lessOrEqual = Enum.YLeaf(2, "lessOrEqual")

    greaterThan = Enum.YLeaf(3, "greaterThan")

    greaterOrEqual = Enum.YLeaf(4, "greaterOrEqual")

    equalTo = Enum.YLeaf(5, "equalTo")

    notEqualTo = Enum.YLeaf(6, "notEqualTo")


class SensorThresholdSeverity(Enum):
    """
    SensorThresholdSeverity (Enum Class)

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

    other = Enum.YLeaf(1, "other")

    minor = Enum.YLeaf(10, "minor")

    major = Enum.YLeaf(20, "major")

    critical = Enum.YLeaf(30, "critical")



class CISCOENTITYSENSORMIB(Entity):
    """
    
    
    .. attribute:: entsensorglobalobjects
    
    	
    	**type**\:  :py:class:`Entsensorglobalobjects <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.Entsensorglobalobjects>`
    
    .. attribute:: entsensorvaluetable
    
    	This table lists the type, scale, and present value of a sensor listed in the Entity\-MIB entPhysicalTable
    	**type**\:  :py:class:`Entsensorvaluetable <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.Entsensorvaluetable>`
    
    .. attribute:: entsensorthresholdtable
    
    	This table lists the threshold severity, relation, and comparison value, for a sensor listed in the Entity\-MIB  entPhysicalTable
    	**type**\:  :py:class:`Entsensorthresholdtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.Entsensorthresholdtable>`
    
    

    """

    _prefix = 'CISCO-ENTITY-SENSOR-MIB'
    _revision = '2015-01-15'

    def __init__(self):
        super(CISCOENTITYSENSORMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-SENSOR-MIB"
        self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("entSensorGlobalObjects", ("entsensorglobalobjects", CISCOENTITYSENSORMIB.Entsensorglobalobjects)), ("entSensorValueTable", ("entsensorvaluetable", CISCOENTITYSENSORMIB.Entsensorvaluetable)), ("entSensorThresholdTable", ("entsensorthresholdtable", CISCOENTITYSENSORMIB.Entsensorthresholdtable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.entsensorglobalobjects = CISCOENTITYSENSORMIB.Entsensorglobalobjects()
        self.entsensorglobalobjects.parent = self
        self._children_name_map["entsensorglobalobjects"] = "entSensorGlobalObjects"
        self._children_yang_names.add("entSensorGlobalObjects")

        self.entsensorvaluetable = CISCOENTITYSENSORMIB.Entsensorvaluetable()
        self.entsensorvaluetable.parent = self
        self._children_name_map["entsensorvaluetable"] = "entSensorValueTable"
        self._children_yang_names.add("entSensorValueTable")

        self.entsensorthresholdtable = CISCOENTITYSENSORMIB.Entsensorthresholdtable()
        self.entsensorthresholdtable.parent = self
        self._children_name_map["entsensorthresholdtable"] = "entSensorThresholdTable"
        self._children_yang_names.add("entSensorThresholdTable")
        self._segment_path = lambda: "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB"


    class Entsensorglobalobjects(Entity):
        """
        
        
        .. attribute:: entsensorthreshnotifglobalenable
        
        	This variable enables the generation of entSensorThresholdNotification globally on the device. If this object value is 'false', then no entSensorThresholdNotification will be generated on this device. If this object value is 'true', then whether a  entSensorThresholdNotification for a threshold will be generated or not depends on the instance value of entSensorThresholdNotificationEnable for that threshold
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-ENTITY-SENSOR-MIB'
        _revision = '2015-01-15'

        def __init__(self):
            super(CISCOENTITYSENSORMIB.Entsensorglobalobjects, self).__init__()

            self.yang_name = "entSensorGlobalObjects"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entsensorthreshnotifglobalenable', YLeaf(YType.boolean, 'entSensorThreshNotifGlobalEnable')),
            ])
            self.entsensorthreshnotifglobalenable = None
            self._segment_path = lambda: "entSensorGlobalObjects"
            self._absolute_path = lambda: "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYSENSORMIB.Entsensorglobalobjects, ['entsensorthreshnotifglobalenable'], name, value)


    class Entsensorvaluetable(Entity):
        """
        This table lists the type, scale, and present value
        of a sensor listed in the Entity\-MIB entPhysicalTable.
        
        .. attribute:: entsensorvalueentry
        
        	An entSensorValueTable entry describes the present reading of a sensor, the measurement units and scale, and sensor operational status
        	**type**\: list of  		 :py:class:`Entsensorvalueentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.Entsensorvaluetable.Entsensorvalueentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-SENSOR-MIB'
        _revision = '2015-01-15'

        def __init__(self):
            super(CISCOENTITYSENSORMIB.Entsensorvaluetable, self).__init__()

            self.yang_name = "entSensorValueTable"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entSensorValueEntry", ("entsensorvalueentry", CISCOENTITYSENSORMIB.Entsensorvaluetable.Entsensorvalueentry))])
            self._leafs = OrderedDict()

            self.entsensorvalueentry = YList(self)
            self._segment_path = lambda: "entSensorValueTable"
            self._absolute_path = lambda: "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYSENSORMIB.Entsensorvaluetable, [], name, value)


        class Entsensorvalueentry(Entity):
            """
            An entSensorValueTable entry describes the
            present reading of a sensor, the measurement units
            and scale, and sensor operational status.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entsensortype
            
            	This variable indicates the type of data reported by the entSensorValue.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\:  :py:class:`SensorDataType <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorDataType>`
            
            .. attribute:: entsensorscale
            
            	This variable indicates the exponent to apply to sensor values reported by entSensorValue.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\:  :py:class:`SensorDataScale <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorDataScale>`
            
            .. attribute:: entsensorprecision
            
            	This variable indicates the number of decimal places of precision in fixed\-point sensor values reported by entSensorValue.  This variable is set to 0 when entSensorType is not a fixed\-point type\: e.g.'percentRH(9)',  'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\: int
            
            	**range:** \-8..9
            
            .. attribute:: entsensorvalue
            
            	This variable reports the most recent measurement seen by the sensor.  To correctly display or interpret this variable's value,  you must also know entSensorType, entSensorScale, and  entSensorPrecision.  However, you can compare entSensorValue with the threshold values given in entSensorThresholdTable without any semantic knowledge
            	**type**\: int
            
            	**range:** \-1000000000..1073741823
            
            .. attribute:: entsensorstatus
            
            	This variable indicates the present operational status of the sensor
            	**type**\:  :py:class:`SensorStatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorStatus>`
            
            .. attribute:: entsensorvaluetimestamp
            
            	This variable indicates the age of the value reported by entSensorValue
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: entsensorvalueupdaterate
            
            	This variable indicates the rate that the agent updates entSensorValue
            	**type**\: int
            
            	**range:** 0..999999999
            
            	**units**\: seconds
            
            .. attribute:: entsensormeasuredentity
            
            	This object identifies the physical entity for which the sensor is taking measurements.  For example, for a sensor measuring the voltage output of a power\-supply, this object would be the entPhysicalIndex of that power\-supply; for a sensor measuring the temperature inside one chassis of a multi\-chassis system, this object would be the enPhysicalIndex of that chassis.  This object has a value of zero when the physical entity for which the sensor is taking measurements can not be represented by any one row in the entPhysicalTable, or that there is no such physical entity
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-ENTITY-SENSOR-MIB'
            _revision = '2015-01-15'

            def __init__(self):
                super(CISCOENTITYSENSORMIB.Entsensorvaluetable.Entsensorvalueentry, self).__init__()

                self.yang_name = "entSensorValueEntry"
                self.yang_parent_name = "entSensorValueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('entsensortype', YLeaf(YType.enumeration, 'entSensorType')),
                    ('entsensorscale', YLeaf(YType.enumeration, 'entSensorScale')),
                    ('entsensorprecision', YLeaf(YType.int32, 'entSensorPrecision')),
                    ('entsensorvalue', YLeaf(YType.int32, 'entSensorValue')),
                    ('entsensorstatus', YLeaf(YType.enumeration, 'entSensorStatus')),
                    ('entsensorvaluetimestamp', YLeaf(YType.uint32, 'entSensorValueTimeStamp')),
                    ('entsensorvalueupdaterate', YLeaf(YType.int32, 'entSensorValueUpdateRate')),
                    ('entsensormeasuredentity', YLeaf(YType.int32, 'entSensorMeasuredEntity')),
                ])
                self.entphysicalindex = None
                self.entsensortype = None
                self.entsensorscale = None
                self.entsensorprecision = None
                self.entsensorvalue = None
                self.entsensorstatus = None
                self.entsensorvaluetimestamp = None
                self.entsensorvalueupdaterate = None
                self.entsensormeasuredentity = None
                self._segment_path = lambda: "entSensorValueEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/entSensorValueTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYSENSORMIB.Entsensorvaluetable.Entsensorvalueentry, ['entphysicalindex', 'entsensortype', 'entsensorscale', 'entsensorprecision', 'entsensorvalue', 'entsensorstatus', 'entsensorvaluetimestamp', 'entsensorvalueupdaterate', 'entsensormeasuredentity'], name, value)


    class Entsensorthresholdtable(Entity):
        """
        This table lists the threshold severity, relation, and
        comparison value, for a sensor listed in the Entity\-MIB 
        entPhysicalTable.
        
        .. attribute:: entsensorthresholdentry
        
        	An entSensorThresholdTable entry describes the thresholds for a sensor\: the threshold severity, the threshold value, the relation, and the  evaluation of the threshold.  Only entities of type sensor(8) are listed in this table. Only pre\-configured thresholds are listed in this table.  Users can create sensor\-value monitoring instruments in different ways, such as RMON alarms, Expression\-MIB, etc.  Entries are created by the agent at system startup and FRU insertion.  Entries are deleted by the agent at FRU removal
        	**type**\: list of  		 :py:class:`Entsensorthresholdentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.CISCOENTITYSENSORMIB.Entsensorthresholdtable.Entsensorthresholdentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-SENSOR-MIB'
        _revision = '2015-01-15'

        def __init__(self):
            super(CISCOENTITYSENSORMIB.Entsensorthresholdtable, self).__init__()

            self.yang_name = "entSensorThresholdTable"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entSensorThresholdEntry", ("entsensorthresholdentry", CISCOENTITYSENSORMIB.Entsensorthresholdtable.Entsensorthresholdentry))])
            self._leafs = OrderedDict()

            self.entsensorthresholdentry = YList(self)
            self._segment_path = lambda: "entSensorThresholdTable"
            self._absolute_path = lambda: "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYSENSORMIB.Entsensorthresholdtable, [], name, value)


        class Entsensorthresholdentry(Entity):
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
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entsensorthresholdindex  (key)
            
            	An index that uniquely identifies an entry in the entSensorThresholdTable. This index permits the same sensor to have several  different thresholds
            	**type**\: int
            
            	**range:** 1..99999999
            
            .. attribute:: entsensorthresholdseverity
            
            	This variable indicates the severity of this threshold
            	**type**\:  :py:class:`SensorThresholdSeverity <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorThresholdSeverity>`
            
            .. attribute:: entsensorthresholdrelation
            
            	This variable indicates the relation between sensor value (entSensorValue) and threshold value (entSensorThresholdValue),  required to trigger the alarm.  when evaluating the relation,  entSensorValue is on the left of entSensorThresholdRelation,  entSensorThresholdValue is on the right.   in pseudo\-code, the evaluation\-alarm mechanism is\:  ... if (entSensorStatus == ok) then     if (evaluate(entSensorValue, entSensorThresholdRelation,           entSensorThresholdValue))      then         if (entSensorThresholdNotificationEnable == true))          then             raise\_alarm(sensor's entPhysicalIndex);         endif     endif endif ..
            	**type**\:  :py:class:`SensorThresholdRelation <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.SensorThresholdRelation>`
            
            .. attribute:: entsensorthresholdvalue
            
            	This variable indicates the value of the threshold.  To correctly display or interpret this variable's value,  you must also know entSensorType, entSensorScale, and  entSensorPrecision.  However, you can directly compare entSensorValue  with the threshold values given in entSensorThresholdTable  without any semantic knowledge
            	**type**\: int
            
            	**range:** \-1000000000..1073741823
            
            .. attribute:: entsensorthresholdevaluation
            
            	This variable indicates the result of the most recent evaluation of the threshold.  If the threshold condition is true, entSensorThresholdEvaluation  is true(1).  If the threshold condition is false,  entSensorThresholdEvaluation is false(2).  Thresholds are evaluated at the rate indicated by  entSensorValueUpdateRate
            	**type**\: bool
            
            .. attribute:: entsensorthresholdnotificationenable
            
            	This variable controls generation of entSensorThresholdNotification for this threshold.  When this variable is 'true', generation of  entSensorThresholdNotification is enabled for this threshold. When this variable is 'false',  generation of entSensorThresholdNotification is disabled for this threshold
            	**type**\: bool
            
            

            """

            _prefix = 'CISCO-ENTITY-SENSOR-MIB'
            _revision = '2015-01-15'

            def __init__(self):
                super(CISCOENTITYSENSORMIB.Entsensorthresholdtable.Entsensorthresholdentry, self).__init__()

                self.yang_name = "entSensorThresholdEntry"
                self.yang_parent_name = "entSensorThresholdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entsensorthresholdindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('entsensorthresholdindex', YLeaf(YType.int32, 'entSensorThresholdIndex')),
                    ('entsensorthresholdseverity', YLeaf(YType.enumeration, 'entSensorThresholdSeverity')),
                    ('entsensorthresholdrelation', YLeaf(YType.enumeration, 'entSensorThresholdRelation')),
                    ('entsensorthresholdvalue', YLeaf(YType.int32, 'entSensorThresholdValue')),
                    ('entsensorthresholdevaluation', YLeaf(YType.boolean, 'entSensorThresholdEvaluation')),
                    ('entsensorthresholdnotificationenable', YLeaf(YType.boolean, 'entSensorThresholdNotificationEnable')),
                ])
                self.entphysicalindex = None
                self.entsensorthresholdindex = None
                self.entsensorthresholdseverity = None
                self.entsensorthresholdrelation = None
                self.entsensorthresholdvalue = None
                self.entsensorthresholdevaluation = None
                self.entsensorthresholdnotificationenable = None
                self._segment_path = lambda: "entSensorThresholdEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entSensorThresholdIndex='" + str(self.entsensorthresholdindex) + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/entSensorThresholdTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYSENSORMIB.Entsensorthresholdtable.Entsensorthresholdentry, ['entphysicalindex', 'entsensorthresholdindex', 'entsensorthresholdseverity', 'entsensorthresholdrelation', 'entsensorthresholdvalue', 'entsensorthresholdevaluation', 'entsensorthresholdnotificationenable'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOENTITYSENSORMIB()
        return self._top_entity

