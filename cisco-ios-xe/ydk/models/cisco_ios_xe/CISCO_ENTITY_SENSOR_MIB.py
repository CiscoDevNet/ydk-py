""" CISCO_ENTITY_SENSOR_MIB 

The CISCO\-ENTITY\-SENSOR\-MIB is used to monitor
the values of sensors in the Entity\-MIB (RFC 2037) 
entPhysicalTable.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Sensordatascale(Enum):
    """
    Sensordatascale

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


class Sensordatatype(Enum):
    """
    Sensordatatype

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


class Sensorstatus(Enum):
    """
    Sensorstatus

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


class Sensorthresholdrelation(Enum):
    """
    Sensorthresholdrelation

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


class Sensorthresholdseverity(Enum):
    """
    Sensorthresholdseverity

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



class CiscoEntitySensorMib(Entity):
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
        super(CiscoEntitySensorMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-SENSOR-MIB"
        self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"

        self.entsensorglobalobjects = CiscoEntitySensorMib.Entsensorglobalobjects()
        self.entsensorglobalobjects.parent = self
        self._children_name_map["entsensorglobalobjects"] = "entSensorGlobalObjects"
        self._children_yang_names.add("entSensorGlobalObjects")

        self.entsensorthresholdtable = CiscoEntitySensorMib.Entsensorthresholdtable()
        self.entsensorthresholdtable.parent = self
        self._children_name_map["entsensorthresholdtable"] = "entSensorThresholdTable"
        self._children_yang_names.add("entSensorThresholdTable")

        self.entsensorvaluetable = CiscoEntitySensorMib.Entsensorvaluetable()
        self.entsensorvaluetable.parent = self
        self._children_name_map["entsensorvaluetable"] = "entSensorValueTable"
        self._children_yang_names.add("entSensorValueTable")


    class Entsensorglobalobjects(Entity):
        """
        
        
        .. attribute:: entsensorthreshnotifglobalenable
        
        	This variable enables the generation of entSensorThresholdNotification globally on the device. If this object value is 'false', then no entSensorThresholdNotification will be generated on this device. If this object value is 'true', then whether a  entSensorThresholdNotification for a threshold will be generated or not depends on the instance value of entSensorThresholdNotificationEnable for that threshold
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-ENTITY-SENSOR-MIB'
        _revision = '2015-01-15'

        def __init__(self):
            super(CiscoEntitySensorMib.Entsensorglobalobjects, self).__init__()

            self.yang_name = "entSensorGlobalObjects"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"

            self.entsensorthreshnotifglobalenable = YLeaf(YType.boolean, "entSensorThreshNotifGlobalEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("entsensorthreshnotifglobalenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEntitySensorMib.Entsensorglobalobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntitySensorMib.Entsensorglobalobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.entsensorthreshnotifglobalenable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.entsensorthreshnotifglobalenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "entSensorGlobalObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.entsensorthreshnotifglobalenable.is_set or self.entsensorthreshnotifglobalenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entsensorthreshnotifglobalenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entSensorThreshNotifGlobalEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "entSensorThreshNotifGlobalEnable"):
                self.entsensorthreshnotifglobalenable = value
                self.entsensorthreshnotifglobalenable.value_namespace = name_space
                self.entsensorthreshnotifglobalenable.value_namespace_prefix = name_space_prefix


    class Entsensorvaluetable(Entity):
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
            super(CiscoEntitySensorMib.Entsensorvaluetable, self).__init__()

            self.yang_name = "entSensorValueTable"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"

            self.entsensorvalueentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEntitySensorMib.Entsensorvaluetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntitySensorMib.Entsensorvaluetable, self).__setattr__(name, value)


        class Entsensorvalueentry(Entity):
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
            	**type**\:   :py:class:`Sensordatascale <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.Sensordatascale>`
            
            .. attribute:: entsensorstatus
            
            	This variable indicates the present operational status of the sensor
            	**type**\:   :py:class:`Sensorstatus <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.Sensorstatus>`
            
            .. attribute:: entsensortype
            
            	This variable indicates the type of data reported by the entSensorValue.  This variable is set by the agent at start\-up and the value does not change during operation
            	**type**\:   :py:class:`Sensordatatype <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.Sensordatatype>`
            
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
                super(CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry, self).__init__()

                self.yang_name = "entSensorValueEntry"
                self.yang_parent_name = "entSensorValueTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.entsensormeasuredentity = YLeaf(YType.int32, "entSensorMeasuredEntity")

                self.entsensorprecision = YLeaf(YType.int32, "entSensorPrecision")

                self.entsensorscale = YLeaf(YType.enumeration, "entSensorScale")

                self.entsensorstatus = YLeaf(YType.enumeration, "entSensorStatus")

                self.entsensortype = YLeaf(YType.enumeration, "entSensorType")

                self.entsensorvalue = YLeaf(YType.int32, "entSensorValue")

                self.entsensorvaluetimestamp = YLeaf(YType.uint32, "entSensorValueTimeStamp")

                self.entsensorvalueupdaterate = YLeaf(YType.int32, "entSensorValueUpdateRate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "entsensormeasuredentity",
                                "entsensorprecision",
                                "entsensorscale",
                                "entsensorstatus",
                                "entsensortype",
                                "entsensorvalue",
                                "entsensorvaluetimestamp",
                                "entsensorvalueupdaterate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.entsensormeasuredentity.is_set or
                    self.entsensorprecision.is_set or
                    self.entsensorscale.is_set or
                    self.entsensorstatus.is_set or
                    self.entsensortype.is_set or
                    self.entsensorvalue.is_set or
                    self.entsensorvaluetimestamp.is_set or
                    self.entsensorvalueupdaterate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.entsensormeasuredentity.yfilter != YFilter.not_set or
                    self.entsensorprecision.yfilter != YFilter.not_set or
                    self.entsensorscale.yfilter != YFilter.not_set or
                    self.entsensorstatus.yfilter != YFilter.not_set or
                    self.entsensortype.yfilter != YFilter.not_set or
                    self.entsensorvalue.yfilter != YFilter.not_set or
                    self.entsensorvaluetimestamp.yfilter != YFilter.not_set or
                    self.entsensorvalueupdaterate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "entSensorValueEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/entSensorValueTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.entsensormeasuredentity.is_set or self.entsensormeasuredentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensormeasuredentity.get_name_leafdata())
                if (self.entsensorprecision.is_set or self.entsensorprecision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorprecision.get_name_leafdata())
                if (self.entsensorscale.is_set or self.entsensorscale.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorscale.get_name_leafdata())
                if (self.entsensorstatus.is_set or self.entsensorstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorstatus.get_name_leafdata())
                if (self.entsensortype.is_set or self.entsensortype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensortype.get_name_leafdata())
                if (self.entsensorvalue.is_set or self.entsensorvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorvalue.get_name_leafdata())
                if (self.entsensorvaluetimestamp.is_set or self.entsensorvaluetimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorvaluetimestamp.get_name_leafdata())
                if (self.entsensorvalueupdaterate.is_set or self.entsensorvalueupdaterate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorvalueupdaterate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "entSensorMeasuredEntity" or name == "entSensorPrecision" or name == "entSensorScale" or name == "entSensorStatus" or name == "entSensorType" or name == "entSensorValue" or name == "entSensorValueTimeStamp" or name == "entSensorValueUpdateRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorMeasuredEntity"):
                    self.entsensormeasuredentity = value
                    self.entsensormeasuredentity.value_namespace = name_space
                    self.entsensormeasuredentity.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorPrecision"):
                    self.entsensorprecision = value
                    self.entsensorprecision.value_namespace = name_space
                    self.entsensorprecision.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorScale"):
                    self.entsensorscale = value
                    self.entsensorscale.value_namespace = name_space
                    self.entsensorscale.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorStatus"):
                    self.entsensorstatus = value
                    self.entsensorstatus.value_namespace = name_space
                    self.entsensorstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorType"):
                    self.entsensortype = value
                    self.entsensortype.value_namespace = name_space
                    self.entsensortype.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorValue"):
                    self.entsensorvalue = value
                    self.entsensorvalue.value_namespace = name_space
                    self.entsensorvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorValueTimeStamp"):
                    self.entsensorvaluetimestamp = value
                    self.entsensorvaluetimestamp.value_namespace = name_space
                    self.entsensorvaluetimestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorValueUpdateRate"):
                    self.entsensorvalueupdaterate = value
                    self.entsensorvalueupdaterate.value_namespace = name_space
                    self.entsensorvalueupdaterate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.entsensorvalueentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.entsensorvalueentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "entSensorValueTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "entSensorValueEntry"):
                for c in self.entsensorvalueentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntitySensorMib.Entsensorvaluetable.Entsensorvalueentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.entsensorvalueentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entSensorValueEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Entsensorthresholdtable(Entity):
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
            super(CiscoEntitySensorMib.Entsensorthresholdtable, self).__init__()

            self.yang_name = "entSensorThresholdTable"
            self.yang_parent_name = "CISCO-ENTITY-SENSOR-MIB"

            self.entsensorthresholdentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEntitySensorMib.Entsensorthresholdtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEntitySensorMib.Entsensorthresholdtable, self).__setattr__(name, value)


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
            	**type**\:   :py:class:`Sensorthresholdrelation <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.Sensorthresholdrelation>`
            
            .. attribute:: entsensorthresholdseverity
            
            	This variable indicates the severity of this threshold
            	**type**\:   :py:class:`Sensorthresholdseverity <ydk.models.cisco_ios_xe.CISCO_ENTITY_SENSOR_MIB.Sensorthresholdseverity>`
            
            .. attribute:: entsensorthresholdvalue
            
            	This variable indicates the value of the threshold.  To correctly display or interpret this variable's value,  you must also know entSensorType, entSensorScale, and  entSensorPrecision.  However, you can directly compare entSensorValue  with the threshold values given in entSensorThresholdTable  without any semantic knowledge
            	**type**\:  int
            
            	**range:** \-1000000000..1073741823
            
            

            """

            _prefix = 'CISCO-ENTITY-SENSOR-MIB'
            _revision = '2015-01-15'

            def __init__(self):
                super(CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry, self).__init__()

                self.yang_name = "entSensorThresholdEntry"
                self.yang_parent_name = "entSensorThresholdTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.entsensorthresholdindex = YLeaf(YType.int32, "entSensorThresholdIndex")

                self.entsensorthresholdevaluation = YLeaf(YType.boolean, "entSensorThresholdEvaluation")

                self.entsensorthresholdnotificationenable = YLeaf(YType.boolean, "entSensorThresholdNotificationEnable")

                self.entsensorthresholdrelation = YLeaf(YType.enumeration, "entSensorThresholdRelation")

                self.entsensorthresholdseverity = YLeaf(YType.enumeration, "entSensorThresholdSeverity")

                self.entsensorthresholdvalue = YLeaf(YType.int32, "entSensorThresholdValue")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "entsensorthresholdindex",
                                "entsensorthresholdevaluation",
                                "entsensorthresholdnotificationenable",
                                "entsensorthresholdrelation",
                                "entsensorthresholdseverity",
                                "entsensorthresholdvalue") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.entsensorthresholdindex.is_set or
                    self.entsensorthresholdevaluation.is_set or
                    self.entsensorthresholdnotificationenable.is_set or
                    self.entsensorthresholdrelation.is_set or
                    self.entsensorthresholdseverity.is_set or
                    self.entsensorthresholdvalue.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.entsensorthresholdindex.yfilter != YFilter.not_set or
                    self.entsensorthresholdevaluation.yfilter != YFilter.not_set or
                    self.entsensorthresholdnotificationenable.yfilter != YFilter.not_set or
                    self.entsensorthresholdrelation.yfilter != YFilter.not_set or
                    self.entsensorthresholdseverity.yfilter != YFilter.not_set or
                    self.entsensorthresholdvalue.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "entSensorThresholdEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[entSensorThresholdIndex='" + self.entsensorthresholdindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/entSensorThresholdTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.entsensorthresholdindex.is_set or self.entsensorthresholdindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorthresholdindex.get_name_leafdata())
                if (self.entsensorthresholdevaluation.is_set or self.entsensorthresholdevaluation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorthresholdevaluation.get_name_leafdata())
                if (self.entsensorthresholdnotificationenable.is_set or self.entsensorthresholdnotificationenable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorthresholdnotificationenable.get_name_leafdata())
                if (self.entsensorthresholdrelation.is_set or self.entsensorthresholdrelation.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorthresholdrelation.get_name_leafdata())
                if (self.entsensorthresholdseverity.is_set or self.entsensorthresholdseverity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorthresholdseverity.get_name_leafdata())
                if (self.entsensorthresholdvalue.is_set or self.entsensorthresholdvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entsensorthresholdvalue.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "entSensorThresholdIndex" or name == "entSensorThresholdEvaluation" or name == "entSensorThresholdNotificationEnable" or name == "entSensorThresholdRelation" or name == "entSensorThresholdSeverity" or name == "entSensorThresholdValue"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorThresholdIndex"):
                    self.entsensorthresholdindex = value
                    self.entsensorthresholdindex.value_namespace = name_space
                    self.entsensorthresholdindex.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorThresholdEvaluation"):
                    self.entsensorthresholdevaluation = value
                    self.entsensorthresholdevaluation.value_namespace = name_space
                    self.entsensorthresholdevaluation.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorThresholdNotificationEnable"):
                    self.entsensorthresholdnotificationenable = value
                    self.entsensorthresholdnotificationenable.value_namespace = name_space
                    self.entsensorthresholdnotificationenable.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorThresholdRelation"):
                    self.entsensorthresholdrelation = value
                    self.entsensorthresholdrelation.value_namespace = name_space
                    self.entsensorthresholdrelation.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorThresholdSeverity"):
                    self.entsensorthresholdseverity = value
                    self.entsensorthresholdseverity.value_namespace = name_space
                    self.entsensorthresholdseverity.value_namespace_prefix = name_space_prefix
                if(value_path == "entSensorThresholdValue"):
                    self.entsensorthresholdvalue = value
                    self.entsensorthresholdvalue.value_namespace = name_space
                    self.entsensorthresholdvalue.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.entsensorthresholdentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.entsensorthresholdentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "entSensorThresholdTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "entSensorThresholdEntry"):
                for c in self.entsensorthresholdentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEntitySensorMib.Entsensorthresholdtable.Entsensorthresholdentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.entsensorthresholdentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entSensorThresholdEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.entsensorglobalobjects is not None and self.entsensorglobalobjects.has_data()) or
            (self.entsensorthresholdtable is not None and self.entsensorthresholdtable.has_data()) or
            (self.entsensorvaluetable is not None and self.entsensorvaluetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.entsensorglobalobjects is not None and self.entsensorglobalobjects.has_operation()) or
            (self.entsensorthresholdtable is not None and self.entsensorthresholdtable.has_operation()) or
            (self.entsensorvaluetable is not None and self.entsensorvaluetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ENTITY-SENSOR-MIB:CISCO-ENTITY-SENSOR-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "entSensorGlobalObjects"):
            if (self.entsensorglobalobjects is None):
                self.entsensorglobalobjects = CiscoEntitySensorMib.Entsensorglobalobjects()
                self.entsensorglobalobjects.parent = self
                self._children_name_map["entsensorglobalobjects"] = "entSensorGlobalObjects"
            return self.entsensorglobalobjects

        if (child_yang_name == "entSensorThresholdTable"):
            if (self.entsensorthresholdtable is None):
                self.entsensorthresholdtable = CiscoEntitySensorMib.Entsensorthresholdtable()
                self.entsensorthresholdtable.parent = self
                self._children_name_map["entsensorthresholdtable"] = "entSensorThresholdTable"
            return self.entsensorthresholdtable

        if (child_yang_name == "entSensorValueTable"):
            if (self.entsensorvaluetable is None):
                self.entsensorvaluetable = CiscoEntitySensorMib.Entsensorvaluetable()
                self.entsensorvaluetable.parent = self
                self._children_name_map["entsensorvaluetable"] = "entSensorValueTable"
            return self.entsensorvaluetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "entSensorGlobalObjects" or name == "entSensorThresholdTable" or name == "entSensorValueTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEntitySensorMib()
        return self._top_entity

