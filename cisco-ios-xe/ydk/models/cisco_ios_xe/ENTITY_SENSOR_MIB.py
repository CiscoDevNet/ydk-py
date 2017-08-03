""" ENTITY_SENSOR_MIB 

This module defines Entity MIB extensions for physical
sensors.

Copyright (C) The Internet Society (2002). This version
of this MIB module is part of RFC 3433; see the RFC
itself for full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Entitysensordatascale(Enum):
    """
    Entitysensordatascale

    An object using this data type represents a data scaling

    factor, represented with an International System of Units

    (SI) prefix.  The actual data units are determined by

    examining an object of this type together with the

    associated EntitySensorDataType object.

    An object of this type SHOULD be defined together with

    objects of type EntitySensorDataType and

    EntitySensorPrecision.  Together, associated objects of

    these three types are used to identify the semantics of an

    object of type EntitySensorValue.

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


class Entitysensordatatype(Enum):
    """
    Entitysensordatatype

    An object using this data type represents the Entity Sensor

    measurement data type associated with a physical sensor

    value. The actual data units are determined by examining an

    object of this type together with the associated

    EntitySensorDataScale object.

    An object of this type SHOULD be defined together with

    objects of type EntitySensorDataScale and

    EntitySensorPrecision.  Together, associated objects of

    these three types are used to identify the semantics of an

    object of type EntitySensorValue.

    Valid values are\:

       other(1)\:        a measure other than those listed below

       unknown(2)\:      unknown measurement, or arbitrary,

                        relative numbers

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


class Entitysensorstatus(Enum):
    """
    Entitysensorstatus

    An object using this data type represents the operational

    status of a physical sensor.

    The value 'ok(1)' indicates that the agent can obtain the

    sensor value.

    The value 'unavailable(2)' indicates that the agent

    presently cannot obtain the sensor value.

    The value 'nonoperational(3)' indicates that the agent

    believes the sensor is broken.  The sensor could have a hard

    failure (disconnected wire), or a soft failure such as out\-

    of\-range, jittery, or wildly fluctuating readings.

    .. data:: ok = 1

    .. data:: unavailable = 2

    .. data:: nonoperational = 3

    """

    ok = Enum.YLeaf(1, "ok")

    unavailable = Enum.YLeaf(2, "unavailable")

    nonoperational = Enum.YLeaf(3, "nonoperational")



class EntitySensorMib(Entity):
    """
    
    
    .. attribute:: entphysensortable
    
    	This table contains one row per physical sensor represented by an associated row in the entPhysicalTable
    	**type**\:   :py:class:`Entphysensortable <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitySensorMib.Entphysensortable>`
    
    

    """

    _prefix = 'ENTITY-SENSOR-MIB'
    _revision = '2002-12-16'

    def __init__(self):
        super(EntitySensorMib, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-SENSOR-MIB"
        self.yang_parent_name = "ENTITY-SENSOR-MIB"

        self.entphysensortable = EntitySensorMib.Entphysensortable()
        self.entphysensortable.parent = self
        self._children_name_map["entphysensortable"] = "entPhySensorTable"
        self._children_yang_names.add("entPhySensorTable")


    class Entphysensortable(Entity):
        """
        This table contains one row per physical sensor represented
        by an associated row in the entPhysicalTable.
        
        .. attribute:: entphysensorentry
        
        	Information about a particular physical sensor.  An entry in this table describes the present reading of a sensor, the measurement units and scale, and sensor operational status.  Entries are created in this table by the agent.  An entry for each physical sensor SHOULD be created at the same time as the associated entPhysicalEntry.  An entry SHOULD be destroyed if the associated entPhysicalEntry is destroyed
        	**type**\: list of    :py:class:`Entphysensorentry <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitySensorMib.Entphysensortable.Entphysensorentry>`
        
        

        """

        _prefix = 'ENTITY-SENSOR-MIB'
        _revision = '2002-12-16'

        def __init__(self):
            super(EntitySensorMib.Entphysensortable, self).__init__()

            self.yang_name = "entPhySensorTable"
            self.yang_parent_name = "ENTITY-SENSOR-MIB"

            self.entphysensorentry = YList(self)

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
                        super(EntitySensorMib.Entphysensortable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(EntitySensorMib.Entphysensortable, self).__setattr__(name, value)


        class Entphysensorentry(Entity):
            """
            Information about a particular physical sensor.
            
            An entry in this table describes the present reading of a
            sensor, the measurement units and scale, and sensor
            operational status.
            
            Entries are created in this table by the agent.  An entry
            for each physical sensor SHOULD be created at the same time
            as the associated entPhysicalEntry.  An entry SHOULD be
            destroyed if the associated entPhysicalEntry is destroyed.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entphysensoroperstatus
            
            	The operational status of the sensor
            	**type**\:   :py:class:`Entitysensorstatus <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.Entitysensorstatus>`
            
            .. attribute:: entphysensorprecision
            
            	The number of decimal places of precision in fixed\-point sensor values returned by the associated entPhySensorValue object.  This object SHOULD be set to '0' when the associated entPhySensorType value is not a fixed\-point type\: e.g., 'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:  int
            
            	**range:** \-8..9
            
            .. attribute:: entphysensorscale
            
            	The exponent to apply to values returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:   :py:class:`Entitysensordatascale <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.Entitysensordatascale>`
            
            .. attribute:: entphysensortype
            
            	The type of data returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:   :py:class:`Entitysensordatatype <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.Entitysensordatatype>`
            
            .. attribute:: entphysensorunitsdisplay
            
            	A textual description of the data units that should be used in the display of entPhySensorValue
            	**type**\:  str
            
            .. attribute:: entphysensorvalue
            
            	The most recent measurement obtained by the agent for this sensor.  To correctly interpret the value of this object, the associated entPhySensorType, entPhySensorScale, and entPhySensorPrecision objects must also be examined
            	**type**\:  int
            
            	**range:** \-1000000000..1073741823
            
            .. attribute:: entphysensorvaluetimestamp
            
            	The value of sysUpTime at the time the status and/or value of this sensor was last obtained by the agent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: entphysensorvalueupdaterate
            
            	An indication of the frequency that the agent updates the associated entPhySensorValue object, representing in milliseconds.  The value zero indicates\:      \- the sensor value is updated on demand (e.g.,       when polled by the agent for a get\-request),     \- the sensor value is updated when the sensor       value changes (event\-driven),     \- the agent does not know the update rate
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'ENTITY-SENSOR-MIB'
            _revision = '2002-12-16'

            def __init__(self):
                super(EntitySensorMib.Entphysensortable.Entphysensorentry, self).__init__()

                self.yang_name = "entPhySensorEntry"
                self.yang_parent_name = "entPhySensorTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.entphysensoroperstatus = YLeaf(YType.enumeration, "entPhySensorOperStatus")

                self.entphysensorprecision = YLeaf(YType.int32, "entPhySensorPrecision")

                self.entphysensorscale = YLeaf(YType.enumeration, "entPhySensorScale")

                self.entphysensortype = YLeaf(YType.enumeration, "entPhySensorType")

                self.entphysensorunitsdisplay = YLeaf(YType.str, "entPhySensorUnitsDisplay")

                self.entphysensorvalue = YLeaf(YType.int32, "entPhySensorValue")

                self.entphysensorvaluetimestamp = YLeaf(YType.uint32, "entPhySensorValueTimeStamp")

                self.entphysensorvalueupdaterate = YLeaf(YType.uint32, "entPhySensorValueUpdateRate")

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
                                "entphysensoroperstatus",
                                "entphysensorprecision",
                                "entphysensorscale",
                                "entphysensortype",
                                "entphysensorunitsdisplay",
                                "entphysensorvalue",
                                "entphysensorvaluetimestamp",
                                "entphysensorvalueupdaterate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(EntitySensorMib.Entphysensortable.Entphysensorentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(EntitySensorMib.Entphysensortable.Entphysensorentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.entphysensoroperstatus.is_set or
                    self.entphysensorprecision.is_set or
                    self.entphysensorscale.is_set or
                    self.entphysensortype.is_set or
                    self.entphysensorunitsdisplay.is_set or
                    self.entphysensorvalue.is_set or
                    self.entphysensorvaluetimestamp.is_set or
                    self.entphysensorvalueupdaterate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.entphysensoroperstatus.yfilter != YFilter.not_set or
                    self.entphysensorprecision.yfilter != YFilter.not_set or
                    self.entphysensorscale.yfilter != YFilter.not_set or
                    self.entphysensortype.yfilter != YFilter.not_set or
                    self.entphysensorunitsdisplay.yfilter != YFilter.not_set or
                    self.entphysensorvalue.yfilter != YFilter.not_set or
                    self.entphysensorvaluetimestamp.yfilter != YFilter.not_set or
                    self.entphysensorvalueupdaterate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "entPhySensorEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/entPhySensorTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.entphysensoroperstatus.is_set or self.entphysensoroperstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensoroperstatus.get_name_leafdata())
                if (self.entphysensorprecision.is_set or self.entphysensorprecision.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensorprecision.get_name_leafdata())
                if (self.entphysensorscale.is_set or self.entphysensorscale.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensorscale.get_name_leafdata())
                if (self.entphysensortype.is_set or self.entphysensortype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensortype.get_name_leafdata())
                if (self.entphysensorunitsdisplay.is_set or self.entphysensorunitsdisplay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensorunitsdisplay.get_name_leafdata())
                if (self.entphysensorvalue.is_set or self.entphysensorvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensorvalue.get_name_leafdata())
                if (self.entphysensorvaluetimestamp.is_set or self.entphysensorvaluetimestamp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensorvaluetimestamp.get_name_leafdata())
                if (self.entphysensorvalueupdaterate.is_set or self.entphysensorvalueupdaterate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysensorvalueupdaterate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "entPhySensorOperStatus" or name == "entPhySensorPrecision" or name == "entPhySensorScale" or name == "entPhySensorType" or name == "entPhySensorUnitsDisplay" or name == "entPhySensorValue" or name == "entPhySensorValueTimeStamp" or name == "entPhySensorValueUpdateRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorOperStatus"):
                    self.entphysensoroperstatus = value
                    self.entphysensoroperstatus.value_namespace = name_space
                    self.entphysensoroperstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorPrecision"):
                    self.entphysensorprecision = value
                    self.entphysensorprecision.value_namespace = name_space
                    self.entphysensorprecision.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorScale"):
                    self.entphysensorscale = value
                    self.entphysensorscale.value_namespace = name_space
                    self.entphysensorscale.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorType"):
                    self.entphysensortype = value
                    self.entphysensortype.value_namespace = name_space
                    self.entphysensortype.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorUnitsDisplay"):
                    self.entphysensorunitsdisplay = value
                    self.entphysensorunitsdisplay.value_namespace = name_space
                    self.entphysensorunitsdisplay.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorValue"):
                    self.entphysensorvalue = value
                    self.entphysensorvalue.value_namespace = name_space
                    self.entphysensorvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorValueTimeStamp"):
                    self.entphysensorvaluetimestamp = value
                    self.entphysensorvaluetimestamp.value_namespace = name_space
                    self.entphysensorvaluetimestamp.value_namespace_prefix = name_space_prefix
                if(value_path == "entPhySensorValueUpdateRate"):
                    self.entphysensorvalueupdaterate = value
                    self.entphysensorvalueupdaterate.value_namespace = name_space
                    self.entphysensorvalueupdaterate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.entphysensorentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.entphysensorentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "entPhySensorTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "entPhySensorEntry"):
                for c in self.entphysensorentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = EntitySensorMib.Entphysensortable.Entphysensorentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.entphysensorentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "entPhySensorEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (self.entphysensortable is not None and self.entphysensortable.has_data())

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.entphysensortable is not None and self.entphysensortable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB" + path_buffer

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

        if (child_yang_name == "entPhySensorTable"):
            if (self.entphysensortable is None):
                self.entphysensortable = EntitySensorMib.Entphysensortable()
                self.entphysensortable.parent = self
                self._children_name_map["entphysensortable"] = "entPhySensorTable"
            return self.entphysensortable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "entPhySensorTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = EntitySensorMib()
        return self._top_entity

