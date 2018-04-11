""" ENTITY_SENSOR_MIB 

This module defines Entity MIB extensions for physical
sensors.

Copyright (C) The Internet Society (2002). This version
of this MIB module is part of RFC 3433; see the RFC
itself for full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class EntitySensorDataScale(Enum):
    """
    EntitySensorDataScale (Enum Class)

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


class EntitySensorDataType(Enum):
    """
    EntitySensorDataType (Enum Class)

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


class EntitySensorStatus(Enum):
    """
    EntitySensorStatus (Enum Class)

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



class ENTITYSENSORMIB(Entity):
    """
    
    
    .. attribute:: entphysensortable
    
    	This table contains one row per physical sensor represented by an associated row in the entPhysicalTable
    	**type**\:  :py:class:`Entphysensortable <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.ENTITYSENSORMIB.Entphysensortable>`
    
    

    """

    _prefix = 'ENTITY-SENSOR-MIB'
    _revision = '2002-12-16'

    def __init__(self):
        super(ENTITYSENSORMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "ENTITY-SENSOR-MIB"
        self.yang_parent_name = "ENTITY-SENSOR-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("entPhySensorTable", ("entphysensortable", ENTITYSENSORMIB.Entphysensortable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.entphysensortable = ENTITYSENSORMIB.Entphysensortable()
        self.entphysensortable.parent = self
        self._children_name_map["entphysensortable"] = "entPhySensorTable"
        self._children_yang_names.add("entPhySensorTable")
        self._segment_path = lambda: "ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB"


    class Entphysensortable(Entity):
        """
        This table contains one row per physical sensor represented
        by an associated row in the entPhysicalTable.
        
        .. attribute:: entphysensorentry
        
        	Information about a particular physical sensor.  An entry in this table describes the present reading of a sensor, the measurement units and scale, and sensor operational status.  Entries are created in this table by the agent.  An entry for each physical sensor SHOULD be created at the same time as the associated entPhysicalEntry.  An entry SHOULD be destroyed if the associated entPhysicalEntry is destroyed
        	**type**\: list of  		 :py:class:`Entphysensorentry <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.ENTITYSENSORMIB.Entphysensortable.Entphysensorentry>`
        
        

        """

        _prefix = 'ENTITY-SENSOR-MIB'
        _revision = '2002-12-16'

        def __init__(self):
            super(ENTITYSENSORMIB.Entphysensortable, self).__init__()

            self.yang_name = "entPhySensorTable"
            self.yang_parent_name = "ENTITY-SENSOR-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("entPhySensorEntry", ("entphysensorentry", ENTITYSENSORMIB.Entphysensortable.Entphysensorentry))])
            self._leafs = OrderedDict()

            self.entphysensorentry = YList(self)
            self._segment_path = lambda: "entPhySensorTable"
            self._absolute_path = lambda: "ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ENTITYSENSORMIB.Entphysensortable, [], name, value)


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
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entphysensortype
            
            	The type of data returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:  :py:class:`EntitySensorDataType <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitySensorDataType>`
            
            .. attribute:: entphysensorscale
            
            	The exponent to apply to values returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:  :py:class:`EntitySensorDataScale <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitySensorDataScale>`
            
            .. attribute:: entphysensorprecision
            
            	The number of decimal places of precision in fixed\-point sensor values returned by the associated entPhySensorValue object.  This object SHOULD be set to '0' when the associated entPhySensorType value is not a fixed\-point type\: e.g., 'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\: int
            
            	**range:** \-8..9
            
            .. attribute:: entphysensorvalue
            
            	The most recent measurement obtained by the agent for this sensor.  To correctly interpret the value of this object, the associated entPhySensorType, entPhySensorScale, and entPhySensorPrecision objects must also be examined
            	**type**\: int
            
            	**range:** \-1000000000..1073741823
            
            .. attribute:: entphysensoroperstatus
            
            	The operational status of the sensor
            	**type**\:  :py:class:`EntitySensorStatus <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitySensorStatus>`
            
            .. attribute:: entphysensorunitsdisplay
            
            	A textual description of the data units that should be used in the display of entPhySensorValue
            	**type**\: str
            
            .. attribute:: entphysensorvaluetimestamp
            
            	The value of sysUpTime at the time the status and/or value of this sensor was last obtained by the agent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: entphysensorvalueupdaterate
            
            	An indication of the frequency that the agent updates the associated entPhySensorValue object, representing in milliseconds.  The value zero indicates\:      \- the sensor value is updated on demand (e.g.,       when polled by the agent for a get\-request),     \- the sensor value is updated when the sensor       value changes (event\-driven),     \- the agent does not know the update rate
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'ENTITY-SENSOR-MIB'
            _revision = '2002-12-16'

            def __init__(self):
                super(ENTITYSENSORMIB.Entphysensortable.Entphysensorentry, self).__init__()

                self.yang_name = "entPhySensorEntry"
                self.yang_parent_name = "entPhySensorTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('entphysensortype', YLeaf(YType.enumeration, 'entPhySensorType')),
                    ('entphysensorscale', YLeaf(YType.enumeration, 'entPhySensorScale')),
                    ('entphysensorprecision', YLeaf(YType.int32, 'entPhySensorPrecision')),
                    ('entphysensorvalue', YLeaf(YType.int32, 'entPhySensorValue')),
                    ('entphysensoroperstatus', YLeaf(YType.enumeration, 'entPhySensorOperStatus')),
                    ('entphysensorunitsdisplay', YLeaf(YType.str, 'entPhySensorUnitsDisplay')),
                    ('entphysensorvaluetimestamp', YLeaf(YType.uint32, 'entPhySensorValueTimeStamp')),
                    ('entphysensorvalueupdaterate', YLeaf(YType.uint32, 'entPhySensorValueUpdateRate')),
                ])
                self.entphysicalindex = None
                self.entphysensortype = None
                self.entphysensorscale = None
                self.entphysensorprecision = None
                self.entphysensorvalue = None
                self.entphysensoroperstatus = None
                self.entphysensorunitsdisplay = None
                self.entphysensorvaluetimestamp = None
                self.entphysensorvalueupdaterate = None
                self._segment_path = lambda: "entPhySensorEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/entPhySensorTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ENTITYSENSORMIB.Entphysensortable.Entphysensorentry, ['entphysicalindex', 'entphysensortype', 'entphysensorscale', 'entphysensorprecision', 'entphysensorvalue', 'entphysensoroperstatus', 'entphysensorunitsdisplay', 'entphysensorvaluetimestamp', 'entphysensorvalueupdaterate'], name, value)

    def clone_ptr(self):
        self._top_entity = ENTITYSENSORMIB()
        return self._top_entity

