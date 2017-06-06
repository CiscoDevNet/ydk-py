""" ENTITY_SENSOR_MIB 

This module defines Entity MIB extensions for physical
sensors.

Copyright (C) The Internet Society (2002). This version
of this MIB module is part of RFC 3433; see the RFC
itself for full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class EntitysensordatascaleEnum(Enum):
    """
    EntitysensordatascaleEnum

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
        from ydk.models.cisco_ios_xe._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['EntitysensordatascaleEnum']


class EntitysensordatatypeEnum(Enum):
    """
    EntitysensordatatypeEnum

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


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['EntitysensordatatypeEnum']


class EntitysensorstatusEnum(Enum):
    """
    EntitysensorstatusEnum

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

    ok = 1

    unavailable = 2

    nonoperational = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['EntitysensorstatusEnum']



class EntitySensorMib(object):
    """
    
    
    .. attribute:: entphysensortable
    
    	This table contains one row per physical sensor represented by an associated row in the entPhysicalTable
    	**type**\:   :py:class:`Entphysensortable <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitySensorMib.Entphysensortable>`
    
    

    """

    _prefix = 'ENTITY-SENSOR-MIB'
    _revision = '2002-12-16'

    def __init__(self):
        self.entphysensortable = EntitySensorMib.Entphysensortable()
        self.entphysensortable.parent = self


    class Entphysensortable(object):
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
            self.parent = None
            self.entphysensorentry = YList()
            self.entphysensorentry.parent = self
            self.entphysensorentry.name = 'entphysensorentry'


        class Entphysensorentry(object):
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
            	**type**\:   :py:class:`EntitysensorstatusEnum <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitysensorstatusEnum>`
            
            .. attribute:: entphysensorprecision
            
            	The number of decimal places of precision in fixed\-point sensor values returned by the associated entPhySensorValue object.  This object SHOULD be set to '0' when the associated entPhySensorType value is not a fixed\-point type\: e.g., 'percentRH(9)', 'rpm(10)', 'cmm(11)', or 'truthvalue(12)'.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:  int
            
            	**range:** \-8..9
            
            .. attribute:: entphysensorscale
            
            	The exponent to apply to values returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:   :py:class:`EntitysensordatascaleEnum <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitysensordatascaleEnum>`
            
            .. attribute:: entphysensortype
            
            	The type of data returned by the associated entPhySensorValue object.  This object SHOULD be set by the agent during entry creation, and the value SHOULD NOT change during operation
            	**type**\:   :py:class:`EntitysensordatatypeEnum <ydk.models.cisco_ios_xe.ENTITY_SENSOR_MIB.EntitysensordatatypeEnum>`
            
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
                self.parent = None
                self.entphysicalindex = None
                self.entphysensoroperstatus = None
                self.entphysensorprecision = None
                self.entphysensorscale = None
                self.entphysensortype = None
                self.entphysensorunitsdisplay = None
                self.entphysensorvalue = None
                self.entphysensorvaluetimestamp = None
                self.entphysensorvalueupdaterate = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/ENTITY-SENSOR-MIB:entPhySensorTable/ENTITY-SENSOR-MIB:entPhySensorEntry[ENTITY-SENSOR-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.entphysensoroperstatus is not None:
                    return True

                if self.entphysensorprecision is not None:
                    return True

                if self.entphysensorscale is not None:
                    return True

                if self.entphysensortype is not None:
                    return True

                if self.entphysensorunitsdisplay is not None:
                    return True

                if self.entphysensorvalue is not None:
                    return True

                if self.entphysensorvaluetimestamp is not None:
                    return True

                if self.entphysensorvalueupdaterate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _ENTITY_SENSOR_MIB as meta
                return meta._meta_table['EntitySensorMib.Entphysensortable.Entphysensorentry']['meta_info']

        @property
        def _common_path(self):

            return '/ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB/ENTITY-SENSOR-MIB:entPhySensorTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.entphysensorentry is not None:
                for child_ref in self.entphysensorentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _ENTITY_SENSOR_MIB as meta
            return meta._meta_table['EntitySensorMib.Entphysensortable']['meta_info']

    @property
    def _common_path(self):

        return '/ENTITY-SENSOR-MIB:ENTITY-SENSOR-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.entphysensortable is not None and self.entphysensortable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _ENTITY_SENSOR_MIB as meta
        return meta._meta_table['EntitySensorMib']['meta_info']


